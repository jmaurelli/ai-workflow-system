#!/usr/bin/env python3
"""
Enhanced Interactive Data Collector for MVP Initialization
Implements the new questioning framework with user stories, business context,
and AI-guided tech stack selection. Designed for CLI interaction with future GUI expansion.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum


class QuestionGroup(Enum):
    """Question groups for organized mental flow"""
    USER_CONTEXT = "👥 USER CONTEXT"
    BUSINESS_CONTEXT = "💼 BUSINESS CONTEXT"
    TECHNICAL_GUIDANCE = "🏗️ TECHNICAL GUIDANCE"


@dataclass
class EnhancedProjectData:
    """Container for enhanced project initialization data"""
    # Required fields first (User Context Group)
    primary_user: str
    user_pain_point: str
    user_success_journey: str
    project_name: str
    user_access_method: str
    
    # Required fields (Business Context Group)
    business_model: str
    key_success_metric: str
    three_month_success: str
    
    # Required fields (Technical Guidance Group)
    project_complexity: str
    team_context: str
    
    # Optional fields with defaults (User Context Group)
    web_primary_device: Optional[str] = None
    mobile_app_type: Optional[str] = None
    
    # Optional fields with defaults (Technical Guidance Group)
    existing_integrations: str = ""
    hard_constraints: str = ""
    recommended_tech_stack: str = ""
    tech_stack_reasoning: str = ""
    alternative_options: str = ""
    challenged_assumptions: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return asdict(self)
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


class EnhancedInteractiveDataCollector:
    """Enhanced CLI-based data collector with conversational AI tech stack guidance"""
    
    def __init__(self, ai_engine=None):
        """Initialize collector with optional AI engine for tech stack guidance"""
        self.ai_engine = ai_engine
        self.collected_data = {}
        
    def collect_mvp_requirements(self) -> EnhancedProjectData:
        """Conduct enhanced CLI session with grouped questions and AI guidance"""
        
        print("🚀 ENHANCED MVP PROJECT INITIALIZATION")
        print("=" * 60)
        print("📊 Target Time: 10 minutes | Grouped by concern for optimal flow")
        print("Let's create a comprehensive project foundation.\n")
        
        # Group 1: User Context (3-4 minutes)
        self._collect_user_context()
        
        # Group 2: Business Context (2-3 minutes)  
        self._collect_business_context()
        
        # Group 3: Technical Guidance (4-5 minutes)
        self._collect_technical_guidance()
        
        # Final confirmation and summary
        data = self._finalize_and_confirm()
        
        return data
    
    def _collect_user_context(self):
        """Collect user-focused questions (3-4 minutes)"""
        print(f"\n{QuestionGroup.USER_CONTEXT.value} GROUP (3-4 minutes)")
        print("─" * 50)
        
        # 1. Primary User Story (Multi-part)
        print("📋 Question 1: Primary User Story")
        self.collected_data['primary_user'] = self._ask_question(
            "Who is your primary user?",
            example="Small business owners managing customer data",
            description="Define the main person who will use this solution",
            required=True
        )
        
        self.collected_data['user_pain_point'] = self._ask_question(
            "What's their biggest pain point you're solving?",
            example="Manually tracking customer information in spreadsheets is error-prone and time-consuming",
            description="The core problem that drives user motivation",
            required=True
        )
        
        self.collected_data['user_success_journey'] = self._ask_question(
            "Walk me through their ideal success scenario in 2-3 steps",
            example="1. User quickly adds new customer, 2. System auto-organizes contact info, 3. User easily finds customer details when needed",
            description="End-to-end user value realization",
            required=True,
            context_aware=True
        )
        
        # 2. Project Identity
        print("\n📋 Question 2: Project Identity")
        self.collected_data['project_name'] = self._ask_question(
            "What's your project name?",
            example="CustomerHub MVP",
            description="Official project name for documentation",
            required=True
        )
        
        # 3. User Access Pattern (Simplified - Fixed Stalling Issue)
        print("\n📋 Question 3: User Access Pattern")
        
        self.collected_data['user_access_method'] = self._ask_question(
            "How will users first discover/access your solution? (web/mobile/desktop/api/other)",
            example="web",
            description="Primary access method determines technical architecture",
            required=True
        )
        
        # Simple conditional follow-up (no complex nested logic to avoid stalling)
        access_method = self.collected_data['user_access_method'].lower()
        
        if 'web' in access_method:
            print("   🚪 You mentioned web access. Would you like to specify device focus? (y/n)")
            if input("   ").strip().lower() in ['y', 'yes']:
                self.collected_data['web_primary_device'] = self._ask_question(
                    "Desktop or mobile browser primary? (desktop/mobile/both)",
                    example="desktop",
                    required=False
                )
        
        elif 'mobile' in access_method:
            print("   🚪 You mentioned mobile. Would you like to specify app type? (y/n)")
            if input("   ").strip().lower() in ['y', 'yes']:
                self.collected_data['mobile_app_type'] = self._ask_question(
                    "Native app or web app? (native/web_app/cross_platform)",
                    example="web_app",
                    required=False
                )
    
    def _collect_business_context(self):
        """Collect business-focused questions (2-3 minutes)"""
        print(f"\n{QuestionGroup.BUSINESS_CONTEXT.value} GROUP (2-3 minutes)")
        print("─" * 50)
        
        # 4. Business Model (Simplified)
        print("📋 Question 4: Business Model")
        
        self.collected_data['business_model'] = self._ask_question(
            "How does this project create value? (free_tool/paid_service/internal_efficiency/cost_reduction/revenue_generation/other)",
            example="internal_efficiency",
            description="Core value proposition",
            required=True,
            context_aware=True
        )
        
        self.collected_data['key_success_metric'] = self._ask_question(
            "What's the key metric that shows it's working?",
            example="Reduces customer lookup time from 5 minutes to 30 seconds",
            description="Measurable success indicator",
            required=True,
            context_aware=True
        )
        
        # 5. MVP Success Definition
        print("\n📋 Question 5: MVP Success Definition")
        self.collected_data['three_month_success'] = self._ask_question(
            "In 3 months, how will you know this MVP succeeded?",
            example="5 team members using it daily, 200+ customers tracked, zero data loss incidents",
            description="Concrete success criteria for MVP validation",
            required=True
        )
    
    def _collect_technical_guidance(self):
        """Collect technical questions with AI guidance (4-5 minutes)"""
        print(f"\n{QuestionGroup.TECHNICAL_GUIDANCE.value} GROUP (4-5 minutes)")
        print("─" * 50)
        
        # 6. Project Complexity Assessment (Simplified with AI Guidance)
        print("📋 Question 6: Project Complexity Assessment")
        
        print("Rate your project complexity:")
        print("   • simple: Basic CRUD operations, simple forms, read/write data")
        print("   • medium: Real-time features, user authentication, file uploads, integrations")
        print("   • complex: ML/AI features, complex workflows, high-performance requirements")
        
        self.collected_data['project_complexity'] = self._ask_question(
            "Your complexity choice (simple/medium/complex)",
            example="simple",
            description="Complexity determines architecture recommendations",
            required=True
        )
        
        # AI Guidance Trigger
        complexity = self.collected_data['project_complexity'].lower()
        print(f"\n🤖 AI GUIDANCE: Based on your {complexity} complexity choice...")
        self._provide_complexity_guidance(complexity)
        
        # 7. Team & Constraints (Multi-part)
        print("\n📋 Question 7: Team & Constraints")
        self.collected_data['team_context'] = self._ask_question(
            "What's your team size and skill level?",
            example="Solo developer, intermediate JavaScript, learning backend",
            description="Team capabilities inform technology choices",
            required=True
        )
        
        self.collected_data['existing_integrations'] = self._ask_question(
            "Any existing systems this needs to integrate with?",
            example="Must connect to existing Google Workspace, export to Excel",
            description="Integration requirements affect architecture",
            required=False
        )
        
        self.collected_data['hard_constraints'] = self._ask_question(
            "Hard constraints? (timeline, budget, compliance, etc.)",
            example="Must launch in 4 weeks, $0 hosting budget for first 3 months",
            description="Non-negotiable limitations",
            required=False
        )
        
        # 8. Interactive Tech Stack Guidance (Conversational AI Session)
        print("\n📋 Question 8: Interactive Tech Stack Guidance")
        if self.ai_engine:
            self._conduct_ai_tech_stack_consultation()
        else:
            # Fallback if no AI engine available
            self.collected_data['recommended_tech_stack'] = self._ask_question(
                "What's your preferred technology stack?",
                example="Node.js + Express + PostgreSQL + React",
                description="Technology choices for backend, frontend, and data storage",
                required=True
            )
            self.collected_data['tech_stack_reasoning'] = "User-specified stack (no AI consultation available)"
    
    def _provide_complexity_guidance(self, complexity: str):
        """Provide immediate guidance based on complexity choice"""
        guidance = {
            "simple": "I recommend focusing on proven, simple technologies with minimal setup. Consider using existing frameworks and avoiding complex architectures.",
            "medium": "I recommend balancing developer productivity with system reliability. Plan for some complexity but avoid over-engineering in the MVP phase.",
            "complex": "I recommend careful technology selection and considering technical risks early. Plan for iterative development and robust testing strategies."
        }
        
        print(f"   💡 {guidance.get(complexity, 'No specific guidance available')}")
        print("   📝 This guidance will inform my tech stack recommendations...\n")
    
    def _conduct_ai_tech_stack_consultation(self):
        """Conduct conversational AI tech stack selection session"""
        print("🤖 Starting AI Tech Stack Consultation...")
        print("   The AI will analyze your answers and provide personalized recommendations.\n")
        
        # Create context from collected data for AI
        context = {
            "user_type": self.collected_data.get('primary_user', ''),
            "pain_point": self.collected_data.get('user_pain_point', ''),
            "access_method": self.collected_data.get('user_access_method', ''),
            "complexity": self.collected_data.get('project_complexity', ''),
            "team": self.collected_data.get('team_context', ''),
            "constraints": self.collected_data.get('hard_constraints', ''),
            "integrations": self.collected_data.get('existing_integrations', '')
        }
        
        # For now, simulate AI consultation (replace with actual AI engine call)
        print("🤖 AI: Based on your answers, I'm analyzing the best tech stack options...")
        print("   📊 Considering: complexity, team skills, constraints, and integrations...")
        print("   💭 Generating recommendations...\n")
        
        # Simulate AI providing options
        print("🤖 AI: I have 3 recommendations for you:\n")
        
        print("   Option 1 (RECOMMENDED): Node.js + Express + SQLite + Vanilla JS")
        print("      ✅ Pros: Simple setup, matches team skills, fast MVP development")
        print("      ⚠️  Cons: May need migration for scaling\n")
        
        print("   Option 2: Python + Flask + PostgreSQL + React")
        print("      ✅ Pros: Great for data handling, robust database")
        print("      ⚠️  Cons: More complex setup, learning curve for React\n")
        
        print("   Option 3: No-code solution (Airtable + Zapier)")
        print("      ✅ Pros: Ultra-fast MVP, no coding required")
        print("      ⚠️  Cons: Limited customization, vendor lock-in\n")
        
        # Get user choice
        while True:
            choice = input("🤖 AI: Which option interests you most, or would you like me to explain any option? (1/2/3/explain): ").strip()
            
            if choice == "1":
                self.collected_data['recommended_tech_stack'] = "Node.js + Express + SQLite + Vanilla JS"
                self.collected_data['tech_stack_reasoning'] = "AI recommended based on team skills and simplicity requirements for fast MVP development."
                self.collected_data['alternative_options'] = "Python+Flask+PostgreSQL+React, No-code solution"
                break
            elif choice == "2":
                self.collected_data['recommended_tech_stack'] = "Python + Flask + PostgreSQL + React"
                self.collected_data['tech_stack_reasoning'] = "AI recommended for robust data handling despite slightly higher complexity."
                self.collected_data['alternative_options'] = "Node.js+Express+SQLite+VanillaJS, No-code solution"
                break
            elif choice == "3":
                self.collected_data['recommended_tech_stack'] = "Airtable + Zapier (No-code)"
                self.collected_data['tech_stack_reasoning'] = "AI recommended for ultra-fast MVP validation before committing to custom development."
                self.collected_data['alternative_options'] = "Node.js+Express+SQLite+VanillaJS, Python+Flask+PostgreSQL+React"
                break
            elif choice.lower() == "explain":
                explain_choice = input("   Which option would you like me to explain? (1/2/3): ").strip()
                if explain_choice == "1":
                    print("   🤖 AI: Option 1 is perfect for your team's JavaScript skills and simple CRUD needs...")
                elif explain_choice == "2":
                    print("   🤖 AI: Option 2 offers more robust data handling if you expect complex queries...")
                elif explain_choice == "3":
                    print("   🤖 AI: Option 3 lets you validate your idea without any code...")
                else:
                    print("   ❌ Please choose 1, 2, or 3")
            else:
                print("   ❌ Please choose 1, 2, 3, or 'explain'")
        
        print(f"   ✅ Tech Stack Decision Recorded!\n")
        
        # Simulate AI challenging assumptions
        challenge = input("🤖 AI: I notice you mentioned time constraints. Have you considered that option 3 (no-code) might get you to market 3x faster? (y/n): ").strip()
        if challenge.lower() in ['y', 'yes']:
            self.collected_data['challenged_assumptions'] = "AI challenged time constraints - suggested considering no-code for speed"
        else:
            self.collected_data['challenged_assumptions'] = "AI suggested speed consideration but user preferred code-based solution"
    
    def _finalize_and_confirm(self) -> EnhancedProjectData:
        """Final confirmation and summary before document generation"""
        print("\n📋 Question 9: Final Confirmation & Summary")
        print("─" * 50)
        
        # Create data object
        data = EnhancedProjectData(**self.collected_data)
        
        # Show comprehensive summary
        print("🤖 AI: Here's a complete summary of your project decisions:\n")
        
        print("👥 USER CONTEXT:")
        print(f"   Primary User: {data.primary_user}")
        print(f"   Pain Point: {data.user_pain_point}")
        print(f"   Success Journey: {data.user_success_journey}")
        print(f"   Project Name: {data.project_name}")
        print(f"   Access Method: {data.user_access_method}")
        
        print("\n💼 BUSINESS CONTEXT:")
        print(f"   Business Model: {data.business_model}")
        print(f"   Key Metric: {data.key_success_metric}")
        print(f"   3-Month Success: {data.three_month_success}")
        
        print("\n🏗️ TECHNICAL DECISIONS:")
        print(f"   Complexity: {data.project_complexity}")
        print(f"   Team: {data.team_context}")
        print(f"   Tech Stack: {data.recommended_tech_stack}")
        if data.tech_stack_reasoning:
            print(f"   AI Reasoning: {data.tech_stack_reasoning}")
        
        # Get final confirmation
        confirm = input("\n🤖 AI: Does this look correct? Ready to generate your MVP documentation? (y/n): ").strip()
        
        if confirm.lower() not in ['y', 'yes']:
            print("❌ Please restart the collection process to make changes.")
            raise ValueError("User rejected final summary")
        
        print("✅ Perfect! Generating comprehensive MVP documentation with rich context...")
        
        return data
    
    def _ask_question(self, question: str, example: str = None, description: str = None, required: bool = True, context_aware: bool = False) -> str:
        """Ask a single question with AI-enhanced formatting and context-aware examples"""
        print(f"❓ {question}")
        
        if description:
            print(f"   💡 {description}")
        
        # Generate AI-enhanced example if we have context and AI engine
        if context_aware and self.ai_engine and len(self.collected_data) > 0:
            try:
                ai_example = self._generate_contextual_example(question, example)
                if ai_example:
                    print(f"   🤖 AI Suggestion based on your answers: {ai_example}")
                elif example:
                    print(f"   📝 Example: {example}")
            except Exception as e:
                # Fallback to static example if AI fails
                if example:
                    print(f"   📝 Example: {example}")
        elif example:
            print(f"   📝 Example: {example}")
        
        required_text = " (required)" if required else " (optional)"
        prompt = f"   Your answer{required_text}: "
        
        while True:
            try:
                answer = input(prompt).strip()
                
                if not answer and required:
                    print("   ❌ This field is required. Please provide an answer.")
                    continue
                
                if answer:
                    print(f"   ✅ Recorded: {answer}")
                
                return answer or ""
                
            except KeyboardInterrupt:
                print("\n❌ Collection cancelled by user")
                raise
            except EOFError:
                print("\n❌ Unexpected end of input")
                raise
    
    def _generate_contextual_example(self, question: str, fallback_example: str) -> str:
        """Generate AI-enhanced examples based on collected context"""
        if not self.ai_engine:
            return fallback_example
        
        try:
            # Create context from already collected data
            context_summary = ""
            if 'primary_user' in self.collected_data:
                context_summary += f"Primary user: {self.collected_data['primary_user']}. "
            if 'user_pain_point' in self.collected_data:
                context_summary += f"Pain point: {self.collected_data['user_pain_point']}. "
            if 'project_name' in self.collected_data:
                context_summary += f"Project: {self.collected_data['project_name']}. "
            
            if not context_summary:
                return fallback_example
            
            # Simple AI prompt for contextual examples
            prompt = f"""Based on this project context: {context_summary}

