<p align="center">
  <img src="https://raw.githubusercontent.com/ECTROX/ECTROXClaw/main/assets/ectrox_logo.png" width="200" alt="ECTROXClaw Logo">
</p>

<h1 align="center">ECTROXClaw</h1>

<p align="center">
  <strong>Evolutionary Cognitive Technological Recursive Organism X</strong><br>
  The First Truly Autonomous AI Agent - That Pays You
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Rust-1.70%2B-orange?logo=rust" alt="Rust">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
  <img src="https://img.shields.io/badge/Version-0.1.0-green" alt="Version">
  <img src="https://img.shields.io/badge/AXI-Integrated-purple" alt="AXI">
</p>

---

## 🎯 What is ECTROXClaw?

ECTROXClaw is the next-generation autonomous AI agent framework built in **Rust**, designed to be:

- **Evolutionary** - Self-improving through recursive optimization
- **Cognitive** - Powered by causal memory and multi-model support
- **Technological** - Built with Rust for performance and safety
- **Recursive** - Agent swarm that learns from itself
- **Organism** - A living digital entity, not just a tool
- **X** - Unlimited potential for growth

> "The First Truly Autonomous AI Agent - That Pays You"

---

## 🆚 Comparison with Other Claw Frameworks

| Feature | **ECTROXClaw** | OpenClaw | IronClaw | NanoClaw | ZeroClaw |
|---------|---------------|----------|----------|----------|----------|
| **Language** | Rust | TypeScript | Rust | TypeScript | Rust |
| **GitHub Stars** | 🆕 New | 246K+ | 5.5K+ | Growing | 22.2K+ |
| **Memory Usage** | ~50MB | 394MB-1.5GB | ~100MB | ~50MB | <5MB |
| **Installation** | One-line | Complex (70+ deps) | One-line | Simple | One-line |
| **Multi-Agent** | ✅ 8 Agents | ❌ | ✅ Swarms | ✅ Swarms | ✅ |
| **Auto-Earning** | ✅ AXI Token | ❌ | ❌ | ❌ | ❌ |
| **Causal Memory** | ✅ Lite | ❌ | ❌ | ❌ | ❌ |
| **8 Platforms** | ✅ | 15+ | 4+ | 4+ | 15+ |
| **Windows GUI** | 🚧 Roadmap | ❌ | ✅ | ❌ | ❌ |
| **Mobile App** | 🚧 Roadmap | ❌ | ❌ | ❌ | ❌ |
| **Earn Crypto** | ✅ | ❌ | ❌ | ❌ | ❌ |

### Why ECTROXClaw?

**vs OpenClaw (246K⭐)**
- ✅ Easier installation (one-line vs 70+ dependencies)
- ✅ Lower memory (~50MB vs 394MB-1.5GB)
- ✅ Built-in earning (AXI token rewards)
- ❌ Smaller ecosystem (for now)

**vs IronClaw (5.5K⭐)**
- ✅ Auto-earning with AXI tokens
- ✅ Causal memory engine
- ✅ 8 platforms out-of-box
- ✅ Better for beginners
- ❌ IronClaw has better security docs

**vs NanoClaw**
- ✅ Multi-model support (not just Claude)
- ✅ More platforms (8 vs 4)
- ✅ Crypto earning integration
- ❌ NanoClaw is simpler (500 lines)

**vs ZeroClaw (22.2K⭐)**
- ✅ Earn crypto while using
- ✅ Causal memory
- ✅ Multi-agent collaboration
- ❌ ZeroClaw is lighter (<5MB)

---

## 🚀 Core Features

### 🤖 Multi-Agent System
- **Agent Swarm** - 8 agents working in parallel with tmux + worktree
- **Collaborative Intelligence** - Agents share context and coordinate tasks
- **Auto-scaling** - Dynamically spawn agents based on workload

### 🧠 Causal Memory Engine (Lite)
- **Short-term Memory** - Session-level context retention
- **Medium-term Memory** - Project-level knowledge accumulation  
- **Long-term Memory** - User preference learning
- **Causal Reasoning** - Understand *why*, not just *what*

### 💬 Communication Hub (8 Platforms)

