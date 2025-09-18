---
description: "Multi-stage performance optimization workflow"
arguments:
  - "$1: File or directory to optimize"
  - "$2: Performance focus (speed|memory|both)"
---
# Performance Optimization Pipeline
echo "🚀 Performance Optimization Workflow"
echo "====================================="
echo "🎯 Target: @$1"
echo "🔍 Focus: ${2:-both}"
echo ""

# Stage 1: Current State Analysis
echo "📊 Stage 1: Performance Baseline Analysis"
echo "-----------------------------------------"

file_size=$(wc -l < "@$1" 2>/dev/null || echo "0")
if [ $file_size -gt 500 ]; then
    echo "🧠 Using Gemini for comprehensive analysis..."
    ask_gemini "Analyze @$1 for current performance characteristics. Identify bottlenecks, inefficient algorithms, resource usage patterns, and performance-critical code paths."
else
    echo "⚡ Using Sequential thinking for systematic analysis..."
    sequentialthinking "Systematically analyze @$1 for performance issues. Focus on algorithm complexity, resource usage, and optimization opportunities."
fi

echo ""
echo "🔬 Stage 2: Specific Performance Analysis"
echo "----------------------------------------"

case "${2:-both}" in
    speed)
        echo "⏱️ Speed optimization focus..."
        ask_gemini "Focus specifically on execution speed for @$1. Analyze time complexity, algorithm efficiency, caching opportunities, and parallelization potential."
        ;;
    memory)
        echo "🧠 Memory optimization focus..."
        sequentialthinking "Analyze @$1 for memory usage optimization. Look for memory leaks, unnecessary object creation, data structure efficiency, and memory allocation patterns."
        ;;
    both)
        echo "⚡ Speed analysis:"
        ask_gemini "Speed optimization analysis of @$1: algorithm efficiency, execution time, bottlenecks."
        echo ""
        echo "🧠 Memory analysis:"
        sequentialthinking "Memory optimization analysis of @$1: memory usage, allocation patterns, potential leaks."
        ;;
esac

echo ""
echo "🛠️ Stage 3: Optimization Recommendations"
echo "---------------------------------------"
ask_qwen "Based on the performance analysis above, provide specific, actionable optimization recommendations for @$1. Include code examples where helpful."

echo ""
echo "📈 Stage 4: Implementation Priority"
echo "----------------------------------"
echo "Please provide:"
echo "1. High-impact, low-effort optimizations (quick wins)"
echo "2. Medium-impact optimizations requiring moderate effort"
echo "3. High-impact optimizations requiring significant refactoring"
echo "4. Estimated performance improvement for each category"
echo "5. Recommended implementation order"