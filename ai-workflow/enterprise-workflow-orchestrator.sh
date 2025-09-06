#!/bin/bash

# 🏗️ Enterprise Scaling Workflow Orchestrator - Automated s01-s08 Sequence Execution
# Supports three automation modes with enterprise governance and compliance

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${SCRIPT_DIR}/enterprise-automation-config.json"
SCALING_WORKFLOW_DIR="${SCRIPT_DIR}/scaling-workflow"
WORKFLOW_LOG="${SCRIPT_DIR}/enterprise-workflow-execution.log"

# Default values
MODE="guided"
FEATURE_NAME=""
DRY_RUN=false
VERBOSE=false
SKIP_GATES=""
REQUIRE_GATES=""
COMPLIANCE_FRAMEWORK=""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
ORANGE='\033[0;33m'
NC='\033[0m' # No Color

# Enterprise workflow sequence
ENTERPRISE_WORKFLOW_SEQUENCE=(
    "s01-mvp-to-scaling-transition.md"
    "s02-gen-design-decisions-scaling.md"
    "s03-gen-srs-scaling.md"
    "s04-create-prd-scaling.md"
    "s05-gen-design-scaling.md"
    "s06-tasks-and-testing-scaling.md"
    "s07-gen-enterprise-completion-summary.md"
    "s08-gen-enterprise-history.md"
)

# Enterprise phase mapping
declare -A ENTERPRISE_PHASES
ENTERPRISE_PHASES=(
    ["s01"]="transition"
    ["s02"]="architecture"
    ["s03"]="architecture"
    ["s04"]="architecture"
    ["s05"]="implementation"
    ["s06"]="implementation"
    ["s07"]="completion"
    ["s08"]="completion"
)

# Enterprise gate mapping
declare -A ENTERPRISE_GATE_NAMES
ENTERPRISE_GATE_NAMES=(
    ["s01"]="mvp_to_scaling_transition"
    ["s02"]="enterprise_design_decisions"
    ["s03"]="enterprise_srs_generation"
    ["s04"]="enterprise_prd_creation"
    ["s05"]="enterprise_design_analysis"
    ["s06"]="enterprise_task_creation"
    ["s07"]="enterprise_completion_summary"
    ["s08"]="enterprise_history_update"
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

log_enterprise() {
    echo -e "${ORANGE}🏢 $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

log_compliance() {
    echo -e "${PURPLE}📋 $*${NC}" | tee -a "${WORKFLOW_LOG}"
}

# Help function
show_help() {
    cat << EOF
🏗️ Enterprise Scaling Workflow Orchestrator - Automated s01-s08 Sequence Execution

USAGE:
    ./enterprise-workflow-orchestrator.sh [OPTIONS]

AUTOMATION MODES:
    --mode=guided      Maximum enterprise oversight (default)
    --mode=autonomous  Balanced enterprise oversight with smart safety
    --mode=learning    Adaptive oversight based on enterprise approval history

OPTIONS:
    --feature=NAME     Feature name for enterprise directory creation
    --dry-run          Show execution plan without running
    --verbose          Enable detailed logging
    --skip-gates=LIST  Comma-separated enterprise gate names to skip
    --require-gates=LIST Comma-separated enterprise gate names to always require
    --compliance=FRAMEWORK Specify compliance framework (GDPR, SOC2, PCI, HIPAA, ISO27001)
    --help             Show this help message

EXAMPLES:
    # Guided mode (traditional enterprise workflow)
    ./enterprise-workflow-orchestrator.sh --mode=guided --feature=user-service

    # Autonomous mode (balanced enterprise gates)
    ./enterprise-workflow-orchestrator.sh --mode=autonomous --feature=api-gateway

    # Learning mode (adaptive enterprise gates)
    ./enterprise-workflow-orchestrator.sh --mode=learning --feature=payment-system

    # Compliance-aware workflow
    ./enterprise-workflow-orchestrator.sh --mode=autonomous --feature=data-processor \\
        --compliance=GDPR

    # Custom enterprise gate configuration
    ./enterprise-workflow-orchestrator.sh --mode=autonomous --feature=microservice \\
        --skip-gates=enterprise_design_analysis,enterprise_completion_summary \\
        --require-gates=enterprise_design_decisions,enterprise_task_creation

    # Dry run to see enterprise execution plan
    ./enterprise-workflow-orchestrator.sh --mode=autonomous --feature=test --dry-run

ENTERPRISE WORKFLOW SEQUENCE:
    PHASE 1: TRANSITION
        s01-mvp-to-scaling-transition.md
    
    PHASE 2: ARCHITECTURE 
        s02-gen-design-decisions-scaling.md → s03-gen-srs-scaling.md → s04-create-prd-scaling.md
    
    PHASE 3: IMPLEMENTATION
        s05-gen-design-scaling.md → s06-tasks-and-testing-scaling.md
    
    PHASE 4: COMPLETION
        s07-gen-enterprise-completion-summary.md → s08-gen-enterprise-history.md

ENTERPRISE GATE BEHAVIOR:
    guided      = Stop at every major enterprise governance gate
    autonomous  = Auto-proceed with enterprise risk-based safety checks
    learning    = Adaptive gates based on enterprise approval history

COMPLIANCE FRAMEWORKS:
    GDPR       = General Data Protection Regulation
    SOC2       = Service Organization Control 2
    PCI        = Payment Card Industry Data Security Standard
    HIPAA      = Health Insurance Portability and Accountability Act
    ISO27001   = International Organization for Standardization 27001

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
            --compliance=*)
                COMPLIANCE_FRAMEWORK="${1#*=}"
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
            log_info "Enterprise automation mode: $MODE"
            ;;
        *)
            log_error "Invalid mode: $MODE. Must be: guided, autonomous, or learning"
            exit 1
            ;;
    esac
}

