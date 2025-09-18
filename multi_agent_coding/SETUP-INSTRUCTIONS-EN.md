# Multi-AI Setup Instructions

## What's copied in this folder
```
.claude/                    # Complete Claude Code configuration
├── commands/              # 9 slash commands for AI routing
├── CLAUDE.md             # SuperClaude configuration
├── COMMANDS.md           # Command system
├── FLAGS.md              # Flags and options
├── MCP.md                # MCP servers
├── PERSONAS.md           # AI personas
├── ORCHESTRATOR.md       # Smart routing
├── MODES.md              # Operation modes
├── PRINCIPLES.md         # Development principles
└── RULES.md              # Operation rules
```

## Installation on New Machine

### 1. Install Dependencies
```bash
# Node.js (v16.0.0+)
node --version

# Claude Code CLI
# Follow official installation instructions
```

### 2. Install MCP Servers
```bash
# Core MCP servers (auto-installed on first use)
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g @upstash/context7-mcp
npm install -g @21st-dev/magic
npm install -g @playwright/mcp

# Additional AI models
npm install -g gemini-mcp-tool
npm install -g qwen-mcp-tool

# Kubernetes (if needed)
pip install kubectl-mcp-tool
```

### 3. Copy Configuration
```bash
# Copy .claude folder to home directory
cp -r .claude ~/

# OPTION A: Automatic setup (recommended)
claude --mcp-config mcp-config.json

# OPTION B: Manual setup of each server
claude mcp add -s local sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking
claude mcp add -s local context7 -- npx -y @upstash/context7-mcp
claude mcp add -s local magic -- npx -y @21st-dev/magic
claude mcp add -s local playwright -- npx -y @playwright/mcp@latest
claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool
claude mcp add -s local qwen-cli -- npx -y qwen-mcp-tool

# Kubernetes (optional)
claude mcp add -s local kubernetes -- python3 -m kubectl_mcp_tool.mcp_server
```

### 4. Verify Installation
```bash
# Check MCP servers
claude mcp list

# Should show:
# ✅ sequential-thinking: @modelcontextprotocol/server-sequential-thinking
# ✅ context7: @upstash/context7-mcp
# ✅ magic: @21st-dev/magic
# ✅ playwright: @playwright/mcp@latest
# ✅ gemini-cli: gemini-mcp-tool
# ✅ qwen-cli: qwen-mcp-tool
# ✅ kubernetes: kubectl_mcp_tool.mcp_server (optional)
```

### 5. Test Slash Commands
```bash
# AI tool recommendations
/ai-help

# Quick analysis
/qwen-quick "what is a closure in JavaScript?"

# Large file deep analysis
/gemini-analyze sample_code.py "security issues"

# Multi-AI code review
/code-review sample_code.py security
```

## Available Commands

### Core Commands
- `/ai-help [file|task] [type]` - AI tool recommendations
- `/ai-route [analyze|debug|quick|format] [file] [context]` - Smart routing
- `/cost-optimize [task]` - Cost-effective routing

### Analysis Commands
- `/gemini-analyze [file] [focus]` - Deep analysis of large files
- `/qwen-quick [question]` - Fast responses
- `/code-review [file] [security|performance|quality|all]` - Multi-AI review

### Specialized Commands
- `/debug-issue [file] [error] [context]` - Systematic debugging
- `/optimize-performance [file] [speed|memory|both]` - Performance optimization
- `/analyze-architecture [dir] [focus]` - Architectural analysis

## Routing Logic

### By File Size
- **>1000 lines**: Gemini (extended context)
- **100-1000 lines**: Smart routing
- **<100 lines**: Qwen (fast and efficient)

### By Task Type
- **Debug**: Sequential thinking (systematic)
- **Quick questions**: Qwen
- **Architecture**: Gemini
- **Token savings**: Qwen → Gemini → Claude

## Benefits
- 🔥 **Token savings**: ~50% through smart routing
- 🧠 **Specialization**: Each AI for its optimal tasks
- 📚 **Extended context**: Gemini for large files
- 💰 **Cost optimization**: Free models first
- 🎯 **Unified interface**: Everything through Claude Code UI

## Troubleshooting

### MCP servers not connecting
```bash
claude mcp list
# Find failed server and restart:
claude mcp remove [server-name] -s local
claude mcp add -s local [server-name] -- [command]
```

### Commands not working
```bash
ls ~/.claude/commands/
chmod +x ~/.claude/commands/*.md
```

### Need to reinstall MCP servers
```bash
npm uninstall -g gemini-mcp-tool qwen-mcp-tool
npm install -g gemini-mcp-tool qwen-mcp-tool
claude mcp list
```

**Done!** Now you have a full-featured multi-AI system in Claude Code! 🚀

## Additional Resources

📖 **MCP-SETUP-GUIDE-EN.md** - Comprehensive guide to all MCP servers:
- Purpose of each server
- Step-by-step setup
- Authentication and troubleshooting
- Commands and usage examples