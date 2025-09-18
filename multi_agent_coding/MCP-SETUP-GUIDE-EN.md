# MCP Servers Setup Guide

Comprehensive guide to setting up all MCP servers for Claude Code multi-AI integration.

## What is MCP?

**Model Context Protocol (MCP)** is a standardized protocol for integrating external tools and AI models with Claude Code. Each MCP server provides specialized capabilities:

## MCP Servers Overview

### 🧠 Sequential Thinking
- **Purpose**: Complex multi-step analysis and systematic problem solving
- **When to use**: Complex debugging, architectural planning, systematic issue resolution
- **Activation**: Automatic with `--think`, `--think-hard`, `--ultrathink` flags
- **Benefits**: Structured reasoning, comprehensive analysis, logical progression

### 📚 Context7
- **Purpose**: Library documentation and framework best practices
- **When to use**: Official documentation lookup, code examples, best practices research
- **Activation**: Automatic with library imports, `/document`, `/explain` commands
- **Benefits**: Up-to-date docs, official examples, framework-specific guidance

### 🎨 Magic (21st.dev)
- **Purpose**: Modern UI component generation and design systems
- **When to use**: Creating React/Vue/Angular components, design system integration
- **Activation**: Component requests, `/design` command, frontend tasks
- **Benefits**: Modern components, accessibility compliance, design system integration

### 🎭 Playwright
- **Purpose**: Browser automation, testing, and performance monitoring
- **When to use**: E2E testing, screenshot capture, performance testing, cross-browser validation
- **Activation**: `/test` command, automatic with QA tasks
- **Benefits**: Multi-browser support, visual testing, performance metrics, user simulation

### 🧠 Gemini CLI (Additional)
- **Purpose**: Extended context window for large file analysis
- **When to use**: Files >1000 lines, architectural reviews, comprehensive analysis
- **Commands**: `/gemini-analyze`, `/ai-route analyze`
- **Benefits**: Large context window, free tier available, comprehensive understanding

### ⚡ Qwen CLI (Additional)
- **Purpose**: Fast and efficient analysis for routine tasks
- **When to use**: Code formatting, quick explanations, routine tasks, cost optimization
- **Commands**: `/qwen-quick`, `/cost-optimize`
- **Benefits**: High speed, token savings, efficient processing

### ☸️ Kubernetes (Optional)
- **Purpose**: Kubernetes cluster management and DevOps automation
- **When to use**: DevOps tasks, deployments, cluster monitoring, infrastructure management
- **Commands**: Kubernetes commands through MCP integration
- **Benefits**: Direct cluster access, automated deployments, monitoring integration

## Step-by-Step Installation

### Step 1: Prerequisites
```bash
# Node.js v16.0.0+
node --version

# Python 3.8+ (for Kubernetes MCP)
python3 --version

# Claude Code CLI
claude --version
```

### Step 2: Install Packages
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

### Step 3: Automatic Configuration
```bash
# Copy configurations
cp -r .claude ~/
cp mcp-config.json ~/

# Configure all servers with one command
claude --mcp-config ~/mcp-config.json
```

### Step 4: Manual Configuration (Alternative)
```bash
# Sequential Thinking
claude mcp add -s local sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking

# Context7
claude mcp add -s local context7 -- npx -y @upstash/context7-mcp

# Magic
claude mcp add -s local magic -- npx -y @21st-dev/magic

# Playwright
claude mcp add -s local playwright -- npx -y @playwright/mcp@latest

# Gemini
claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool

# Qwen
claude mcp add -s local qwen-cli -- npx -y qwen-mcp-tool

# Kubernetes (optional)
claude mcp add -s local kubernetes -- python3 -m kubectl_mcp_tool.mcp_server
```

### Step 5: Verification
```bash
# List all servers
claude mcp list

# Expected output:
# ✅ sequential-thinking: Connected
# ✅ context7: Connected
# ✅ magic: Connected
# ✅ playwright: Connected
# ✅ gemini-cli: Connected
# ✅ qwen-cli: Connected
# ✅ kubernetes: Connected (if installed)
```

## Authentication Setup

### Gemini MCP
- **Method**: Google account via OAuth
- **Setup**: Automatic on first use
- **Free tier**: Available
- **Process**: Browser opens for Google authentication

### Qwen MCP
- **Method**: API keys
- **Setup**: Configured through MCP server
- **Limitations**: Depends on plan
- **Process**: API key prompt on first use

### Context7
- **Method**: No authentication required (free)
- **Limitations**: Rate limiting applies
- **Process**: Works immediately

### Other Servers
- **Sequential, Magic, Playwright**: No authentication required
- **Kubernetes**: Uses ~/.kube/config automatically

## Usage Patterns

