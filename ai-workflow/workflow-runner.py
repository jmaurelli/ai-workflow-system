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
import getpass
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

def prompt_ai_vendor_setup() -> tuple:
    """Interactive prompt for AI vendor, model selection, and API key"""
    print("\n🤖 AI CONSULTANT SETUP")
    print("=" * 40)
    
    # Step 1: Choose provider
    providers = {
        "1": {"name": "OpenAI", "provider": "openai", "env_var": "OPENAI_API_KEY"},
        "2": {"name": "Claude (Anthropic)", "provider": "anthropic", "env_var": "ANTHROPIC_API_KEY"},
        "3": {"name": "Google Gemini", "provider": "google", "env_var": "GOOGLE_API_KEY"},
        "4": {"name": "Exit (AI consultant required)", "provider": None}
    }
    
    print("⚡ Choose your AI provider:")
    for key, provider in providers.items():
        if provider["provider"]:
            print(f"   {key}. {provider['name']}")
        else:
            print(f"   {key}. {provider['name']}")
    print()
    
    while True:
        try:
            max_choice = len(providers)
            choice = input(f"Select AI provider (1-{max_choice}): ").strip()
            if choice in providers:
                selected_provider = providers[choice]
                if not selected_provider["provider"]:
                    print("\n🚫 AI consultant is required for this project")
                    return "skip", None
                
                # Step 2: Get API key
                existing_key = os.getenv(selected_provider["env_var"])
                api_key = None
                
                if existing_key:
                    print(f"✅ Found existing {selected_provider['name']} API key")
                    api_key = existing_key
                else:
                    # Prompt for API key with 3 attempt limit
                    max_attempts = 3
                    for attempt in range(max_attempts):
                        print(f"\n🔑 {selected_provider['name']} API Key (Attempt {attempt + 1}/{max_attempts})")
                        if selected_provider['provider'] == 'openai':
                            print("💡 Get your key from: https://platform.openai.com/api-keys")
                        elif selected_provider['provider'] == 'anthropic':
                            print("💡 Get your key from: https://console.anthropic.com/settings/keys")
                        elif selected_provider['provider'] == 'google':
                            print("💡 Get your key from: https://aistudio.google.com/app/apikey")
                        print("🔒 Your API key will be hidden for security")
                        
                        try:
                            api_key = getpass.getpass(f"Enter your {selected_provider['name']} API key: ").strip()
                        except (KeyboardInterrupt, EOFError):
                            print("\n❌ API key input cancelled")
                            return "cancelled", None
                            
                        if not api_key:
                            print("❌ API key required for AI consultant")
                            if attempt < max_attempts - 1:
                                continue
                            else:
                                break
                        
                        # Validate API key format
                        if not _validate_api_key(selected_provider["provider"], api_key):
                            print(f"❌ Invalid {selected_provider['name']} API key format")
                            if selected_provider['provider'] == 'openai':
                                print("💡 OpenAI keys start with 'sk-' and are ~51 characters long")
                            elif selected_provider['provider'] == 'anthropic':
                                print("💡 Claude keys start with 'sk-ant-' and are longer")
                            elif selected_provider['provider'] == 'google':
                                print("💡 Google keys are typically 39 characters, mix of letters/numbers")
                            
                            if attempt < max_attempts - 1:
                                print("🔄 Please try again with a valid API key")
                                continue
                            else:
                                break
                        else:
                            print(f"✅ API key format looks valid for {selected_provider['name']}")
                            break
                    
                    if not api_key or not _validate_api_key(selected_provider["provider"], api_key):
                        print(f"\n❌ Failed to get valid {selected_provider['name']} API key after {max_attempts} attempts")
                        print("🚫 AI consultant is required for this project - cannot proceed")
                        return "failed", None

                # Step 3: Get available models (simplified for workflow-runner)
                available_models = _get_fallback_models(selected_provider["provider"])
                
                print(f"\nChoose your {selected_provider['name']} model:")
                for i, model in enumerate(available_models, 1):
                    print(f"   {i}. {model['name']} - {model['description']}")
                print()
                
                # Model selection loop
                while True:
                    try:
                        model_choice = input(f"Select model (1-{len(available_models)}): ").strip()
                        if model_choice.isdigit():
                            model_idx = int(model_choice) - 1
                            if 0 <= model_idx < len(available_models):
                                selected_model = available_models[model_idx]
                                
                                # Create final vendor config
                                vendor_config = {
                                    "name": selected_provider["name"],
                                    "provider": selected_provider["provider"], 
                                    "model": selected_model["id"],
                                    "env_var": selected_provider["env_var"]
                                }
                                
                                print(f"✅ Selected: {selected_model['name']} ({selected_model['id']})")
                                
                                # Set API key in environment for subprocess inheritance
                                os.environ[selected_provider["env_var"]] = api_key
                                
                                return vendor_config, api_key
                            else:
                                print(f"❌ Please enter a number from 1 to {len(available_models)}")
                        else:
                            print(f"❌ Please enter a number from 1 to {len(available_models)}")
                            
                    except KeyboardInterrupt:
                        print("\n❌ Model selection cancelled")
                        return "cancelled", None
                        
            else:
                print(f"❌ Please enter a number from 1 to {max_choice}")
                
        except KeyboardInterrupt:
            print("\n❌ AI setup cancelled")
            return "cancelled", None

