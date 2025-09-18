---
description: "Analyze large files using Gemini's extended context window"
arguments:
  - "$1: File path to analyze"
  - "$2: Analysis focus (optional)"
---
# Gemini Large File Analysis
echo "🧠 Analyzing @$1 with Gemini for extended context..."

# Check file size
file_size=$(wc -l < "@$1" 2>/dev/null || echo "0")
echo "📄 File size: $file_size lines"

if [ $file_size -gt 500 ]; then
    echo "✅ Large file detected - Using Gemini's extended context window"
else
    echo "ℹ️  Standard file size - Gemini can provide deep analysis"
fi

# Use Gemini MCP to analyze the file
if [ -n "$2" ]; then
    echo "🎯 Focus: $2"
    # Ask Gemini to analyze with specific focus
    ask_gemini "Please analyze the file @$1 with focus on: $2. Provide detailed insights leveraging the full context."
else
    # General analysis
    ask_gemini "Please provide a comprehensive analysis of @$1. Include code quality, architecture, potential improvements, and any issues you identify."
fi