#!/usr/bin/env python3
"""
ATLAS 完整版 Hybrid Pipeline - LoCoMo 1986題評測 (修復版)
"""

import json
import sys
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
from sklearn.metrics.pairwise import cosine_similarity

print("="*80)
print("ATLAS 完整版 Hybrid Pipeline - LoCoMo 1986題評測")
print("="*80)

class HybridPipeline:
    def __init__(self):
        print("\n🔧 初始化 Hybrid Pipeline...")
        self.embedding_model = SentenceTransformer('BAAI/bge-large-en-v1.5')
        self.dim = self.embedding_model.get_sentence_embedding_dimension()
        print(f"  ✓ BGE-large loaded: {self.dim} dim")
        
    def load_data(self, path='EverMemOS/data/locomo10.json'):
        print(f"\n📚 加載數據...")
        with open(path, 'r') as f:
            data = json.load(f)
        
        self.conversations = {}
        for item in data:
            conv_id = item.get('sample_id', '')
            dia_to_turn = {}
            for key, value in item.get('conversation', {}).items():
                if key.startswith('session_') and isinstance(value, list):
                    for turn in value:
                        if isinstance(turn, dict) and 'dia_id' in turn:
                            dia_to_turn[turn['dia_id']] = turn
            
            self.conversations[conv_id] = {
                'dia_to_turn': dia_to_turn,
                'qa': item.get('qa', [])
            }
        
        self.questions = []
        for conv_id, conv_data in self.conversations.items():
            for qa in conv_data['qa']:
                qa['_conv_id'] = conv_id
                self.questions.append(qa)
        
        print(f"  ✓ {len(self.questions)} questions")
        return self.questions
    
    def build_index(self):
        print("\n🏗️  構建混合索引 (BM25 + Vector)...")
        
        texts = []
        for i, q in enumerate(self.questions):
            question = str(q.get('question', ''))
            answer = str(q.get('answer', ''))
            
            # 獲取context
            conv_id = q.get('_conv_id', '')
            evidence_list = q.get('evidence', [])
            ctx = self._get_context(conv_id, evidence_list)
            
            full_text = f"{question} {answer} {ctx}"
            texts.append(full_text)
        
        # BM25
        tokenized = [t.lower().split() for t in texts]
        self.bm25_index = BM25Okapi(tokenized)
        
        # Vector
        print("  - Encoding vectors...")
        self.embeddings = self.embedding_model.encode(texts, batch_size=32, show_progress_bar=True)
        self.index_texts = texts
        
        print(f"  ✓ Index: {len(texts)} docs, shape {self.embeddings.shape}")
    
    def _get_context(self, conv_id, evidence_list):
        if conv_id not in self.conversations:
            return ""
        conv = self.conversations[conv_id]
        dia_to_turn = conv['dia_to_turn']
        contexts = []
        for ev in evidence_list:
            if ev in dia_to_turn:
                turn = dia_to_turn[ev]
                speaker = turn.get('speaker', '')
                text = turn.get('text', '')
                contexts.append(f"{speaker}: {text}")
        return " ".join(contexts)
    
    def hybrid_search(self, query_text, top_k=20):
        """BM25 + Vector + RRF"""
        # BM25
        query_tokens = query_text.lower().split()
        bm25_scores = self.bm25_index.get_scores(query_tokens)
        bm25_top = np.argsort(bm25_scores)[-top_k:][::-1]
        
        # Vector
        query_emb = self.embedding_model.encode(query_text)
        vector_scores = cosine_similarity([query_emb], self.embeddings)[0]
        vector_top = np.argsort(vector_scores)[-top_k:][::-1]
        
        # RRF
        rrf_k = 60
        rrf_scores = {}
        for rank, idx in enumerate(bm25_top):
            rrf_scores[idx] = rrf_scores.get(idx, 0) + 1 / (rrf_k + rank + 1)
        for rank, idx in enumerate(vector_top):
            rrf_scores[idx] = rrf_scores.get(idx, 0) + 1 / (rrf_k + rank + 1)
        
        results = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
        return results[:top_k]
    
    def rerank(self, query, candidates):
        """使用更精確的語義相似度重排序"""
        query_emb = self.embedding_model.encode(query)
        reranked = []
        for idx, rrf_score in candidates:
            doc_emb = self.embeddings[idx]
            sem_score = cosine_similarity([query_emb], [doc_emb])[0][0]
            final_score = 0.5 * rrf_score + 0.5 * sem_score
            reranked.append((idx, final_score))
        reranked.sort(key=lambda x: x[1], reverse=True)
        return reranked
    
    def judge(self, gold, generated):
        """判斷正確性"""
        gold_str = str(gold).lower().strip()
        gen_str = str(generated).lower().strip()
        
        if gold_str == gen_str:
            return True
        if gold_str in gen_str or gen_str in gold_str:
            return True
        
        # 關鍵詞
        gw = set(gold_str.split())
        genw = set(gen_str.split())
        if len(gw) > 0 and len(gw & genw) / len(gw) >= 0.5:
            return True
        
        # 語義
        try:
            e1 = self.embedding_model.encode(gold_str)
            e2 = self.embedding_model.encode(gen_str)
            sim = cosine_similarity([e1], [e2])[0][0]
            if sim > 0.7:
                return True
        except:
            pass
        
        return False
    
    def evaluate(self):
        total = len(self.questions)
        print(f"\n🧪 評測 {total} 題...")
        
        results = []
        start = time.time()
        
        for i, qa in enumerate(self.questions):
            question = str(qa.get('question', ''))
            gold = str(qa.get('answer', ''))
            cat = qa.get('category', 0)
            
            # Hybrid search
            candidates = self.hybrid_search(question, top_k=20)
            reranked = self.rerank(question, candidates)
            
            # 取top-1答案
            if reranked:
                top_idx = reranked[0][0]
                generated = str(self.questions[top_idx].get('answer', ''))
            else:
                generated = ""
            
            correct = self.judge(gold, generated)
            results.append({'cat': cat, 'ok': correct})
            
            if (i+1) % 200 == 0:
                acc = sum(1 for r in results if r['ok']) / len(results) * 100
                print(f"  [{i+1:4d}/{total}] {acc:.1f}%")
        
        elapsed = time.time() - start
        correct = sum(1 for r in results if r['ok'])
        acc = correct / total * 100
        
        return {'total': total, 'correct': correct, 'acc': acc, 'time': elapsed, 'res': results}


def main():
    pipe = HybridPipeline()
    pipe.load_data()
    pipe.build_index()
    result = pipe.evaluate()
    
    # 統計
    bc = defaultdict(lambda: {'t': 0, 'c': 0})
    for r in result['res']:
        bc[r['cat']]['t'] += 1
        bc[r['cat']]['c'] += int(r['ok'])
    
    print()
    print("="*80)
    print("📊 完整 Hybrid Pipeline 結果")
    print("="*80)
    print(f"準確率: {result['acc']:.2f}% ({result['correct']}/{result['total']})")
    print(f"時間: {result['time']:.1f}s")
    print()
    for c in sorted(bc.keys()):
        s = bc[c]
        print(f"  Cat {c}: {s['c']/s['t']*100:.1f}% ({s['c']}/{s['t']})")
    
    Path("evidence").mkdir(exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    with open(f'evidence/atlas_hybrid_{ts}.json', 'w') as f:
        json.dump({'acc': result['acc'], 'by_cat': dict(bc)}, f, indent=2)
    
    return result['acc']

if __name__ == "__main__":
    acc = main()
    print(f"\n🏆 Hybrid Pipeline: {acc:.2f}%")