def _validate_api_key(provider: str, api_key: str) -> bool:
    """Validate API key format for different providers"""
    if not api_key or not api_key.strip():
        return False
    
    api_key = api_key.strip()
    
    if provider == "openai":
        # OpenAI keys start with 'sk-' and are typically 51 characters
        return api_key.startswith("sk-") and len(api_key) >= 20
    
    elif provider == "anthropic":
        # Anthropic keys start with 'sk-ant-' 
        return api_key.startswith("sk-ant-") and len(api_key) >= 20
    
    elif provider == "google":
        # Google API keys are typically 39 characters, alphanumeric + some symbols
        return len(api_key) >= 20 and len(api_key) <= 50 and api_key.replace("-", "").replace("_", "").isalnum()
    
    return False

def _get_fallback_models(provider: str) -> List[Dict[str, str]]:
    """Get fallback models for a provider"""
    fallback_models = {
        "openai": [
            {"id": "gpt-4o", "name": "GPT-4o", "description": "Latest multimodal model - text, images, audio"},
            {"id": "gpt-4o-mini", "name": "GPT-4o Mini", "description": "Efficient & fast multimodal model"},
            {"id": "gpt-4-turbo", "name": "GPT-4 Turbo", "description": "Advanced reasoning with large context"},
            {"id": "gpt-3.5-turbo", "name": "GPT-3.5 Turbo", "description": "Fast & cost-effective"}
        ],
        "anthropic": [
            {"id": "claude-3-5-sonnet-20241022", "name": "Claude 3.5 Sonnet", "description": "Latest Sonnet - Balanced intelligence & speed"},
            {"id": "claude-3-5-haiku-20241022", "name": "Claude 3.5 Haiku", "description": "Fastest - Optimized for speed"},
            {"id": "claude-3-opus-20240229", "name": "Claude 3 Opus", "description": "Most intelligent - Complex reasoning"}
        ],
        "google": [
            {"id": "gemini-2.0-flash-exp", "name": "Gemini 2.0 Flash", "description": "Latest experimental - fast & efficient"},
            {"id": "gemini-1.5-pro", "name": "Gemini 1.5 Pro", "description": "Advanced reasoning & large context"},
            {"id": "gemini-1.5-flash", "name": "Gemini 1.5 Flash", "description": "Fast & efficient processing"}
        ]
    }
    
    return fallback_models.get(provider, [])

