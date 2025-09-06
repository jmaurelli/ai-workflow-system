#!/usr/bin/env python3

"""
🏢 Enterprise AI Workflow Runner - Intelligent s01-s08 Sequence Execution
Orchestrates AI agents through enterprise scaling workflow with governance and compliance
"""

import json
import os
import sys
import argparse
import logging
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class AutomationMode(Enum):
    GUIDED = "guided"
    AUTONOMOUS = "autonomous" 
    LEARNING = "learning"

class GateDecision(Enum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    SKIP = "skip"
    LEARN_FROM_HISTORY = "learn_from_history"
    APPROVAL_BOARD_REQUIRED = "approval_board_required"

class ComplianceFramework(Enum):
    GDPR = "GDPR"
    SOC2 = "SOC2"
    PCI = "PCI"
    HIPAA = "HIPAA"
    ISO27001 = "ISO27001"

@dataclass
class EnterpriseWorkflowStep:
    number: str
    doc_name: str
    phase: str
    gate_name: str
    dependencies: List[str]
    compliance_impact: bool = False
    
@dataclass
class EnterpriseExecutionContext:
    feature_name: str
    mode: AutomationMode
    project_root: Path
    enterprise_feature_dir: Optional[Path] = None
    risk_score: float = 0.0
    technology_stack: List[str] = None
    approval_history: Dict[str, bool] = None
    compliance_framework: Optional[ComplianceFramework] = None
    multi_team_coordination: bool = False
    architecture_impact: bool = False

class EnterpriseWorkflowOrchestrator:
    """Intelligent enterprise workflow orchestrator for AI agents"""
    
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load_config()
        self.workflow_steps = self._initialize_workflow_steps()
        self.logger = self._setup_logging()
        
    def _load_config(self) -> Dict:
        """Load enterprise automation configuration"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to load enterprise config: {e}")
    
    def _initialize_workflow_steps(self) -> List[EnterpriseWorkflowStep]:
        """Initialize enterprise workflow steps from configuration"""
        steps = []
        sequence = self.config['enterprise_workflow_execution']['numbered_sequence']
        phase_mapping = self.config['enterprise_workflow_execution']['phase_mapping']
        dependencies = self.config['enterprise_workflow_execution']['dependency_chain']
        
        gate_names = {
            "s01": "mvp_to_scaling_transition",
            "s02": "enterprise_design_decisions",
            "s03": "enterprise_srs_generation",
            "s04": "enterprise_prd_creation",
            "s05": "enterprise_design_analysis",
            "s06": "enterprise_task_creation",
            "s07": "enterprise_completion_summary",
            "s08": "enterprise_history_update"
        }
        
        # Compliance-critical steps
        compliance_critical = {"s03", "s04", "s06", "s07"}
        
        for i, doc_name in enumerate(sequence, 1):
            step_num = f"s{i:02d}"
            phase = self._get_phase_for_step(step_num, phase_mapping)
            
            step = EnterpriseWorkflowStep(
                number=step_num,
                doc_name=doc_name,
                phase=phase,
                gate_name=gate_names.get(step_num, f"enterprise_step_{step_num}"),
                dependencies=dependencies.get(step_num, []),
                compliance_impact=step_num in compliance_critical
            )
            steps.append(step)
            
        return steps
    
    def _get_phase_for_step(self, step_num: str, phase_mapping: Dict) -> str:
        """Get phase name for a step number"""
        for phase, steps in phase_mapping.items():
            if step_num in steps:
                return phase
        return "unknown"
    
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('enterprise_workflow_orchestrator')
        logger.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
        # File handler
        log_file = Path(__file__).parent / 'enterprise-ai-workflow-execution.log'
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        
        return logger
    
    def assess_enterprise_risk_score(self, context: EnterpriseExecutionContext) -> float:
        """Assess enterprise risk score for the workflow execution"""
        risk_score = 0.0
        risk_config = self.config['enterprise_risk_assessment']
        
        # Base enterprise risk is higher than MVP
        risk_score = 0.4
        
        # Compliance framework increases risk oversight need
        if context.compliance_framework:
            risk_score += 0.2
            
        # Multi-team coordination increases risk
        if context.multi_team_coordination:
            risk_score += 0.1
            
        # Architecture impact increases risk
        if context.architecture_impact:
            risk_score += 0.2
        
        # Cap at 1.0
        return min(risk_score, 1.0)
    
    def is_enterprise_gate_required(self, step: EnterpriseWorkflowStep, context: EnterpriseExecutionContext) -> GateDecision:
        """Determine if a gate is required for a specific enterprise step"""
        mode_config = self.config['automation_modes'][context.mode.value]
        gate_config = mode_config['gates']
        
        # Check gate configuration for this step
        gate_behavior = gate_config.get(step.gate_name, "required")
        
        # Compliance framework may override gate requirements
        if context.compliance_framework and step.compliance_impact:
            if gate_behavior == "skip":
                gate_behavior = "required"  # Compliance requires oversight
        
        if gate_behavior == "required":
            return GateDecision.REQUIRED
        elif gate_behavior == "optional":
            return GateDecision.OPTIONAL
        elif gate_behavior == "skip":
            return GateDecision.SKIP
        elif gate_behavior == "learn_from_history":
            return self._evaluate_enterprise_learning_gate(step, context)
        elif gate_behavior == "required_for_new_architecture":
            return self._evaluate_architecture_gate(step, context)
        elif gate_behavior == "required_for_compliance_changes":
            return self._evaluate_compliance_gate(step, context)
        elif gate_behavior == "required_for_production_changes":
            return self._evaluate_production_gate(step, context)
        elif gate_behavior == "required_with_approval_board":
            return GateDecision.APPROVAL_BOARD_REQUIRED
        else:
            return GateDecision.REQUIRED  # Default to safe
    
    def _evaluate_enterprise_learning_gate(self, step: EnterpriseWorkflowStep, context: EnterpriseExecutionContext) -> GateDecision:
        """Evaluate gate requirement based on enterprise learning history"""
        # TODO: Implement enterprise learning logic
        # For now, default to required for enterprise safety
        return GateDecision.REQUIRED
    
    def _evaluate_architecture_gate(self, step: EnterpriseWorkflowStep, context: EnterpriseExecutionContext) -> GateDecision:
        """Evaluate gate requirement for architecture decisions"""
        if context.architecture_impact:
            return GateDecision.REQUIRED
        return GateDecision.OPTIONAL
    
    def _evaluate_compliance_gate(self, step: EnterpriseWorkflowStep, context: EnterpriseExecutionContext) -> GateDecision:
        """Evaluate gate requirement for compliance-related changes"""
        if context.compliance_framework and step.compliance_impact:
            return GateDecision.REQUIRED
        return GateDecision.OPTIONAL
    
    def _evaluate_production_gate(self, step: EnterpriseWorkflowStep, context: EnterpriseExecutionContext) -> GateDecision:
        """Evaluate gate requirement for production-impacting operations"""
        # Enterprise task implementation should always require approval
        if step.gate_name == "enterprise_task_creation":
            return GateDecision.REQUIRED
        return GateDecision.OPTIONAL
    
    def create_enterprise_execution_plan(self, context: EnterpriseExecutionContext) -> List[Tuple[EnterpriseWorkflowStep, GateDecision]]:
        """Create enterprise execution plan with gate decisions"""
        plan = []
        
        for step in self.workflow_steps:
            gate_decision = self.is_enterprise_gate_required(step, context)
            plan.append((step, gate_decision))
            
        return plan
    
    def display_enterprise_execution_plan(self, plan: List[Tuple[EnterpriseWorkflowStep, GateDecision]], context: EnterpriseExecutionContext):
        """Display the enterprise execution plan to the user"""
        print(f"\n🏢 ENTERPRISE AI WORKFLOW EXECUTION PLAN")
        print(f"{'='*60}")
        print(f"Feature: {context.feature_name}")
        print(f"Mode: {context.mode.value}")
        print(f"Risk Score: {context.risk_score:.2f}")
        if context.compliance_framework:
            print(f"Compliance: {context.compliance_framework.value}")
        if context.multi_team_coordination:
            print(f"Coordination: Multi-team required")
        if context.architecture_impact:
            print(f"Architecture: Impact detected")
        print()
        
        current_phase = ""
        for step, gate_decision in plan:
            # Show phase headers
            if step.phase != current_phase:
                print(f"\n🏗️  ENTERPRISE PHASE: {step.phase.upper()}")
                print("-" * 40)
                current_phase = step.phase
            
            # Show step with gate decision
            gate_icon = self._get_enterprise_gate_icon(gate_decision)
            gate_text = self._get_enterprise_gate_text(gate_decision)
            compliance_marker = "📋" if step.compliance_impact else ""
            print(f"  {step.number} → {gate_icon} {gate_text} → {step.doc_name} {compliance_marker}")
        
        print(f"\n{'='*60}")
        
        # Show legend
        print("\nLEGEND:")
        print("🚪 = Human gate required")
        print("🏛️ = Approval board required") 
        print("🔶 = Optional gate")
        print("⚡ = Auto proceed")
        print("🧠 = Learning gate")
        print("📋 = Compliance impact")
    
    def _get_enterprise_gate_icon(self, decision: GateDecision) -> str:
        """Get icon for enterprise gate decision"""
        icons = {
            GateDecision.REQUIRED: "🚪",
            GateDecision.OPTIONAL: "🔶",
            GateDecision.SKIP: "⚡",
            GateDecision.LEARN_FROM_HISTORY: "🧠",
            GateDecision.APPROVAL_BOARD_REQUIRED: "🏛️"
        }
        return icons.get(decision, "❓")
    
    def _get_enterprise_gate_text(self, decision: GateDecision) -> str:
        """Get text description for enterprise gate decision"""
        texts = {
            GateDecision.REQUIRED: "HUMAN GATE",
            GateDecision.OPTIONAL: "optional gate",
            GateDecision.SKIP: "auto proceed",
            GateDecision.LEARN_FROM_HISTORY: "learning gate",
            GateDecision.APPROVAL_BOARD_REQUIRED: "APPROVAL BOARD"
        }
        return texts.get(decision, "unknown")
    
    def execute_enterprise_workflow(self, context: EnterpriseExecutionContext, dry_run: bool = False) -> bool:
        """Execute the complete enterprise workflow"""
        self.logger.info(f"Starting enterprise workflow execution: {context.feature_name}")
        
        # Create execution plan
        plan = self.create_enterprise_execution_plan(context)
        
        # Display plan
        self.display_enterprise_execution_plan(plan, context)
        
        if dry_run:
            print("\n✅ ENTERPRISE DRY RUN COMPLETE - No actions executed")
            return True
        
        # Confirm execution
        response = input("\nStart enterprise workflow execution? (y/N): ")
        if response.lower() != 'y':
            print("Enterprise workflow execution cancelled")
            return False
        
        # Execute each step
        success = True
        for step, gate_decision in plan:
            try:
                if not self._execute_enterprise_step(step, gate_decision, context):
                    success = False
                    break
            except Exception as e:
                self.logger.error(f"Enterprise step {step.number} failed: {e}")
                success = False
                break
        
        if success:
            self.logger.info("🎉 Enterprise workflow completed successfully!")
            print("\n🎉 ENTERPRISE WORKFLOW COMPLETED SUCCESSFULLY!")
        else:
            self.logger.error("❌ Enterprise workflow execution failed")
            print("\n❌ ENTERPRISE WORKFLOW EXECUTION FAILED")
        
        return success
    
    def _execute_enterprise_step(self, step: EnterpriseWorkflowStep, gate_decision: GateDecision, context: EnterpriseExecutionContext) -> bool:
        """Execute a single enterprise workflow step"""
        self.logger.info(f"Executing enterprise step {step.number}: {step.doc_name}")
        
        # Handle gate if required
        if gate_decision in [GateDecision.REQUIRED, GateDecision.APPROVAL_BOARD_REQUIRED]:
            if not self._execute_enterprise_human_gate(step, gate_decision, context):
                return False
        
        # Execute the actual step
        success = self._execute_enterprise_document_workflow(step, context)
        
        if success:
            self.logger.info(f"✅ Enterprise step {step.number} completed successfully")
        else:
            self.logger.error(f"❌ Enterprise step {step.number} failed")
        
        return success
    
    def _execute_enterprise_human_gate(self, step: EnterpriseWorkflowStep, gate_decision: GateDecision, context: EnterpriseExecutionContext) -> bool:
        """Execute enterprise human approval gate"""
        print(f"\n🚪 ENTERPRISE GATE: {step.gate_name}")
        print(f"Phase: {step.phase}")
        print(f"Step: {step.number} - {step.doc_name}")
        if step.compliance_impact:
            print(f"📋 Compliance Impact: YES")
        if context.compliance_framework:
            print(f"📋 Framework: {context.compliance_framework.value}")
        
        if gate_decision == GateDecision.APPROVAL_BOARD_REQUIRED:
            print("🏛️ APPROVAL BOARD REQUIRED")
            response = input("Has the approval board approved this step? (y/N): ")
        else:
            response = input("Do you approve proceeding? (y/N): ")
        
        approved = response.lower() == 'y'
        
        if approved:
            self.logger.info(f"Enterprise gate approved: {step.gate_name}")
        else:
            self.logger.warning(f"Enterprise gate rejected: {step.gate_name}")
        
        return approved
    
    def _execute_enterprise_document_workflow(self, step: EnterpriseWorkflowStep, context: EnterpriseExecutionContext) -> bool:
        """Execute the actual enterprise document workflow step"""
        # TODO: Implement actual enterprise document execution
        # For now, just simulate successful execution
        
        print(f"  📄 Executing enterprise: {step.doc_name}")
        if step.compliance_impact:
            print(f"  📋 Compliance validation: {context.compliance_framework.value if context.compliance_framework else 'Standard'}")
        
        # Simulate processing time
        import time
        time.sleep(1.5)  # Enterprise steps take longer
        
        print(f"  ✅ Completed enterprise: {step.doc_name}")
        return True

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="🏢 Enterprise AI Workflow Runner - Intelligent s01-s08 Sequence Execution"
    )
    
    parser.add_argument("--mode", 
                       choices=[mode.value for mode in AutomationMode],
                       default="guided",
                       help="Enterprise automation mode")
    
    parser.add_argument("--feature", 
                       required=True,
                       help="Feature name for enterprise workflow execution")
    
    parser.add_argument("--dry-run", 
                       action="store_true",
                       help="Show enterprise execution plan without running")
    
    parser.add_argument("--config",
                       type=Path,
                       default=Path(__file__).parent / "enterprise-automation-config.json",
                       help="Path to enterprise automation configuration file")
    
    parser.add_argument("--verbose",
                       action="store_true", 
                       help="Enable verbose logging")
    
    parser.add_argument("--compliance",
                       choices=[cf.value for cf in ComplianceFramework],
                       help="Compliance framework to apply")
    
    parser.add_argument("--multi-team",
                       action="store_true",
                       help="Enable multi-team coordination mode")
    
    parser.add_argument("--architecture-impact",
                       action="store_true", 
                       help="Flag that this feature has architecture impact")
    
    args = parser.parse_args()
    
    # Setup logging level
    if args.verbose:
        logging.getLogger('enterprise_workflow_orchestrator').setLevel(logging.DEBUG)
    
    try:
        # Initialize orchestrator
        orchestrator = EnterpriseWorkflowOrchestrator(args.config)
        
        # Create execution context
        context = EnterpriseExecutionContext(
            feature_name=args.feature,
            mode=AutomationMode(args.mode),
            project_root=Path.cwd(),
            compliance_framework=ComplianceFramework(args.compliance) if args.compliance else None,
            multi_team_coordination=args.multi_team,
            architecture_impact=args.architecture_impact
        )
        
        # Assess risk
        context.risk_score = orchestrator.assess_enterprise_risk_score(context)
        
        # Execute workflow
        success = orchestrator.execute_enterprise_workflow(context, dry_run=args.dry_run)
        
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Enterprise Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
