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
    
    def __init__(self, llm_config_path: Optional[Path] = None, debug: bool = False, 
                 user_provider: Optional[str] = None, user_model: Optional[str] = None):
        self.debug = debug
        self.logger = self._setup_logging()
        
        # Store user-specified provider and model (overrides config)
        self.user_provider = user_provider
        self.user_model = user_model
        
        # Load LLM configuration
        if llm_config_path and llm_config_path.exists():
            with open(llm_config_path, 'r') as f:
                self.llm_config_data = json.load(f)
        else:
            # Use default configuration
            config_path = Path(__file__).parent / "llm-config.json"
            with open(config_path, 'r') as f:
                self.llm_config_data = json.load(f)
        
        # Initialize default LLM integration (defer until needed)
        default_provider = self.user_provider or self.llm_config_data["default_provider"]
        self.default_provider = default_provider
        self.default_llm = None
        
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
            
            # Use user selection if available, otherwise fall back to config or default
            provider_name = self.user_provider or config.get("provider", self.default_provider)
            model_name = self.user_model or config.get("model")
            
            # Get base provider configuration
            provider_config = self.llm_config_data["providers"][provider_name].copy()
            
            # Override with workflow-specific settings, but preserve user model choice
            if model_name:
                provider_config["model"] = model_name
            
            provider_config.update({
                "temperature": config.get("temperature", provider_config["temperature"]),
                "max_tokens": config.get("max_tokens", provider_config["max_tokens"])
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
        
        # Lazy initialization of default LLM
        if self.default_llm is None:
            try:
                self.default_llm = self._create_llm_integration(self.default_provider)
            except Exception as e:
                self.logger.error(f"Failed to initialize LLM integration: {e}")
                raise ValueError(f"LLM initialization failed: {e}")
        
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
        
        # Add workflow document content (CRITICAL FIX!)
        workflow_doc_path = Path(request.workflow_document)
        if workflow_doc_path.exists():
            with open(workflow_doc_path, 'r', encoding='utf-8') as f:
                workflow_content = f.read()
            
            prompt_parts.append(f"# Workflow Document: {workflow_doc_path.name}")
            prompt_parts.append(f"## Complete Workflow Document Content:")
            prompt_parts.append(f"```markdown\n{workflow_content}\n```")
            prompt_parts.append(f"\n**INSTRUCTION**: Follow the specific instructions, questions, and guidelines provided in the workflow document above.")
        else:
            # Fallback to filename only if file not found
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
            prompt_parts.append(f"\n## Project Data (CRITICAL CONTEXT)")
            prompt_parts.append(f"```json\n{json.dumps(request.context.project_data, indent=2)}\n```")
            
            # Instructions for ALL content types to use project data
            prompt_parts.append(f"\n## CRITICAL: Use Real Project Data")
            prompt_parts.append(f"**IMPORTANT**: The project data above contains REAL user answers from enhanced MVP initialization.")
            prompt_parts.append(f"- **Project Name**: `{request.context.project_data.get('project_name', 'Unknown Project')}`")
            prompt_parts.append(f"- **Primary User**: `{request.context.project_data.get('primary_user', 'Unknown User')}`")
            prompt_parts.append(f"- **Pain Point**: `{request.context.project_data.get('user_pain_point', 'Unknown Pain Point')}`")
            prompt_parts.append(f"- **Tech Stack**: `{request.context.project_data.get('recommended_tech_stack', 'Unknown Tech Stack')}`")
            prompt_parts.append(f"- **Business Model**: `{request.context.project_data.get('business_model', 'Unknown Business Model')}`")
            prompt_parts.append(f"- **Success Metric**: `{request.context.project_data.get('key_success_metric', 'Unknown Metric')}`")
            
            # Content-type specific instructions
            if request.content_type == "mvp_entrypoint":
                prompt_parts.append(f"\n**MVP ENTRYPOINT INSTRUCTIONS**:")
                prompt_parts.append(f"- Replace ALL placeholder fields with actual values from project data")
                prompt_parts.append(f"- Generate comprehensive, real documentation based on collected user data")
                prompt_parts.append(f"- Do NOT use placeholder text or field names")
            
            elif request.content_type == "tasks":
                prompt_parts.append(f"\n**TASKS GENERATION INSTRUCTIONS**:")
                prompt_parts.append(f"- Use the EXACT tech stack: `{request.context.project_data.get('recommended_tech_stack', 'specified stack')}`")
                prompt_parts.append(f"- Target the specific user type: `{request.context.project_data.get('primary_user', 'users')}`")
                prompt_parts.append(f"- Address the specific pain point: `{request.context.project_data.get('user_pain_point', 'user needs')}`")
                prompt_parts.append(f"- Align with business model: `{request.context.project_data.get('business_model', 'business approach')}`")
                prompt_parts.append(f"- Target success metric: `{request.context.project_data.get('key_success_metric', 'success measures')}`")
                prompt_parts.append(f"- Reference AI tech stack reasoning: `{request.context.project_data.get('tech_stack_reasoning', 'technical decisions')}`")
            
            elif request.content_type == "design_decisions":
                prompt_parts.append(f"\n**CRITICAL OVERRIDE: DESIGN DECISIONS INSTRUCTIONS**:")
                prompt_parts.append(f"**IGNORE WORKFLOW QUESTIONNAIRES** - The user has completed an ENHANCED AI-guided tech stack selection process.")
                prompt_parts.append(f"")
                prompt_parts.append(f"**SELECTED TECHNOLOGY STACK**: `{request.context.project_data.get('recommended_tech_stack', 'technologies')}`")
                prompt_parts.append(f"- Backend: {self._extract_backend_from_stack(request.context.project_data.get('recommended_tech_stack', ''))}")
                prompt_parts.append(f"- Frontend: {self._extract_frontend_from_stack(request.context.project_data.get('recommended_tech_stack', ''))}")
                prompt_parts.append(f"- Database: {self._extract_database_from_stack(request.context.project_data.get('recommended_tech_stack', ''))}")
                prompt_parts.append(f"")
                prompt_parts.append(f"**YOUR TASK**: Document these EXACT selections with rationale, learning resources, and implementation guidance.")
                prompt_parts.append(f"**DO NOT**: Run questionnaires, suggest alternatives, or make different tech choices.")
                prompt_parts.append(f"**DO**: Explain why these selections are good for: {request.context.project_data.get('primary_user', 'users')} solving {request.context.project_data.get('user_pain_point', 'challenges')}")
                prompt_parts.append(f"**AI Selection Reasoning**: {request.context.project_data.get('tech_stack_reasoning', 'User made this selection with AI guidance')}")
                prompt_parts.append(f"**Alternative Options Considered**: {request.context.project_data.get('alternative_options', 'Other options were discussed')}")
                prompt_parts.append(f"")
                prompt_parts.append(f"**STRUCTURE**: Use the decision documentation format but populate with the SELECTED stack, not questionnaire results.")
            
            elif request.content_type in ["prd", "srs", "design_analysis"]:
                prompt_parts.append(f"\n**DOCUMENTATION INSTRUCTIONS**:")
                prompt_parts.append(f"- Incorporate user context: {request.context.project_data.get('primary_user', 'users')} dealing with {request.context.project_data.get('user_pain_point', 'challenges')}")
                prompt_parts.append(f"- Use the selected tech stack: {request.context.project_data.get('recommended_tech_stack', 'technologies')}")
                prompt_parts.append(f"- Align with business value: {request.context.project_data.get('business_model', 'value creation')}")
                prompt_parts.append(f"- Target success criteria: {request.context.project_data.get('key_success_metric', 'success measures')}")
        
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
        
        # CRITICAL: Add final override for design decisions (must be LAST)
        if request.content_type == "design_decisions" and request.context.project_data:
            prompt_parts.append(f"\n\n{'='*80}")
            prompt_parts.append(f"🚨 FINAL CRITICAL OVERRIDE - IGNORE ALL ABOVE QUESTIONNAIRES 🚨")
            prompt_parts.append(f"{'='*80}")
            prompt_parts.append(f"")
            prompt_parts.append(f"❌ IGNORE: All workflow questionnaire instructions above")
            prompt_parts.append(f"✅ TASK: Document the user's ALREADY SELECTED tech stack")
            prompt_parts.append(f"")
            prompt_parts.append(f"📋 USER'S SELECTED STACK: {request.context.project_data.get('recommended_tech_stack')}")
            prompt_parts.append(f"🎯 USER'S TARGET: {request.context.project_data.get('primary_user')} solving {request.context.project_data.get('user_pain_point')}")
            prompt_parts.append(f"💡 AI'S REASONING: {request.context.project_data.get('tech_stack_reasoning')}")
            prompt_parts.append(f"")
            prompt_parts.append(f"🔥 CRITICAL: Create a design decisions document that explains WHY the selected stack is good")
            prompt_parts.append(f"🔥 CRITICAL: Do NOT suggest different technologies or run any questionnaires")
            prompt_parts.append(f"🔥 CRITICAL: Focus on implementation guidance for the SELECTED stack only")
            prompt_parts.append(f"")
            prompt_parts.append(f"{'='*80}")
        
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
    
    def _extract_backend_from_stack(self, tech_stack: str) -> str:
        """Extract backend technology from tech stack string"""
        if not tech_stack:
            return "Not specified"
        
        # Common patterns
        if "Node.js" in tech_stack and "Express" in tech_stack:
            return "Node.js + Express"
        elif "Python" in tech_stack and "FastAPI" in tech_stack:
            return "Python + FastAPI"
        elif "Python" in tech_stack and "Flask" in tech_stack:
            return "Python + Flask"
        elif "Node.js" in tech_stack:
            return "Node.js"
        elif "Python" in tech_stack:
            return "Python"
        else:
            # Extract first technology mentioned
            parts = tech_stack.split("+")
            return parts[0].strip() if parts else "Not specified"
    
    def _extract_frontend_from_stack(self, tech_stack: str) -> str:
        """Extract frontend technology from tech stack string"""
        if not tech_stack:
            return "Not specified"
        
        # Look for specific frontend technologies
        if "Vanilla JS" in tech_stack or "vanilla" in tech_stack.lower():
            return "Vanilla JavaScript"
        elif "React" in tech_stack:
            return "React"
        elif "Vue" in tech_stack:
            return "Vue.js"
        elif "Angular" in tech_stack:
            return "Angular"
        elif "HTML/CSS/JS" in tech_stack:
            return "HTML/CSS/JavaScript"
        else:
            # Look for general patterns
            if "JavaScript" in tech_stack or "JS" in tech_stack:
                return "JavaScript"
            else:
                return "Not specified"
    
    def _extract_database_from_stack(self, tech_stack: str) -> str:
        """Extract database technology from tech stack string"""
        if not tech_stack:
            return "Not specified"
        
        # Look for specific databases
        if "SQLite" in tech_stack:
            return "SQLite"
        elif "PostgreSQL" in tech_stack:
            return "PostgreSQL"
        elif "MySQL" in tech_stack:
            return "MySQL"
        elif "MongoDB" in tech_stack:
            return "MongoDB"
        else:
            return "Not specified"
    
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
        if self.default_llm is None:
            return {"usage": "no_llm_initialized"}
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
