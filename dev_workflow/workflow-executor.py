#!/usr/bin/env python3

"""
🤖 Universal Workflow Document Executor
Executes individual workflow documents (01-09, s01-s08) with AI agent integration
"""

import json
import os
import sys
import argparse
import logging
import subprocess
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import tempfile

@dataclass
class WorkflowContext:
    """Context data passed between workflow steps"""
    feature_name: str
    feature_slug: str
    feature_dir: Path
    mode: str
    phase: str
    step_number: str
    project_data: Dict[str, Any]
    generated_files: List[str]
    execution_log: List[str]
    
    def save_to_manifest(self):
        """Save context to feature manifest"""
        manifest_path = self.feature_dir / "feature-manifest.json"
        
        if manifest_path.exists():
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
        else:
            manifest = self._create_base_manifest()
        
        # Update workflow status
        manifest["workflow_status"]["current_phase"] = self.phase
        manifest["workflow_status"]["last_updated"] = datetime.now(timezone.utc).isoformat()
        
        # Update execution log
        if "execution_log" not in manifest:
            manifest["execution_log"] = []
        manifest["execution_log"].extend(self.execution_log)
        
        # Update generated files
        if "generated_files" not in manifest:
            manifest["generated_files"] = []
        manifest["generated_files"].extend(self.generated_files)
        
        # Save updated manifest
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
    
    def _create_base_manifest(self):
        """Create base manifest structure"""
        return {
            "feature_metadata": {
                "feature_name": self.feature_name,
                "feature_slug": self.feature_slug,
                "creation_date": datetime.now(timezone.utc).isoformat(),
                "creator": "workflow-executor"
            },
            "workflow_status": {
                "current_phase": self.phase,
                "phases_completed": [],
                "phases_remaining": [],
                "last_updated": datetime.now(timezone.utc).isoformat()
            },
            "document_status": {},
            "execution_log": [],
            "generated_files": []
        }

