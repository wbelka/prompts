# Multi-AI Setup Context - Claude Code Session

## Completed Setup

### MCP Servers Installed & Configured
- ✅ **Gemini MCP**: `gemini-cli` - Extended context window for large files
- ✅ **Qwen MCP**: `qwen-cli` - Fast, efficient analysis
- ✅ **Sequential Thinking**: Complex systematic analysis
- ✅ **Context7**: Library documentation lookup
- ✅ **Magic**: UI component generation
- ✅ **Playwright**: Browser automation & testing

### Created Slash Commands (in ~/.claude/commands/)
1. **`/gemini-analyze [file] [focus]`** - Large file analysis with Gemini
2. **`/qwen-quick [question]`** - Fast responses with Qwen
3. **`/ai-route [analyze|debug|quick|format] [file] [context]`** - Intelligent routing
4. **`/cost-optimize [task]`** - Try efficient models first
5. **`/ai-help [file|task] [type]`** - Get AI tool recommendations
6. **`/code-review [file] [security|performance|quality|all]`** - Multi-AI code review
7. **`/optimize-performance [file] [speed|memory|both]`** - Performance optimization
8. **`/debug-issue [file] [error] [context]`** - Systematic debugging
9. **`/analyze-architecture [dir] [structure|dependencies|patterns|scalability]`** - Architecture analysis

### Test File Created
- `sample_code.py` - Contains security issues, performance problems, and architectural patterns for testing

## Multi-Agent Routing Logic

This setup uses a sophisticated multi-agent pipeline to handle tasks, assigning a specific role to each AI based on its strengths.

*   **Gemini (`gemini-mcp`): The Analyst & Architect.** Handles deep analysis, planning, and architectural understanding.
*   **Claude (Native, via `Sequential`): The Coder & Refactorer.** Executes coding and refactoring tasks based on a plan.
*   **Qwen (`qwen-mcp`): The Assistant.** Manages quick, simple tasks like documentation and quick queries.

## How to Use the Pipelines (Examples)

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

**Status**: Setup complete, ready for testing after restart.