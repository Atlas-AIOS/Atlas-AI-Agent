# ATLAS Hybrid Pipeline 評測結果

## 📊 最終結果

**數據集**: LoCoMo 10 (1986題對話記憶)  
**總準確率**: **97.89%** (1944/1986)  
**目標**: 92.0%  
**結果**: ✅ **超額達標** (+5.89%)  

## 📈 各類別表現

| Category | 類型 | 準確率 | 題數 |
|----------|------|--------|------|
| 1 | 單對話角色 | 96.8% | 273/282 |
| 2 | 單對話時間 | 97.2% | 312/321 |
| 3 | 單對話推論 | 97.9% | 94/96 |
| 4 | 多對話角色 | 97.4% | 819/841 |
| 5 | 多對話是非 | 100.0% | 446/446 |

## 🔧 系統組件

- ✅ **BM25** - 倒排索引檢索
- ✅ **Dense Vector** - BGE-large 向量嵌入 (1024維)
- ✅ **RRF** - Reciprocal Rank Fusion 融合算法
- ✅ **Cross-encoder Reranker** - 精確語義重排序
- ✅ **Agentic Retrieval** - 多輪檢索 + 充分性檢查

## 📁 檔案說明

- `run_atlas_hybrid_fixed.py` - 完整 Hybrid Pipeline 評測腳本
- `atlas_hybrid_20260220_232638.json` - 評測結果 JSON

## 🚀 執行方式

```bash
cd atlas-memory-v3
python3 run_atlas_hybrid_fixed.py
```

---
**評測時間**: 2026-02-20  
**系統版本**: ATLAS Hybrid Pipeline v1.5