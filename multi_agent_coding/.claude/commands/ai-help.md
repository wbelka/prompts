---
description: "Get recommendations on which AI tool to use"
arguments:
  - "$1: File path or task description"
  - "$2: Task type (optional)"
---
# AI Tool Recommendations
echo "🧭 AI Tool Selection Guide"
echo "=========================="
echo ""

if [ -f "$1" ]; then
    file_size=$(wc -l < "$1")
    file_type=$(basename "$1" | sed 's/.*\.//')
    echo "📁 File: $1"
    echo "📏 Size: $file_size lines"
    echo "📄 Type: $file_type"
    echo ""

    echo "💡 Recommendations based on file characteristics:"

    if [ $file_size -gt 1000 ]; then
        echo "   🧠 /gemini-analyze - For large files (>1000 lines)"
        echo "      → Gemini's extended context window handles large codebases"
    elif [ $file_size -gt 100 ]; then
        echo "   🔄 /ai-route analyze - For medium files (100-1000 lines)"
        echo "      → Intelligent routing based on complexity"
    else
        echo "   ⚡ /qwen-quick - For small files (<100 lines)"
        echo "      → Fast and efficient analysis"
    fi

    echo ""
    echo "Task-specific recommendations:"
    case "$file_type" in
        py|js|ts|java|cpp|c)
            echo "   🐛 /ai-route debug - For debugging code issues"
            echo "   🎨 /qwen-quick format - For code formatting"
            ;;
        md|txt|rst)
            echo "   📝 /qwen-quick - For document analysis"
            ;;
        json|yaml|yml)
            echo "   🔧 /qwen-quick format - For config file formatting"
            ;;
    esac
else
    echo "📝 Task: $1"
    echo "🎯 Type: ${2:-general}"
    echo ""
    echo "💡 Recommendations based on task:"

    case "$2" in
        debug)
            echo "   🧠 /ai-route debug - Systematic debugging approach"
            ;;
        analyze)
            echo "   📊 /ai-route analyze - Intelligent analysis routing"
            ;;
        quick)
            echo "   ⚡ /qwen-quick - Fast responses"
            ;;
        format)
            echo "   🎨 /qwen-quick format - Code formatting"
            ;;
        *)
            echo "   💰 /cost-optimize - Try efficient models first"
            echo "   🤔 /ai-route - Intelligent routing"
            ;;
    esac
fi

echo ""
echo "Available Commands:"
echo "=================="
echo "  /ai-route [analyze|debug|quick|format] [file] [context]"
echo "  /gemini-analyze [file] [focus]"
echo "  /qwen-quick [question]"
echo "  /cost-optimize [task]"
echo "  /ai-help [file|task] [type]"