class WorkflowDocumentExecutor:
    """Executes individual workflow documents with AI integration"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('workflow_executor')
        level = logging.DEBUG if self.debug else logging.INFO
        logger.setLevel(level)
        
        # Console handler
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        return logger
    
    def execute_workflow_document(self, 
                                  document_path: Path, 
                                  context: WorkflowContext,
                                  ai_agent_available: bool = True) -> bool:
        """Execute a workflow document using available methods"""
        
        self.logger.info(f"🔄 Executing workflow document: {document_path.name}")
        
        # Parse workflow document for instructions
        instructions = self._parse_workflow_document(document_path)
        
        if not instructions:
            self.logger.error(f"❌ Failed to parse workflow document: {document_path}")
            return False
        
        # Choose execution method
        if ai_agent_available:
            success = self._execute_with_ai_agent(document_path, instructions, context)
        else:
            success = self._execute_with_templates(document_path, instructions, context)
        
        if success:
            self.logger.info(f"✅ Successfully executed: {document_path.name}")
            context.execution_log.append(f"Executed {document_path.name} at {datetime.now().isoformat()}")
            context.save_to_manifest()
        else:
            self.logger.error(f"❌ Failed to execute: {document_path.name}")
        
        return success
    
    def _parse_workflow_document(self, document_path: Path) -> Dict[str, Any]:
        """Parse workflow document for execution instructions"""
        try:
            with open(document_path, 'r') as f:
                content = f.read()
            
            instructions = {
                "document_name": document_path.name,
                "objective": self._extract_objective(content),
                "inputs_required": self._extract_inputs_required(content),
                "outputs_expected": self._extract_outputs_expected(content),
                "ai_directives": self._extract_ai_directives(content),
                "template_sections": self._extract_template_sections(content),
                "validation_criteria": self._extract_validation_criteria(content)
            }
            
            return instructions
            
        except Exception as e:
            self.logger.error(f"Error parsing {document_path}: {e}")
            return {}
    
    def _extract_objective(self, content: str) -> str:
        """Extract objective/purpose from workflow document"""
        # Look for common objective patterns
        patterns = [
            r"##?\s*(?:Purpose|Objective|Goal)\s*\n(.*?)(?=\n##|\n---|\Z)",
            r"This document\s+(.*?)(?=\n|\Z)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return "Execute workflow document"
    
    def _extract_inputs_required(self, content: str) -> List[str]:
        """Extract required inputs from workflow document"""
        inputs = []
        
        # Look for input patterns
        input_patterns = [
            r"(?:Input|Inputs Required|Prerequisites).*?:\s*\n(.*?)(?=\n##|\n---|\Z)",
            r"Read\s+`([^`]+\.md)`",
            r"requires?\s+([^.\n]+)(?:\.|\n)"
        ]
        
        for pattern in input_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            inputs.extend(matches)
        
        return list(set(inputs))  # Remove duplicates
    
    def _extract_outputs_expected(self, content: str) -> List[str]:
        """Extract expected outputs from workflow document"""
        outputs = []
        
        # Look for output patterns
        output_patterns = [
            r"(?:Output|Outputs?|Generate|Create).*?:\s*\n(.*?)(?=\n##|\n---|\Z)",
            r"Generate\s+`([^`]+\.md)`",
            r"Create\s+`([^`]+\.md)`",
            r"save\s+(?:as\s+)?`([^`]+\.md)`"
        ]
        
        for pattern in output_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            outputs.extend(matches)
        
        return list(set(outputs))  # Remove duplicates
    
    def _extract_ai_directives(self, content: str) -> List[str]:
        """Extract AI agent directives from workflow document"""
        directives = []
        
        # Look for AI directive patterns
        ai_patterns = [
            r"##?\s*AI Agent Directives\s*\n(.*?)(?=\n##|\n---|\Z)",
            r"AI\s+(?:should|must|will)\s+(.*?)(?=\n|\Z)",
            r"-\s*([^.\n]*AI[^.\n]*)(?=\n|-)"
        ]
        
        for pattern in ai_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            directives.extend(matches)
        
        return [d.strip() for d in directives if d.strip()]
    
    def _extract_template_sections(self, content: str) -> Dict[str, str]:
        """Extract template sections from workflow document"""
        sections = {}
        
        # Look for template patterns
        template_match = re.search(r"##?\s*Template\s*\n(.*?)(?=\n##|\Z)", content, re.IGNORECASE | re.DOTALL)
        if template_match:
            template_content = template_match.group(1)
            
            # Extract sections within template
            section_matches = re.findall(r"###?\s*([^\n]+)\s*\n(.*?)(?=\n###?|\Z)", template_content, re.DOTALL)
            for title, section_content in section_matches:
                sections[title.strip()] = section_content.strip()
        
        return sections
    
    def _extract_validation_criteria(self, content: str) -> List[str]:
        """Extract validation criteria from workflow document"""
        criteria = []
        
        # Look for validation patterns
        validation_patterns = [
            r"(?:Validation|Validate|Check|Ensure).*?:\s*\n(.*?)(?=\n##|\n---|\Z)",
            r"[Mm]ust\s+(.*?)(?=\n|\Z)",
            r"[Ss]hould\s+(.*?)(?=\n|\Z)"
        ]
        
        for pattern in validation_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            criteria.extend(matches)
        
        return [c.strip() for c in criteria if c.strip()]
    
    def _execute_with_ai_agent(self, 
                               document_path: Path, 
                               instructions: Dict[str, Any], 
                               context: WorkflowContext) -> bool:
        """Execute workflow document using AI agent integration"""
        
        self.logger.info(f"🤖 Executing with AI agent: {document_path.name}")
        
        # Create AI agent prompt
        ai_prompt = self._create_ai_agent_prompt(instructions, context)
        
        # Save prompt to temp file for AI agent execution
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(ai_prompt)
            prompt_file = Path(f.name)
        
        try:
            # For now, create a structured output file that AI can follow
            output_file = context.feature_dir / f"{context.step_number}-output.md"
            
            # Create execution instructions for AI
            self._create_ai_execution_file(prompt_file, output_file, instructions, context)
            
            # Log the AI execution request
            self.logger.info(f"📝 Created AI execution instructions: {output_file}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"AI agent execution failed: {e}")
            return False
        finally:
            # Cleanup temp file
            if prompt_file.exists():
                prompt_file.unlink()
    
    def _create_ai_agent_prompt(self, instructions: Dict[str, Any], context: WorkflowContext) -> str:
        """Create structured prompt for AI agent execution"""
        
        prompt = f"""# AI Agent Execution Request