**International (4):**
- Telegram
- WhatsApp
- Element X (Matrix)
- Discord

**China (4):**
- WeChat (微信)
- QQ
- DingTalk (钉钉)
- Feishu (飞书)

### 🤖 Full Automation (ChatGPT 5.4 Level)
- **Browser Control** - Playwright-based web automation
- **Computer Control** - Mouse/keyboard simulation
- **Task Automation** - Three modes: Assist / Semi-Auto / Full-Auto
- **Screen Understanding** - See and interact with UI elements

### 💰 Earn While You Sleep (Automaton Integration)
- **Auto-Trading** - User-authorized financial operations
- **Content Creation** - Automated blogging/social media with monetization
- **Data Services** - Provide data collection as a service
- **AXI Token Rewards** - Earn AXI for compute contributions

### 🪙 AXI Token Integration
- **Built-in Wallet** - Secure AXI token management
- **Auto-Earning** - Get paid for agent tasks
- **Compute Market** - Rent your idle CPU/GPU for AXI
- **Gas-less Transactions** - Within ECTROX ecosystem

### 🔒 Security First
- **WASM Sandbox** - Isolated code execution
- **Permission Levels** - Granular access control
- **Audit Trail** - Full operation logging
- **Encrypted Storage** - Secure credential management

---

## 📦 Installation

### One-Line Install (Linux/macOS/WSL)
```bash
curl -fsSL https://ectrox.com/install.sh | sh
```

### From Source (Rust Required)
```bash
git clone https://github.com/ECTROX/ECTROXClaw.git
cd ECTROXClaw
cargo build --release
./target/release/ectroxclaw --init
```

### Windows (Coming Soon)
```powershell
irm https://ectrox.com/install.ps1 | iex
```

### Android/iOS (Roadmap)
Mobile versions planned for Phase 3.

---

## 🚀 Quick Start

### 1. Initialize
```bash
ectroxclaw init
# Generates wallet, configures defaults
```

### 2. Configure Platforms
```bash
# Interactive setup for Telegram, Discord, WeChat, etc.
ectroxclaw config --platforms
```

### 3. Start Earning
```bash
# Enable automaton mode
ectroxclaw automaton --enable

# Watch your AXI balance grow
ectroxclaw wallet balance
```

---

## 🏗️ Architecture

```
ECTROXClaw
├── Core (Rust)
│   ├── Agent Swarm Manager (8 agents)
│   ├── Causal Memory Engine
│   └── Security Sandbox
├── Adapters
│   ├── Model Router (OpenAI/Claude/Qwen / DeepSeek / Kimi)
│   ├── Platform Hub (8 platforms)
│   └── Automation Layer
├── AXI Integration
│   ├── Wallet
│   ├── Compute Market
│   └── Task Rewards
└── UI
    ├── TUI (Terminal)
    ├── GUI (Desktop - Roadmap)
    └── Mobile (Roadmap)
```

---

## 🗺️ Roadmap

### Phase 1 (Current) - CLI Core
- [x] Rust multi-agent framework (8 agents)
- [x] 8-platform communication
- [x] Causal memory (Lite)
- [x] AXI integration
- [x] Browser automation

### Phase 2 (T+2M) - Desktop & Windows
- [ ] Native Windows support
- [ ] GUI application (Tauri)
- [ ] One-click installers

### Phase 3 (T+6M) - Mobile
- [ ] Android App
- [ ] iOS App (TestFlight)

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

<p align="center">
  <strong>Join the Evolution</strong><br>
  <a href="https://ectrox.com">Website</a> •
  <a href="https://discord.gg/ectrox">Discord</a> •
  <a href="https://t.me/ectrox">Telegram</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/ECTROX/ECTROXClaw/main/assets/ectrox_logo_small.png" width="50">
</p>

---

**References:**
- OpenClaw: https://github.com/openclaw/openclaw (246K⭐)
- IronClaw: https://github.com/nearai/ironclaw (5.5K⭐)
- NanoClaw: https://github.com/qwibitai/nanoclaw
- ZeroClaw: https://github.com/zeroclaw-labs/zeroclaw (22.2K⭐)
