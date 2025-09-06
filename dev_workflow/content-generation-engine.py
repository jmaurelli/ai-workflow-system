#!/usr/bin/env python3

"""
🚀 Content Generation Engine for Workflow Automation
Generates real PRD, SRS, tasks, and other workflow content using LLM APIs
"""

import json
import os
import sys
import argparse
import logging
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
import tempfile

# Import our LLM integration
from llm_api_integration import LLMAPIIntegration, LLMConfig, LLMRequest, LLMResponse, LLMProvider, load_llm_config

@dataclass
class WorkflowContext:
    feature_name: str
    feature_slug: str
    feature_dir: Path
    workflow_step: str
    phase: str
    project_data: Dict[str, Any]
    previous_outputs: Dict[str, str] = None

@dataclass
class ContentGenerationRequest:
    workflow_document: str
    context: WorkflowContext
    output_file: str
    content_type: str  # prd, srs, tasks, etc.
    template_sections: Dict[str, str] = None
    ai_directives: List[str] = None

class ContentGenerationEngine:
    """Generates real workflow content using LLM APIs"""
    
    def __init__(self, llm_config_path: Optional[Path] = None, debug: bool = False):
        self.debug = debug
        self.logger = self._setup_logging()
        
        # Load LLM configuration
        if llm_config_path and llm_config_path.exists():
            with open(llm_config_path, 'r') as f:
                self.llm_config_data = json.load(f)
        else:
            # Use default configuration
            config_path = Path(__file__).parent / "llm-config.json"
            with open(config_path, 'r') as f:
                self.llm_config_data = json.load(f)
        
        # Initialize default LLM integration
        default_provider = self.llm_config_data["default_provider"]
        self.default_llm = self._create_llm_integration(default_provider)
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('content_generation_engine')
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
    
    def _create_llm_integration(self, provider_name: str) -> LLMAPIIntegration:
        """Create LLM integration for specific provider"""
        
        provider_config = self.llm_config_data["providers"][provider_name]
        
        config = LLMConfig(
            provider=LLMProvider(provider_config["provider"]),
            model=provider_config["model"],
            api_key=provider_config.get("api_key"),
            base_url=provider_config.get("base_url"),
            max_tokens=provider_config["max_tokens"],
            temperature=provider_config["temperature"],
            timeout=provider_config["timeout"],
            max_retries=provider_config["max_retries"],
            cost_limit_usd=provider_config["cost_limit_usd"]
        )
        
        return LLMAPIIntegration(config, debug=self.debug)
    
    def generate_content(self, request: ContentGenerationRequest) -> str:
        """Generate content for workflow step using appropriate LLM"""
        
        self.logger.info(f"🚀 Generating {request.content_type} content for {request.workflow_document}")
        
        # Determine which LLM configuration to use
        llm_integration = self._select_llm_for_content_type(request.content_type)
        
        # Create specialized prompt for content type
        llm_request = self._create_specialized_prompt(request)
        
        # Generate content
        response = llm_integration.generate_content(llm_request)
        
        if not response.validated:
            self.logger.warning(f"Generated content failed validation: {response.validation_errors}")
        
        # Post-process content
        final_content = self._post_process_content(response.content, request)
        
        self.logger.info(f"✅ Generated {len(final_content)} characters of {request.content_type} content")
        
        return final_content
    
    def _select_llm_for_content_type(self, content_type: str) -> LLMAPIIntegration:
        """Select appropriate LLM integration based on content type"""
        
        workflow_configs = self.llm_config_data["workflow_specific_configs"]
        
        # Map content types to workflow configs
        content_type_mapping = {
            "mvp_entrypoint": "mvp_entrypoint",
            "prd": "gen_prd", 
            "srs": "gen_srs",
            "design_decisions": "gen_design_decisions",
            "design_analysis": "gen_design",
            "tasks": "gen_tasks_and_testing",
            "task_processing": "process_tasks",
            "completion_summary": "gen_completion_summary",
            "enterprise": "enterprise_scaling"
        }
        
        config_key = content_type_mapping.get(content_type, "gen_prd")
        
        if config_key in workflow_configs:
            config = workflow_configs[config_key]
            provider_name = config["provider"]
            
            # Create specialized LLM integration
            provider_config = self.llm_config_data["providers"][provider_name].copy()
            provider_config.update({
                "model": config["model"],
                "temperature": config["temperature"],
                "max_tokens": config["max_tokens"]
            })
            
            llm_config = LLMConfig(
                provider=LLMProvider(provider_config["provider"]),
                model=provider_config["model"],
                api_key=provider_config.get("api_key"),
                base_url=provider_config.get("base_url"),
                max_tokens=provider_config["max_tokens"],
                temperature=provider_config["temperature"],
                timeout=provider_config["timeout"],
                max_retries=provider_config["max_retries"],
                cost_limit_usd=provider_config["cost_limit_usd"]
            )
            
            return LLMAPIIntegration(llm_config, debug=self.debug)
        
        return self.default_llm
    
    def _create_specialized_prompt(self, request: ContentGenerationRequest) -> LLMRequest:
        """Create specialized prompt for specific content type"""
        
        # Get workflow-specific configuration
        workflow_configs = self.llm_config_data["workflow_specific_configs"]
        content_type_mapping = {
            "mvp_entrypoint": "mvp_entrypoint",
            "prd": "gen_prd",
            "srs": "gen_srs", 
            "design_decisions": "gen_design_decisions",
            "design_analysis": "gen_design",
            "tasks": "gen_tasks_and_testing",
            "task_processing": "process_tasks",
            "completion_summary": "gen_completion_summary",
            "enterprise": "enterprise_scaling"
        }
        
        config_key = content_type_mapping.get(request.content_type, "gen_prd")
        system_prompt = workflow_configs.get(config_key, {}).get("system_prompt", "You are a helpful AI assistant.")
        
        # Build comprehensive prompt
        prompt_parts = []
        
        # Add workflow document reference
        prompt_parts.append(f"# Workflow Document: {request.workflow_document}")
        prompt_parts.append(f"Please execute the instructions in the workflow document: {request.workflow_document}")
        
        # Add context information
        prompt_parts.append(f"\n## Project Context")
        prompt_parts.append(f"- **Feature Name**: {request.context.feature_name}")
        prompt_parts.append(f"- **Feature Slug**: {request.context.feature_slug}")
        prompt_parts.append(f"- **Workflow Step**: {request.context.workflow_step}")
        prompt_parts.append(f"- **Phase**: {request.context.phase}")
        prompt_parts.append(f"- **Output File**: {request.output_file}")
        
        # Add project data if available
        if request.context.project_data:
            prompt_parts.append(f"\n## Project Data")
            prompt_parts.append(f"```json\n{json.dumps(request.context.project_data, indent=2)}\n```")
        
        # Add previous outputs for context
        if request.context.previous_outputs:
            prompt_parts.append(f"\n## Previous Workflow Outputs")
            for step, content in request.context.previous_outputs.items():
                if content and len(content) > 100:  # Only include substantial content
                    truncated = content[:500] + "..." if len(content) > 500 else content
                    prompt_parts.append(f"### {step}")
                    prompt_parts.append(f"```\n{truncated}\n```")
        
        # Add AI directives if provided
        if request.ai_directives:
            prompt_parts.append(f"\n## AI Directives")
            for directive in request.ai_directives:
                prompt_parts.append(f"- {directive}")
        
        # Add template sections if provided
        if request.template_sections:
            prompt_parts.append(f"\n## Template Sections")
            for section_name, section_content in request.template_sections.items():
                if section_content.strip():
                    prompt_parts.append(f"### {section_name}")
                    prompt_parts.append(section_content)
        
        # Add common instructions
        common_instructions = self.llm_config_data["prompt_engineering"]["common_instructions"]
        prompt_parts.append(f"\n## Instructions")
        for instruction in common_instructions:
            prompt_parts.append(f"- {instruction}")
        
        # Add specific output requirements
        prompt_parts.append(f"\n## Output Requirements")
        prompt_parts.append(f"- Generate content for: **{request.output_file}**")
        prompt_parts.append(f"- Content type: **{request.content_type}**")
        prompt_parts.append(f"- Use markdown formatting for clear structure")
        prompt_parts.append(f"- Follow the workflow document instructions precisely")
        prompt_parts.append(f"- Include all required sections and subsections")
        prompt_parts.append(f"- Make content practical and immediately actionable")
        
        # Feature-centric path instructions
        prompt_parts.append(f"\n## Feature-Centric Integration")
        prompt_parts.append(f"- Save content as: `{request.output_file}` (relative path within feature directory)")
        prompt_parts.append(f"- Use relative references to other workflow documents (e.g., `./prd.md`, `./srs.md`)")
        prompt_parts.append(f"- Include appropriate linkages to related workflow documents")
        
        full_prompt = "\n".join(prompt_parts)
        
        # Get validation criteria for content type
        validation_criteria = self._get_validation_criteria(request.content_type)
        
        return LLMRequest(
            prompt=full_prompt,
            system_prompt=system_prompt,
            context_data=request.context.project_data,
            expected_format="markdown",
            validation_criteria=validation_criteria
        )
    
    def _get_validation_criteria(self, content_type: str) -> List[str]:
        """Get validation criteria for specific content type"""
        
        validation_config = self.llm_config_data["prompt_engineering"]["validation_criteria"]
        
        # Return specific criteria if available, otherwise default
        return validation_config.get(content_type, validation_config["default"])
    
    def _post_process_content(self, content: str, request: ContentGenerationRequest) -> str:
        """Post-process generated content for consistency and quality"""
        
        # Add metadata header
        processed_content = f"# {request.context.feature_name} - {request.content_type.upper()}\n\n"
        processed_content += f"*Generated by automated workflow on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        
        # Clean up the generated content
        cleaned_content = content.strip()
        
        # Remove duplicate titles if LLM generated them
        lines = cleaned_content.split('\n')
        if lines and lines[0].startswith('#'):
            # Remove first line if it's a duplicate title
            feature_words = request.context.feature_name.lower().split()
            first_line_lower = lines[0].lower()
            if any(word in first_line_lower for word in feature_words):
                lines = lines[1:]
                cleaned_content = '\n'.join(lines).strip()
        
        processed_content += cleaned_content
        
        # Add footer with workflow integration
        processed_content += f"\n\n---\n"
        processed_content += f"*Generated by: {request.workflow_document} | Step: {request.context.workflow_step} | Phase: {request.context.phase}*\n"
        
        return processed_content
    
    def generate_multiple_outputs(self, requests: List[ContentGenerationRequest]) -> Dict[str, str]:
        """Generate multiple content outputs efficiently"""
        
        results = {}
        
        for request in requests:
            try:
                content = self.generate_content(request)
                results[request.output_file] = content
                
                # Write content to file
                output_path = request.context.feature_dir / request.output_file
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_path, 'w') as f:
                    f.write(content)
                
                self.logger.info(f"✅ Generated and saved: {output_path}")
                
            except Exception as e:
                self.logger.error(f"❌ Failed to generate {request.output_file}: {e}")
                results[request.output_file] = f"# Error\n\nFailed to generate content: {e}"
        
        return results
    
    def get_usage_summary(self) -> Dict[str, Any]:
        """Get usage summary across all LLM integrations"""
        
        # This would aggregate usage across all LLM integrations
        # For now, return default LLM stats
        return self.default_llm.get_usage_stats()