## Workflow Document: {instructions['document_name']}

### Objective
{instructions['objective']}

### Context
- Feature Name: {context.feature_name}
- Feature Directory: {context.feature_dir}
- Current Phase: {context.phase}
- Current Step: {context.step_number}
- Mode: {context.mode}

### Available Project Data
{json.dumps(context.project_data, indent=2)}

### Required Inputs
{chr(10).join(f"- {inp}" for inp in instructions['inputs_required'])}

### Expected Outputs
{chr(10).join(f"- {out}" for out in instructions['outputs_expected'])}

### AI Directives
{chr(10).join(f"- {directive}" for directive in instructions['ai_directives'])}

### Template Sections
"""
        
        for section_title, section_content in instructions['template_sections'].items():
            prompt += f"\n#### {section_title}\n{section_content}\n"
        
        prompt += f"""
### Validation Criteria
{chr(10).join(f"- {criteria}" for criteria in instructions['validation_criteria'])}

### Execution Instructions
1. Read the workflow document: {instructions['document_name']}
2. Follow the AI directives specified in the document
3. Use the provided project data and context
4. Generate the expected outputs in the feature directory: {context.feature_dir}
5. Validate outputs against the criteria
6. Update the execution status

### Output Requirements
- Save all generated files in: {context.feature_dir}/
- Use relative paths in document references
- Follow the feature-centric architecture
- Update feature-manifest.json with completion status
"""
        
        return prompt
    
    def _create_ai_execution_file(self, 
                                  prompt_file: Path, 
                                  output_file: Path, 
                                  instructions: Dict[str, Any], 
                                  context: WorkflowContext):
        """Create structured file for AI execution tracking"""
        
        execution_data = {
            "workflow_step": {
                "document": instructions['document_name'],
                "step_number": context.step_number,
                "phase": context.phase,
                "timestamp": datetime.now().isoformat()
            },
            "execution_status": "ready_for_ai_agent",
            "ai_prompt_file": str(prompt_file),
            "feature_directory": str(context.feature_dir),
            "expected_outputs": instructions['outputs_expected'],
            "validation_criteria": instructions['validation_criteria'],
            "completion_status": {
                "started": False,
                "completed": False,
                "validated": False,
                "errors": []
            }
        }
        
        with open(output_file, 'w') as f:
            f.write(f"# AI Execution Status: {instructions['document_name']}\n\n")
            f.write("```json\n")
            f.write(json.dumps(execution_data, indent=2))
            f.write("\n```\n\n")
            f.write("## Instructions for AI Agent\n\n")
            f.write(f"Execute the workflow document `{instructions['document_name']}` using the context and data provided.\n\n")
            f.write("### Next Steps\n")
            f.write("1. Read the workflow document\n")
            f.write("2. Execute the instructions\n") 
            f.write("3. Generate required outputs\n")
            f.write("4. Validate results\n")
            f.write("5. Update completion status\n")
        
        context.generated_files.append(str(output_file))
    
    def _execute_with_templates(self, 
                                document_path: Path, 
                                instructions: Dict[str, Any], 
                                context: WorkflowContext) -> bool:
        """Execute workflow document using template-based generation"""
        
        self.logger.info(f"📄 Executing with templates: {document_path.name}")
        
        try:
            # Generate basic template files based on instructions
            for output in instructions['outputs_expected']:
                if output.endswith('.md'):
                    output_path = context.feature_dir / output
                    self._generate_template_file(output_path, instructions, context)
                    context.generated_files.append(str(output_path))
            
            return True
            
        except Exception as e:
            self.logger.error(f"Template execution failed: {e}")
            return False
    
    def _generate_template_file(self, 
                                output_path: Path, 
                                instructions: Dict[str, Any], 
                                context: WorkflowContext):
        """Generate a template file based on workflow instructions"""
        
        content = f"""# {output_path.stem.replace('-', ' ').title()}

