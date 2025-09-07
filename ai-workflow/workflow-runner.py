#!/usr/bin/env python3

"""
🤖 AI Workflow Runner - Intelligent Numbered Sequence Execution
Orchestrates AI agents through the MVP workflow with smart automation
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

@dataclass
class WorkflowStep:
    number: str
    doc_name: str
    phase: str
    gate_name: str
    dependencies: List[str]
    
@dataclass
class ExecutionContext:
    feature_name: str
    mode: AutomationMode
    project_root: Path
    feature_dir: Optional[Path] = None
    risk_score: float = 0.0
    technology_stack: List[str] = None
    approval_history: Dict[str, bool] = None
    context_mode: str = "STANDALONE_FEATURE"
    existing_project: Optional[str] = None

class WorkflowOrchestrator:
    """Intelligent workflow orchestrator for AI agents"""
    
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load_config()
        self.workflow_steps = self._initialize_workflow_steps()
        self.logger = self._setup_logging()
        
        # LLM API integration attributes
        self.llm_api_enabled = False
        self.llm_provider = None
        self.llm_model = None
        self.llm_config_file = None
        self.cost_limit = None
        
    def _load_config(self) -> Dict:
        """Load automation configuration"""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to load config: {e}")
    
    def _initialize_workflow_steps(self) -> List[WorkflowStep]:
        """Initialize workflow steps from configuration"""
        steps = []
        sequence = self.config['workflow_execution']['numbered_sequence']
        phase_mapping = self.config['workflow_execution']['phase_mapping']
        dependencies = self.config['workflow_execution']['dependency_chain']
        
        gate_names = {
            "01": "feature_directory_creation",
            "02": "prd_generation", 
            "03": "srs_generation",
            "04": "design_decisions",
            "05": "design_analysis",
            "06": "task_creation",
            "07": "task_implementation",
            "08": "completion_summary",
            "09": "project_history"
        }
        
        for i, doc_name in enumerate(sequence, 1):
            step_num = f"{i:02d}"
            phase = self._get_phase_for_step(step_num, phase_mapping)
            
            step = WorkflowStep(
                number=step_num,
                doc_name=doc_name,
                phase=phase,
                gate_name=gate_names.get(step_num, f"step_{step_num}"),
                dependencies=dependencies.get(step_num, [])
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
        logger = logging.getLogger('workflow_orchestrator')
        logger.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        
        # File handler
        log_file = Path(__file__).parent / 'ai-workflow-execution.log'
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        
        return logger
    
    def assess_risk_score(self, context: ExecutionContext) -> float:
        """Assess risk score for the workflow execution"""
        risk_score = 0.0
        risk_config = self.config['risk_assessment']
        
        # Check for high-risk indicators
        high_risk_indicators = risk_config['high_risk_indicators']
        # TODO: Implement actual risk assessment logic
        # For now, return a default moderate risk
        
        return 0.3  # Moderate risk
    
    def is_gate_required(self, step: WorkflowStep, context: ExecutionContext) -> GateDecision:
        """Determine if a gate is required for a specific step"""
        mode_config = self.config['automation_modes'][context.mode.value]
        gate_config = mode_config['gates']
        
        # Check gate configuration for this step
        gate_behavior = gate_config.get(step.gate_name, "required")
        
        if gate_behavior == "required":
            return GateDecision.REQUIRED
        elif gate_behavior == "optional":
            return GateDecision.OPTIONAL
        elif gate_behavior == "skip":
            return GateDecision.SKIP
        elif gate_behavior == "learn_from_history":
            return self._evaluate_learning_gate(step, context)
        elif gate_behavior == "required_for_new_tech":
            return self._evaluate_technology_gate(step, context)
        elif gate_behavior == "required_for_destructive":
            return self._evaluate_destructive_gate(step, context)
        else:
            return GateDecision.REQUIRED  # Default to safe
    
    def _evaluate_learning_gate(self, step: WorkflowStep, context: ExecutionContext) -> GateDecision:
        """Evaluate gate requirement based on learning history"""
        # TODO: Implement learning logic
        # For now, default to required
        return GateDecision.REQUIRED
    
    def _evaluate_technology_gate(self, step: WorkflowStep, context: ExecutionContext) -> GateDecision:
        """Evaluate gate requirement for technology decisions"""
        # TODO: Check if technology stack contains new/unknown technologies
        return GateDecision.OPTIONAL
    
    def _evaluate_destructive_gate(self, step: WorkflowStep, context: ExecutionContext) -> GateDecision:
        """Evaluate gate requirement for potentially destructive operations"""
        # Task implementation should always require human approval for destructive actions
        if step.gate_name == "task_implementation":
            return GateDecision.REQUIRED
        return GateDecision.OPTIONAL
    
    def create_execution_plan(self, context: ExecutionContext) -> List[Tuple[WorkflowStep, GateDecision]]:
        """Create execution plan with gate decisions"""
        plan = []
        
        for step in self.workflow_steps:
            gate_decision = self.is_gate_required(step, context)
            plan.append((step, gate_decision))
            
        return plan
    
    def display_execution_plan(self, plan: List[Tuple[WorkflowStep, GateDecision]], context: ExecutionContext):
        """Display the execution plan to the user"""
        print(f"\n🚀 AI WORKFLOW EXECUTION PLAN")
        print(f"{'='*50}")
        print(f"Feature: {context.feature_name}")
        print(f"Mode: {context.mode.value}")
        print(f"Risk Score: {context.risk_score:.2f}")
        print()
        
        current_phase = ""
        for step, gate_decision in plan:
            # Show phase headers
            if step.phase != current_phase:
                print(f"\n🏗️  PHASE: {step.phase.upper()}")
                print("-" * 30)
                current_phase = step.phase
            
            # Show step with gate decision
            gate_icon = self._get_gate_icon(gate_decision)
            gate_text = self._get_gate_text(gate_decision)
            print(f"  {step.number} → {gate_icon} {gate_text} → {step.doc_name}")
        
        print(f"\n{'='*50}")
    
    def _get_gate_icon(self, decision: GateDecision) -> str:
        """Get icon for gate decision"""
        icons = {
            GateDecision.REQUIRED: "🚪",
            GateDecision.OPTIONAL: "🔶",
            GateDecision.SKIP: "⚡",
            GateDecision.LEARN_FROM_HISTORY: "🧠"
        }
        return icons.get(decision, "❓")
    
    def _get_gate_text(self, decision: GateDecision) -> str:
        """Get text description for gate decision"""
        texts = {
            GateDecision.REQUIRED: "HUMAN GATE",
            GateDecision.OPTIONAL: "optional gate",
            GateDecision.SKIP: "auto proceed",
            GateDecision.LEARN_FROM_HISTORY: "learning gate"
        }
        return texts.get(decision, "unknown")
    
    def execute_workflow(self, context: ExecutionContext, dry_run: bool = False) -> bool:
        """Execute the complete workflow"""
        self.logger.info(f"Starting workflow execution: {context.feature_name}")
        
        # Create execution plan
        plan = self.create_execution_plan(context)
        
        # Display plan
        self.display_execution_plan(plan, context)
        
        if dry_run:
            print("\n✅ DRY RUN COMPLETE - No actions executed")
            return True
        
        # Confirm execution (skip prompt in autonomous mode)
        if context.mode.value == "autonomous":
            print("\n🚀 Starting autonomous workflow execution...")
        else:
            response = input("\nStart workflow execution? (y/N): ")
            if response.lower() != 'y':
                print("Workflow execution cancelled")
                return False
        
        # Execute each step
        success = True
        for step, gate_decision in plan:
            try:
                if not self._execute_step(step, gate_decision, context):
                    success = False
                    break
            except Exception as e:
                self.logger.error(f"Step {step.number} failed: {e}")
                success = False
                break
        
        if success:
            self.logger.info("🎉 Workflow completed successfully!")
            print("\n🎉 WORKFLOW COMPLETED SUCCESSFULLY!")
        else:
            self.logger.error("❌ Workflow execution failed")
            print("\n❌ WORKFLOW EXECUTION FAILED")
        
        return success
    
    def _execute_step(self, step: WorkflowStep, gate_decision: GateDecision, context: ExecutionContext) -> bool:
        """Execute a single workflow step"""
        self.logger.info(f"Executing step {step.number}: {step.doc_name}")
        
        # Handle gate if required
        if gate_decision == GateDecision.REQUIRED:
            if not self._execute_human_gate(step, context):
                return False
        
        # Execute the actual step
        success = self._execute_document_workflow(step, context)
        
        if success:
            self.logger.info(f"✅ Step {step.number} completed successfully")
        else:
            self.logger.error(f"❌ Step {step.number} failed")
        
        return success
    
    def _execute_human_gate(self, step: WorkflowStep, context: ExecutionContext) -> bool:
        """Execute human approval gate"""
        print(f"\n🚪 HUMAN GATE: {step.gate_name}")
        print(f"Phase: {step.phase}")
        print(f"Step: {step.number} - {step.doc_name}")
        
        response = input("Do you approve proceeding? (y/N): ")
        approved = response.lower() == 'y'
        
        if approved:
            self.logger.info(f"Gate approved: {step.gate_name}")
        else:
            self.logger.warning(f"Gate rejected: {step.gate_name}")
        
        return approved
    
    def _execute_document_workflow(self, step: WorkflowStep, context: ExecutionContext) -> bool:
        """Execute the actual document workflow step"""
        print(f"  📄 Executing: {step.doc_name}")
        
        # Prepare feature directory
        feature_slug = context.feature_name.lower().replace(' ', '-').replace('_', '-')
        date_prefix = datetime.now().strftime('%Y-%m-%d')
        feature_dir = context.project_root / "features" / f"{date_prefix}-{feature_slug}"
        feature_dir.mkdir(parents=True, exist_ok=True)
        
        # Prepare document path
        workflow_dir = Path(__file__).parent / "lean-workflow"
        doc_path = workflow_dir / step.doc_name
        
        if not doc_path.exists():
            self.logger.error(f"Workflow document not found: {doc_path}")
            return False
        
        # Execute using workflow executor
        try:
            import subprocess
            
            cmd = [
                "python3", 
                str(Path(__file__).parent / "workflow-executor.py"),
                str(doc_path),
                "--feature", context.feature_name,
                "--feature-dir", str(feature_dir),
                "--mode", context.mode.value,
                "--step", step.number,
                "--phase", step.phase
            ]
            
            # Add LLM API configuration if enabled
            if self.llm_api_enabled:
                cmd.append("--llm-api")
                
                if self.llm_provider:
                    cmd.extend(["--llm-provider", self.llm_provider])
                
                if self.llm_model:
                    cmd.extend(["--llm-model", self.llm_model])
                
                if self.llm_config_file:
                    cmd.extend(["--llm-config", str(self.llm_config_file)])
                
                if self.cost_limit:
                    cmd.extend(["--cost-limit", str(self.cost_limit)])
                
                self.logger.info(f"🤖 LLM API enabled: Real content generation mode!")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print(f"  ✅ Completed: {step.doc_name}")
                print(f"  📁 Output saved to: {feature_dir}")
                self.logger.info(f"Workflow step {step.number} completed successfully")
                return True
            else:
                print(f"  ❌ Failed: {step.doc_name}")
                self.logger.error(f"Workflow step {step.number} failed: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            self.logger.error(f"Workflow step {step.number} timed out")
            return False
        except Exception as e:
            self.logger.error(f"Error executing workflow step {step.number}: {e}")
            return False

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="🤖 AI Workflow Runner - Intelligent Numbered Sequence Execution"
    )
    
    parser.add_argument("--mode", 
                       choices=[mode.value for mode in AutomationMode],
                       default="guided",
                       help="Automation mode")
    
    parser.add_argument("--feature", 
                       required=True,
                       help="Feature name for workflow execution")
    
    parser.add_argument("--existing-project",
                       help="Existing project name (for feature addition to MVP projects)")
    
    parser.add_argument("--dry-run", 
                       action="store_true",
                       help="Show execution plan without running")
    
    parser.add_argument("--config",
                       type=Path,
                       default=Path(__file__).parent / "automation-config.json",
                       help="Path to automation configuration file")
    
    parser.add_argument("--verbose",
                       action="store_true", 
                       help="Enable verbose logging")
    
    # LLM API integration arguments
    parser.add_argument("--llm-api",
                       action="store_true",
                       help="Enable real LLM API content generation")
    
    parser.add_argument("--llm-provider",
                       help="LLM provider (openai, anthropic, local_ollama, groq)")
    
    parser.add_argument("--llm-model",
                       help="LLM model to use")
    
    parser.add_argument("--llm-config",
                       type=Path,
                       help="Path to LLM configuration file")
    
    parser.add_argument("--cost-limit",
                       type=float,
                       help="Override cost limit for LLM usage")
    
    args = parser.parse_args()
    
    # Setup logging level
    if args.verbose:
        logging.getLogger('workflow_orchestrator').setLevel(logging.DEBUG)
    
    try:
        # Initialize orchestrator
        orchestrator = WorkflowOrchestrator(args.config)
        
        # Configure LLM API if enabled
        if args.llm_api:
            orchestrator.llm_api_enabled = True
            orchestrator.llm_provider = args.llm_provider
            orchestrator.llm_model = args.llm_model
            orchestrator.llm_config_file = args.llm_config
            orchestrator.cost_limit = args.cost_limit
        
        # Determine project directory and context mode
        if args.existing_project:
            # Feature addition to existing MVP project
            project_root = Path.home() / "Projects" / args.existing_project
            context_mode = "FEATURE_ADDITION"
            
            if not project_root.exists():
                print(f"❌ Error: Project '{args.existing_project}' not found in ~/Projects/")
                print(f"💡 Tip: Use mvp-initializer.py to create new projects")
                sys.exit(1)
                
            print(f"➕ Adding feature '{args.feature}' to existing project '{args.existing_project}'")
        else:
            # Standalone feature (legacy mode)
            project_root = Path.cwd()
            context_mode = "STANDALONE_FEATURE"
            print(f"🔧 Creating standalone feature '{args.feature}'")

        # Create execution context
        context = ExecutionContext(
            feature_name=args.feature,
            mode=AutomationMode(args.mode),
            project_root=project_root
        )
        
        # Add context mode for LLM prompting
        context.context_mode = context_mode
        context.existing_project = args.existing_project
        
        # Assess risk
        context.risk_score = orchestrator.assess_risk_score(context)
        
        # Execute workflow
        if args.dry_run:
            print(f"\n🧪 DRY RUN - Execution Plan for '{args.feature}':")
            if args.existing_project:
                print(f"   📁 Target: Adding to existing project '{args.existing_project}'")
            else:
                print(f"   📁 Target: Creating standalone feature")
            
            success = orchestrator.execute_workflow(context, dry_run=True)
        else:
            success = orchestrator.execute_workflow(context, dry_run=False)
            
            if success:
                if args.existing_project:
                    print(f"\n🎉 Feature '{args.feature}' added successfully to project '{args.existing_project}'!")
                    print(f"📁 Project location: {context.project_root}")
                else:
                    print(f"\n🎉 Standalone feature '{args.feature}' completed successfully!")
            else:
                print(f"\n❌ Workflow failed for '{args.feature}'")
        
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