def main():
    """Main entry point for content generation engine testing"""
    parser = argparse.ArgumentParser(
        description="🚀 Content Generation Engine for Workflow Automation"
    )
    
    parser.add_argument("--workflow-document",
                       required=True,
                       help="Workflow document to execute")
    
    parser.add_argument("--feature-name",
                       required=True,
                       help="Feature name")
    
    parser.add_argument("--feature-dir",
                       type=Path,
                       required=True,
                       help="Feature directory")
    
    parser.add_argument("--content-type",
                       required=True,
                       choices=["prd", "srs", "design_decisions", "design_analysis", "tasks", "completion_summary"],
                       help="Type of content to generate")
    
    parser.add_argument("--output-file",
                       required=True,
                       help="Output file name")
    
    parser.add_argument("--project-data",
                       type=Path,
                       help="Path to project data JSON file")
    
    parser.add_argument("--llm-config",
                       type=Path,
                       help="Path to LLM configuration file")
    
    parser.add_argument("--debug",
                       action="store_true",
                       help="Enable debug logging")
    
    args = parser.parse_args()
    
    try:
        # Load project data
        project_data = {}
        if args.project_data and args.project_data.exists():
            with open(args.project_data, 'r') as f:
                project_data = json.load(f)
        
        # Create workflow context
        feature_slug = args.feature_name.lower().replace(' ', '-').replace('_', '-')
        context = WorkflowContext(
            feature_name=args.feature_name,
            feature_slug=feature_slug,
            feature_dir=args.feature_dir,
            workflow_step="test",
            phase="test",
            project_data=project_data
        )
        
        # Create content generation request
        request = ContentGenerationRequest(
            workflow_document=args.workflow_document,
            context=context,
            output_file=args.output_file,
            content_type=args.content_type
        )
        
        # Initialize content generation engine
        engine = ContentGenerationEngine(args.llm_config, debug=args.debug)
        
        # Generate content
        content = engine.generate_content(request)
        
        # Save content
        output_path = args.feature_dir / args.output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            f.write(content)
        
        print(f"✅ Generated content saved to: {output_path}")
        
        # Show usage stats
        stats = engine.get_usage_summary()
        print(f"Usage Stats: {stats}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
