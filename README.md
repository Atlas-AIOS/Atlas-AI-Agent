# Atlas AI Agent

<div align="center">

**高性能 AI 助手框架，整合仿生人腦神經元向量記憶系統**  
**High-Performance AI Assistant Framework with Neural Memory System**

[![Rust](https://img.shields.io/badge/Rust-1.70+-orange.svg)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-green.svg)](https://github.com/Atlas-AIOS/Atlas-AI-Agent)

**高性能目標 · 安全導向 · 模塊化架構 · 開源免費**  
**Performance Goals · Security-oriented · Modular Architecture · Open Source**

</div>

---

## 📖 目錄 / Table of Contents

- [項目簡介 / Introduction](#項目簡介--introduction)
- [核心特色 / Core Features](#核心特色--core-features)
- [功能清單 / Feature List](#功能清單--feature-list)
- [快速開始 / Quick Start](#快速開始--quick-start)
- [架構設計 / Architecture](#架構設計--architecture)
- [與 OpenClaw 對比 / Comparison with OpenClaw](#與-openclaw-對比--comparison-with-openclaw)
- [文檔導航 / Documentation](#文檔導航--documentation)
- [開發團隊 / Development Team](#開發團隊--development-team)
- [許可證 / License](#許可證--license)

---

## 🎯 項目簡介 / Introduction

**Atlas AI Agent** 是一個高性能、安全可靠的 AI 助手框架，基於 Rust 構建，整合了仿生人腦神經元向量記憶系統，打造最強的 AI-Agent 系統。

**Atlas AI Agent** is a high-performance, secure, and reliable AI assistant framework built with Rust, integrating a bionic neural vector memory system to create the most powerful AI-Agent system.

### 設計理念 / Design Philosophy

- **性能優先 / Performance First**：基於 Rust，持續優化啟動時間、內存占用和延遲  
  Built with Rust, continuously optimizing startup time, memory footprint, and latency

- **安全第一 / Security First**：多層安全機制，Skill 沙箱隔離，加密存儲  
  Multi-layered security mechanisms, Skill sandbox isolation, encrypted storage

- **功能演進 / Feature Evolution**：支持多 Provider / 多通道 / 多記憶後端，持續驗證完善  
  Supports multi-provider / multi-channel / multi-memory backends with ongoing validation

- **開源友好 / Open Source Friendly**：MIT 許可證，歡迎社區貢獻  
  MIT License, community contributions welcome

---

## ✨ 核心特色 / Core Features

### 1. 🚀 性能基線 / Performance Baseline

- **可重複基準 / Reproducible Benchmark**：使用 `scripts/benchmark.ps1` 生成本地基線報告  
  Generate local baseline with `scripts/benchmark.ps1`

- **啟動延遲 / Startup Latency**：以 `status` 命令做多次測量（Avg / P95）  
  Measured via repeated `status` runs (Avg / P95)

- **運行內存 / Runtime Memory**：提供 Gateway 進程空載內存快照  
  Includes idle gateway process memory snapshot

- **並發處理 / Concurrent Processing**：支持數千並發連接  
  Supports thousands of concurrent connections

### 實證文檔 / Evidence

- [Performance Baseline](docs/PERFORMANCE_BASELINE.md)
- [Validation Matrix](docs/VALIDATION_MATRIX.md)
- [Release Checklist](docs/RELEASE_CHECKLIST.md)

### 2. 🧠 仿生神經元記憶系統 / Bionic Neural Memory System

- **三層記憶架構 / Three-Layer Memory Architecture**：L1（即時）、L2（短期）、L3（長期）  
  L1 (Instant), L2 (Short-term), L3 (Long-term)

- **神經元向量存儲 / Neural Vector Storage**：模擬人腦記憶結構  
  Simulates human brain memory structure

- **智能記憶檢索 / Intelligent Memory Retrieval**：基於語義相似度的向量搜索  
  Vector search based on semantic similarity

- **記憶重要性評分 / Memory Importance Scoring**：自動評估記憶價值  
  Automatically evaluates memory value

- **區域記憶 / Regional Memory**：支持多 Brain ID 和 Universe ID  
  Supports multiple Brain IDs and Universe IDs

- **因果記憶索引 / Causal Memory Indexing**：建立記憶之間的關聯  
  Establishes relationships between memories

### 3. 🔒 企業級安全機制 / Enterprise-Grade Security

- **Skill 驗證 / Skill Validation**：Manifest 驗證、代碼簽名、危險模式掃描  
  Manifest validation, code signing, dangerous pattern scanning

- **沙箱隔離 / Sandbox Isolation**：文件系統、網絡、環境變量、資源限制  
  File system, network, environment variable, resource limits

- **加密存儲 / Encrypted Storage**：ChaCha20Poly1305 加密，HMAC-SHA256 密鑰派生  
  ChaCha20Poly1305 encryption, HMAC-SHA256 key derivation

- **訪問控制 / Access Control**：License Key 驗證、操作白名單、速率限制  
  License Key validation, operation whitelist, rate limiting

- **審計日誌 / Audit Logging**：完整操作記錄，異常檢測告警  
  Complete operation logs, anomaly detection alerts

### 4. 🌐 全平台支持 / Full Platform Support

- **9 大 API 提供商 / 9 Major API Providers**：Atlas、OpenAI、Google、Claude、GLM、Kimi、Qwen、DeepSeek、OpenRouter  
  Atlas, OpenAI, Google, Claude, GLM, Kimi, Qwen, DeepSeek, OpenRouter

- **本地模型支持 / Local Model Support**：Ollama、LM Studio、vLLM、TGI  
  Ollama, LM Studio, vLLM, TGI

- **中國平台 / Chinese Platforms**：QQ、釘釘、飛書（WebSocket 支持）  
  QQ, DingTalk, Feishu (WebSocket support)

- **國際平台 / International Platforms**：Telegram、Discord（WebSocket 支持）  
  Telegram, Discord (WebSocket support)

- **CLI 模式 / CLI Mode**：命令行交互界面  
  Command-line interactive interface

### 5. 🛠️ 豐富的工具生態 / Rich Tool Ecosystem

- **文件操作 / File Operations**：讀寫、搜索、監控  
  Read/write, search, monitor

- **網絡工具 / Network Tools**：Web 搜索（DuckDuckGo）、HTTP 請求  
  Web search (DuckDuckGo), HTTP requests

- **系統工具 / System Tools**：Shell 執行（安全沙箱）、進程管理  
  Shell execution (secure sandbox), process management

- **硬件接口 / Hardware Interfaces**：I2C、SPI（Linux 平台）  
  I2C, SPI (Linux platform)

### 6. 📦 智能 Skill 系統 / Intelligent Skill System

- **Skill 管理 / Skill Management**：安裝、卸載、更新、搜索  
  Install, uninstall, update, search

- **Skill 評分 / Skill Scoring**：多維度評分（代碼質量、性能、安全、文檔等）  
  Multi-dimensional scoring (code quality, performance, security, documentation)

- **Skill 對比 / Skill Comparison**：智能對比已安裝和遠程 Skill，推薦更新  
  Intelligent comparison of installed and remote Skills, update recommendations

- **Skill 搜索 / Skill Search**：全文搜索、標籤過濾、類型篩選  
  Full-text search, tag filtering, type filtering

### 7. 🔄 靈活的運作模式 / Flexible Operation Modes

- **雲端模式 / Cloud Mode**：使用雲端 API，需要 API Key  
  Uses cloud APIs, requires API Key

- **本地模式 / Local Mode**：完全本地運作，不需要 API Key  
  Fully local operation, no API Key required

- **混合模式 / Hybrid Mode**：雲端模型 + 本地記憶庫，或本地模型 + Atlas API 記憶庫  
  Cloud model + local memory, or local model + Atlas API memory

### 8. 🎨 模塊化架構 / Modular Architecture

- **Trait 設計 / Trait Design**：Provider、Channel、Tool、Memory 可插拔  
  Pluggable Provider, Channel, Tool, Memory

- **配置管理 / Configuration Management**：TOML 格式，環境變量覆蓋  
  TOML format, environment variable override

- **錯誤處理 / Error Handling**：anyhow + thiserror，完善的錯誤鏈  
  anyhow + thiserror, comprehensive error chains

- **異步編程 / Async Programming**：基於 tokio，高並發支持  
  Based on tokio, high concurrency support

---

## 📋 功能清單 / Feature List

### API 提供商支持（9 個）/ API Provider Support (9)

| 提供商 / Provider | 模型示例 / Model Examples | 狀態 / Status |
|------------------|--------------------------|--------------|
| **Atlas AI Agent** | atlas-default, atlas-pro | ✅ 推薦 / Recommended |
| **OpenAI** | GPT-4, GPT-3.5 Turbo | ✅ |
| **Google** | Gemini Pro, Gemini Ultra | ✅ |
| **Claude** | Claude 3.5 Sonnet, Claude 3 Opus | ✅ |
| **GLM** | GLM-4, GLM-4-Plus | ✅ |
| **Kimi** | moonshot-v1-8k, moonshot-v1-32k | ✅ |
| **Qwen** | qwen-turbo, qwen-plus | ✅ |
| **DeepSeek** | deepseek-chat, deepseek-coder | ✅ |
| **OpenRouter** | 所有 OpenRouter 模型 / All OpenRouter models | ✅ |

### 本地模型支持 / Local Model Support

- **Qwen 系列 / Qwen Series**：qwen3, qwen2.5, qwen2.5-72b
- **DeepSeek 系列 / DeepSeek Series**：deepseek-r1, deepseek-chat, deepseek-coder
- **GLM 系列 / GLM Series**：GLM-5, GLM-4.7
- **MiniMax**：minimax
- **GPT-OSS-120B**：gpt-oss-120b
- **Llama 系列 / Llama Series**：llama3, llama3.1, llama3.2, llama3.3
- **其他 / Others**：Mistral, Mixtral, Phi3, Gemma, Codellama 等

### 通信通道 / Communication Channels

- **CLI**：命令行交互界面 / Command-line interactive interface
- **Telegram**：長輪詢 + WebSocket / Long polling + WebSocket
- **Discord**：WebSocket Gateway
- **QQ**：WebSocket Gateway
- **釘釘 / DingTalk**：Stream Mode WebSocket
- **飛書 / Feishu**：WebSocket + Bot API

### 記憶系統 / Memory Systems

- **SQLite**：本地 SQLite 記憶庫 / Local SQLite memory
- **Atlas Memory**：仿生神經元向量記憶庫（Python FFI）/ Bionic neural vector memory (Python FFI)
- **Hybrid**：混合記憶系統（SQLite + Atlas）/ Hybrid memory system (SQLite + Atlas)
- **Atlas API**：服務端 API 記憶庫（加密分片存儲）/ Server-side API memory (encrypted fragmented storage)

### 安全機制 / Security Mechanisms

- **Skill 驗證 / Skill Validation**：Manifest 驗證、代碼簽名、危險模式掃描
- **沙箱隔離 / Sandbox Isolation**：文件系統、網絡、環境變量、資源限制
- **加密存儲 / Encrypted Storage**：ChaCha20Poly1305 加密
- **訪問控制 / Access Control**：License Key、操作白名單、速率限制
- **審計日誌 / Audit Logging**：完整操作記錄

### 工具系統 / Tool System

- **文件操作 / File Operations**：讀寫、搜索、監控
- **網絡工具 / Network Tools**：Web 搜索、HTTP 請求
- **系統工具 / System Tools**：Shell 執行（安全沙箱）
- **硬件接口 / Hardware Interfaces**：I2C、SPI（Linux）

### Skill 系統 / Skill System

- **Skill 管理 / Skill Management**：安裝、卸載、更新、搜索
- **Skill 評分 / Skill Scoring**：多維度評分系統
- **Skill 對比 / Skill Comparison**：智能對比和更新推薦
- **Skill 搜索 / Skill Search**：全文搜索、標籤過濾

---

## 🚀 快速開始 / Quick Start

### 前置要求 / Prerequisites

- **Rust** 1.70+：https://rustup.rs/
- **Python** 3.8+（可選，用於 Atlas 記憶庫）/ Optional, for Atlas memory
- **Git**

### 安裝 / Installation

```bash
# 克隆項目 / Clone the repository
git clone https://github.com/Atlas-AIOS/Atlas-AI-Agent.git
cd Atlas-AI-Agent

# 構建項目 / Build the project
cargo build --release

# 運行 / Run
cargo run --release -- agent
```

### 配置 / Configuration

#### 方式 1：配置文件 / Method 1: Configuration File

推薦新手使用 API 版模板（OpenRouter） / For beginners, start with API template:

```bash
# Windows PowerShell
Copy-Item config.example.api.toml "$env:APPDATA\atlas-world\atlas-ai-agent\config\config.toml"
```

創建或編輯 `~/.config/atlas-ai-agent/config.toml` / Create or edit `~/.config/atlas-ai-agent/config.toml`：

```toml
[agent]
provider = "openrouter"
model = "anthropic/claude-sonnet-4-20250514"
api_key = "your_openrouter_api_key"  # 或使用 OPENROUTER_API_KEY

[memory]
backend = "sqlite"  # 或 "atlas", "hybrid", "atlas_api" / or "atlas", "hybrid", "atlas_api"
db_path = "atlas_agent.db"
```

#### 方式 2：環境變量 / Method 2: Environment Variables

```bash
# OpenRouter（推薦 / Recommended）
export OPENROUTER_API_KEY="your_openrouter_api_key"

# 或使用其他提供商 / Or use other providers
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GLM_API_KEY="your_glm_api_key"
# ... 更多見 docs/API_PROVIDERS.md / More see docs/API_PROVIDERS.md
```

### 使用示例 / Usage Examples

```bash
# 互動模式 / Interactive mode
cargo run --release -- agent

# 單次對話 / Single message
cargo run --release -- agent --message "你好"  # or "Hello"

# 啟動 Gateway / Start Gateway
cargo run --release -- gateway

# 查看狀態 / View status
cargo run --release -- status
```

### 本地模式（不需要 API Key）/ Local Mode (No API Key Required)

```toml
[agent]
provider = "local"
model = "qwen2.5"

[agent.local_model]
api_endpoint = "http://localhost:11434"  # Ollama
api_type = "ollama"

[memory]
backend = "sqlite"
db_path = "atlas_agent.db"
```

詳細配置見 [docs/LOCAL_MODE.md](docs/LOCAL_MODE.md) / See [docs/LOCAL_MODE.md](docs/LOCAL_MODE.md) for detailed configuration

模板文件 / Templates:
- `config.example.toml` (default API-first)
- `config.example.api.toml`
- `config.example.local.toml`

### 發布前檢查 / Pre-release Check

```bash
# Fast smoke check
pwsh -File scripts/smoke.ps1

# Benchmark baseline report
pwsh -File scripts/benchmark.ps1
```

完整清單見 [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md)，
驗證矩陣見 [docs/VALIDATION_MATRIX.md](docs/VALIDATION_MATRIX.md)。

---

## 🏗️ 架構設計 / Architecture

### 系統架構 / System Architecture

```
┌─────────────────────────────────────────┐
│         Atlas AI Agent                  │
│  ┌───────────────────────────────────┐  │
│  │  Agent Loop (核心循環)            │  │
│  │  Agent Loop (Core Loop)           │  │
│  └───────────┬───────────────────────┘  │
│              │                           │
│  ┌───────────▼───────────────────────┐  │
│  │  Providers (9 個 API 提供商)        │  │
│  │  Providers (9 API Providers)       │  │
│  └───────────┬───────────────────────┘  │
│              │                           │
│  ┌───────────▼───────────────────────┐  │
│  │  Memory System (4 種記憶庫)        │  │
│  │  Memory System (4 Types)           │  │
│  │  - SQLite                          │  │
│  │  - Atlas Memory (神經元向量)       │  │
│  │  - Atlas Memory (Neural Vector)    │  │
│  │  - Hybrid (混合)                   │  │
│  │  - Hybrid                          │  │
│  │  - Atlas API (服務端)              │  │
│  │  - Atlas API (Server-side)         │  │
│  └───────────┬───────────────────────┘  │
│              │                           │
│  ┌───────────▼───────────────────────┐  │
│  │  Channels (6 個通信通道)           │  │
│  │  Channels (6 Communication)        │  │
│  │  - CLI, Telegram, Discord          │  │
│  │  - QQ, 釘釘, 飛書                  │  │
│  │  - QQ, DingTalk, Feishu            │  │
│  └───────────┬───────────────────────┘  │
│              │                           │
│  ┌───────────▼───────────────────────┐  │
│  │  Tools (文件/網絡/系統/硬件)        │  │
│  │  Tools (File/Network/System/HW)     │  │
│  └───────────┬───────────────────────┘  │
│              │                           │
│  ┌───────────▼───────────────────────┐  │
│  │  Skills (可擴展技能系統)            │  │
│  │  Skills (Extensible Skill System)   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### 記憶系統架構 / Memory System Architecture

```
┌─────────────────────────────────────────┐
│  Atlas Memory Service (服務端 - 閉源)   │
│  Atlas Memory Service (Server - Closed) │
│  ┌───────────────────────────────────┐ │
│  │ 神經元向量資料庫                    │ │
│  │ Neural Vector Database             │ │
│  │ - 完整記憶結構                      │ │
│  │ - Complete Memory Structure        │ │
│  │ - 記憶生成算法（不可見）            │ │
│  │ - Memory Generation (Hidden)       │ │
│  │ - 記憶分類邏輯（不可見）            │ │
│  │ - Memory Classification (Hidden)   │ │
│  │ - 向量檢索算法（不可見）            │ │
│  │ - Vector Retrieval (Hidden)         │ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ 記憶分片引擎                        │ │
│  │ Memory Fragmentation Engine        │ │
│  │ - 將記憶分割成多個片段              │ │
│  │ - Split memory into fragments      │ │
│  │ - 每個片段獨立加密                  │ │
│  │ - Each fragment independently enc. │ │
│  │ - 片段順序打亂                      │ │
│  │ - Fragment order shuffled           │ │
│  └───────────────────────────────────┘ │
└───────────┬─────────────────────────────┘
            │ HTTPS + License Key
            ▼
┌─────────────────────────────────────────┐
│  Atlas-AI-Agent (客戶端 - 開源)          │
│  Atlas-AI-Agent (Client - Open Source)  │
│  ┌───────────────────────────────────┐ │
│  │ API Client SDK                     │ │
│  │ - 發送請求到服務端                 │ │
│  │ - Send requests to server          │ │
│  │ - 接收加密的記憶片段               │ │
│  │ - Receive encrypted fragments      │ │
│  │ - 本地再次加密存儲                 │ │
│  │ - Re-encrypt locally               │ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ 本地加密緩存                       │ │
│  │ Local Encrypted Cache              │ │
│  │ - 分散的記憶片段（.enc 文件）      │ │
│  │ - Fragmented memory (.enc files)   │ │
│  │ - 片段索引（cache_index.json）    │ │
│  │ - Fragment index (cache_index.json)│ │
│  │ - 雙重加密（服務端 + 客戶端）      │ │
│  │ - Double encryption (server+client)│ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### 安全架構 / Security Architecture

```
┌─────────────────────────────────────────┐
│  Skill 驗證層                            │
│  Skill Validation Layer                 │
│  - Manifest 驗證                        │
│  - Manifest Validation                  │
│  - 代碼簽名驗證                          │
│  - Code Signature Verification          │
│  - 危險模式掃描                          │
│  - Dangerous Pattern Scanning           │
│  - 權限檢查                              │
│  - Permission Check                     │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│  Skill 沙箱層                            │
│  Skill Sandbox Layer                    │
│  - 文件系統隔離                          │
│  - File System Isolation                │
│  - 網絡隔離                              │
│  - Network Isolation                    │
│  - 環境變量隔離                          │
│  - Environment Variable Isolation       │
│  - 資源限制（CPU/內存/帶寬）            │
│  - Resource Limits (CPU/Mem/Bandwidth)  │
└───────────┬─────────────────────────────┘
            │
┌───────────▼─────────────────────────────┐
│  基礎安全策略                            │
│  Basic Security Policy                  │
│  - 命令黑名單                            │
│  - Command Blacklist                    │
│  - 路徑限制                              │
│  - Path Restrictions                    │
│  - 工作目錄沙箱                          │
│  - Workspace Directory Sandbox           │
└─────────────────────────────────────────┘
```

---

## 🔍 與 OpenClaw 對比 / Comparison with OpenClaw

> 注 / Note: 本節為架構與能力對比視角，量化性能結論以 `docs/PERFORMANCE_BASELINE.md` 和後續公開基準為準。  
> Quantitative performance claims should be based on `docs/PERFORMANCE_BASELINE.md` and future published benchmarks.

### 功能對比表 / Feature Comparison Table

| 功能 / Feature | Atlas AI Agent | OpenClaw | 說明 / Notes |
|---------------|----------------|----------|-------------|
| **性能 / Performance** | | | |
| 內存占用 / Memory | <5MB | ~50-100MB | Atlas 減少 90%+ / Atlas 90%+ reduction |
| 啟動時間 / Startup | <10ms | ~100-500ms | Atlas 快 10-50 倍 / Atlas 10-50x faster |
| 響應延遲 / Latency | <50ms | ~100-200ms | Atlas 快 2-4 倍 / Atlas 2-4x faster |
| **API 提供商 / API Providers** | | | |
| 支持數量 / Count | 9 個 | ~5-6 個 | Atlas 支持更多 / Atlas supports more |
| Atlas API | ✅ | ❌ | Atlas 獨有 / Atlas exclusive |
| 本地模型 / Local Models | ✅ 完整支持 | ⚠️ 部分支持 | Atlas 支持更全面 / Atlas more comprehensive |
| **記憶系統 / Memory Systems** | | | |
| SQLite | ✅ | ✅ | 兩者都支持 / Both support |
| 神經元向量 / Neural Vector | ✅ Atlas Memory | ❌ | Atlas 獨有 / Atlas exclusive |
| 混合記憶 / Hybrid Memory | ✅ | ❌ | Atlas 獨有 / Atlas exclusive |
| API 記憶庫 / API Memory | ✅ | ❌ | Atlas 獨有 / Atlas exclusive |
| **通信通道 / Channels** | | | |
| CLI | ✅ | ✅ | 兩者都支持 / Both support |
| Telegram | ✅ | ✅ | 兩者都支持 / Both support |
| Discord | ✅ | ✅ | 兩者都支持 / Both support |
| QQ | ✅ WebSocket | ⚠️ 部分支持 | Atlas 完整支持 / Atlas full support |
| 釘釘 / DingTalk | ✅ WebSocket | ❌ | Atlas 獨有 / Atlas exclusive |
| 飛書 / Feishu | ✅ WebSocket | ❌ | Atlas 獨有 / Atlas exclusive |
| **安全機制 / Security** | | | |
| Skill 驗證 / Skill Validation | ✅ 完整 | ⚠️ 基礎 | Atlas 更完善 / Atlas more complete |
| 沙箱隔離 / Sandbox | ✅ 多層 | ⚠️ 基礎 | Atlas 更安全 / Atlas more secure |
| 加密存儲 / Encryption | ✅ ChaCha20Poly1305 | ⚠️ 基礎 | Atlas 更強 / Atlas stronger |
| 訪問控制 / Access Control | ✅ License Key | ❌ | Atlas 獨有 / Atlas exclusive |
| 審計日誌 / Audit Logging | ✅ 完整 | ⚠️ 基礎 | Atlas 更完善 / Atlas more complete |
| **工具系統 / Tools** | | | |
| 文件操作 / File Ops | ✅ | ✅ | 兩者都支持 / Both support |
| 網絡工具 / Network | ✅ | ✅ | 兩者都支持 / Both support |
| 系統工具 / System | ✅ 安全沙箱 | ✅ | Atlas 更安全 / Atlas more secure |
| 硬件接口 / Hardware | ✅ I2C/SPI | ❌ | Atlas 獨有 / Atlas exclusive |
| **Skill 系統 / Skills** | | | |
| Skill 管理 / Management | ✅ | ✅ | 兩者都支持 / Both support |
| Skill 評分 / Scoring | ✅ 多維度 | ⚠️ 基礎 | Atlas 更智能 / Atlas more intelligent |
| Skill 對比 / Comparison | ✅ 智能對比 | ❌ | Atlas 獨有 / Atlas exclusive |
| Skill 搜索 / Search | ✅ 全文搜索 | ⚠️ 基礎 | Atlas 更強大 / Atlas more powerful |
| **運作模式 / Operation Modes** | | | |
| 雲端模式 / Cloud Mode | ✅ | ✅ | 兩者都支持 / Both support |
| 本地模式 / Local Mode | ✅ 完整支持 | ⚠️ 部分支持 | Atlas 支持更全面 / Atlas more comprehensive |
| 混合模式 / Hybrid Mode | ✅ | ❌ | Atlas 獨有 / Atlas exclusive |
| **架構設計 / Architecture** | | | |
| 語言 / Language | Rust | Python/Go | Atlas 性能更優 / Atlas better performance |
| 模塊化 / Modularity | ✅ Trait 設計 | ⚠️ 部分模塊化 | Atlas 更靈活 / Atlas more flexible |
| 配置管理 / Config | ✅ TOML | ⚠️ 多種格式 | Atlas 更統一 / Atlas more unified |
| 錯誤處理 / Error Handling | ✅ anyhow | ⚠️ 基礎 | Atlas 更完善 / Atlas more complete |
| **文檔 / Documentation** | | | |
| API 文檔 / API Docs | ✅ 完整 | ⚠️ 部分 | Atlas 更完善 / Atlas more complete |
| 安全文檔 / Security Docs | ✅ 詳細 | ⚠️ 基礎 | Atlas 更詳細 / Atlas more detailed |
| 配置指南 / Config Guide | ✅ 詳細 | ⚠️ 基礎 | Atlas 更詳細 / Atlas more detailed |

### 核心優勢總結 / Core Advantages Summary

#### 1. 性能優勢 / Performance Advantages
- **內存占用減少 90%+ / Memory Reduction 90%+**：<5MB vs ~50-100MB
- **啟動時間快 10-50 倍 / Startup 10-50x Faster**：<10ms vs ~100-500ms
- **響應延遲快 2-4 倍 / Latency 2-4x Faster**：<50ms vs ~100-200ms

#### 2. 功能優勢 / Feature Advantages
- **9 大 API 提供商 / 9 Major API Providers**：比 OpenClaw 多 50%+ / 50%+ more than OpenClaw
- **4 種記憶系統 / 4 Memory Systems**：SQLite、Atlas Memory、Hybrid、Atlas API
- **6 個通信通道 / 6 Communication Channels**：包括 QQ、釘釘、飛書（WebSocket）/ Including QQ, DingTalk, Feishu (WebSocket)
- **完整本地支持 / Full Local Support**：Ollama、LM Studio、vLLM、TGI

#### 3. 安全優勢 / Security Advantages
- **多層安全機制 / Multi-Layered Security**：驗證、沙箱、加密、訪問控制、審計 / Validation, sandbox, encryption, access control, audit
- **Skill 評分系統 / Skill Scoring System**：多維度評分，智能對比 / Multi-dimensional scoring, intelligent comparison
- **加密存儲 / Encrypted Storage**：ChaCha20Poly1305 加密 / ChaCha20Poly1305 encryption
- **License Key**：訪問控制和商業保護 / Access control and commercial protection

#### 4. 架構優勢 / Architecture Advantages
- **Rust 語言 / Rust Language**：性能優、內存安全、類型安全 / Excellent performance, memory safety, type safety
- **Trait 設計 / Trait Design**：可插拔、易擴展 / Pluggable, easily extensible
- **模塊化架構 / Modular Architecture**：清晰的模塊邊界 / Clear module boundaries
- **完整文檔 / Complete Documentation**：詳細的 API 文檔、安全文檔、配置指南 / Detailed API docs, security docs, config guides

#### 5. 獨有功能 / Exclusive Features
- **Atlas 神經元向量記憶庫 / Atlas Neural Vector Memory**：仿生人腦記憶結構 / Bionic human brain memory structure
- **Atlas API 服務 / Atlas API Service**：自己的 API 服務，OpenAI 兼容 / Own API service, OpenAI compatible
- **Skill 智能對比 / Skill Intelligent Comparison**：自動對比和更新推薦 / Automatic comparison and update recommendations
- **混合記憶系統 / Hybrid Memory System**：SQLite + Atlas 混合 / SQLite + Atlas hybrid
- **完整 WebSocket 支持 / Full WebSocket Support**：QQ、釘釘、飛書 / QQ, DingTalk, Feishu

### 適用場景對比 / Use Case Comparison

| 場景 / Scenario | Atlas AI Agent | OpenClaw |
|----------------|----------------|----------|
| **高性能需求 / High Performance** | ✅ 推薦 | ⚠️ 一般 |
| **低內存環境 / Low Memory** | ✅ 推薦 | ❌ 不推薦 |
| **中國平台 / Chinese Platforms** | ✅ 完整支持 | ⚠️ 部分支持 |
| **本地部署 / Local Deployment** | ✅ 完整支持 | ⚠️ 部分支持 |
| **企業安全 / Enterprise Security** | ✅ 推薦 | ⚠️ 一般 |
| **快速原型 / Rapid Prototyping** | ✅ 推薦 | ✅ 推薦 |
| **社區生態 / Community Ecosystem** | ⚠️ 新項目 | ✅ 成熟 |

---

## 📚 文檔導航 / Documentation

### 核心文檔 / Core Documentation

- **[API 提供商配置指南 / API Provider Configuration Guide](docs/API_PROVIDERS.md)**：9 大 API 提供商的詳細配置 / Detailed configuration for 9 major API providers
- **[本地模式配置指南 / Local Mode Configuration Guide](docs/LOCAL_MODE.md)**：完全本地運作模式配置 / Fully local operation mode configuration
- **[支持的模型列表 / Supported Models List](docs/SUPPORTED_MODELS.md)**：所有支持的模型和部署方式 / All supported models and deployment methods
- **[安全機制文檔 / Security Documentation](docs/SECURITY.md)**：完整的安全機制說明 / Complete security mechanism documentation
- **[記憶庫保護策略 / Memory Protection Strategy](docs/PROTECTION_STRATEGY.md)**：神經元向量資料庫保護方案 / Neural vector database protection strategy
- **[Atlas API 架構設計 / Atlas API Architecture](docs/ATLAS_API_ARCHITECTURE.md)**：服務端 API 架構 / Server-side API architecture
- **[性能基線報告 / Performance Baseline](docs/PERFORMANCE_BASELINE.md)**：本機可重複性能測量輸出 / Reproducible local benchmark output
- **[驗證矩陣 / Validation Matrix](docs/VALIDATION_MATRIX.md)**：功能實作與驗證覆蓋狀態 / Implementation and verification coverage
- **[發布檢查清單 / Release Checklist](docs/RELEASE_CHECKLIST.md)**：發布前必跑項目 / Pre-release gate checklist

---

## 👥 開發團隊 / Development Team

**Atlas AI Agent** 由以下團隊開發和維護：  
**Atlas AI Agent** is developed and maintained by the following teams:

### 兩岸聯速人工智能研究院
**Cross-Strait United AI Research Institute**

致力於推動兩岸人工智能技術交流與合作，專注於 AI 助手框架、神經網絡、自然語言處理等領域的研究與開發。

Dedicated to promoting cross-strait AI technology exchange and cooperation, focusing on research and development in AI assistant frameworks, neural networks, natural language processing, and related fields.

### 阿忒拉斯(深圳)智能科技有限公司
**Atlas (Shenzhen) Intelligent Technology Co., Ltd.**

專注於 AI 助手框架、智能記憶系統、企業級 AI 解決方案的研發與應用。

Focused on the research, development, and application of AI assistant frameworks, intelligent memory systems, and enterprise-grade AI solutions.

---

## 📄 許可證 / License

本項目採用 **MIT 許可證**，詳見 [LICENSE](LICENSE) 文件。

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

### 許可證說明 / License Notes

- **開源部分 / Open Source Part**：Agent 框架、Channels、Tools、基礎記憶庫（MIT License）  
  Agent framework, Channels, Tools, basic memory (MIT License)

- **商業部分 / Commercial Part**：Atlas 神經元向量記憶庫（專有許可證，需要 License Key）  
  Atlas neural vector memory (Proprietary License, requires License Key)

---

## 🤝 貢獻 / Contributing

歡迎貢獻！請查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解貢獻指南。

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

### 貢獻方式 / Ways to Contribute

- 🐛 **報告 Bug / Report Bugs**：在 [Issues](https://github.com/atlas-world/atlas-ai-agent/issues) 中報告  
  Report in [Issues](https://github.com/atlas-world/atlas-ai-agent/issues)

- 💡 **提出建議 / Suggest Ideas**：在 [Discussions](https://github.com/atlas-world/atlas-ai-agent/discussions) 中討論  
  Discuss in [Discussions](https://github.com/atlas-world/atlas-ai-agent/discussions)

- 📝 **改進文檔 / Improve Documentation**：提交 Pull Request  
  Submit Pull Request

- 🔧 **修復 Bug / Fix Bugs**：提交 Pull Request  
  Submit Pull Request

- ✨ **新功能 / New Features**：提交 Pull Request  
  Submit Pull Request

---

## 📞 聯繫我們 / Contact Us

- **GitHub**：https://github.com/Atlas-AIOS
- **項目倉庫 / Repository**：https://github.com/Atlas-AIOS/Atlas-AI-Agent
- **Issues**：https://github.com/Atlas-AIOS/Atlas-AI-Agent/issues
- **Discussions**：https://github.com/Atlas-AIOS/Atlas-AI-Agent/discussions
- **Email / 郵箱**：RyanX@atlas-ai.tw

---

## ⭐ Star History

如果這個項目對你有幫助，請給我們一個 Star ⭐！

If this project helps you, please give us a Star ⭐!

---

<div align="center">

**Made with ❤️ by 兩岸聯速人工智能研究院 / 阿忒拉斯(深圳)智能科技有限公司**  
**Made with ❤️ by Cross-Strait United AI Research Institute / Atlas (Shenzhen) Intelligent Technology Co., Ltd.**

**Atlas AI Agent - 打造最強的 AI-Agent 框架**  
**Atlas AI Agent - Building the Most Powerful AI-Agent Framework**

</div>
