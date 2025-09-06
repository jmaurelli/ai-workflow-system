#!/usr/bin/env python3

"""
🤖 AI Agent Integration for Workflow Execution
Provides seamless integration between workflow orchestrators and AI agents
"""

import json
import os
import sys
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
import subprocess

class AIAgentIntegration:
    """Handles AI agent integration for workflow execution"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('ai_agent_integration')
        level = logging.DEBUG if self.debug else logging.INFO
        logger.setLevel(level)
        
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        return logger
    
    def process_workflow_outputs(self, feature_dir: Path) -> bool:
        """Process and validate workflow outputs in feature directory"""
        
        self.logger.info(f"🔍 Processing workflow outputs in: {feature_dir}")
        
        if not feature_dir.exists():
            self.logger.error(f"Feature directory not found: {feature_dir}")
            return False
        
        # Find AI execution status files
        status_files = list(feature_dir.glob("*-output.md"))
        
        if not status_files:
            self.logger.warning("No AI execution status files found")
            return True
        
        for status_file in status_files:
            self._process_ai_status_file(status_file)
        
        return True
    
    def _process_ai_status_file(self, status_file: Path):
        """Process individual AI status file"""
        
        self.logger.info(f"📄 Processing: {status_file.name}")
        
        try:
            with open(status_file, 'r') as f:
                content = f.read()
            
            # Extract JSON data from markdown
            import re
            json_match = re.search(r'```json\s*\n(.*?)\n```', content, re.DOTALL)
            
            if json_match:
                execution_data = json.loads(json_match.group(1))
                
                # Display status information
                self._display_execution_status(execution_data)
                
                # Check if AI agent assistance is needed
                if execution_data.get("execution_status") == "ready_for_ai_agent":
                    self._provide_ai_guidance(execution_data, status_file)
            
        except Exception as e:
            self.logger.error(f"Error processing {status_file}: {e}")
    
    def _display_execution_status(self, execution_data: Dict[str, Any]):
        """Display execution status information"""
        
        workflow_step = execution_data.get("workflow_step", {})
        completion_status = execution_data.get("completion_status", {})
        
        print(f"\n🔄 WORKFLOW STEP STATUS")
        print(f"Document: {workflow_step.get('document', 'Unknown')}")
        print(f"Step: {workflow_step.get('step_number', 'Unknown')}")
        print(f"Phase: {workflow_step.get('phase', 'Unknown')}")
        print(f"Timestamp: {workflow_step.get('timestamp', 'Unknown')}")
        
        print(f"\n📊 COMPLETION STATUS")
        print(f"Started: {'✅' if completion_status.get('started') else '❌'}")
        print(f"Completed: {'✅' if completion_status.get('completed') else '❌'}")
        print(f"Validated: {'✅' if completion_status.get('validated') else '❌'}")
        
        errors = completion_status.get('errors', [])
        if errors:
            print(f"\n❌ ERRORS:")
            for error in errors:
                print(f"  - {error}")
    
    def _provide_ai_guidance(self, execution_data: Dict[str, Any], status_file: Path):
        """Provide guidance for AI agent execution"""
        
        print(f"\n🤖 AI AGENT GUIDANCE")
        print(f"{'='*50}")
        
        document = execution_data.get("workflow_step", {}).get("document", "Unknown")
        feature_dir = execution_data.get("feature_directory", "")
        
        print(f"📋 Next Steps for AI Agent:")
        print(f"1. Read workflow document: {document}")
        print(f"2. Review feature directory: {feature_dir}")
        print(f"3. Execute workflow instructions")
        print(f"4. Generate expected outputs:")
        
        for output in execution_data.get("expected_outputs", []):
            print(f"   - {output}")
        
        print(f"\n✅ Validation Criteria:")
        for criteria in execution_data.get("validation_criteria", []):
            print(f"   - {criteria}")
        
        print(f"\n📝 Update Status When Complete:")
        print(f"   Edit: {status_file}")
        print(f"   Set: completion_status.completed = true")
        
        # Create helper script for AI agent
        self._create_ai_helper_script(execution_data, status_file)
    
    def _create_ai_helper_script(self, execution_data: Dict[str, Any], status_file: Path):
        """Create helper script for AI agent execution"""
        
        feature_dir = Path(execution_data.get("feature_directory", ""))
        if not feature_dir.exists():
            return
        
        helper_script = feature_dir / "ai-helper.sh"
        
        workflow_step = execution_data.get("workflow_step", {})
        document = workflow_step.get("document", "")
        
        script_content = f"""#!/bin/bash

# 🤖 AI Agent Helper Script
# Generated for workflow step: {document}

echo "🤖 AI Agent Helper for {document}"
echo "{'='*50}"

echo "📂 Feature Directory: {feature_dir}"
echo "📄 Workflow Document: {document}"
echo "📋 Status File: {status_file}"

echo ""
echo "🎯 Expected Outputs:"
"""
        
        for output in execution_data.get("expected_outputs", []):
            script_content += f'echo "   - {output}"\n'
        
        script_content += f"""
echo ""
echo "✅ When complete, update status:"
echo "   Edit {status_file}"
echo "   Set completion_status.completed = true"

