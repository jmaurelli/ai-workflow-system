#!/usr/bin/env python3

"""
🚀 MVP Initializer - New MVP Project Creation
Creates new MVP projects in organized /projects/ directory structure
"""

import argparse
import json
import os
import sys
import logging
import getpass
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List
import subprocess

# Import LLM integration for AI-powered dynamic questioning  
try:
    import importlib.util
    import requests
    spec = importlib.util.spec_from_file_location("llm_api_integration", 
                                                  Path(__file__).parent / "llm-api-integration.py")
    llm_api_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(llm_api_module)
    
    LLMAPIIntegration = llm_api_module.LLMAPIIntegration
    LLMConfig = llm_api_module.LLMConfig
    LLMRequest = llm_api_module.LLMRequest
    LLMProvider = llm_api_module.LLMProvider
    LLM_AVAILABLE = True
except Exception:
    # Fallback: basic AI integration available if we have requests
    try:
        import requests
        LLM_AVAILABLE = "basic"
    except ImportError:
        LLM_AVAILABLE = False

def prompt_ai_vendor_setup() -> tuple:
    """Interactive prompt for AI vendor and API key"""
    print("\n🤖 AI CONSULTANT SETUP")
    print("=" * 40)
    
    # Always show all big 3 providers
    vendors = {
        "1": {"name": "OpenAI", "provider": "openai", "model": "gpt-3.5-turbo", "env_var": "OPENAI_API_KEY"},
        "2": {"name": "Claude (Anthropic)", "provider": "anthropic", "model": "claude-3-5-sonnet-20241022", "env_var": "ANTHROPIC_API_KEY"},
        "3": {"name": "Google Gemini", "provider": "google", "model": "gemini-1.5-flash", "env_var": "GOOGLE_API_KEY"},
        "4": {"name": "Skip AI questions", "provider": None}
    }
    
    # Show integration status
    if LLM_AVAILABLE == True:
        print("✨ Full AI integration available - all providers with advanced features!")
    else:
        print("⚡ Basic integration - all providers supported with core features!")
    
    print("\nChoose your AI assistant:")
    for key, vendor in vendors.items():
        if vendor["provider"]:
            print(f"   {key}. {vendor['name']} ({vendor['model']})")
        else:
            print(f"   {key}. {vendor['name']}")
    print()
    
    while True:
        try:
            max_choice = len(vendors)
            choice = input(f"Select AI vendor (1-{max_choice}): ").strip()
            if choice in vendors:
                selected = vendors[choice]
                if not selected["provider"]:
                    return "skip", None  # User chose to skip AI questions
                
                # Check if API key is already in environment
                existing_key = os.getenv(selected["env_var"])
                if existing_key:
                    print(f"✅ Found existing {selected['name']} API key")
                    return selected, existing_key
                
                # Prompt for API key
                print(f"\n🔑 {selected['name']} API Key")
                if selected['provider'] == 'openai':
                    print("💡 Get your key from: https://platform.openai.com/api-keys")
                elif selected['provider'] == 'anthropic':
                    print("💡 Get your key from: https://console.anthropic.com/settings/keys")
                elif selected['provider'] == 'google':
                    print("💡 Get your key from: https://aistudio.google.com/app/apikey")
                print("🔒 Your API key will be hidden for security")
                
                try:
                    api_key = getpass.getpass(f"Enter your {selected['name']} API key: ").strip()
                except (KeyboardInterrupt, EOFError):
                    print("\n❌ API key input cancelled")
                    continue
                    
                if not api_key:
                    print("❌ API key required for AI questions")
                    continue
                    
                return selected, api_key
            else:
                print(f"❌ Please enter a number from 1 to {max_choice}")
                
        except KeyboardInterrupt:
            print("\n❌ AI setup cancelled")
            return "cancelled", None

def _call_openai_api(api_key: str, messages: List[Dict], model: str = "gpt-3.5-turbo") -> str:
    """Simple OpenAI API call using requests"""
    import requests
    
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": messages,
            "max_tokens": 300,
            "temperature": 0.7
        },
        timeout=30
    )
    
    if response.status_code != 200:
        raise Exception(f"OpenAI API call failed: {response.status_code}")
    
    return response.json()["choices"][0]["message"]["content"]

