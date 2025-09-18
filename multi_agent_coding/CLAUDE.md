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

## Smart Routing Logic

### File Size Based
- **Large files (>1000 lines)**: Gemini (extended context)
- **Medium files (100-1000)**: Intelligent routing
- **Small files (<100)**: Qwen (efficient)

### Task Type Based
- **Debug/Error**: Sequential thinking (systematic)
- **Quick/Format**: Qwen (fast)
- **Architecture**: Gemini (comprehensive)
- **Cost-sensitive**: Try Qwen → Gemini → Claude fallback

## Next Steps After Restart
1. Test MCP server connections: `claude mcp list`
2. Test slash commands with sample_code.py:
   - `/ai-help sample_code.py`
   - `/code-review sample_code.py security`
   - `/debug-issue sample_code.py "performance issues"`
3. If MCP servers need restart: `claude mcp restart`

## Integration Benefits
- **Token Savings**: ~50% through intelligent routing
- **Specialized Analysis**: Each AI for optimal tasks
- **Extended Context**: Gemini for large codebases
- **Cost Optimization**: Free models first, premium as needed
- **Unified Interface**: All through Claude Code UI

## Command Usage Examples
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

**Status**: Setup complete, ready for testing after restart.