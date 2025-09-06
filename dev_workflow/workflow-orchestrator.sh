#!/bin/bash

# 🚀 MVP Workflow Orchestrator - Automated Numbered Sequence Execution
# Supports three automation modes: guided, autonomous, learning

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${SCRIPT_DIR}/automation-config.json"
LEAN_WORKFLOW_DIR="${SCRIPT_DIR}/lean-workflow"
WORKFLOW_LOG="${SCRIPT_DIR}/workflow-execution.log"

# Default values
MODE="guided"
FEATURE_NAME=""
DRY_RUN=false
VERBOSE=false
SKIP_GATES=""
REQUIRE_GATES=""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Workflow sequence
WORKFLOW_SEQUENCE=(
    "01-mvp-entrypoint.md"
    "02-gen-prd.md"
    "03-gen-srs.md"
    "04-gen-design-decisions-lite.md"
    "05-gen-design.md"
    "06-gen-tasks-and-testing.md"
    "07-process-tasks.md"
    "08-gen-completion-summary.md"
    "09-gen-project-history.md"
)

# Phase mapping
declare -A PHASES
PHASES=(
    ["01"]="foundation"
    ["02"]="foundation"
    ["03"]="foundation"
    ["04"]="design"
    ["05"]="design"
    ["06"]="implementation"
    ["07"]="implementation"
    ["08"]="completion"
    ["09"]="completion"
)

# Gate mapping
declare -A GATE_NAMES
GATE_NAMES=(
    ["01"]="feature_directory_creation"
    ["02"]="prd_generation"
    ["03"]="srs_generation"
    ["04"]="design_decisions"
    ["05"]="design_analysis"
    ["06"]="task_creation"
    ["07"]="task_implementation"
    ["08"]="completion_summary"
    ["09"]="project_history"
)

# Logging functions
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $*" | tee -a "${WORKFLOW_LOG}"
}

log_info() {
    echo -e "${BLUE}ℹ️  $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

log_success() {
    echo -e "${GREEN}✅ $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

log_error() {
    echo -e "${RED}❌ $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

log_gate() {
    echo -e "${PURPLE}🚪 $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

log_phase() {
    echo -e "${CYAN}🏗️  $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

# Help function
show_help() {
    cat << EOF
🚀 MVP Workflow Orchestrator - Automated Numbered Sequence Execution

USAGE:
    ./workflow-orchestrator.sh [OPTIONS]

AUTOMATION MODES:
    --mode=guided      Maximum human oversight (default)
    --mode=autonomous  Minimal human oversight with smart safety
    --mode=learning    Adaptive oversight based on approval history

OPTIONS:
    --feature=NAME     Feature name for directory creation
    --dry-run          Show execution plan without running
    --verbose          Enable detailed logging
    --skip-gates=LIST  Comma-separated gate names to skip
    --require-gates=LIST Comma-separated gate names to always require
    --help             Show this help message

EXAMPLES:
    # Guided mode (traditional workflow)
    ./workflow-orchestrator.sh --mode=guided --feature=user-auth

    # Autonomous mode (minimal gates)
    ./workflow-orchestrator.sh --mode=autonomous --feature=dashboard

    # Learning mode (adaptive gates)
    ./workflow-orchestrator.sh --mode=learning --feature=api-v2

    # Custom gate configuration
    ./workflow-orchestrator.sh --mode=autonomous --feature=search \\
        --skip-gates=design_analysis,completion_summary \\
        --require-gates=task_implementation

    # Dry run to see execution plan
    ./workflow-orchestrator.sh --mode=autonomous --feature=test --dry-run

WORKFLOW SEQUENCE:
    PHASE 1: FOUNDATION
        01-mvp-entrypoint.md → 02-gen-prd.md → 03-gen-srs.md
    
    PHASE 2: DESIGN 
        04-gen-design-decisions-lite.md → 05-gen-design.md
    
    PHASE 3: IMPLEMENTATION
        06-gen-tasks-and-testing.md → 07-process-tasks.md
    
    PHASE 4: COMPLETION
        08-gen-completion-summary.md → 09-gen-project-history.md

GATE BEHAVIOR:
    guided      = Stop at every major gate for human approval
    autonomous  = Auto-proceed with risk-based safety checks
    learning    = Adaptive gates based on approval history

For more details, see: workflow-sequence-guide.md
EOF
}

# Parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --mode=*)
                MODE="${1#*=}"
                ;;
            --feature=*)
                FEATURE_NAME="${1#*=}"
                ;;
            --dry-run)
                DRY_RUN=true
                ;;
            --verbose)
                VERBOSE=true
                ;;
            --skip-gates=*)
                SKIP_GATES="${1#*=}"
                ;;
            --require-gates=*)
                REQUIRE_GATES="${1#*=}"
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
        shift
    done
}

# Validate mode
validate_mode() {
    case $MODE in
        guided|autonomous|learning)
            log_info "Automation mode: $MODE"
            ;;
        *)
            log_error "Invalid mode: $MODE. Must be: guided, autonomous, or learning"
            exit 1
            ;;
    esac
}