def _call_anthropic_api(api_key: str, messages: List[Dict], model: str = "claude-3-5-sonnet-20241022") -> str:
    """Simple Anthropic API call using requests"""
    import requests
    
    # Convert messages format for Claude
    system_msg = next((msg["content"] for msg in messages if msg["role"] == "system"), "")
    user_msg = next((msg["content"] for msg in messages if msg["role"] == "user"), "")
    
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        },
        json={
            "model": model,
            "max_tokens": 300,
            "system": system_msg,
            "messages": [{"role": "user", "content": user_msg}]
        },
        timeout=30
    )
    
    if response.status_code != 200:
        raise Exception(f"Claude API call failed: {response.status_code}")
    
    return response.json()["content"][0]["text"]

def _call_google_api(api_key: str, messages: List[Dict], model: str = "gemini-1.5-flash") -> str:
    """Simple Google Gemini API call using requests"""
    import requests
    
    # Combine system and user messages for Gemini
    combined_prompt = ""
    for msg in messages:
        if msg["role"] == "system":
            combined_prompt += f"Instructions: {msg['content']}\n\n"
        elif msg["role"] == "user":
            combined_prompt += msg["content"]
    
    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}",
        headers={
            "Content-Type": "application/json"
        },
        json={
            "contents": [{
                "parts": [{"text": combined_prompt}]
            }],
            "generationConfig": {
                "maxOutputTokens": 300,
                "temperature": 0.7
            }
        },
        timeout=30
    )
    
    if response.status_code != 200:
        raise Exception(f"Gemini API call failed: {response.status_code}")
    
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