# Validate compliance framework
validate_compliance() {
    if [[ -n "$COMPLIANCE_FRAMEWORK" ]]; then
        case $COMPLIANCE_FRAMEWORK in
            GDPR|SOC2|PCI|HIPAA|ISO27001)
                log_compliance "Compliance framework: $COMPLIANCE_FRAMEWORK"
                ;;
            *)
                log_error "Invalid compliance framework: $COMPLIANCE_FRAMEWORK"
                log_error "Supported: GDPR, SOC2, PCI, HIPAA, ISO27001"
                exit 1
                ;;
        esac
    fi
}

# Check if enterprise gate is required based on mode and configuration
is_enterprise_gate_required() {
    local step="$1"
    local gate_name="${ENTERPRISE_GATE_NAMES[$step]}"
    
    # Check custom overrides first
    if [[ "$SKIP_GATES" == *"$gate_name"* ]]; then
        return 1  # Skip gate
    fi
    
    if [[ "$REQUIRE_GATES" == *"$gate_name"* ]]; then
        return 0  # Require gate
    fi
    
    # Mode-based enterprise gate logic
    case $MODE in
        guided)
            # Guided mode requires most enterprise gates
            case $gate_name in
                enterprise_history_update)
                    return 1  # Optional in guided mode
                    ;;
                *)
                    return 0  # Required
                    ;;
            esac
            ;;
        autonomous)
            # Autonomous mode uses enterprise risk-based gates
            case $gate_name in
                enterprise_design_decisions|enterprise_srs_generation|enterprise_task_creation)
                    # TODO: Implement enterprise risk assessment
                    return 1  # Skip for now in autonomous
                    ;;
                enterprise_task_implementation)
                    return 0  # Always required for production changes
                    ;;
                *)
                    return 1  # Skip most gates in autonomous
                    ;;
            esac
            ;;
        learning)
            # Learning mode uses enterprise approval history
            # TODO: Implement enterprise learning logic
            return 0  # Default to required until learning implemented
            ;;
    esac
}

