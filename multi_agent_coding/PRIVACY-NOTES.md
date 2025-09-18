# Privacy & Security Notes

## ✅ Cleaned for Sharing

**Removed sensitive directories:**
- `logs/` - Contained installation logs with system paths
- `shell-snapshots/` - Terminal history snapshots
- `todos/` - Personal task history
- `projects/` - Project cache with paths
- `statsig/` - Analytics data
- `backups/` - Backup files with potentially personal data
- `.superclaude-metadata.json` - Installation metadata
- `plugins/config.json` - Plugin configurations

## ✅ Safe to Share

**Directories included:**
- `commands/` - Custom slash commands (generic)
- `hooks/` - Empty directory
- `plugins/` - Empty directory structure

**Files included:**
- Core framework files (CLAUDE.md, COMMANDS.md, etc.)
- `settings.json` - Only contains `{"model": "sonnet"}`

## 🔒 Missing Configuration

**On new machine you'll need:**
1. Install MCP servers: `npm install -g gemini-mcp-tool qwen-mcp-tool`
2. Add MCP servers to Claude Code:
   ```bash
   claude mcp add -s local gemini-cli -- npx -y gemini-mcp-tool
   claude mcp add -s local qwen-cli -- npx -y qwen-mcp-tool
   ```
3. Test: `claude mcp list`

## 🎯 Ready for Demo

This configuration is now safe to share publicly and contains:
- 9 intelligent slash commands for AI routing
- Complete SuperClaude framework
- No personal data, paths, or sensitive information
- Generic configuration suitable for any user

**Usage:** Copy `.claude/` to `~/` on target machine + install MCP servers.