def generate_dynamic_questions(project_goal: str, vendor_config: Dict, api_key: str, previous_answers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """Generate personalized follow-up questions using AI"""
    if not LLM_AVAILABLE or not vendor_config or not api_key:
        return []
    
    try:
        if LLM_AVAILABLE == True:
            # Use full LLM integration
            config = LLMConfig(
                provider=LLMProvider(vendor_config["provider"]),
                model=vendor_config["model"],
                api_key=api_key,
                max_tokens=300,
                temperature=0.7,
                timeout=30,
                max_retries=2,
                cost_limit_usd=0.15
            )
            llm = LLMAPIIntegration(config, debug=False)
        else:
            # Use basic API calls with requests
            pass  # All providers now supported in basic mode
        
        # Create dynamic prompt
        previous_context = ""
        if previous_answers:
            previous_context = f"Previous answers: {json.dumps(previous_answers, indent=2)}"
        
        prompt_text = f"""You are an expert project consultant helping someone plan their MVP. 

Their project goal: "{project_goal}"
{previous_context}

Generate 2-4 specific, insightful follow-up questions that would help you understand their needs better. Focus on:
- WHO will use this (target users)
- WHAT specific features they need most  
- HOW they'll measure success
- WHERE/HOW they want to deploy it

Make questions conversational and include helpful suggestions when possible.

Return ONLY a JSON array, no other text:
[
  {{"prompt": "👤 Who is your main target user?", "example": "Small business owners, students, developers, etc."}},
  {{"prompt": "🎯 What's the #1 thing users should accomplish?", "options": ["Save time on X", "Solve problem Y", "Learn about Z"], "help": "This helps prioritize features"}},
  {{"prompt": "📱 How will people access this?", "options": ["Web browser", "Mobile app", "Desktop app", "Command line"], "default": "Web browser"}}
]"""

        # Generate response based on available integration
        if LLM_AVAILABLE == True:
            # Use full LLM integration
            request = LLMRequest(
                prompt=prompt_text,
                system_message="You are a helpful project consultant who asks great questions."
            )
            response = llm.generate_content(request)
            content = response.content.strip()
        else:
            # Use basic API calls with requests
            messages = [
                {"role": "system", "content": "You are a helpful project consultant who asks great questions."},
                {"role": "user", "content": prompt_text}
            ]
            
            provider = vendor_config["provider"]
            if provider == "openai":
                content = _call_openai_api(api_key, messages, vendor_config["model"])
            elif provider == "anthropic":
                content = _call_anthropic_api(api_key, messages, vendor_config["model"])
            elif provider == "google":
                content = _call_google_api(api_key, messages, vendor_config["model"])
            else:
                raise Exception(f"Unsupported provider: {provider}")
        
        # Parse JSON response
        try:
            questions = json.loads(content)
            return questions if isinstance(questions, list) else []
        except json.JSONDecodeError:
            return []
            
    except Exception as e:
        print(f"💭 AI question generation not available: {e}")
        return []

def _ask_dynamic_question(key: str, question_config: Dict[str, Any], answers: Dict[str, str]) -> bool:
    """Ask a single AI-generated dynamic question"""
    try:
        # Show help text if available
        if "help" in question_config:
            print(f"💡 {question_config['help']}")
        elif "example" in question_config:
            print(f"💡 Example: {question_config['example']}")
        
        # Show options if available
        if "options" in question_config:
            print("Options:")
            for i, option in enumerate(question_config["options"], 1):
                print(f"   {i}. {option}")
            print()
        
        # Get user response
        response = input(f"{question_config['prompt']} ").strip()
        
        # Handle options selection
        if "options" in question_config and response.isdigit():
            option_index = int(response) - 1
            if 0 <= option_index < len(question_config["options"]):
                response = question_config["options"][option_index]
        
        answers[key] = response
        print()
        return True
        
    except KeyboardInterrupt:
        print("\n❌ Setup cancelled by user")
        return False

def prompt_project_questions(non_interactive: bool = False, enable_ai: bool = True) -> Dict[str, str]:
    """Prompt user for project initialization questions with AI-powered dynamic follow-ups"""
    if non_interactive or not sys.stdin.isatty():
        return {}
    
    print("\n🎯 PROJECT SETUP WITH AI CONSULTANT")
    print("=" * 50)
    
    answers = {}
    
    # Start with the core question
    try:
        print("💡 Example: Create a web tool that helps engineers analyze log files and find issues faster")
        project_goal = input("🎯 What does this project do? (one sentence): ").strip()
        if not project_goal:
            print("❌ Project description is required")
            return None
        answers["project_goal"] = project_goal
        print()
    except KeyboardInterrupt:
        print("\n❌ Setup cancelled by user")
        return None
    
    # Try to get AI-powered dynamic questions
    if enable_ai and LLM_AVAILABLE:
        # Prompt for AI vendor setup
        vendor_config, api_key = prompt_ai_vendor_setup()
        
        # Check if user cancelled during AI setup
        if vendor_config == "cancelled":
            # User pressed Ctrl+C during AI setup - respect that and exit completely
            print("💭 AI setup cancelled - exiting")
            return None
        elif vendor_config == "skip":
            # User chose to skip AI questions - proceed to static questions
            print("💭 Skipping AI questions, using standard questions...")
        elif vendor_config and api_key:
            print(f"\n🤖 {vendor_config['name']} will help create personalized questions...")
            try:
                ai_questions = generate_dynamic_questions(project_goal, vendor_config, api_key, answers)
                if ai_questions:
                    print("✨ Here are some AI-generated questions tailored for your project:")
                    print()
                    
                    # Ask AI-generated questions
                    for i, question_config in enumerate(ai_questions, 1):
                        if not _ask_dynamic_question(f"ai_question_{i}", question_config, answers):
                            return None
                        
                    print(f"🎉 Great! {vendor_config['name']} helped gather the perfect project context.")
                    return answers
                    
            except Exception as e:
                print(f"💭 {vendor_config['name']} consultant unavailable ({e}), using standard questions...")
    
    # Fallback to static questions
    static_questions = {
        "what_to_build": {
            "prompt": "🔨 What are the main things users will be able to do? (2-3 key features)",
            "example": "Upload log files, search for errors, generate summary reports",
            "required": True
        },
        "where_to_run": {
            "prompt": "🌐 Where will this run?",
            "options": ["local", "cloud", "container", "serverless"],
            "option_help": {
                "local": "On my computer only",
                "cloud": "Online for others to use", 
                "container": "In Docker/containers",
                "serverless": "Cloud functions (AWS Lambda, etc.)"
            },
            "default": "local",
            "required": False
        },
        "user_success": {
            "prompt": "👤 How will users know this is working well for them?",
            "example": "Tasks complete quickly, easy to find what they need, saves them time",
            "required": True
        }
    }
    
    print("\n📝 A few more questions to understand your needs:")
    
    for key, config in static_questions.items():
        while True:
            try:
                # Build prompt text
                prompt_text = config["prompt"]
                if "default" in config:
                    prompt_text += f" [{config['default']}]"
                    
                # Show example for required fields or help text  
                if "example" in config and config.get("required", False):
                    print(f"💡 Example: {config['example']}")
                elif "help" in config:
                    print(f"💡 {config['help']}")
                
                # Show options with help text (only once)
                if "options" in config and "option_help" in config:
                    print("Options:")
                    for option in config["options"]:
                        help_text = config["option_help"].get(option, "")
                        print(f"   {option} - {help_text}")
                
                response = input(f"{prompt_text}: ").strip()
                
                # Handle defaults
                if not response and "default" in config:
                    response = config["default"]
                
                # Handle required fields
                if config.get("required", False) and not response:
                    print("❌ This field is required. Please provide an answer.")
                    continue
                
                # Handle boolean type
                if config.get("type") == "boolean":
                    response = response.lower() in ['y', 'yes', 'true', '1']
                
                # Handle options validation
                if "options" in config and response and response not in config["options"]:
                    print(f"❌ Please enter one of: {', '.join(config['options'])}")
                    continue
                
                answers[key] = response if response else ""
                print()
                break
                
            except KeyboardInterrupt:
                print("\n❌ Setup cancelled by user")
                return None
    
    print("✅ Project initialization complete!")
    print()
    return answers

def view_project_report(project_name: str, base_dir: Path = None) -> None:
    """View executive report for an existing project"""
    if not base_dir:
        base_dir = Path.home() / "Projects"
    
    project_dir = base_dir / project_name
    if not project_dir.exists():
        print(f"❌ Project '{project_name}' not found in {base_dir}/")
        print("💡 Use --project-dir to specify a different location")
        return
    
    manifest_path = project_dir / "project-manifest.json"
    if not manifest_path.exists():
        print(f"❌ No project manifest found for '{project_name}'")
        return
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        print(f"\n📊 PROJECT REPORT: {project_name}")
        print("=" * 60)
        
        # Basic project info
        print(f"📁 Location: {project_dir}")
        print(f"📅 Created: {manifest.get('created_at', 'Unknown')}")
        print(f"🏷️  Type: {manifest.get('project_type', 'Unknown')}")
        print(f"📊 Status: {manifest.get('status', 'Unknown')}")
        print(f"🤖 Mode: {manifest.get('mvp_context', {}).get('automation_mode', 'Unknown')}")
        
        # Project initialization context
        if "project_initialization" in manifest:
            init_data = manifest["project_initialization"]
            print(f"\n🎯 PROJECT CONTEXT ({init_data['questions_answered']} questions answered):")
            print("-" * 40)
            context = init_data.get("project_context", {})
            
            for key, value in context.items():
                if value:  # Only show non-empty answers
                    label = key.replace("_", " ").title()
                    print(f"• {label}: {value}")
        
        # Features summary
        features = manifest.get("features", [])
        print(f"\n🔧 FEATURES ({len(features)} total):")
        print("-" * 40)
        if features:
            for feature in features:
                print(f"• {feature}")
        else:
            print("• No additional features yet")
        
        # Feature directory contents
        features_dir = project_dir / "features"
        if features_dir.exists():
            feature_dirs = [d for d in features_dir.iterdir() if d.is_dir()]
            if feature_dirs:
                print(f"\n📄 GENERATED DOCUMENTATION:")
                print("-" * 40)
                for feature_dir in feature_dirs:
                    print(f"📁 {feature_dir.name}/")
                    
                    # Show key files
                    output_files = list(feature_dir.glob("*-output.md"))
                    if output_files:
                        print(f"   📋 {len(output_files)} workflow documents generated")
                    
                    manifest_file = feature_dir / "feature-manifest.json"
                    if manifest_file.exists():
                        try:
                            with open(manifest_file, 'r') as f:
                                feature_manifest = json.load(f)
                            status = feature_manifest.get('status', 'unknown')
                            print(f"   📊 Status: {status}")
                        except:
                            print(f"   📊 Status: manifest found")
        
        print(f"\n🚀 NEXT STEPS:")
        print("-" * 40)
        print(f"• Review documentation: {project_dir}/features/")
        print(f"• Add features: ./workflow-runner.py --feature=FEATURE_NAME --existing-project={project_name}")
        print(f"• View files: ls -la {project_dir}/")
        print()
        
    except Exception as e:
        print(f"❌ Error reading project report: {e}")

def setup_logging(verbose: bool = False) -> logging.Logger:
    """Setup logging configuration"""
    logger = logging.getLogger('mvp_initializer')
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)
    
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger

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