def create_project_structure(project_path: Path, project_name: str) -> None:
    """Create standard project structure with basic files"""
    try:
        # Create standard directories
        directories = ["src", "docs", "tests", "features"]
        for dir_name in directories:
            dir_path = project_path / dir_name
            if not dir_path.exists():
                dir_path.mkdir()
                print(f"📁 Created {dir_name}/ directory")
        
        # Create standard README.md
        readme_path = project_path / "README.md"
        if not readme_path.exists():
            readme_content = f"""# {project_name.replace('-', ' ').title()}

## Overview

This project was created using the AI Workflow System for automated MVP development and documentation.

## Project Structure

```
{project_name}/
├── README.md              # This file - project overview
├── src/                   # Source code
├── docs/                  # Project documentation
├── tests/                 # Test files
├── features/              # AI-generated workflow specifications
│   └── 2025-XX-XX-{project_name}-mvp-initialization/
│       ├── prd.md         # Product Requirements Document
│       ├── srs.md         # Software Requirements Specification
│       ├── tasks.md       # Implementation roadmap
│       └── design-analysis.md # Architecture decisions
└── project-manifest.json  # Project metadata
```

## Getting Started

1. **Review the AI-generated specifications**: Navigate to `features/` directory
2. **Check the latest workflow**: Look in the most recent dated directory in `features/`
3. **Follow the implementation plan**: Use the generated `tasks.md` for development guidance
4. **Start development**: Build your application in the `src/` directory

## Adding Features

```bash
# Add new features to this project
./workflow-runner.py add-feature FEATURE_NAME --to {project_name}
```

## Development

This project follows standard development practices with AI-assisted planning and documentation generation.

---
*Generated by AI Workflow System*
"""
            readme_path.write_text(readme_content)
            print("📄 Created standard README.md")
        
        # Create basic .gitignore
        gitignore_path = project_path / ".gitignore"
        if not gitignore_path.exists():
            gitignore_content = """# Dependencies
node_modules/
__pycache__/
*.pyc
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Build outputs
dist/
build/
*.egg-info/
"""
            gitignore_path.write_text(gitignore_content)
            print("📄 Created .gitignore")
        
        # Create project manifest
        manifest_path = project_path / "project-manifest.json"
        if not manifest_path.exists():
            from datetime import datetime
            manifest = {
                "project_name": project_name,
                "created_at": datetime.now().isoformat(),
                "project_type": "MVP", 
                "status": "initializing",
                "workflow_version": "3.0",
                "features": [],
                "mvp_context": {
                    "initialization_mode": "workflow-runner-create-mvp",
                    "automation_mode": "guided"
                }
            }
            
            import json
            with open(manifest_path, 'w') as f:
                json.dump(manifest, f, indent=2)
            print("📊 Created project-manifest.json")
            
        print("🎉 Standard project structure created!")
        
    except Exception as e:
        print(f"⚠️  Error creating project structure: {e}")

def validate_project_name(project_name: str) -> str:
    """Validate and normalize project name"""
    if not project_name:
        raise ValueError("Project name cannot be empty")
    
    # Convert to lowercase and replace spaces/underscores with hyphens
    normalized = project_name.lower().replace(' ', '-').replace('_', '-')
    
    # Remove any characters that aren't alphanumeric or hyphens
    import re
    normalized = re.sub(r'[^a-z0-9-]', '', normalized)
    
    if not normalized:
        raise ValueError("Project name must contain alphanumeric characters")
    
    return normalized

def list_projects() -> None:
    """List all MVP projects in ~/Projects/"""
    projects_dir = Path.home() / "Projects"
    
    if not projects_dir.exists():
        print("📁 No ~/Projects/ directory found")
        print("💡 Create your first MVP with: ./workflow-runner.py create-mvp PROJECT_NAME")
        return
    
    project_dirs = [d for d in projects_dir.iterdir() if d.is_dir()]
    
    if not project_dirs:
        print("📁 No projects found in ~/Projects/")
        print("💡 Create your first MVP with: ./workflow-runner.py create-mvp PROJECT_NAME")
        return
    
    print("📋 MVP PROJECTS IN ~/Projects/")
    print("=" * 40)
    
    for project_dir in sorted(project_dirs):
        manifest_path = project_dir / "project-manifest.json"
        if manifest_path.exists():
            try:
                import json
                with open(manifest_path, 'r') as f:
                    manifest = json.load(f)
                status = manifest.get('status', 'unknown')
                created = manifest.get('created_at', 'unknown')[:10]  # Just date
                features_count = len(manifest.get('features', []))
                print(f"  📁 {project_dir.name} - {status} (created: {created}, {features_count} features)")
            except:
                print(f"  📁 {project_dir.name} - status unknown")
        else:
            print(f"  📁 {project_dir.name} - not an MVP project")

