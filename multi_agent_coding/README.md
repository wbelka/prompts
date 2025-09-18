# Multi-AI Setup for Claude Code

Transform Claude Code from a single-model tool into a multi-AI orchestration platform. Access Gemini's massive context window, specialized AI models, and powerful tools—all within Claude Code's familiar interface.

## 🎯 The Problem: Single-Model Limitations

Every developer using AI tools faces these challenges:

- **Token depletion** during critical debugging sessions
- **Context window limitations** when analyzing large codebases
- **Cost accumulation** on tasks that could use free alternatives
- **Model limitations** where one AI excels but others struggle
- **Vendor lock-in** restricting workflow flexibility

## 🔗 The Solution: MCP Server Integration

Model Context Protocol (MCP) servers transform Claude Code into a multi-AI platform. Think of MCP servers as specialized connectors that let Claude Code communicate with any AI service or tool.

**Architecture**: Claude Code UI → Slash Command → MCP Server → External AI → Results

This means you can:
- Use slash commands to access different AI models
- Stay in Claude Code UI while leveraging specialized tools
- Offload routine tasks to appropriate models
- Access specialized capabilities without switching interfaces

## 📦 What's Included

```
📦 Multi-AI Claude Code Setup
├── 📁 .claude/                    # Clean configuration (9 slash commands)
├── 📄 mcp-config.json            # Configuration for all 7 MCP servers
├── 📖 SETUP-INSTRUCTIONS.md      # Quick setup guide
├── 📖 MCP-SETUP-GUIDE.md         # Detailed MCP server guide
├── 📖 PRIVACY-NOTES.md           # What was cleaned for sharing
├── 📖 CLAUDE.md                  # Session context
└── 🐍 sample_code.py             # Test file with issues
```

### 🧠 AI Models & Tools

**Core MCP Servers**:
- **Sequential Thinking** - Complex multi-step analysis
- **Context7** - Library documentation and best practices
- **Magic** - UI component generation (21st.dev)
- **Playwright** - Browser automation and E2E testing

**Additional AI Models**:
- **Gemini CLI** - Extended context window for large files
- **Qwen CLI** - Fast, efficient analysis
- **Kubernetes** - Cluster management (optional)

### ⚡ Smart Routing Commands

**Intelligent AI Selection**:
- `/ai-route [analyze|debug|quick|format] [file] [context]` - Smart routing to best AI
- `/cost-optimize [task]` - Try free models first, escalate if needed
- `/ai-help [file|task] [type]` - Get AI tool recommendations

**Specialized Workflows**:
- `/code-review [file] [security|performance|quality|all]` - Multi-AI code review
- `/debug-issue [file] [error] [context]` - Systematic debugging pipeline
- `/optimize-performance [file] [speed|memory|both]` - Performance optimization
- `/analyze-architecture [dir] [focus]` - Architecture analysis with Gemini

**Direct AI Access**:
- `/gemini-analyze [file] [focus]` - Large file analysis with extended context
- `/qwen-quick [question]` - Fast responses for simple queries

## 🚀 Quick Setup

### Prerequisites
```bash
node --version  # v16.0.0+
claude --version  # Latest Claude Code CLI
```

### One-Command Setup
```bash
# 1. Copy configuration
cp -r .claude ~/

# 2. Install MCP servers
npm install -g gemini-mcp-tool qwen-mcp-tool

# 3. Configure all servers at once
claude --mcp-config mcp-config.json

# 4. Test
claude mcp list
```

### Verify Installation
```bash
# Should see all servers connected:
# ✅ sequential-thinking
# ✅ context7
# ✅ magic
# ✅ playwright
# ✅ gemini-cli
# ✅ qwen-cli
```

## 💡 Smart Routing Logic

### File Size Based
- **Large files (>1000 lines)**: Gemini (extended context)
- **Medium files (100-1000)**: Intelligent routing
- **Small files (<100)**: Qwen (efficient)

### Task Type Based
- **Debug/Error**: Sequential thinking (systematic)
- **Quick/Format**: Qwen (fast)
- **Architecture**: Gemini (comprehensive)
- **Cost-sensitive**: Try Qwen → Gemini → Claude fallback

## 📊 Benefits

- 🔥 **Token Savings**: ~50% through intelligent routing
- 🧠 **Specialization**: Each AI optimized for specific tasks
- 📚 **Extended Context**: Gemini for large codebases
- 💰 **Cost Optimization**: Free models first, premium as needed
- 🎯 **Unified Interface**: Everything through Claude Code UI

## 🧪 Example Usage

```bash
# Get recommendations
/ai-help large_file.py analyze

# Quick analysis
/qwen-quick "explain this regex pattern"

# Large file deep analysis
/gemini-analyze microservice.py "performance bottlenecks"

# Multi-perspective code review
/code-review auth.py security

# Systematic debugging
/debug-issue api.py "500 internal server error" "happens on POST requests"

# Architecture analysis
/analyze-architecture src/ scalability
```

## 🔧 Detailed Setup

For comprehensive setup instructions including:
- Step-by-step MCP server installation
- Authentication for each service
- Troubleshooting common issues
- Advanced usage patterns

See: **[MCP-SETUP-GUIDE.md](./MCP-SETUP-GUIDE.md)**

## 🛡️ Privacy & Security

This configuration has been cleaned for public sharing:
- ❌ No personal data, logs, or system paths
- ❌ No API keys or credentials
- ❌ No usage history or cache files
- ✅ Only generic configuration and commands

See: **[PRIVACY-NOTES.md](./PRIVACY-NOTES.md)** for details.

## 🆘 Troubleshooting

### MCP servers not connecting
```bash
claude mcp list
# Restart problematic servers
claude mcp remove [server-name] -s local
claude mcp add -s local [server-name] -- [command]
```

### Commands not working
```bash
ls ~/.claude/commands/
chmod +x ~/.claude/commands/*.md
```

### Need to reinstall everything
```bash
npm uninstall -g gemini-mcp-tool qwen-mcp-tool
npm install -g gemini-mcp-tool qwen-mcp-tool
claude mcp list
```

## 🎯 Real-World Use Cases

### Large-Scale Refactoring
```bash
# 1. Repository exploration with intelligent context
/ai-route analyze . "deprecated patterns"

# 2. Architecture planning with extended context
/gemini-analyze legacy_system.py "migration strategy"

# 3. Systematic implementation
# Sequential thinking coordinates the refactoring process
```

### Security Audit Workflow
```bash
# 1. Pattern detection across codebase
/code-review . security

# 2. Vulnerability analysis with specialized focus
/debug-issue auth.py "potential security issues"

# 3. Architecture review with comprehensive context
/analyze-architecture . security
```

### Performance Optimization
```bash
# 1. Bottleneck identification
/optimize-performance api/ speed

# 2. Algorithm analysis with extended context
/gemini-analyze slow_function.py "optimization opportunities"

# 3. Implementation with smart routing
/ai-route implement . "optimized algorithms"
```

## 🚀 Getting Started

1. **Copy this repository** to your machine
2. **Run the quick setup** commands above
3. **Test with sample file**: `/code-review sample_code.py security`
4. **Explore slash commands**: `/ai-help`

**Ready to transform your Claude Code experience!** 🎉