def create_project_directory(project_name: str, base_dir: Path) -> Path:
    """Create project directory structure"""
    project_dir = base_dir / project_name
    
    if project_dir.exists():
        raise FileExistsError(f"Project '{project_name}' already exists at {project_dir}")
    
    # Create base directory if it doesn't exist
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # Create project directory structure
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # Create subdirectories for organization
    (project_dir / "features").mkdir(exist_ok=True)
    (project_dir / "docs").mkdir(exist_ok=True)
    (project_dir / "artifacts").mkdir(exist_ok=True)
    
    return project_dir

def create_project_manifest(project_dir: Path, project_name: str, args: argparse.Namespace, project_context: Dict[str, str] = None) -> None:
    """Create project manifest file"""
    manifest = {
        "project_name": project_name,
        "created_at": datetime.now().isoformat(),
        "project_type": "MVP",
        "status": "initializing",
        "workflow_version": "2.0",
        "features": [],
        "mvp_context": {
            "initialization_mode": "mvp-initializer",
            "llm_api_enabled": getattr(args, 'llm_api', False),
            "llm_provider": getattr(args, 'llm_provider', None),
            "automation_mode": args.mode
        },
        "directory_structure": {
            "features": "Feature-specific development artifacts",
            "docs": "Project documentation and specifications", 
            "artifacts": "Generated content and assets"
        }
    }
    
    # Add project initialization questions if provided
    if project_context:
        manifest["project_initialization"] = {
            "questions_answered": len(project_context),
            "project_context": project_context,
            "context_timestamp": datetime.now().isoformat()
        }
    
    manifest_path = project_dir / "project-manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

