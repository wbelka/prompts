---
description: "Comprehensive architecture analysis using Gemini's extended context"
arguments:
  - "$1: Directory or main file to analyze"
  - "$2: Architecture aspect (structure|dependencies|patterns|scalability|all)"
---
# Architecture Analysis Pipeline
echo "🏗️ Architecture Analysis Workflow"
echo "=================================="
echo "📁 Target: @$1"
echo "🎯 Focus: ${2:-all}"
echo ""

# Check scope
if [ -d "$1" ]; then
    echo "📊 Project-level architecture analysis"
    file_count=$(find "$1" -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.java" | wc -l)
    echo "📄 Code files found: $file_count"
else
    echo "📄 File-level architecture analysis"
    file_count=1
fi

echo ""
echo "🧠 Stage 1: High-Level Architecture Overview"
echo "--------------------------------------------"
ask_gemini "Provide a comprehensive architectural overview of @$1. Focus on:
- Overall system structure and organization
- Key components and their relationships
- Architectural patterns used
- Design principles followed or violated
- Entry points and main workflows"

echo ""
echo "🔍 Stage 2: Focused Analysis"
echo "---------------------------"

case "${2:-all}" in
    structure)
        echo "🏗️ Structural analysis..."
        sequentialthinking "Analyze the structural aspects of @$1:
        - Directory/module organization
        - Code layering and separation of concerns
        - Component boundaries and interfaces
        - Coupling and cohesion patterns"
        ;;
    dependencies)
        echo "🔗 Dependency analysis..."
        ask_gemini "Analyze dependencies in @$1:
        - External dependencies and their usage
        - Internal dependencies between modules
        - Dependency injection patterns
        - Circular dependencies or other issues"
        ;;
    patterns)
        echo "🎨 Design pattern analysis..."
        sequentialthinking "Identify and analyze design patterns in @$1:
        - Creational patterns (Singleton, Factory, Builder, etc.)
        - Structural patterns (Adapter, Decorator, Facade, etc.)
        - Behavioral patterns (Observer, Strategy, Command, etc.)
        - Anti-patterns and code smells"
        ;;
    scalability)
        echo "📈 Scalability analysis..."
        ask_gemini "Analyze scalability aspects of @$1:
        - Performance bottlenecks
        - Resource utilization patterns
        - Horizontal/vertical scaling potential
        - Load handling capabilities
        - Caching and optimization opportunities"
        ;;
    all)
        echo "🎯 Comprehensive architectural analysis..."
        echo ""
        echo "Structure analysis:"
        sequentialthinking "Structural analysis of @$1: organization, layering, boundaries, coupling."
        echo ""
        echo "Pattern analysis:"
        ask_gemini "Design pattern analysis of @$1: identify patterns and anti-patterns."
        echo ""
        echo "Scalability analysis:"
        ask_qwen "Quick scalability assessment of @$1: bottlenecks and scaling opportunities."
        ;;
esac

echo ""
echo "💡 Stage 3: Recommendations"
echo "--------------------------"
ask_gemini "Based on the architectural analysis above, provide specific recommendations for @$1:

1. **Immediate Improvements**: Quick wins that can be implemented soon
2. **Structural Refactoring**: Larger changes to improve architecture
3. **Long-term Evolution**: Strategic improvements for future scalability
4. **Risk Assessment**: Potential issues and their mitigation strategies
5. **Implementation Priority**: Order of recommended changes

Focus on actionable, specific recommendations with justification."

echo ""
echo "📋 Architecture Summary:"
echo "======================="
echo "Please provide a concise summary including:"
echo "1. Current architecture strengths"
echo "2. Key areas for improvement"
echo "3. Recommended next steps"
echo "4. Risk/effort assessment for major changes"