# Execute enterprise human gate
execute_enterprise_gate() {
    local step="$1"
    local phase="${ENTERPRISE_PHASES[$step]}"
    local gate_name="${ENTERPRISE_GATE_NAMES[$step]}"
    local doc_name="${ENTERPRISE_WORKFLOW_SEQUENCE[$((${step:1}-1))]}"
    
    log_gate "ENTERPRISE GATE: $gate_name (Step $step - $phase phase)"
    log_gate "About to execute: $doc_name"
    
    if [[ -n "$COMPLIANCE_FRAMEWORK" ]]; then
        log_compliance "Compliance framework active: $COMPLIANCE_FRAMEWORK"
    fi
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] Would request enterprise approval for: $gate_name"
        return 0
    fi
    
    echo -e "${PURPLE}🚪 ENTERPRISE GATE REQUIRED${NC}"
    echo -e "Phase: ${CYAN}$phase${NC}"
    echo -e "Step: ${YELLOW}$step${NC} - $doc_name"
    echo -e "Gate: ${PURPLE}$gate_name${NC}"
    if [[ -n "$COMPLIANCE_FRAMEWORK" ]]; then
        echo -e "Compliance: ${PURPLE}$COMPLIANCE_FRAMEWORK${NC}"
    fi
    echo ""
    
    read -p "Do you approve proceeding with enterprise workflow? (y/N): " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        log_success "Enterprise gate approved: $gate_name"
        return 0
    else
        log_warning "Enterprise gate rejected: $gate_name"
        return 1
    fi
}

# Execute enterprise workflow step
execute_enterprise_step() {
    local step="$1"
    local doc_name="${ENTERPRISE_WORKFLOW_SEQUENCE[$((${step:1}-1))]}"
    local phase="${ENTERPRISE_PHASES[$step]}"
    local doc_path="${SCALING_WORKFLOW_DIR}/${doc_name}"
    
    log_info "Executing Enterprise Step $step: $doc_name ($phase phase)"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] Would execute: $doc_name"
        return 0
    fi
    
    # Check if document exists
    if [[ ! -f "$doc_path" ]]; then
        log_error "Enterprise document not found: $doc_path"
        return 1
    fi
    
    # Execute enterprise workflow document using workflow executor
    log_info "🏢 Executing enterprise workflow document: $doc_name"
    
    # Prepare enterprise feature directory
    local feature_slug=$(echo "$FEATURE_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr '_' '-')
    local date_prefix=$(date +"%Y-%m-%d")
    local enterprise_feature_dir="${PWD}/enterprise-features/${date_prefix}-${feature_slug}"
    
    # Create enterprise feature directory if it doesn't exist
    mkdir -p "$enterprise_feature_dir"
    mkdir -p "$enterprise_feature_dir/artifacts/architecture-diagrams"
    mkdir -p "$enterprise_feature_dir/artifacts/api-contracts"
    mkdir -p "$enterprise_feature_dir/artifacts/design-system"
    mkdir -p "$enterprise_feature_dir/artifacts/performance-reports"
    mkdir -p "$enterprise_feature_dir/artifacts/security-audits"
    mkdir -p "$enterprise_feature_dir/artifacts/integration-tests"
    mkdir -p "$enterprise_feature_dir/artifacts/deployment-configs"
    mkdir -p "$enterprise_feature_dir/artifacts/monitoring-dashboards"
    
    # Execute using workflow executor with enterprise context
    local executor_args=(
        "${SCRIPT_DIR}/workflow-executor.py" "$doc_path"
        --feature="$FEATURE_NAME"
        --feature-dir="$enterprise_feature_dir"
        --mode="$MODE"
        --step="$step"
        --phase="$phase"
    )
    
    # Add compliance framework if specified
    if [[ -n "$COMPLIANCE_FRAMEWORK" ]]; then
        # Create compliance context file
        local compliance_data="${enterprise_feature_dir}/compliance-context.json"
        cat > "$compliance_data" << EOF
{
  "compliance_framework": "$COMPLIANCE_FRAMEWORK",
  "enterprise_mode": true,
  "multi_team_coordination": true,
  "governance_level": "enterprise"
}
EOF
        executor_args+=(--project-data="$compliance_data")
    fi
    
    if python3 "${executor_args[@]}"; then
        log_success "✅ Enterprise Step $step completed: $doc_name"
        log_success "📁 Enterprise output saved to: $enterprise_feature_dir"
        if [[ -n "$COMPLIANCE_FRAMEWORK" ]]; then
            log_compliance "📋 Compliance framework applied: $COMPLIANCE_FRAMEWORK"
        fi
        return 0
    else
        log_error "❌ Enterprise Step $step failed: $doc_name"
        return 1
    fi
}