# Check if gate is required based on mode and configuration
is_gate_required() {
    local step="$1"
    local gate_name="${GATE_NAMES[$step]}"
    
    # Check custom overrides first
    if [[ "$SKIP_GATES" == *"$gate_name"* ]]; then
        return 1  # Skip gate
    fi
    
    if [[ "$REQUIRE_GATES" == *"$gate_name"* ]]; then
        return 0  # Require gate
    fi
    
    # Mode-based gate logic
    case $MODE in
        guided)
            # Guided mode requires most gates
            case $gate_name in
                design_analysis|completion_summary|project_history)
                    return 1  # Optional in guided mode
                    ;;
                *)
                    return 0  # Required
                    ;;
            esac
            ;;
        autonomous)
            # Autonomous mode skips most gates except high-risk
            case $gate_name in
                task_implementation)
                    return 0  # Always required for destructive actions
                    ;;
                design_decisions)
                    # TODO: Check if new technology detected
                    return 1  # Skip for now in autonomous
                    ;;
                *)
                    return 1  # Skip most gates
                    ;;
            esac
            ;;
        learning)
            # Learning mode uses approval history
            # TODO: Implement learning logic
            return 0  # Default to required until learning implemented
            ;;
    esac
}

# Execute human gate
execute_gate() {
    local step="$1"
    local phase="${PHASES[$step]}"
    local gate_name="${GATE_NAMES[$step]}"
    local doc_name="${WORKFLOW_SEQUENCE[$((step-1))]}"
    
    log_gate "HUMAN GATE: $gate_name (Step $step - $phase phase)"
    log_gate "About to execute: $doc_name"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] Would request human approval for: $gate_name"
        return 0
    fi
    
    echo -e "${PURPLE}🚪 HUMAN GATE REQUIRED${NC}"
    echo -e "Phase: ${CYAN}$phase${NC}"
    echo -e "Step: ${YELLOW}$step${NC} - $doc_name"
    echo -e "Gate: ${PURPLE}$gate_name${NC}"
    echo ""
    
    read -p "Do you approve proceeding? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        log_success "Gate approved: $gate_name"
        return 0
    else
        log_warning "Gate rejected: $gate_name"
        return 1
    fi
}

# Execute workflow step
execute_step() {
    local step="$1"
    local doc_name="${WORKFLOW_SEQUENCE[$((step-1))]}"
    local phase="${PHASES[$step]}"
    local doc_path="${LEAN_WORKFLOW_DIR}/${doc_name}"
    
    log_info "Executing Step $step: $doc_name ($phase phase)"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] Would execute: $doc_name"
        return 0
    fi
    
    # Check if document exists
    if [[ ! -f "$doc_path" ]]; then
        log_error "Document not found: $doc_path"
        return 1
    fi
    
    # For now, just log the execution
    # TODO: Implement actual document execution logic
    log_success "Step $step completed: $doc_name"
    
    return 0
}

# Show execution plan
show_execution_plan() {
    log_phase "WORKFLOW EXECUTION PLAN"
    echo ""
    echo -e "${CYAN}Mode:${NC} $MODE"
    echo -e "${CYAN}Feature:${NC} $FEATURE_NAME"
    echo -e "${CYAN}Sequence:${NC}"
    echo ""
    
    local current_phase=""
    for i in "${!WORKFLOW_SEQUENCE[@]}"; do
        local step=$((i + 1))
        local step_padded=$(printf "%02d" $step)
        local doc_name="${WORKFLOW_SEQUENCE[i]}"
        local phase="${PHASES[$step_padded]}"
        local gate_name="${GATE_NAMES[$step_padded]}"
        
        # Show phase header
        if [[ "$phase" != "$current_phase" ]]; then
            echo -e "\n${CYAN}🏗️  PHASE: ${phase^^}${NC}"
            current_phase="$phase"
        fi
        
        # Show step
        if is_gate_required "$step_padded"; then
            echo -e "  ${YELLOW}$step_padded${NC} → ${PURPLE}🚪 $gate_name${NC} → $doc_name"
        else
            echo -e "  ${YELLOW}$step_padded${NC} → ⚡ auto → $doc_name"
        fi
    done
    echo ""
}

# Main execution function
main() {
    log_info "🚀 Starting MVP Workflow Orchestrator"
    log_info "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
    
    # Validate inputs
    validate_mode
    
    if [[ -z "$FEATURE_NAME" ]]; then
        log_error "Feature name is required. Use --feature=NAME"
        exit 1
    fi
    
    # Show execution plan
    show_execution_plan
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "Dry run complete. No actions were executed."
        exit 0
    fi
    
    # Confirm execution start
    echo ""
    read -p "Start workflow execution? (y/N): " -n 1 -r
    echo ""
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Workflow execution cancelled by user"
        exit 0
    fi
    
    # Execute workflow sequence
    local current_phase=""
    for i in "${!WORKFLOW_SEQUENCE[@]}"; do
        local step=$((i + 1))
        local step_padded=$(printf "%02d" $step)
        local phase="${PHASES[$step_padded]}"
        
        # Show phase transition
        if [[ "$phase" != "$current_phase" ]]; then
            log_phase "ENTERING PHASE: ${phase^^}"
            current_phase="$phase"
        fi
        
        # Check if gate is required
        if is_gate_required "$step_padded"; then
            if ! execute_gate "$step_padded"; then
                log_error "Workflow stopped at gate: ${GATE_NAMES[$step_padded]}"
                exit 1
            fi
        fi
        
        # Execute the step
        if ! execute_step "$step"; then
            log_error "Workflow failed at step $step"
            exit 1
        fi
        
        echo ""
    done
    
    log_success "🎉 Workflow completed successfully!"
    log_success "Feature: $FEATURE_NAME"
    log_success "Mode: $MODE" 
    log_success "Total steps: ${#WORKFLOW_SEQUENCE[@]}"
}

# Parse arguments and run
parse_args "$@"
main