*Generated by workflow executor on {datetime.now().isoformat()}*

## Objective
{instructions['objective']}

## Context
- Feature: {context.feature_name}
- Step: {context.step_number}
- Phase: {context.phase}
"""
        
        # Add template sections if available
        for section_title, section_content in instructions['template_sections'].items():
            content += f"\n## {section_title}\n{section_content}\n"
        
        # Add placeholder content
        content += f"""
## Generated Content
*This file was generated as a template. An AI agent or human should complete the content based on the workflow document: {instructions['document_name']}*

### Required Inputs
{chr(10).join(f"- {inp}" for inp in instructions['inputs_required'])}

### AI Directives
{chr(10).join(f"- {directive}" for directive in instructions['ai_directives'])}

### Validation Criteria
{chr(10).join(f"- {criteria}" for criteria in instructions['validation_criteria'])}

---
*To complete this document, follow the instructions in: {instructions['document_name']}*
"""
        
        with open(output_path, 'w') as f:
            f.write(content)

def main():
    """Main entry point for workflow executor"""
    parser = argparse.ArgumentParser(
        description="🤖 Universal Workflow Document Executor"
    )
    
    parser.add_argument("document", 
                       help="Path to workflow document to execute")
    
    parser.add_argument("--feature", 
                       required=True,
                       help="Feature name")
    
    parser.add_argument("--feature-dir",
                       type=Path,
                       help="Feature directory path (auto-created if not provided)")
    
    parser.add_argument("--mode",
                       default="guided",
                       choices=["guided", "autonomous", "learning"],
                       help="Execution mode")
    
    parser.add_argument("--step",
                       help="Step number (e.g., 01, s02)")
    
    parser.add_argument("--phase", 
                       help="Workflow phase")
    
    parser.add_argument("--project-data",
                       type=Path,
                       help="Path to JSON file containing project data")
    
    parser.add_argument("--no-ai-agent",
                       action="store_true",
                       help="Use template-based execution instead of AI agent")
    
    parser.add_argument("--debug",
                       action="store_true",
                       help="Enable debug logging")
    
    args = parser.parse_args()
    
    try:
        # Initialize executor
        executor = WorkflowDocumentExecutor(debug=args.debug)
        
        # Setup feature directory
        if args.feature_dir:
            feature_dir = args.feature_dir
        else:
            feature_slug = args.feature.lower().replace(' ', '-').replace('_', '-')
            date_prefix = datetime.now().strftime('%Y-%m-%d')
            feature_dir = Path.cwd() / "features" / f"{date_prefix}-{feature_slug}"
        
        feature_dir.mkdir(parents=True, exist_ok=True)
        
        # Load project data
        project_data = {}
        if args.project_data and args.project_data.exists():
            with open(args.project_data, 'r') as f:
                project_data = json.load(f)
        
        # Create workflow context
        context = WorkflowContext(
            feature_name=args.feature,
            feature_slug=args.feature.lower().replace(' ', '-').replace('_', '-'),
            feature_dir=feature_dir,
            mode=args.mode,
            phase=args.phase or "unknown",
            step_number=args.step or "unknown",
            project_data=project_data,
            generated_files=[],
            execution_log=[]
        )
        
        # Execute workflow document
        document_path = Path(args.document)
        ai_agent_available = not args.no_ai_agent
        
        success = executor.execute_workflow_document(
            document_path, 
            context, 
            ai_agent_available
        )
        
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Workflow execution error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
