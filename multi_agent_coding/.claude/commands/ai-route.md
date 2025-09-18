---
description: "Intelligently route tasks to the best AI model"
arguments:
  - "$1: Task type (analyze|debug|quick|format)"
  - "$2: File path or content"
  - "$3: Additional context"
---
# Intelligent AI Routing
echo "🤔 Routing decision for task: $1"
echo "📁 Target: $2"
echo "📝 Context: $3"
echo ""

# Get file info if it's a file path
if [ -f "$2" ]; then
    file_size=$(wc -l < "$2")
    file_type=$(file -b "$2")
    echo "📏 File size: $file_size lines"
    echo "📄 File type: $file_type"
else
    file_size=0
    echo "📝 Working with text/query, not a file"
fi

echo ""
echo "💡 Routing decision:"

case "$1" in
    analyze)
        if [ $file_size -gt 500 ]; then
            echo "   → Using Gemini for large file analysis (extended context)"
            ask_gemini "Analyze @$2 with focus on: $3"
        elif [ $file_size -gt 100 ]; then
            echo "   → Using Sequential thinking for medium complexity"
            # Use sequential thinking MCP
            sequentialthinking "Analyze the file @$2 focusing on $3. Provide structured analysis."
        else
            echo "   → Using Claude Code for balanced analysis"
            echo "Analyzing @$2 with focus on: $3"
        fi
        ;;
    debug)
        echo "   → Using Sequential thinking for systematic debugging"
        sequentialthinking "Debug the issue in @$2 related to: $3. Follow systematic debugging methodology."
        ;;
    quick)
        echo "   → Using Qwen for quick, efficient analysis"
        ask_qwen "$2 $3"
        ;;
    format)
        echo "   → Using Qwen for code formatting"
        ask_qwen "Format and optimize the code in @$2 according to best practices for $3"
        ;;
    *)
        echo "   → Using Claude Code for general tasks"
        echo "Processing: $1 $2 $3"
        ;;
esac