### Smart Routing Commands
```bash
# Automatic AI selection based on task complexity and file size
/ai-route analyze large_file.py "performance issues"
/cost-optimize "format this JSON file"
/ai-help sample_code.py debug
```

### Direct MCP Usage
```bash
# Sequential Thinking - systematic analysis
sequentialthinking "Analyze authentication flow for security vulnerabilities"

# Context7 - documentation lookup (automatic)
# Activates automatically when mentioning libraries

# Magic - UI components (automatic)
# Activates automatically for frontend requests

# Gemini - large files
/gemini-analyze large_codebase.py "architecture review"

# Qwen - quick tasks
/qwen-quick "explain this regex pattern"
```

### Workflow Examples
```bash
# Multi-AI code review
/code-review auth.py security
# Uses Sequential for analysis, Context7 for security patterns

# Performance optimization pipeline
/optimize-performance api.py speed
# Uses Gemini for analysis, Sequential for systematic optimization

# Architecture analysis
/analyze-architecture src/ scalability
# Uses Gemini for comprehensive analysis, Context7 for patterns
```

## Troubleshooting

### MCP Server Not Connecting
```bash
# Check server status
claude mcp list

# Find problematic server and reinstall
# Example for Gemini:
npm uninstall -g gemini-mcp-tool
npm install -g gemini-mcp-tool
claude mcp remove gemini-cli -s local
claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool
```

### Commands Not Working
```bash
# Check command permissions
ls -la ~/.claude/commands/
chmod +x ~/.claude/commands/*.md

# Restart Claude Code
# Exit and launch again
```

### Gemini Authentication Issues
```bash
# Clear OAuth cache
rm -rf ~/.cache/gemini-mcp-tool/

# Try authentication again
/gemini-cli:ping "test"
```

### Python MCP Servers (Kubernetes)
```bash
# Upgrade if not working
pip install --upgrade kubectl-mcp-tool

# Check KUBECONFIG
echo $KUBECONFIG
# Should point to ~/.kube/config
```

### General Issues
```bash
# Reset all MCP configurations
claude mcp reset-project-choices

# Restart with fresh config
claude --mcp-config mcp-config.json
```

## Advanced Configuration

### Custom MCP Server
```json
{
  "mcpServers": {
    "stdio": {
      "custom-server": {
        "command": "your-command",
        "args": ["--your", "args"],
        "env": {
          "YOUR_ENV": "value"
        }
      }
    }
  }
}
```

### Environment Variables
```bash
# MCP debugging
export ANTHROPIC_LOG=debug

# Custom timeouts
export MCP_TIMEOUT=30000
export MCP_TOOL_TIMEOUT=10000

# Custom config directory
export CLAUDE_CONFIG_DIR=/custom/path
```

### Multiple Config Files
```bash
# Use multiple configurations
claude --mcp-config config1.json config2.json

# Strict mode (only use specified configs)
claude --strict-mcp-config --mcp-config mcp-config.json
```

## Performance Optimization

### Server Selection Strategy
1. **Small tasks**: Qwen CLI (fast, efficient)
2. **Large files**: Gemini CLI (extended context)
3. **Complex analysis**: Sequential Thinking
4. **Documentation**: Context7 (automatic)
5. **UI work**: Magic (automatic)
6. **Testing**: Playwright (automatic)

### Cost Optimization
- Use `/cost-optimize` for automatic free-tier routing
- Qwen CLI for formatting and simple tasks
- Gemini free tier for large file analysis
- Sequential Thinking for complex reasoning

### Token Management
- Smart routing reduces token usage by ~50%
- Free tiers available for Gemini and Context7
- Qwen CLI optimized for efficiency
- Automatic fallback to Claude when needed

## Server Updates

```bash
# Update all npm packages
npm update -g @modelcontextprotocol/server-sequential-thinking
npm update -g @upstash/context7-mcp
npm update -g @21st-dev/magic
npm update -g @playwright/mcp
npm update -g gemini-mcp-tool
npm update -g qwen-mcp-tool

# Update Python packages
pip install --upgrade kubectl-mcp-tool

# Restart Claude Code to apply changes
```

## Benefits of Multi-MCP Setup

1. **Specialization**: Each AI optimized for specific tasks
2. **Cost Savings**: ~50% reduction through intelligent routing
3. **Redundancy**: Alternatives when hitting Claude limits
4. **Extended Capabilities**: Access to specialized tools
5. **Unified Interface**: Everything through Claude Code UI
6. **Scalability**: Easy to add new MCP servers
7. **Flexibility**: Mix of free and premium models

## Security Considerations

- MCP servers run locally or connect to authorized services
- Authentication handled per server (OAuth, API keys)
- No data shared between different MCP servers
- Claude Code manages all communication securely
- Configuration files contain no sensitive data

Ready to supercharge your Claude Code experience! 🚀