def run_workflow_for_mvp(project_dir: Path, project_name: str, args: argparse.Namespace, logger: logging.Logger) -> bool:
    """Run the complete workflow for MVP initialization"""
    
    logger.info(f"🚀 Running MVP workflow for project: {project_name}")
    
    # Prepare workflow runner command
    workflow_runner_path = Path(__file__).parent / "workflow-runner.py"
    
    cmd = [
        "python3",
        str(workflow_runner_path),
        "--feature", f"{project_name}-mvp-initialization",
        "--mode", args.mode
    ]
    
    # Add LLM API configuration if enabled
    if args.llm_api:
        cmd.append("--llm-api")
        
        if args.llm_provider:
            cmd.extend(["--llm-provider", args.llm_provider])
        
        if args.llm_model:
            cmd.extend(["--llm-model", args.llm_model])
        
        if args.llm_config:
            cmd.extend(["--llm-config", str(args.llm_config)])
        
        if args.cost_limit:
            cmd.extend(["--cost-limit", str(args.cost_limit)])
    
    if args.verbose:
        cmd.append("--verbose")
    
    if args.dry_run:
        cmd.append("--dry-run")
        logger.info(f"🧪 [DRY RUN] Would execute: {' '.join(cmd)}")
        return True
    
    try:
        # Change to project directory before running workflow
        original_cwd = Path.cwd()
        os.chdir(project_dir)
        
        logger.info(f"📁 Changed to project directory: {project_dir}")
        logger.info(f"🤖 Executing workflow command: {' '.join(cmd)}")
        
        # Execute workflow (allow interactive prompts by not capturing output)
        result = subprocess.run(cmd, text=True, timeout=600)
        
        # Change back to original directory
        os.chdir(original_cwd)
        
        if result.returncode == 0:
            logger.info("✅ MVP workflow completed successfully")
            return True
        else:
            logger.error(f"❌ MVP workflow failed with return code: {result.returncode}")
            logger.error("Check workflow output above for details")
            return False
            
    except subprocess.TimeoutExpired:
        logger.error("❌ MVP workflow timed out")
        return False
    except Exception as e:
        logger.error(f"❌ Error executing MVP workflow: {e}")
        return False
    finally:
        # Ensure we're back in original directory
        os.chdir(original_cwd)

