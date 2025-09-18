---
description: "Systematic debugging workflow using AI assistance"
arguments:
  - "$1: File with the issue"
  - "$2: Error description or symptoms"
  - "$3: Additional context (optional)"
---
# Systematic Debugging Pipeline
echo "🐛 Systematic Debugging Workflow"
echo "================================"
echo "📁 File: @$1"
echo "❌ Issue: $2"
echo "📝 Context: ${3:-None provided}"
echo ""

# Stage 1: Problem Understanding
echo "🎯 Stage 1: Problem Analysis"
echo "----------------------------"
sequentialthinking "Analyze the debugging problem: File @$1 has issue '$2'. Additional context: '$3'. Break down the problem systematically and identify what we need to investigate."

echo ""
echo "🔍 Stage 2: Code Analysis"
echo "------------------------"

file_size=$(wc -l < "@$1" 2>/dev/null || echo "0")
if [ $file_size -gt 300 ]; then
    echo "🧠 Using Gemini for large file analysis..."
    ask_gemini "Analyze @$1 in the context of the error: '$2'. Look for the root cause, related code patterns, and potential issues. Context: $3"
else
    echo "⚡ Using focused analysis..."
    ask_qwen "Analyze @$1 for the issue: '$2'. Focus on the specific problem area and immediate surroundings. Context: $3"
fi

echo ""
echo "🧠 Stage 3: Root Cause Investigation"
echo "------------------------------------"
sequentialthinking "Based on the code analysis above, systematically investigate the root cause of '$2' in @$1. Consider:
1. Direct causes (syntax, logic errors)
2. Indirect causes (dependencies, environment)
3. Edge cases and boundary conditions
4. Data flow issues
5. State management problems"

echo ""
echo "⚡ Stage 4: Solution Development"
echo "------------------------------"
ask_gemini "Based on the root cause analysis, develop specific solutions for the issue '$2' in @$1. Provide:
1. Immediate fixes for the direct problem
2. Preventive measures to avoid similar issues
3. Code examples for the fixes
4. Testing recommendations"

echo ""
echo "✅ Stage 5: Validation & Testing"
echo "-------------------------------"
ask_qwen "Suggest comprehensive testing approaches to validate the fix for '$2' in @$1. Include:
1. Unit tests for the fixed functionality
2. Integration tests for affected workflows
3. Edge case testing
4. Regression testing recommendations"

echo ""
echo "📋 Summary Requirements:"
echo "======================="
echo "Please provide a final summary including:"
echo "1. Root cause explanation"
echo "2. Recommended fix with code example"
echo "3. Testing strategy"
echo "4. Prevention measures for the future"