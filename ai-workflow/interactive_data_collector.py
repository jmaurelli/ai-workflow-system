#!/usr/bin/env python3
"""
Interactive Data Collector for MVP Initialization
Handles CLI-based questioning for project setup data collection.
Designed to be GUI-replaceable in the future.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Question:
    """Represents a single initialization question"""
    field: str
    question: str
    type: str
    example: Optional[str] = None
    required: bool = True
    default: Optional[str] = None
    description: Optional[str] = None


@dataclass 
class ProjectInitializationData:
    """Container for collected project initialization data"""
    project_name: str
    project_goal: str
    mvp_scope: str
    mvp_constraints: str = ""
    tech_stack: str = "Node.js + Express + SQLite + HTML/CSS/JS"
    external_services: bool = False
    deployment_target: str = "local"
    success_criteria: str = ""
    mvp_timeline: str = "4 weeks"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return asdict(self)
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


class InteractiveDataCollector:
    """Collects MVP initialization data through CLI interaction"""
    
    def __init__(self):
        self.questions = self._load_questions()
    
    def _load_questions(self) -> List[Question]:
        """Load questions from 01-mvp-entrypoint.md workflow document"""
        # Define the 9 structured questions from the workflow document
        return [
            Question(
                field="project_name",
                question="What is the project name?",
                type="string",
                example="User Authentication Service",
                required=True,
                description="The official name for the project, used in documentation and artifacts"
            ),
            Question(
                field="project_goal", 
                question="What is the one-liner goal of this project?",
                type="string",
                example="Enable secure user authentication for web applications",
                required=True,
                description="Concise statement of why this project exists and what problem it solves"
            ),
            Question(
                field="mvp_scope",
                question="What is the MVP scope in 2-3 sentences?",
                type="string", 
                example="User registration, login, password reset, and basic profile management. No social login or advanced security features in MVP.",
                required=True,
                description="Clear definition of what is and isn't included in the MVP phase"
            ),
            Question(
                field="mvp_constraints",
                question="What are the primary constraints for this MVP?",
                type="string",
                example="Must be deployable to standard cloud hosting, complete within 2 weeks, use existing tech stack",
                required=False,
                default="",
                description="Time, budget, technical, or business constraints that limit MVP scope"
            ),
            Question(
                field="tech_stack",
                question="What is your preferred technology stack?",
                type="string",
                example="Node.js + Express + PostgreSQL + React",
                required=False,
                default="Node.js + Express + SQLite + HTML/CSS/JS",
                description="Technology choices for backend, frontend, and data storage"
            ),
            Question(
                field="external_services",
                question="Do you need external services or integrations? (y/n)",
                type="boolean",
                example="n",
                required=False,
                default="n",
                description="Whether the MVP requires third-party APIs, authentication providers, or external services"
            ),
            Question(
                field="deployment_target",
                question="What is your deployment target? (local/cloud/container)",
                type="enum",
                example="local",
                required=False,
                default="local",
                description="Where the MVP will be deployed"
            ),
            Question(
                field="success_criteria",
                question="What defines MVP success? (list 2-3 key criteria)",
                type="string",
                example="Users can register and login successfully, basic profile management works, system handles 100 concurrent users",
                required=True,
                description="Measurable outcomes that indicate the MVP is complete and functional"
            ),
            Question(
                field="mvp_timeline",
                question="What is your timeline for MVP completion?",
                type="string",
                example="2 weeks",
                required=False,
                default="4 weeks",
                description="Expected timeframe to complete the MVP phase"
            )
        ]
    
    def collect_mvp_requirements(self) -> ProjectInitializationData:
        """Conduct interactive CLI session to collect MVP requirements"""
        
        print("🎯 MVP PROJECT INITIALIZATION")
        print("=" * 50)
        print("Let's gather the essential information for your MVP project.")
        print("You can always revise answers later.\n")
        
        collected_data = {}
        
        for i, question in enumerate(self.questions, 1):
            print(f"📋 Question {i}/{len(self.questions)}")
            answer = self._ask_question(question)
            collected_data[question.field] = answer
            print()  # Add spacing between questions
        
        # Create and return structured data
        data = ProjectInitializationData(**collected_data)
        
        # Show summary for confirmation
        self._show_summary(data)
        
        return data
    
    def _ask_question(self, question: Question) -> Any:
        """Ask a single question and get validated response"""
        
        # Show question with context
        print(f"❓ {question.question}")
        
        if question.description:
            print(f"   💡 {question.description}")
        
        if question.example:
            print(f"   📝 Example: {question.example}")
        
        if question.default and not question.required:
            print(f"   🔧 Default: {question.default}")
        
        required_text = " (required)" if question.required else " (optional)"
        prompt = f"   Your answer{required_text}: "
        
        while True:
            try:
                answer = input(prompt).strip()
                
                # Handle empty responses
                if not answer:
                    if question.required:
                        print("   ❌ This field is required. Please provide an answer.")
                        continue
                    else:
                        # Use default for optional fields
                        answer = question.default or ""
                        if answer:
                            print(f"   ✅ Using default: {answer}")
                        break
                
                # Type-specific validation
                if question.type == "boolean":
                    if answer.lower() in ['y', 'yes', 'true', '1']:
                        answer = True
                    elif answer.lower() in ['n', 'no', 'false', '0']:
                        answer = False
                    else:
                        print("   ❌ Please answer with 'y' or 'n'")
                        continue
                
                elif question.type == "enum" and question.field == "deployment_target":
                    if answer.lower() not in ['local', 'cloud', 'container']:
                        print("   ❌ Please choose: local, cloud, or container")
                        continue
                    answer = answer.lower()
                
                # Success
                print(f"   ✅ Recorded: {answer}")
                return answer
                
            except KeyboardInterrupt:
                print("\n❌ Collection cancelled by user")
                raise
            except EOFError:
                print("\n❌ Unexpected end of input")
                raise
    
    def _show_summary(self, data: ProjectInitializationData):
        """Show collected data summary for user confirmation"""
        
        print("\n" + "=" * 50)
        print("📊 COLLECTED PROJECT DATA SUMMARY")
        print("=" * 50)
        
        print(f"🏷️  Project Name: {data.project_name}")
        print(f"🎯 Goal: {data.project_goal}")
        print(f"📋 MVP Scope: {data.mvp_scope}")
        print(f"⚙️  Tech Stack: {data.tech_stack}")
        print(f"🏁 Success Criteria: {data.success_criteria}")
        print(f"⏱️  Timeline: {data.mvp_timeline}")
        
        if data.mvp_constraints:
            print(f"⚠️  Constraints: {data.mvp_constraints}")
        
        if data.external_services:
            print(f"🔗 External Services: Yes")
        
        print(f"🚀 Deployment: {data.deployment_target}")
        
        print("\n✅ Data collection complete! Proceeding to document generation...")


def main():
    """Standalone test of interactive data collector"""
    try:
        collector = InteractiveDataCollector()
        data = collector.collect_mvp_requirements()
        
        print("\n" + "=" * 50)
        print("🔍 COLLECTED DATA (JSON):")
        print("=" * 50)
        print(data.to_json())
        
    except KeyboardInterrupt:
        print("\n❌ Data collection cancelled")
    except Exception as e:
        print(f"❌ Error during data collection: {e}")


if __name__ == "__main__":
    main()