def show_project_status(project_name: str) -> None:
    """Show detailed status for a project"""
    project_path = Path.home() / "Projects" / project_name
    
    if not project_path.exists():
        print(f"❌ Project '{project_name}' not found in ~/Projects/")
        print("💡 Use 'list-projects' to see available projects")
        return
    
    manifest_path = project_path / "project-manifest.json"
    if not manifest_path.exists():
        print(f"❌ '{project_name}' is not an MVP project (no project-manifest.json)")
        return
    
    try:
        import json
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        print(f"📊 PROJECT STATUS: {project_name}")
        print("=" * 50)
        print(f"📁 Location: {project_path}")
        print(f"📅 Created: {manifest.get('created_at', 'Unknown')}")
        print(f"📊 Status: {manifest.get('status', 'Unknown')}")
        print(f"🤖 Workflow Version: {manifest.get('workflow_version', 'Unknown')}")
        
        features = manifest.get('features', [])
        print(f"\n🔧 FEATURES ({len(features)} total):")
        print("-" * 30)
        if features:
            for feature in features:
                print(f"  • {feature}")
        else:
            print("  • No additional features yet")
        
        # Show feature directories
        features_dir = project_path / "features"
        if features_dir.exists():
            feature_dirs = sorted([d for d in features_dir.iterdir() if d.is_dir()])
            if feature_dirs:
                print(f"\n📄 GENERATED DOCUMENTATION:")
                print("-" * 30)
                for feature_dir in feature_dirs:
                    print(f"  📁 {feature_dir.name}/")
                    # Count generated files
                    md_files = list(feature_dir.glob("*.md"))
                    if md_files:
                        print(f"     📋 {len(md_files)} documents generated")
        
        print(f"\n🚀 NEXT STEPS:")
        print("-" * 30)
        print(f"  • Add features: ./workflow-runner.py add-feature FEATURE_NAME --to {project_name}")
        print(f"  • View files: ls -la {project_path}/")
        
    except Exception as e:
        print(f"❌ Error reading project status: {e}")

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
        """Execute human approval gate with enhanced context"""
        print(f"\n🚪 HUMAN GATE: {step.gate_name}")
        print("=" * 60)
        print(f"📋 Phase: {step.phase.upper()}")
        print(f"📄 Step: {step.number} - {step.doc_name}")
        print(f"🎯 Feature: {context.feature_name}")
        print()
        
        # Show step context and impact
        step_descriptions = {
            "01-mvp-entrypoint.md": "Collect project requirements and initialize project data",
            "02-gen-prd.md": "Generate Product Requirements Document with features and goals",
            "03-gen-srs.md": "Create Software Requirements Specification with quality standards",
            "04-gen-design-decisions-lite.md": "Choose technology stack and architecture patterns",
            "05-gen-design.md": "Analyze existing code and plan component integration",
            "06-gen-tasks-and-testing.md": "Generate implementation tasks with acceptance criteria",
            "07-process-tasks.md": "Execute tasks with Test-Driven Development approach",
            "08-gen-completion-summary.md": "Generate executive summary with traceability links",
            "09-gen-project-history.md": "Capture organizational learning and insights"
        }
        
        description = step_descriptions.get(step.doc_name, "Execute workflow step")
        print(f"📝 About to: {description}")
        
        # Show impact
        if "design-decisions" in step.doc_name:
            print(f"💡 Impact: Technology choices will affect all subsequent implementation steps")
        elif "tasks" in step.doc_name:
            print(f"💡 Impact: Generated tasks will define the implementation roadmap")
        elif "prd" in step.doc_name:
            print(f"💡 Impact: Requirements will define scope and success criteria")
        elif "completion" in step.doc_name:
            print(f"💡 Impact: Creates final project report and documentation")
        else:
            print(f"💡 Impact: Generates documentation for {step.phase} phase")
        
        print(f"📁 Output location: {context.feature_dir}")
        print()
        print("Options:")
        print("  y - Approve and proceed")
        print("  n - Reject and stop workflow")
        print("  s - Skip this step")
        print("  ? - Show more details")
        
        while True:
            try:
                response = input("Decision (y/N/s/?): ").lower().strip()
                
                if response == 'y':
                    print("✅ Step approved - proceeding...")
                    self.logger.info(f"Gate approved: {step.gate_name}")
                    return True
                    
                elif response == 'n' or response == '':
                    print("❌ Step rejected - stopping workflow")
                    self.logger.warning(f"Gate rejected: {step.gate_name}")
                    return False
                    
                elif response == 's':
                    print("⏭️ Step skipped - continuing to next step")
                    self.logger.info(f"Gate skipped: {step.gate_name}")
                    return True
                    
                elif response == '?':
                    print(f"\n📖 STEP DETAILS:")
                    print(f"Document: {step.doc_name}")
                    print(f"Purpose: {description}")
                    print(f"Phase: {step.phase}")
                    print(f"Previous steps: {step.number - 1} completed")
                    print(f"Feature directory: {context.feature_dir}")
                    print(f"Project root: {context.project_root}")
                    print()
                    continue
                    
                else:
                    print("Please enter 'y' (yes), 'n' (no), 's' (skip), or '?' (help)")
                    continue
                    
            except KeyboardInterrupt:
                print("\n❌ Workflow cancelled by user")
                return False
    
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
        
        # Execute using workflow executor (direct module import - no subprocess)
        try:
            # Import workflow executor using importlib to handle hyphenated filename
            import sys
            import importlib.util
            
            # Load workflow-executor.py as a module
            workflow_executor_path = Path(__file__).parent / "workflow-executor.py"
            spec = importlib.util.spec_from_file_location("workflow_executor", workflow_executor_path)
            workflow_executor_module = importlib.util.module_from_spec(spec)
            sys.modules["workflow_executor"] = workflow_executor_module
            spec.loader.exec_module(workflow_executor_module)
            
            # Import the classes we need
            WorkflowDocumentExecutor = workflow_executor_module.WorkflowDocumentExecutor
            WorkflowContext = workflow_executor_module.WorkflowContext
            
            # Create workflow executor instance
            executor = WorkflowDocumentExecutor(debug=False)
            
            # Configure LLM API settings if enabled
            if self.llm_api_enabled:
                executor.llm_api_enabled = True
                executor.llm_provider = self.llm_provider
                executor.llm_model = self.llm_model
                executor.llm_config_file = self.llm_config_file
                executor.cost_limit = self.cost_limit
                self.logger.info(f"🤖 LLM API enabled: Real content generation mode!")
            
            # Create workflow context for executor
            workflow_context = WorkflowContext(
                feature_name=context.feature_name,
                feature_slug=context.feature_name.lower().replace(' ', '-').replace('_', '-'),
                feature_dir=feature_dir,
                mode=context.mode.value,
                phase=step.phase,
                step_number=step.number,
                project_data={},  # Will be populated by interactive collection in Step 01
                generated_files=[],
                execution_log=[]
            )
            
            # Execute the workflow document directly
            success = executor.execute_workflow_document(
                doc_path,
                workflow_context,
                ai_agent_available=True
            )
            
            if success:
                print(f"  ✅ Completed: {step.doc_name}")
                print(f"  📁 Output saved to: {feature_dir}")
                self.logger.info(f"Workflow step {step.number} completed successfully")
                return True
            else:
                print(f"  ❌ Failed: {step.doc_name}")
                self.logger.error(f"Workflow step {step.number} failed")
                return False
                
        except ImportError as e:
            self.logger.error(f"Error importing workflow executor: {e}")
            print(f"  ❌ Failed: Missing workflow executor module")
            return False
        except Exception as e:
            self.logger.error(f"Error executing workflow step {step.number}: {e}")
            print(f"  ❌ Failed: {step.doc_name} - {e}")
            return False