def update_project_status(project_dir: Path, status: str, logger: logging.Logger) -> None:
    """Update project status in manifest"""
    manifest_path = project_dir / "project-manifest.json"
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        manifest["status"] = status
        manifest["updated_at"] = datetime.now().isoformat()
        
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
            
        logger.info(f"📊 Updated project status to: {status}")
        
    except Exception as e:
        logger.warning(f"⚠️ Could not update project status: {e}")

def main():
    """Main entry point for MVP initializer"""
    parser = argparse.ArgumentParser(
        description="🚀 MVP Initializer - Create new MVP projects with automated workflow"
    )
    
    parser.add_argument("--project",
                       help="Project name for new MVP")
    
    parser.add_argument("--project-dir", 
                       help="Base directory where project should be created (default: ~/Projects, interactive prompt in all modes)")
    parser.add_argument("--non-interactive", action="store_true",
                       help="Disable interactive prompts (useful for automated testing)")
    
    parser.add_argument("--mode",
                       choices=["guided", "autonomous", "learning"],
                       default="guided",
                       help="Automation mode for workflow execution")
    
    parser.add_argument("--dry-run",
                       action="store_true",
                       help="Show what would be created without actually creating")
    
    parser.add_argument("--verbose",
                       action="store_true",
                       help="Enable verbose logging")
    
    # LLM API integration arguments
    parser.add_argument("--llm-api",
                       action="store_true",
                       help="Enable real LLM API content generation")
    
    parser.add_argument("--llm-provider",
                       help="LLM provider (openai, anthropic, google, local_ollama, groq)")
    
    parser.add_argument("--llm-model",
                       help="LLM model to use")
    
    parser.add_argument("--llm-config",
                       type=Path,
                       help="Path to LLM configuration file")
    
    parser.add_argument("--cost-limit",
                       type=float,
                       help="Override cost limit for LLM usage")
    
    parser.add_argument("--view-report",
                       metavar="PROJECT_NAME",
                       help="View executive report for existing project")
    
    parser.add_argument("--disable-ai-questions", action="store_true",
                       help="Disable AI-powered dynamic questioning (use static questions only)")
    
    parser.add_argument("--enable-ai-questions", action="store_true", 
                       help="[DEPRECATED] AI questions are now enabled by default in guided mode")
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.verbose)
    
    # Handle view-report mode
    if args.view_report:
        base_dir = None
        if args.project_dir:
            base_dir = Path(args.project_dir).expanduser().resolve()
        view_project_report(args.view_report, base_dir)
        return
    
    # Handle project name - prompt if not provided and in interactive mode
    if not args.project and not args.view_report:
        if not args.non_interactive and sys.stdin.isatty():
            print("\n🚀 NEW PROJECT SETUP")
            print("=" * 40)
            try:
                project_input = input("📝 What do you want to name this project? ").strip()
                if not project_input:
                    print("❌ Project name is required")
                    return
                args.project = project_input
            except KeyboardInterrupt:
                print("\n❌ Project setup cancelled")
                return
        else:
            parser.error("--project is required when not using --view-report or in non-interactive mode")
    
    try:
        # Validate and normalize project name
        project_name = validate_project_name(args.project)
        
        if project_name != args.project:
            logger.info(f"📝 Normalized project name: '{args.project}' → '{project_name}'")
        
        logger.info(f"🚀 Initializing new MVP project: {project_name}")
        
        # Determine project base directory
        if args.project_dir:
            base_dir = Path(args.project_dir).expanduser().resolve()
        else:
            # Default to ~/Projects for better organization
            default_base = Path.home() / "Projects"
            
            # Prompt for project directory (unless non-interactive or not a tty)
            if not args.non_interactive and sys.stdin.isatty():
                try:
                    print(f"\n📁 PROJECT LOCATION")
                    print(f"Creating project: {project_name}")
                    print(f"Default location: {default_base}/{project_name}/")
                    print()
                    print("💡 Press Enter for default, or specify a different parent directory")
                    response = input(f"📂 Parent directory [{default_base}]: ").strip()
                    if response:
                        response_path = Path(response).expanduser()
                        # If it's not absolute, treat it as relative to the default base directory
                        if not response_path.is_absolute():
                            base_dir = (default_base / response).resolve()
                        else:
                            base_dir = response_path.resolve()
                    else:
                        base_dir = default_base
                        
                    print(f"✅ Project will be created at: {base_dir}/{project_name}/")
                    print()
                except KeyboardInterrupt:
                    logger.info("❌ Operation cancelled by user")
                    return
            else:
                base_dir = default_base
        
        # Determine AI questions setting - default True for guided mode unless disabled
        enable_ai = not args.disable_ai_questions and args.mode == "guided"
        
        # Prompt for project questions (interactive only)
        project_context = prompt_project_questions(args.non_interactive, enable_ai)
        
        # If user cancelled during questions, exit completely
        if project_context is None:
            logger.info("❌ Project initialization cancelled by user")
            return
        
        # Handle dry-run mode
        if args.dry_run:
            project_dir = base_dir / project_name
            logger.info(f"🧪 [DRY RUN] Would create project directory: {project_dir}")
            logger.info("🧪 [DRY RUN] Would create project structure (features/, docs/, artifacts/)")
            if project_context:
                logger.info(f"🧪 [DRY RUN] Would store project context: {len(project_context)} answers provided")
            logger.info("🧪 [DRY RUN] Would run complete MVP workflow")
            return
        
        # Create project directory (only in non-dry-run mode)
        project_dir = create_project_directory(project_name, base_dir)
        
        logger.info(f"📁 Created project directory: {project_dir}")
        
        # Create project manifest
        create_project_manifest(project_dir, project_name, args, project_context)
        if project_context:
            logger.info(f"📊 Created project manifest with {len(project_context)} initialization answers")
        else:
            logger.info("📊 Created project manifest")
        
        # Run MVP workflow
        success = run_workflow_for_mvp(project_dir, project_name, args, logger)
        
        if success:
            update_project_status(project_dir, "initialized", logger)
            
            print(f"\n🎉 SUCCESS! MVP project '{project_name}' created successfully!")
            print(f"📁 Project location: {project_dir}")
            print(f"📊 Project manifest: {project_dir}/project-manifest.json")
            print(f"\n🚀 Next steps:")
            print(f"   1. Review generated MVP documentation in {project_dir}/")
            print(f"   2. Add features with: workflow-runner.py --feature=FEATURE_NAME --existing-project={project_name} --llm-api")
            print(f"   3. Start development based on generated tasks!")
            
        else:
            update_project_status(project_dir, "failed", logger)
            print(f"\n❌ MVP initialization failed. Check logs for details.")
            sys.exit(1)
            
    except FileExistsError as e:
        logger.error(f"❌ {e}")
        print(f"\n💡 Tip: Use workflow-runner.py --existing-project={project_name} to add features to existing projects")
        sys.exit(1)
    except ValueError as e:
        logger.error(f"❌ Invalid project name: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    import os
    main()

