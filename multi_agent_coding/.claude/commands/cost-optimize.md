---
description: "Try cost-effective models first, escalate if needed"
arguments:
  - "$ARGUMENTS: Task to process with cost optimization"
---
# Cost-Optimized AI Routing
echo "💰 Attempting cost-effective routing..."

# Try Qwen first for simple tasks
echo "🔄 Step 1: Trying Qwen (efficient model)..."
if echo "$ARGUMENTS" | grep -qE "(format|style|quick|simple|basic)"; then
    echo "✅ Task suitable for Qwen"
    ask_qwen "$ARGUMENTS"
    exit 0
fi

# Check if it's a large file analysis that needs Gemini
if echo "$ARGUMENTS" | grep -qE "(@[^[:space:]]+)" && [ -f "$(echo "$ARGUMENTS" | grep -oE '@[^[:space:]]+' | sed 's/@//')" ]; then
    file_path=$(echo "$ARGUMENTS" | grep -oE '@[^[:space:]]+' | sed 's/@//')
    if [ -f "$file_path" ]; then
        file_size=$(wc -l < "$file_path")
        if [ $file_size -gt 500 ]; then
            echo "📈 Large file detected ($file_size lines) - Using Gemini"
            ask_gemini "$ARGUMENTS"
            exit 0
        fi
    fi
fi

# For complex analysis, use Sequential thinking
if echo "$ARGUMENTS" | grep -qE "(complex|analyze|debug|investigate|systematic)"; then
    echo "🧠 Complex task detected - Using Sequential thinking"
    sequentialthinking "$ARGUMENTS"
    exit 0
fi

# Default to Claude Code for balanced processing
echo "⚖️  Using Claude Code for balanced processing"
echo "$ARGUMENTS"