echo ""
echo "📚 Available Commands:"
echo "   cd {feature_dir}        # Navigate to feature directory"
echo "   ls -la                  # List generated files"
echo "   cat feature-manifest.json  # View feature manifest"

echo ""
echo "🚀 Ready for AI agent execution!"
"""
        
        try:
            with open(helper_script, 'w') as f:
                f.write(script_content)
            
            helper_script.chmod(0o755)
            self.logger.info(f"📝 Created AI helper script: {helper_script}")
            
        except Exception as e:
            self.logger.error(f"Failed to create helper script: {e}")
    
    def mark_step_completed(self, status_file: Path, success: bool = True, errors: List[str] = None) -> bool:
        """Mark a workflow step as completed"""
        
        if not status_file.exists():
            self.logger.error(f"Status file not found: {status_file}")
            return False
        
        try:
            with open(status_file, 'r') as f:
                content = f.read()
            
            # Extract and update JSON data
            import re
            json_match = re.search(r'```json\s*\n(.*?)\n```', content, re.DOTALL)
            
            if json_match:
                execution_data = json.loads(json_match.group(1))
                
                # Update completion status
                execution_data["completion_status"]["started"] = True
                execution_data["completion_status"]["completed"] = success
                execution_data["completion_status"]["validated"] = success
                execution_data["completion_status"]["completion_timestamp"] = datetime.now().isoformat()
                
                if errors:
                    execution_data["completion_status"]["errors"] = errors
                
                # Update content
                updated_json = json.dumps(execution_data, indent=2)
                updated_content = re.sub(
                    r'```json\s*\n.*?\n```',
                    f'```json\n{updated_json}\n```',
                    content,
                    flags=re.DOTALL
                )
                
                with open(status_file, 'w') as f:
                    f.write(updated_content)
                
                self.logger.info(f"✅ Updated completion status: {status_file}")
                return True
            
        except Exception as e:
            self.logger.error(f"Failed to update status file: {e}")
            return False
        
        return False
    
    def validate_feature_outputs(self, feature_dir: Path) -> Dict[str, Any]:
        """Validate all outputs in a feature directory"""
        
        validation_results = {
            "feature_directory": str(feature_dir),
            "validation_timestamp": datetime.now().isoformat(),
            "files_found": [],
            "missing_files": [],
            "validation_passed": True,
            "errors": []
        }
        
        if not feature_dir.exists():
            validation_results["validation_passed"] = False
            validation_results["errors"].append(f"Feature directory not found: {feature_dir}")
            return validation_results
        
        # Check for manifest file
        manifest_file = feature_dir / "feature-manifest.json"
        if manifest_file.exists():
            validation_results["files_found"].append(str(manifest_file))
        else:
            validation_results["missing_files"].append(str(manifest_file))
            validation_results["validation_passed"] = False
        
        # Check for common output files
        expected_files = [
            "prd.md", "srs.md", "design-decisions.md", 
            "design-analysis.md", "tasks.md", "completion-summary.md"
        ]
        
        for expected_file in expected_files:
            file_path = feature_dir / expected_file
            if file_path.exists():
                validation_results["files_found"].append(str(file_path))
            else:
                validation_results["missing_files"].append(str(file_path))
        
        # Check artifacts directory
        artifacts_dir = feature_dir / "artifacts"
        if artifacts_dir.exists():
            validation_results["files_found"].append(str(artifacts_dir))
        
        self.logger.info(f"🔍 Validation complete for: {feature_dir}")
        self.logger.info(f"Files found: {len(validation_results['files_found'])}")
        self.logger.info(f"Missing files: {len(validation_results['missing_files'])}")
        
        return validation_results

def main():
    """Main entry point for AI agent integration"""
    parser = argparse.ArgumentParser(
        description="🤖 AI Agent Integration for Workflow Execution"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Process outputs command
    process_parser = subparsers.add_parser('process', help='Process workflow outputs')
    process_parser.add_argument('feature_dir', type=Path, help='Feature directory to process')
    
    # Mark completed command
    complete_parser = subparsers.add_parser('complete', help='Mark workflow step as completed')
    complete_parser.add_argument('status_file', type=Path, help='Status file to update')
    complete_parser.add_argument('--success', action='store_true', default=True, help='Mark as successful')
    complete_parser.add_argument('--errors', nargs='*', help='List of errors')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate feature outputs')
    validate_parser.add_argument('feature_dir', type=Path, help='Feature directory to validate')
    
    # Global options
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        integration = AIAgentIntegration(debug=args.debug)
        
        if args.command == 'process':
            success = integration.process_workflow_outputs(args.feature_dir)
            sys.exit(0 if success else 1)
            
        elif args.command == 'complete':
            success = integration.mark_step_completed(
                args.status_file, 
                args.success, 
                args.errors or []
            )
            sys.exit(0 if success else 1)
            
        elif args.command == 'validate':
            results = integration.validate_feature_outputs(args.feature_dir)
            print(json.dumps(results, indent=2))
            sys.exit(0 if results['validation_passed'] else 1)
        
    except Exception as e:
        print(f"❌ AI Agent Integration Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
