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

This setup includes the following components:

```
📦 Multi-AI Claude Code Setup
├── 📁 .claude/                    # Clean configuration (9 slash commands)
├── 📄 mcp-config.json            # Configuration for all 7 MCP servers
├── 📖 SETUP.md                  # This setup guide
├── 📖 PRIVACY-NOTES.md           # What was cleaned for sharing
├── 📖 CLAUDE.md                  # Session context
└── 🐍 sample_code.py             # Test file with issues
```

## 🚀 Setup Instructions

### Step 1: Prerequisites

Before you begin, ensure you have the following prerequisites installed and configured:

#### Core Dependencies
```bash
# Node.js v16.0.0+
node --version

# Python 3.8+ (for Kubernetes MCP)
python3 --version

# Claude Code CLI
claude --version
```

#### External AI Tools

You will also need to have the following AI tools installed and authenticated. These tools provide the connection to the Gemini and Qwen language models.

-   **Gemini MCP Tool (`gemini-mcp-tool`)**
    -   **Installation and Authentication:** Follow the instructions in the official repository to install the tool and authenticate with your Google account.
    -   **GitHub Repository:** [jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)

-   **Qwen MCP Tool (`qwen-mcp-tool`)**
    -   **Installation and Authentication:** Follow the instructions in the official repository to install the tool and configure it with your API keys.
    -   **GitHub Repository:** [Gy920/qwen-mcp-tool](https://github.com/Gy920/qwen-mcp-tool)


### Step 2: Installation

You can choose between a quick automatic setup or a manual setup.

#### Option A: Quick Setup (Recommended)

This single command will copy the configuration, install the necessary MCP servers, and configure them.

```bash
# 1. Copy configuration
cp -r .claude ~/
cp mcp-config.json ~/

# 2. Install MCP servers
npm install -g gemini-mcp-tool qwen-mcp-tool @modelcontextprotocol/server-sequential-thinking @upstash/context7-mcp @21st-dev/magic @playwright/mcp

# 3. Configure all servers at once
claude --mcp-config ~/mcp-config.json
```

#### Option B: Manual Setup

If you prefer to install and configure each server manually, you can use the following commands:

```bash
# Install Core MCP Servers
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g @upstash/context7-mcp
npm install -g @21st-dev/magic
npm install -g @playwright/mcp

# Install Additional AI Models
npm install -g gemini-mcp-tool
npm install -g qwen-mcp-tool

# Install Kubernetes MCP (if needed)
pip install kubectl-mcp-tool

# Configure Servers
claude mcp add -s local sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking
claude mcp add -s local context7 -- npx -y @upstash/context7-mcp
claude mcp add -s local magic -- npx -y @21st-dev/magic
claude mcp add -s local playwright -- npx -y @playwright/mcp@latest
claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool
claude mcp add -s local qwen-cli -- npx -y qwen-mcp-tool
claude mcp add -s local kubernetes -- python3 -m kubectl_mcp_tool.mcp_server # Optional
```

### Step 3: Verification

After installation, verify that all MCP servers are connected:

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

## 🧠 AI Models & Tools Overview

This setup integrates a variety of AI models and tools, each with its own specialization.

### Core MCP Servers
- **Sequential Thinking**: For complex multi-step analysis and systematic problem solving.
- **Context7**: For library documentation and framework best practices.
- **Magic (21st.dev)**: For modern UI component generation and design systems.
- **Playwright**: For browser automation, testing, and performance monitoring.

### Additional AI Models
- **Gemini CLI**: Provides an extended context window for large file analysis.
- **Qwen CLI**: For fast and efficient analysis of routine tasks.
- **Kubernetes**: For Kubernetes cluster management and DevOps automation (optional).

## ⚡ Available Commands

This setup adds a powerful set of slash commands to your Claude Code environment.

### Smart Routing Commands
- `/ai-route [analyze|debug|quick|format] [file] [context]`: Intelligently routes your task to the best AI model.
- `/cost-optimize [task]`: Executes your task using free-tier models first to save costs.
- `/ai-help [file|task] [type]`: Recommends the best AI tool for your specific need.

### Specialized Workflow Commands
- `/code-review [file] [security|performance|quality|all]`: Performs a comprehensive code review using multiple AI models.
- `/debug-issue [file] [error] [context]`: Guides you through a systematic debugging process.
- `/optimize-performance [file] [speed|memory|both]`: Helps you optimize your code for speed and memory usage.
- `/analyze-architecture [dir] [focus]`: Analyzes the architecture of your codebase.

### Direct AI Access Commands
- `/gemini-analyze [file] [focus]`: Sends a file directly to Gemini for in-depth analysis.
- `/qwen-quick [question]`: Gets a fast response from Qwen for simple questions.

## 💡 Multi-Agent Routing Logic

This setup uses a sophisticated multi-agent pipeline to handle tasks, assigning a specific role to each AI based on its strengths.

*   **Gemini (`gemini-mcp`): The Analyst & Architect.** Handles deep analysis, planning, and architectural understanding.
*   **Claude (Native, via `Sequential`): The Coder & Refactorer.** Executes coding and refactoring tasks based on a plan.
*   **Qwen (`qwen-mcp`): The Assistant.** Manages quick, simple tasks like documentation and quick queries.

## 🧪 How to Use the Pipelines (Examples)

The orchestration happens automatically based on the command you use. You don't need to specify the model manually.

### Example 1: Improving Existing Code

When you want to refactor or improve a file, you can use the `/improve` command.

```bash
/improve sample_code.py
```

*   **What happens:**
    1.  **Gemini (Analysis):** Analyzes `sample_code.py` to find security flaws, performance issues, and areas for refactoring. It creates a step-by-step plan.
    2.  **Claude (Implementation):** Receives the plan and systematically modifies the code to implement the proposed improvements.
    3.  **Qwen (Summarization):** (Optional) Can be triggered to generate a summary of the changes or a commit message.

### Example 2: Implementing a New Feature

To implement a new feature, you can use the `/implement` command with a description.

```bash
/implement "a new function to export users to a CSV file"
```

*   **What happens:**
    1.  **Gemini (Planning):** Analyzes the request and the existing codebase (`UserManager` class, etc.). It designs the function and creates a plan for where to add it and how it should work.
    2.  **Claude (Coding):** Takes the plan and writes the new `export_to_csv` function, including necessary imports and error handling.

### Example 3: A Quick Question

For simple, fast questions, you can use `/qwen-quick`.

```bash
/qwen-quick "what does the 'os' module in python do?"
```

*   **What happens:** The query is routed directly to **Qwen** for a fast and efficient answer.

## 🆘 Troubleshooting

If you encounter any issues, here are some common troubleshooting steps.

### MCP Server Not Connecting
```bash
# 1. Check the server status
claude mcp list

# 2. Find the problematic server and reinstall it
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

# Ensure the command files are executable
chmod +x ~/.claude/commands/*.md

# Restart Claude Code
```

### Gemini Authentication Issues
```bash
# Clear the OAuth cache
rm -rf ~/.cache/gemini-mcp-tool/

# Try authenticating again by running a Gemini command
/gemini-analyze sample_code.py "test"
```