Generate a specific, relevant example for this question: "{question}"

Keep it concise (1-2 sentences max) and directly related to their project context.
Don't use generic examples - make it specific to their user and pain point.

Example:"""
            
            # This would need to be implemented with actual AI call
            # For now, return enhanced fallback
            return self._create_enhanced_example(question, fallback_example)
            
        except Exception:
            return fallback_example
    
    def _create_enhanced_example(self, question: str, fallback: str) -> str:
        """Create enhanced examples based on collected context (simplified version)"""
        context = self.collected_data
        
        # Enhanced examples based on what we know
        if 'primary_user' in context and 'user_pain_point' in context:
            user = context['primary_user']
            pain = context['user_pain_point']
            
            if 'success scenario' in question.lower():
                if 'cli' in pain.lower() or 'command' in pain.lower():
                    return f"1. {user} opens your CLI reference tool, 2. Quickly searches/filters commands by topic, 3. Finds exact command with examples in under 30 seconds"
                elif 'search' in pain.lower():
                    return f"1. {user} needs specific info, 2. Uses your centralized search tool, 3. Gets accurate results without checking multiple sources"
            
            elif 'business model' in question.lower() or 'create value' in question.lower():
                if 'engineer' in user.lower() or 'support' in user.lower():
                    return "internal_efficiency (saves engineering team time and reduces context switching)"
                elif 'business' in user.lower():
                    return "cost_reduction (eliminates inefficiencies and reduces operational costs)"
            
            elif 'key metric' in question.lower():
                if 'cli' in pain.lower():
                    return "Reduces command lookup time from 2-5 minutes to under 30 seconds"
                elif 'search' in pain.lower():
                    return "Eliminates time spent searching multiple sources - single source of truth"
        
        return fallback
    
    def _ask_human_gate(self, question: str) -> bool:
        """Ask a human gate question (y/n)"""
        while True:
            answer = input(f"   🚪 {question} ").strip().lower()
            if answer in ['y', 'yes']:
                return True
            elif answer in ['n', 'no']:
                return False
            else:
                print("   ❌ Please answer 'y' or 'n'")


def main():
    """Standalone test of enhanced interactive data collector"""
    try:
        collector = EnhancedInteractiveDataCollector()
        data = collector.collect_mvp_requirements()
        
        print("\n" + "=" * 60)
        print("🔍 COLLECTED ENHANCED DATA (JSON):")
        print("=" * 60)
        print(data.to_json())
        
    except KeyboardInterrupt:
        print("\n❌ Data collection cancelled")
    except Exception as e:
        print(f"❌ Error during data collection: {e}")


if __name__ == "__main__":
    main()