def main():
    """Main entry point with subcommand support"""
    parser = argparse.ArgumentParser(
        description="🤖 AI Workflow Runner - Intelligent Project & Feature Management",
        prog="workflow-runner.py"
    )
    
    # Global flags
    parser.add_argument("--mode", 
                       choices=[mode.value for mode in AutomationMode],
                       default="guided",
                       help="Automation mode (default: guided)")
    
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
    
    # Advanced LLM configuration (LLM API is always enabled)
    parser.add_argument("--llm-provider",
                       help="LLM provider (openai, anthropic, google) - will prompt if not specified")
    
    parser.add_argument("--llm-model",
                       help="LLM model to use - will prompt if not specified")
    
    parser.add_argument("--llm-config",
                       type=Path,
                       help="Path to LLM configuration file")
    
    parser.add_argument("--cost-limit",
                       type=float,
                       help="Override cost limit for LLM usage")
    
    # Create subparsers for commands
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
        metavar="COMMAND"
    )
    
    # create-mvp subcommand
    create_mvp_parser = subparsers.add_parser(
        "create-mvp",
        help="Create a new MVP project with standard structure",
        description="🚀 Create a new MVP project in ~/Projects/ with AI-generated documentation"
    )
    create_mvp_parser.add_argument(
        "project_name",
        help="Name of the new MVP project"
    )
    
    # add-feature subcommand  
    add_feature_parser = subparsers.add_parser(
        "add-feature", 
        help="Add a feature to an existing MVP project",
        description="➕ Add a new feature to an existing MVP project with AI-generated documentation"
    )
    add_feature_parser.add_argument(
        "feature_name",
        help="Name of the feature to add"
    )
    add_feature_parser.add_argument(
        "--to",
        dest="project_name",
        required=True,
        help="Target project name (must exist in ~/Projects/)"
    )
    
    # list-projects subcommand
    list_projects_parser = subparsers.add_parser(
        "list-projects",
        help="List all MVP projects",
        description="📋 List all MVP projects in ~/Projects/"
    )
    
    # status subcommand
    status_parser = subparsers.add_parser(
        "status",
        help="Show project status and recent activity", 
        description="📊 Show detailed status for an MVP project"
    )
    status_parser.add_argument(
        "project_name", 
        help="Project name to show status for"
    )
    
    args = parser.parse_args()
    
    # Show help if no command provided
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Setup logging level
    if args.verbose:
        logging.getLogger('workflow_orchestrator').setLevel(logging.DEBUG)
    
    # Handle utility commands first (no orchestrator needed)
    if args.command == "list-projects":
        list_projects()
        return
    
    if args.command == "status":
        show_project_status(args.project_name)
        return
    
    try:
        # Initialize orchestrator for workflow commands
        orchestrator = WorkflowOrchestrator(args.config)
        
        # Always configure LLM API (no --llm-api flag needed)
        api_key_available = any([
            os.getenv("OPENAI_API_KEY"),
            os.getenv("ANTHROPIC_API_KEY"), 
            os.getenv("GOOGLE_API_KEY")
        ])
        
        # If no API key available and no specific provider/model given, prompt for setup
        if not api_key_available and not (args.llm_provider and args.llm_model):
            print("🤖 LLM API required - no API key found in environment variables")
            vendor_setup = prompt_ai_vendor_setup()
            
            if vendor_setup in ["cancelled", "failed", "skip"]:
                print("❌ AI consultant is required for workflow operations")
                sys.exit(1)
            
            vendor_config, api_key = vendor_setup
            
            # Use the selected provider and model
            orchestrator.llm_api_enabled = True
            orchestrator.llm_provider = vendor_config["provider"]
            orchestrator.llm_model = vendor_config["model"]
            orchestrator.llm_config_file = args.llm_config
            orchestrator.cost_limit = args.cost_limit
            
            print(f"✅ Configured {vendor_config['name']} with model {vendor_config['model']}")
        else:
            # Use provided arguments or environment variables
            orchestrator.llm_api_enabled = True
            orchestrator.llm_provider = args.llm_provider
            orchestrator.llm_model = args.llm_model
            orchestrator.llm_config_file = args.llm_config
            orchestrator.cost_limit = args.cost_limit
            
            if api_key_available:
                print("✅ Using existing API key from environment variables")
        
        # Handle create-mvp command
        if args.command == "create-mvp":
            project_name = validate_project_name(args.project_name)
            project_root = Path.home() / "Projects" / project_name
            
            # Check if project already exists
            if project_root.exists():
                print(f"❌ Project '{project_name}' already exists at {project_root}")
                print(f"💡 Use 'add-feature' to add features to existing projects")
                sys.exit(1)
            
            # Create project directory and structure
            project_root.mkdir(parents=True, exist_ok=True)
            print(f"🚀 Creating new MVP project: {project_name}")
            print(f"📁 Project location: {project_root}")
            
            # Create standard project structure
            create_project_structure(project_root, project_name)
            
            # Create execution context for MVP initialization  
            feature_name = f"{project_name}-mvp-initialization"
            context = ExecutionContext(
                feature_name=feature_name,
                mode=AutomationMode(args.mode),
                project_root=project_root,
                context_mode="MVP_CREATION"
            )
            
            print(f"\n🤖 Starting AI workflow for MVP initialization...")
            
        # Handle add-feature command
        elif args.command == "add-feature":
            project_name = args.project_name
            feature_name = args.feature_name
            project_root = Path.home() / "Projects" / project_name
            
            # Check if project exists
            if not project_root.exists():
                print(f"❌ Project '{project_name}' not found in ~/Projects/")
                print(f"💡 Create it first with: ./workflow-runner.py create-mvp {project_name}")
                sys.exit(1)
            
            # Verify it's an MVP project
            manifest_path = project_root / "project-manifest.json"
            if not manifest_path.exists():
                print(f"❌ '{project_name}' is not an MVP project (no project-manifest.json)")
                print(f"💡 Create it first with: ./workflow-runner.py create-mvp {project_name}")
                sys.exit(1)
            
            print(f"➕ Adding feature '{feature_name}' to project '{project_name}'")
            
            # Create execution context for feature addition
            context = ExecutionContext(
                feature_name=feature_name,
                mode=AutomationMode(args.mode),
                project_root=project_root,
                context_mode="FEATURE_ADDITION",
                existing_project=project_name
            )
        
        # Assess risk
        context.risk_score = orchestrator.assess_risk_score(context)
        
        # Execute workflow
        if args.dry_run:
            print(f"\n🧪 DRY RUN - Execution Plan:")
            if args.command == "create-mvp":
                print(f"   📁 Target: Create new MVP project '{project_name}' in ~/Projects/")
            else:
                print(f"   📁 Target: Add feature '{args.feature_name}' to '{args.project_name}'")
            
            success = orchestrator.execute_workflow(context, dry_run=True)
        else:
            success = orchestrator.execute_workflow(context, dry_run=False)
            
            if success:
                if args.command == "create-mvp":
                    # Update project status
                    try:
                        import json
                        manifest_path = project_root / "project-manifest.json"
                        with open(manifest_path, 'r') as f:
                            manifest = json.load(f)
                        manifest["status"] = "initialized"
                        manifest["mvp_context"]["automation_mode"] = args.mode
                        with open(manifest_path, 'w') as f:
                            json.dump(manifest, f, indent=2)
                    except Exception as e:
                        print(f"⚠️  Could not update project status: {e}")
                    
                    print(f"\n🎉 MVP project '{project_name}' created successfully!")
                    print(f"📁 Project location: {project_root}")
                    print(f"\n🚀 Next steps:")
                    print(f"   • Review AI-generated documentation in features/ directory")
                    print(f"   • Add features: ./workflow-runner.py add-feature FEATURE_NAME --to {project_name}")
                    print(f"   • Start development in src/ directory")
                else:
                    print(f"\n🎉 Feature '{args.feature_name}' added successfully to '{args.project_name}'!")
                    print(f"📁 Project location: {project_root}")
            else:
                print(f"\n❌ Workflow failed")
        
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
