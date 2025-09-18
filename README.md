# Multi-Agent AI-Powered Software Development Framework

This project provides a sophisticated framework for leveraging multiple AI models to automate and assist in various software development tasks. It showcases a multi-agent system that can be orchestrated to perform complex workflows, such as a full CI/CD pipeline for a Java application.

## 🚀 Project Overview

This repository is structured into two main components:

1.  **`multi_agent_coding`**: The core of the project, this directory contains a "Multi-AI Setup for Claude Code". It uses a Model Context Protocol (MCP) to integrate various AI models like Gemini and Qwen directly into the Claude Code environment. This allows for intelligent routing of tasks to the most suitable AI model, optimizing for cost, performance, and context window size.

2.  **`cicd_aitool`**: This directory contains a practical example of the multi-agent system in action. It's an interactive HTML page that visualizes a CI/CD pipeline for a Java application, where each step of the pipeline is handled by a specialized AI agent.

## ✨ Features

*   **Multi-AI Integration**: Seamlessly switch between different AI models (Claude, Gemini, Qwen) within a unified interface.
*   **Intelligent Task Routing**: An advanced orchestration engine analyzes user requests and automatically routes them to the most appropriate AI model or tool.
*   **CI/CD Pipeline Automation**: A complete, interactive example of a CI/CD pipeline for a Java application, orchestrated by a team of specialized AI agents.
*   **Extensible Framework**: The Model Context Protocol (MCP) allows for the integration of new AI models and tools.
*   **Comprehensive Documentation**: The project includes detailed documentation on the architecture, protocols, and setup instructions.

## 📂 Project Structure

```
.
├── cicd_aitool/
│   └── HOWTO_CICDJAVA_WITH_CLAUDE.html  # Interactive CI/CD pipeline visualization
├── multi_agent_coding/
│   ├── .claude/                         # Configuration files for the multi-agent system
│   ├── mcp-config.json                  # MCP server configuration
│   ├── README.md                        # Detailed README for the multi-agent setup
│   └── ...
└── prompts/
    └── MotherOfPrompts.md
```

## 🛠️ Getting Started

To get started with the multi-agent coding setup, please refer to the detailed instructions in the `multi_agent_coding` directory.

1.  **Navigate to the `multi_agent_coding` directory:**
    ```bash
    cd multi_agent_coding
    ```

2.  **Follow the setup instructions:**
    Open the `README.md` file in this directory for a complete guide on how to install the necessary tools, configure the MCP servers, and start using the multi-AI capabilities.

## 💡 Usage

### Multi-Agent Coding

Once the setup is complete, you can use the new slash commands in your Claude Code environment to interact with the multi-agent system. For example:

*   **`/ai-route [task]`**: Let the orchestrator choose the best AI for your task.
*   **`/gemini-analyze [file]`**: Analyze a large file using Gemini's extended context window.
*   **`/code-review [file]`**: Perform a code review using multiple AI models for a comprehensive analysis.

For a full list of commands and their usage, please see the `multi_agent_coding/README.md` file.

### CI/CD Pipeline Visualization

To explore the CI/CD pipeline example, open the `cicd_aitool/HOWTO_CICDJAVA_WITH_CLAUDE.html` file in your web browser. You can click on each step of the pipeline to see the details of the AI agent responsible for that task.

