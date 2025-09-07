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
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
import subprocess

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

def create_project_manifest(project_dir: Path, project_name: str, args: argparse.Namespace) -> None:
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
                       required=True,
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
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.verbose)
    
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
                    response = input(f"📁 Where do you want to create this project? [{default_base}]: ").strip()
                    if response:
                        response_path = Path(response).expanduser()
                        # If it's not absolute, treat it as relative to the default base directory
                        if not response_path.is_absolute():
                            base_dir = (default_base / response).resolve()
                        else:
                            base_dir = response_path.resolve()
                    else:
                        base_dir = default_base
                except KeyboardInterrupt:
                    logger.info("❌ Operation cancelled by user")
                    return
            else:
                base_dir = default_base
        
        # Handle dry-run mode
        if args.dry_run:
            project_dir = base_dir / project_name
            logger.info(f"🧪 [DRY RUN] Would create project directory: {project_dir}")
            logger.info("🧪 [DRY RUN] Would create project structure (features/, docs/, artifacts/)")
            logger.info("🧪 [DRY RUN] Would run complete MVP workflow")
            return
        
        # Create project directory (only in non-dry-run mode)
        project_dir = create_project_directory(project_name, base_dir)
        
        logger.info(f"📁 Created project directory: {project_dir}")
        
        # Create project manifest
        create_project_manifest(project_dir, project_name, args)
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
