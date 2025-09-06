#!/bin/bash

# 🚀 Test Script for Complete LLM API Automation
# Tests the revolutionary LLM integration with real content generation

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}ℹ️  $*${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $*${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $*${NC}"
}

log_error() {
    echo -e "${RED}❌ $*${NC}"
}

log_header() {
    echo -e "${PURPLE}🚀 $*${NC}"
}

# Test configuration
TEST_FEATURE="test-llm-automation"
TEST_DATE=$(date +"%Y-%m-%d")
TEST_FEATURE_DIR="${SCRIPT_DIR}/features/${TEST_DATE}-${TEST_FEATURE}"

echo ""
log_header "LLM API AUTOMATION REVOLUTION TEST SUITE"
echo ""

# Check if we have API keys available
check_api_keys() {
    log_info "Checking for available LLM API providers..."
    
    local providers_available=()
    
    if [[ -n "${OPENAI_API_KEY:-}" ]]; then
        providers_available+=("openai")
        log_success "OpenAI API key found"
    fi
    
    if [[ -n "${ANTHROPIC_API_KEY:-}" ]]; then
        providers_available+=("anthropic")
        log_success "Anthropic API key found"
    fi
    
    if [[ -n "${GROQ_API_KEY:-}" ]]; then
        providers_available+=("groq")
        log_success "Groq API key found"
    fi
    
    if [[ -n "${GOOGLE_API_KEY:-}" ]]; then
        providers_available+=("google")
        log_success "Google Gemini API key found"
    fi
    
    # Check for local Ollama
    if curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
        providers_available+=("local_ollama")
        log_success "Local Ollama instance found"
    fi
    
    if [[ ${#providers_available[@]} -eq 0 ]]; then
        log_warning "No LLM API providers available. Set API keys or start Ollama."
        log_info "Available environment variables to set:"
        log_info "  export OPENAI_API_KEY=your_key_here"
        log_info "  export ANTHROPIC_API_KEY=your_key_here"
        log_info "  export GROQ_API_KEY=your_key_here"
        log_info "  export GOOGLE_API_KEY=your_key_here"
        log_info "Or start Ollama: ollama serve"
        return 1
    fi
    
    echo "${providers_available[0]}"  # Return first available provider
}

# Test basic LLM integration
test_llm_integration() {
    local provider="$1"
    
    log_header "Testing LLM Integration with $provider"
    
    if ! python3 "${SCRIPT_DIR}/llm-api-integration.py" \
        --provider="$provider" \
        --model="gpt-3.5-turbo" \
        --prompt="Generate a simple PRD section for a user authentication feature. Keep it under 200 words." \
        --system-prompt="You are a helpful product manager."; then
        
        log_error "LLM integration test failed"
        return 1
    fi
    
    log_success "LLM integration test passed"
}

# Test content generation engine
test_content_generation() {
    local provider="$1"
    
    log_header "Testing Content Generation Engine with $provider"
    
    mkdir -p "$TEST_FEATURE_DIR"
    
    if ! python3 "${SCRIPT_DIR}/content-generation-engine.py" \
        --workflow-document="02-gen-prd.md" \
        --feature-name="$TEST_FEATURE" \
        --feature-dir="$TEST_FEATURE_DIR" \
        --content-type="prd" \
        --output-file="test-prd.md"; then
        
        log_error "Content generation test failed"
        return 1
    fi
    
    if [[ -f "$TEST_FEATURE_DIR/test-prd.md" ]]; then
        log_success "Content generation test passed"
        log_info "Generated file: $TEST_FEATURE_DIR/test-prd.md"
        log_info "File size: $(wc -c < "$TEST_FEATURE_DIR/test-prd.md") bytes"
    else
        log_error "Expected output file not created"
        return 1
    fi
}

# Test workflow executor with LLM
test_workflow_executor() {
    local provider="$1"
    
    log_header "Testing Workflow Executor with LLM API"
    
    if ! python3 "${SCRIPT_DIR}/workflow-executor.py" \
        "${SCRIPT_DIR}/lean-workflow/02-gen-prd.md" \
        --feature="$TEST_FEATURE" \
        --feature-dir="$TEST_FEATURE_DIR" \
        --mode="autonomous" \
        --step="02" \
        --phase="foundation" \
        --llm-api \
        --llm-provider="$provider"; then
        
        log_error "Workflow executor LLM test failed"
        return 1
    fi
    
    log_success "Workflow executor LLM test passed"
}

# Test complete orchestrator automation
test_orchestrator_automation() {
    local provider="$1"
    
    log_header "Testing Complete Orchestrator Automation"
    
    # Clean up any previous test
    rm -rf "${SCRIPT_DIR}/features/${TEST_DATE}-${TEST_FEATURE}-orchestrator"
    
    if ! "${SCRIPT_DIR}/workflow-orchestrator.sh" \
        --mode=autonomous \
        --feature="${TEST_FEATURE}-orchestrator" \
        --llm-api \
        --llm-provider="$provider" \
        --verbose; then
        
        log_error "Orchestrator automation test failed"
        return 1
    fi
    
    log_success "Orchestrator automation test passed"
}

# Test AI workflow runner automation
test_ai_workflow_runner() {
    local provider="$1"
    
    log_header "Testing AI Workflow Runner Automation"
    
    # Clean up any previous test
    rm -rf "${SCRIPT_DIR}/features/${TEST_DATE}-${TEST_FEATURE}-ai-runner"
    
    if ! python3 "${SCRIPT_DIR}/ai-workflow-runner.py" \
        --mode=autonomous \
        --feature="${TEST_FEATURE}-ai-runner" \
        --llm-api \
        --llm-provider="$provider" \
        --verbose; then
        
        log_error "AI workflow runner test failed"
        return 1
    fi
    
    log_success "AI workflow runner test passed"
}

# Cleanup function
cleanup() {
    log_info "Cleaning up test files..."
    rm -rf "$TEST_FEATURE_DIR"
    rm -rf "${SCRIPT_DIR}/features/${TEST_DATE}-${TEST_FEATURE}-orchestrator"
    rm -rf "${SCRIPT_DIR}/features/${TEST_DATE}-${TEST_FEATURE}-ai-runner"
    log_success "Cleanup completed"
}

# Main test execution
main() {
    local provider
    if ! provider=$(check_api_keys); then
        log_error "No LLM providers available - cannot run tests"
        exit 1
    fi
    
    log_header "Running tests with provider: $provider"
    echo ""
    
    # Run tests
    local failed_tests=()
    
    if ! test_llm_integration "$provider"; then
        failed_tests+=("LLM Integration")
    fi
    
    if ! test_content_generation "$provider"; then
        failed_tests+=("Content Generation")
    fi
    
    if ! test_workflow_executor "$provider"; then
        failed_tests+=("Workflow Executor")
    fi
    
    if ! test_orchestrator_automation "$provider"; then
        failed_tests+=("Orchestrator Automation")
    fi
    
    if ! test_ai_workflow_runner "$provider"; then
        failed_tests+=("AI Workflow Runner")
    fi
    
    echo ""
    log_header "TEST RESULTS SUMMARY"
    echo ""
    
    if [[ ${#failed_tests[@]} -eq 0 ]]; then
        log_success "🎉 ALL TESTS PASSED! LLM API automation is WORKING!"
        log_success "🚀 The automation revolution is COMPLETE!"
        echo ""
        log_info "You can now run:"
        log_info "  ./workflow-orchestrator.sh --mode=autonomous --feature=my-feature --llm-api"
        log_info "  ./ai-workflow-runner.py --mode=autonomous --feature=my-feature --llm-api"
        echo ""
        log_success "Real content generation is now LIVE! 🤖✨"
    else
        log_error "Failed tests: ${failed_tests[*]}"
        log_error "LLM API automation needs attention"
        exit 1
    fi
    
    # Cleanup
    cleanup
}

# Help function
show_help() {
    cat << EOF
🚀 LLM API Automation Test Suite

USAGE:
    ./test-llm-automation.sh [OPTIONS]

OPTIONS:
    --no-cleanup    Skip cleanup of test files
    --help         Show this help message

REQUIREMENTS:
    Set at least one API key:
    - export OPENAI_API_KEY=your_key_here
    - export ANTHROPIC_API_KEY=your_key_here  
    - export GROQ_API_KEY=your_key_here
    - export GOOGLE_API_KEY=your_key_here
    
    OR start local Ollama:
    - ollama serve

TESTS:
    1. LLM Integration - Basic API connection
    2. Content Generation - Real content creation
    3. Workflow Executor - Document execution with LLM
    4. Orchestrator Automation - Complete shell automation
    5. AI Workflow Runner - Complete Python automation

This test suite validates the complete LLM API integration system!
EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --no-cleanup)
            CLEANUP=false
            shift
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Run main function
main