# Show enterprise execution plan
show_enterprise_execution_plan() {
    log_phase "ENTERPRISE WORKFLOW EXECUTION PLAN"
    echo ""
    echo -e "${CYAN}Mode:${NC} $MODE"
    echo -e "${CYAN}Feature:${NC} $FEATURE_NAME"
    if [[ -n "$COMPLIANCE_FRAMEWORK" ]]; then
        echo -e "${CYAN}Compliance:${NC} $COMPLIANCE_FRAMEWORK"
    fi
    echo -e "${CYAN}Enterprise Sequence:${NC}"
    echo ""
    
    local current_phase=""
    for i in "${!ENTERPRISE_WORKFLOW_SEQUENCE[@]}"; do
        local step_num=$((i + 1))
        local step_padded=$(printf "s%02d" $step_num)
        local doc_name="${ENTERPRISE_WORKFLOW_SEQUENCE[i]}"
        local phase="${ENTERPRISE_PHASES[$step_padded]}"
        local gate_name="${ENTERPRISE_GATE_NAMES[$step_padded]}"
        
        # Show phase header
        if [[ "$phase" != "$current_phase" ]]; then
            echo -e "\n${CYAN}🏗️  ENTERPRISE PHASE: ${phase^^}${NC}"
            current_phase="$phase"
        fi
        
        # Show step
        if is_enterprise_gate_required "$step_padded"; then
            echo -e "  ${YELLOW}$step_padded${NC} → ${PURPLE}🚪 $gate_name${NC} → $doc_name"
        else
            echo -e "  ${YELLOW}$step_padded${NC} → ⚡ auto → $doc_name"
        fi
    done
    echo ""
}

# Main execution function
main() {
    log_enterprise "🏗️ Starting Enterprise Scaling Workflow Orchestrator"
    log_info "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
    
    # Validate inputs
    validate_mode
    validate_compliance
    
    if [[ -z "$FEATURE_NAME" ]]; then
        log_error "Feature name is required. Use --feature=NAME"
        exit 1
    fi
    
    # Show execution plan
    show_enterprise_execution_plan
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "Enterprise dry run complete. No actions were executed."
        exit 0
    fi
    
    # Confirm execution start
    echo ""
    read -p "Start enterprise workflow execution? (y/N): " -n 1 -r
    echo ""
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Enterprise workflow execution cancelled by user"
        exit 0
    fi
    
    # Execute enterprise workflow sequence
    local current_phase=""
    for i in "${!ENTERPRISE_WORKFLOW_SEQUENCE[@]}"; do
        local step_num=$((i + 1))
        local step_padded=$(printf "s%02d" $step_num)
        local phase="${ENTERPRISE_PHASES[$step_padded]}"
        
        # Show phase transition
        if [[ "$phase" != "$current_phase" ]]; then
            log_phase "ENTERING ENTERPRISE PHASE: ${phase^^}"
            current_phase="$phase"
        fi
        
        # Check if enterprise gate is required
        if is_enterprise_gate_required "$step_padded"; then
            if ! execute_enterprise_gate "$step_padded"; then
                log_error "Enterprise workflow stopped at gate: ${ENTERPRISE_GATE_NAMES[$step_padded]}"
                exit 1
            fi
        fi
        
        # Execute the enterprise step
        if ! execute_enterprise_step "$step_padded"; then
            log_error "Enterprise workflow failed at step $step_padded"
            exit 1
        fi
        
        echo ""
    done
    
    log_success "🎉 Enterprise workflow completed successfully!"
    log_success "Feature: $FEATURE_NAME"
    log_success "Mode: $MODE" 
    if [[ -n "$COMPLIANCE_FRAMEWORK" ]]; then
        log_success "Compliance: $COMPLIANCE_FRAMEWORK"
    fi
    log_success "Total enterprise steps: ${#ENTERPRISE_WORKFLOW_SEQUENCE[@]}"
}

# Parse arguments and run
parse_args "$@"
main
