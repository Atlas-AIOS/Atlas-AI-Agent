# 快速開始指南 / Quick Start Guide

## ✅ API Key 已驗證

您的 OpenRouter API Key 已成功驗證並可以正常使用！

- **API Key**: `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`
- **狀態**: ✅ 有效
- **可用模型**: `openai/gpt-3.5-turbo` ✅

## 快速測試

### 方法 1: 使用測試腳本（推薦）

```powershell
# 運行 OpenRouter API 測試
.\test_openrouter.ps1
```

### 方法 2: 直接測試 API

```powershell
# 設置環境變量
$env:OPENROUTER_API_KEY = "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"

# 測試 API
$body = @{
    model = "openai/gpt-3.5-turbo"
    messages = @(@{ role = "user"; content = "你好" })
} | ConvertTo-Json -Depth 5

Invoke-RestMethod -Uri "https://openrouter.ai/api/v1/chat/completions" `
    -Headers @{
        Authorization = "Bearer $env:OPENROUTER_API_KEY"
        "Content-Type" = "application/json"
        "HTTP-Referer" = "https://github.com/Atlas-AIOS/Atlas-AI-Agent"
        "X-Title" = "Atlas AI Agent"
    } `
    -Method Post -Body $body
```

### 方法 3: 使用 Atlas AI Agent

```powershell
# 設置環境變量
$env:OPENROUTER_API_KEY = "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"

# 編譯並運行（如果編譯成功）
cargo build --release
cargo run --release -- agent --message "你好"

# 或直接運行（如果已編譯）
cargo run --release -- agent --message "你好"
```

## 配置說明

### 默認配置

項目已配置為使用：
- **Provider**: `openrouter`
- **Model**: `openai/gpt-3.5-turbo`（免費模型）
- **API Key**: 從環境變量 `OPENROUTER_API_KEY` 讀取

### 永久設置環境變量（可選）

```powershell
# 用戶級環境變量（永久）
[System.Environment]::SetEnvironmentVariable(
    "OPENROUTER_API_KEY",
    "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",
    "User"
)

# 重新啟動 PowerShell 後生效
```

### 使用配置文件（可選）

編輯 `~/.config/atlas-ai-agent/config.toml`：

```toml
[agent]
provider = "openrouter"
model = "openai/gpt-3.5-turbo"
api_key = "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"
```

## 可用模型

根據測試結果：

- ✅ `openai/gpt-3.5-turbo` - **可用**（免費）
- ❌ `anthropic/claude-3.5-sonnet` - 需要付費（402 Payment Required）
- ❌ `anthropic/claude-sonnet-4-20250514` - 模型不存在

### 其他可能可用的模型

- `openai/gpt-4` - 可能需要付費
- `google/gemini-pro` - 可能需要付費
- `meta-llama/llama-3-8b-instruct` - 可能需要付費

## 測試結果

```
✅ API Key 驗證成功
✅ 模型 'openai/gpt-3.5-turbo' 測試成功
✅ 回應: "Pong!"
```

## 下一步

1. **如果編譯成功**：直接使用 `cargo run --release -- agent --message "你好"`
2. **如果編譯失敗**：先修復編譯錯誤，然後再測試
3. **測試互動模式**：`cargo run --release -- agent`（無參數）

## 問題排查

如果遇到問題，請參考 `README_TESTING.md` 獲取詳細的故障排除指南。
