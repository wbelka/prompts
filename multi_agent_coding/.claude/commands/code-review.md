---
description: "Comprehensive code review using multiple AI perspectives"
arguments:
  - "$1: File or directory to review"
  - "$2: Review focus (security|performance|quality|all)"
---
# Multi-AI Code Review Pipeline
echo "🔍 Starting comprehensive code review for @$1"
echo "🎯 Focus: ${2:-all}"
echo "======================================================"

# Check if it's a directory or file
if [ -d "$1" ]; then
    echo "📁 Directory review - analyzing structure..."
    file_count=$(find "$1" -type f -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.java" -o -name "*.cpp" | wc -l)
    echo "📊 Found $file_count code files"
else
    echo "📄 Single file review"
    file_count=1
fi

echo ""
echo "🚀 Stage 1: Initial Analysis"
echo "----------------------------"

if [ $file_count -gt 20 ] || [ "$(wc -l < "$1" 2>/dev/null || echo 0)" -gt 1000 ]; then
    echo "🧠 Using Gemini for large codebase analysis..."
    ask_gemini "Perform an initial code review of @$1 focusing on overall architecture and structure. Identify major issues and areas for improvement."
else
    echo "⚡ Using Qwen for efficient initial scan..."
    ask_qwen "Quickly scan @$1 for obvious issues and provide a summary."
fi

echo ""
echo "🔬 Stage 2: Focused Analysis"
echo "----------------------------"

case "${2:-all}" in
    security)
        echo "🛡️ Security-focused analysis..."
        sequentialthinking "Conduct a thorough security analysis of @$1. Check for vulnerabilities, injection risks, authentication issues, and security best practices."
        ;;
    performance)
        echo "⚡ Performance analysis..."
        ask_gemini "Analyze @$1 for performance bottlenecks, inefficient algorithms, memory usage, and optimization opportunities."
        ;;
    quality)
        echo "✨ Code quality analysis..."
        sequentialthinking "Review @$1 for code quality: maintainability, readability, design patterns, SOLID principles, and technical debt."
        ;;
    all)
        echo "🎯 Comprehensive analysis..."
        echo ""
        echo "Security perspective:"
        sequentialthinking "Security analysis of @$1: vulnerabilities, authentication, input validation."
        echo ""
        echo "Performance perspective:"
        ask_gemini "Performance analysis of @$1: bottlenecks, optimization opportunities."
        echo ""
        echo "Quality perspective:"
        ask_qwen "Code quality review of @$1: maintainability, best practices, technical debt."
        ;;
esac

echo ""
echo "📋 Stage 3: Synthesis"
echo "--------------------"
echo "Please synthesize the above analyses and provide:"
echo "1. Priority ranking of issues found"
echo "2. Recommended action items"
echo "3. Estimated effort for fixes"
echo "4. Risk assessment for each issue"