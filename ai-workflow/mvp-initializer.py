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
    
    # Show integration status
    if LLM_AVAILABLE == True:
        print("✨ Full AI integration available - all providers with advanced features!")
    else:
        print("⚡ Basic integration - all providers supported with core features!")
    
    print("\nChoose your AI provider:")
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
                    return "skip", None  # User chose to exit
                
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

                # Step 3: Dynamic model selection
                print(f"\n🤖 Loading available {selected_provider['name']} models...")
                available_models = _get_available_models(selected_provider["provider"], api_key)
                
                if not available_models:
                    print(f"❌ Could not load models for {selected_provider['name']}")
                    return "failed", None
                
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

def _get_available_models(provider: str, api_key: str) -> List[Dict[str, str]]:
    """Get available models for a provider (dynamic where possible)"""
    
    try:
        import requests
        
        if provider == "openai":
            # Query OpenAI models API
            response = requests.get(
                "https://api.openai.com/v1/models",
                headers={"Authorization": f"Bearer {api_key}"},
                timeout=10
            )
            if response.status_code == 200:
                models_data = response.json()["data"]
                # Filter to chat models and sort by popularity/recency
                chat_models = []
                preferred_order = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"]
                
                for model in models_data:
                    model_id = model["id"]
                    if any(prefix in model_id for prefix in ["gpt-4", "gpt-3.5-turbo"]):
                        # Create cleaner model descriptions
                        display_name = model_id.replace("-", " ").title()
                        if "gpt-4o" in model_id:
                            if "mini" in model_id:
                                description = "Efficient & fast multimodal model"
                            else:
                                description = "Latest multimodal model - text, images, audio"
                        elif "gpt-4-turbo" in model_id:
                            description = "Advanced reasoning with large context"
                        elif "gpt-4" in model_id:
                            description = "Powerful reasoning model"
                        elif "gpt-3.5-turbo" in model_id:
                            description = "Fast & cost-effective"
                        else:
                            description = f"OpenAI {model_id}"
                            
                        chat_models.append({
                            "id": model_id,
                            "name": display_name,
                            "description": description
                        })
                
                # Sort by preferred order
                def sort_key(model):
                    try:
                        return preferred_order.index(model["id"])
                    except ValueError:
                        return 999
                        
                return sorted(chat_models, key=sort_key)[:5]  # Top 5 models
                
        elif provider == "google":
            # Query Gemini models API
            response = requests.get(
                f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}",
                timeout=10
            )
            if response.status_code == 200:
                models_data = response.json().get("models", [])
                gemini_models = []
                
                for model in models_data:
                    model_name = model.get("name", "").replace("models/", "")
                    if "gemini" in model_name.lower():
                        # Create cleaner descriptions for Gemini models
                        display_name = model_name.replace("-", " ").title()
                        if "2.0" in model_name:
                            if "flash" in model_name:
                                description = "Latest experimental - fast & efficient"
                            else:
                                description = "Latest generation model"
                        elif "1.5-pro" in model_name:
                            description = "Advanced reasoning & large context"
                        elif "1.5-flash" in model_name:
                            description = "Fast & efficient processing"
                        else:
                            description = f"Google {model_name}"
                            
                        gemini_models.append({
                            "id": model_name,
                            "name": display_name,
                            "description": description
                        })
                
                return gemini_models[:5]  # Top 5 models
                
        elif provider == "anthropic":
            # Anthropic doesn't have a public models API, use curated list
            return [
                {"id": "claude-3-5-sonnet-20241022", "name": "Claude 3.5 Sonnet", "description": "Latest Sonnet - Balanced intelligence & speed"},
                {"id": "claude-3-5-haiku-20241022", "name": "Claude 3.5 Haiku", "description": "Fastest - Optimized for speed"},
                {"id": "claude-3-opus-20240229", "name": "Claude 3 Opus", "description": "Most intelligent - Complex reasoning"},
                {"id": "claude-3-sonnet-20240229", "name": "Claude 3 Sonnet", "description": "Previous generation Sonnet"},
                {"id": "claude-3-haiku-20240307", "name": "Claude 3 Haiku", "description": "Previous generation Haiku"}
            ]
            
    except Exception as e:
        print(f"💭 Could not fetch models for {provider}: {e}")
    
    # Fallback to hardcoded models  
    fallback_models = {
        "openai": [
            {"id": "gpt-4o", "name": "Gpt 4O", "description": "Latest multimodal model - text, images, audio"},
            {"id": "gpt-4o-mini", "name": "Gpt 4O Mini", "description": "Efficient & fast multimodal model"},
            {"id": "gpt-4-turbo", "name": "Gpt 4 Turbo", "description": "Advanced reasoning with large context"},
            {"id": "gpt-3.5-turbo", "name": "Gpt 3.5 Turbo", "description": "Fast & cost-effective"}
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

def _call_openai_api_extended(api_key: str, messages: List[Dict], model: str) -> str:
    """Call OpenAI API with extended token limit for complex responses"""
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": messages,
            "max_tokens": 1500,  # Much higher limit for complex JSON responses
            "temperature": 0.7
        },
        timeout=60  # Longer timeout for complex responses
    )
    
    if response.status_code != 200:
        raise Exception(f"OpenAI API call failed: {response.status_code} - {response.text}")
    
    return response.json()["choices"][0]["message"]["content"]

def _call_anthropic_api_extended(api_key: str, messages: List[Dict], model: str) -> str:
    """Call Anthropic API with extended token limit for complex responses"""
    system_msg = messages[0]["content"] if messages and messages[0]["role"] == "system" else ""
    user_msg = messages[-1]["content"] if messages else ""
    
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": model,
            "max_tokens": 1500,  # Much higher limit
            "system": system_msg,
            "messages": [{"role": "user", "content": user_msg}]
        },
        timeout=60
    )
    
    if response.status_code != 200:
        raise Exception(f"Anthropic API call failed: {response.status_code}")
    
    return response.json()["content"][0]["text"]

def _call_google_api_extended(api_key: str, messages: List[Dict], model: str) -> str:
    """Call Google Gemini API with extended token limit for complex responses"""
    system_msg = messages[0]["content"] if messages and messages[0]["role"] == "system" else ""
    user_msg = messages[-1]["content"] if messages else ""
    
    combined_prompt = f"{system_msg}\n\nUser: {user_msg}"
    
    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{
                "parts": [{"text": combined_prompt}]
            }],
            "generationConfig": {
                "maxOutputTokens": 1500,  # Much higher limit
                "temperature": 0.7
            }
        },
        timeout=60
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

Generate 3-4 specific, insightful follow-up questions that avoid overlap and gather diverse information:

1. WHO (target users) - be specific to the domain
2. WHAT (key capability/outcome) - focus on user value, not features  
3. HOW (success metrics) - measurable outcomes different from #2
4. WHERE/WHEN (context/deployment) - how they'll use it

Make each question unique and avoid similar answers. Include helpful options when relevant.

Return ONLY a JSON array:
[
  {{"prompt": "👥 Who specifically would benefit most from this?", "example": "DevOps engineers troubleshooting production, junior developers learning CLI tools, system administrators managing servers"}},
  {{"prompt": "🎯 What's the main outcome users want?", "example": "Find the right command quickly, understand complex syntax, avoid common mistakes"}},
  {{"prompt": "📊 How will you know users find it valuable?", "options": ["Time saved per task", "Reduced support tickets", "User engagement metrics", "Error reduction"], "help": "Pick measurable success indicators"}},
  {{"prompt": "💻 What's the ideal user experience?", "options": ["Quick web lookup", "Interactive terminal tool", "Mobile reference app", "IDE integration"], "help": "Consider when/where they'd use it"}}
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
        
        # Parse JSON response - strip markdown formatting if present
        try:
            # Clean the content - remove markdown code blocks
            clean_content = content.strip()
            if clean_content.startswith("```json"):
                clean_content = clean_content[7:]  # Remove ```json
            if clean_content.startswith("```"):
                clean_content = clean_content[3:]   # Remove ```
            if clean_content.endswith("```"):
                clean_content = clean_content[:-3]  # Remove closing ```
            clean_content = clean_content.strip()
            
            questions = json.loads(clean_content)
            return questions if isinstance(questions, list) else []
        except json.JSONDecodeError as e:
            # If JSON parsing fails, log the issue for debugging but don't show to user
            print(f"💭 Unable to parse AI response - using fallback questions")
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
            print("💡 Choose from options or enter your own:")
            for i, option in enumerate(question_config["options"], 1):
                print(f"   {i}. {option}")
            print()
        
        # Build prompt with guidance
        prompt_text = question_config['prompt']
        if "options" in question_config:
            prompt_text += f" (1-{len(question_config['options'])} or your own answer)"
        
        # Get user response
        response = input(f"{prompt_text}: ").strip()
        
        # Handle options selection
        if "options" in question_config and response.isdigit():
            option_index = int(response) - 1
            if 0 <= option_index < len(question_config["options"]):
                selected_option = question_config["options"][option_index]
                print(f"✅ Selected: {selected_option}")
                response = selected_option
            else:
                print(f"💡 Using custom answer: {response}")
        
        if not response:
            print("❌ This question needs an answer to continue")
            return _ask_dynamic_question(key, question_config, answers)  # Retry
        
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
        
        # Check if user cancelled or failed during AI setup
        if vendor_config == "cancelled":
            # User pressed Ctrl+C during AI setup - respect that and exit completely
            print("💭 AI setup cancelled - exiting")
            return None
        elif vendor_config == "failed":
            # User failed to provide valid API key after 3 attempts - AI is mandatory
            print("💭 AI consultant setup failed - project cannot continue without valid API key")
            return None
        elif vendor_config == "skip":
            # User chose to exit - AI is mandatory
            return None
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
                else:
                    print("💭 Unable to generate AI questions - using standard fallback")
                    
            except Exception as e:
                print(f"💭 {vendor_config['name']} API call failed: {e}")
                if "401" in str(e):
                    print("🔑 This usually means the API key is invalid or expired")
                elif "429" in str(e):
                    print("⚠️ Rate limit exceeded - try again in a moment")
                elif "timeout" in str(e).lower():
                    print("🌐 Network timeout - check your connection")
                else:
                    print("🔧 Check your API key and network connection")
                print("🚫 AI consultant is required for this project - cannot proceed without working AI")
                return None
    
    # If we get here, LLM is not available but AI is required
    print("\n💭 AI consultant is not available - this project requires AI capabilities")
    return None

def ai_first_consultation(non_interactive: bool = False) -> Dict[str, Any]:
    """Complete AI-driven project consultation from the very beginning"""
    if non_interactive:
        print("❌ AI-first mode requires interactive input")
        return None
    
    print("\n🤖 AI-FIRST PROJECT CONSULTATION")
    print("=" * 50)
    print("💫 Welcome to your personal AI project consultant!")
    print("💡 Let's discover your project together through conversation...")
    print()
    
    # Step 1: AI Setup First (before any project discussion)
    print("🔧 First, let's set up your AI consultant:")
    vendor_setup = prompt_ai_vendor_setup()
    
    if not vendor_setup or vendor_setup in ["cancelled", "failed", "skip"]:
        print("💭 AI consultant is required for AI-first mode")
        return None
    
    vendor_config, api_key = vendor_setup
    ai_name = vendor_config['name']
    
    # Step 2: Open-ended project discovery conversation
    print(f"\n🎯 {ai_name.upper()} PROJECT DISCOVERY CONVERSATION")
    print("=" * 60)
    print(f"💬 Your {ai_name} consultant is ready to help!")
    print()
    
    try:
        # Initial open-ended question
        print("🤔 Let's start with the big picture...")
        project_idea = input("💡 Tell me about your project idea (be as detailed or brief as you like): ").strip()
        
        if not project_idea:
            print("❌ We need some initial idea to work with")
            return None
            
        print(f"\n🧠 {ai_name} is analyzing your idea and preparing personalized guidance...")
        
        # AI analyzes and guides the conversation
        consultation_result = ai_guided_consultation(project_idea, vendor_config, api_key)
        
        if not consultation_result:
            print(f"💭 {ai_name} consultation failed - falling back to standard questions")
            return None
            
        return consultation_result
        
    except KeyboardInterrupt:
        print(f"\n❌ {ai_name} consultation cancelled")
        return None

def ai_guided_consultation(initial_idea: str, vendor_config: Dict, api_key: str) -> Dict[str, Any]:
    """AI guides the entire project consultation conversation"""
    
    consultation_prompt = f"""
You are an expert project consultant. A user has described their project idea: "{initial_idea}"

CRITICAL: Do NOT make assumptions about project type, platform, or architecture. Instead, create clarifying questions to understand what the user actually wants.

Your task is to create an INTERACTIVE consultation and return a JSON response with the following structure:

{{
  "clarifying_questions": [
    {{
      "prompt": "What type of application are you envisioning?",
      "options": ["Web application", "Mobile app", "Desktop app", "CLI tool", "API service", "Something else"],
      "help": "This determines the entire technical approach"
    }},
    {{
      "prompt": "Who will be using this log analyzer?",
      "options": ["App developers", "DevOps engineers", "Support engineers", "System administrators"],
      "help": "Understanding users shapes the interface and features"
    }},
    {{
      "prompt": "How do users currently analyze logs?",
      "options": ["Manual text files", "Basic grep/commands", "Enterprise tools", "No current solution"],
      "help": "This helps us understand the improvement needed"
    }},
    {{
      "prompt": "What's the main pain point you want to solve?",
      "help": "Focus on the core problem - be specific"
    }}
  ],
  "follow_up_questions": [
    {{
      "prompt": "How will you know this project is successful?",
      "options": ["Faster issue detection", "Reduced debug time", "Team adoption", "Better insights"],
      "help": "Define your success metrics early"
    }}
  ],
  "potential_names": ["LogWise", "AppLogAnalyzer", "LogInsight"],
  "next_steps": [
    "Step 1: Clarify project requirements",
    "Step 2: Choose platform and tech stack", 
    "Step 3: Define core features",
    "Step 4: Start with MVP"
  ]
}}

IMPORTANT: Focus on asking clarifying questions rather than making assumptions. The user will answer these questions, then you can provide specific technical recommendations.
"""
    
    try:
        # Generate AI consultation response
        if LLM_AVAILABLE == True:
            # Use full LLM integration
            request = LLMRequest(
                prompt=consultation_prompt,
                system_message="You are an expert project consultant who provides comprehensive, practical guidance."
            )
            llm = LLMAPIIntegration(LLMConfig(provider=LLMProvider[vendor_config["provider"].upper()]))
            response = llm.generate_content(request)
            content = response.content.strip()
        else:
            # Use extended API calls with higher token limits for complex consultation
            messages = [
                {"role": "system", "content": "You are an expert project consultant who provides comprehensive, practical guidance."},
                {"role": "user", "content": consultation_prompt}
            ]
            
            provider = vendor_config["provider"]
            if provider == "openai":
                content = _call_openai_api_extended(api_key, messages, vendor_config["model"])
            elif provider == "anthropic":
                content = _call_anthropic_api_extended(api_key, messages, vendor_config["model"])
            elif provider == "google":
                content = _call_google_api_extended(api_key, messages, vendor_config["model"])
            else:
                raise Exception(f"Unsupported provider: {provider}")
        
        # Parse AI consultation response
        clean_content = content.strip()
        if clean_content.startswith("```json"):
            clean_content = clean_content[7:]
        if clean_content.startswith("```"):
            clean_content = clean_content[3:]
        if clean_content.endswith("```"):
            clean_content = clean_content[:-3]
        clean_content = clean_content.strip()
        
        consultation_data = json.loads(clean_content)
        
        # Present AI analysis and get user feedback
        return present_ai_consultation(consultation_data, vendor_config['name'])
        
    except Exception as e:
        print(f"💭 AI consultation failed: {e}")
        print("🔄 You can try again or contact support if this persists")
        return None

def present_ai_consultation(consultation_data: Dict, ai_name: str) -> Dict[str, Any]:
    """Present AI consultation results and gather user input"""
    
    print(f"\n🤖 {ai_name.upper()} CONSULTATION QUESTIONS")
    print("=" * 50)
    
    answers = {}
    
    # Handle clarifying questions first
    clarifying_questions = consultation_data.get("clarifying_questions", [])
    if clarifying_questions:
        print("🤔 First, let me ask some clarifying questions:")
        print()
        
        for i, question in enumerate(clarifying_questions, 1):
            try:
                if not _ask_dynamic_question(f"clarifying_{i}", question, answers):
                    return None
            except KeyboardInterrupt:
                print("\n❌ AI consultation cancelled")
                return None
        
        print(f"\n💡 Great! Now {ai_name} will analyze your answers and provide recommendations...")
        
        # TODO: Here we could make a second AI call with the user's answers to get specific recommendations
        # For now, let's continue with name selection
    
    # Show suggested names
    suggested_names = consultation_data.get("potential_names", [])
    if suggested_names:
        print(f"\n📝 {ai_name.upper()} SUGGESTS THESE NAMES:")
        for i, name in enumerate(suggested_names[:3], 1):
            print(f"   {i}. {name}")
        print(f"   4. Let me choose my own name")
        print()
        
        try:
            name_choice = input("Choose a name (1-4): ").strip()
            if name_choice in ["1", "2", "3"] and int(name_choice) <= len(suggested_names):
                project_name = suggested_names[int(name_choice) - 1]
            else:
                project_name = input("💭 Enter your preferred project name: ").strip()
        except KeyboardInterrupt:
            print("\n❌ Name selection cancelled")
            return None
            
        if not project_name:
            print("❌ Project name is required")
            return None
    else:
        try:
            project_name = input("📝 What would you like to name this project? ").strip()
        except KeyboardInterrupt:
            print("\n❌ Project naming cancelled")
            return None
        if not project_name:
            return None
    
    # Store core project information
    answers.update({
        "project_goal": f"AI-guided project: {project_name}",
        "ai_consultation": consultation_data,
        "project_name": project_name
    })
    
    # Ask follow-up questions with proper error handling
    follow_up_questions = consultation_data.get("follow_up_questions", [])
    if follow_up_questions:
        print(f"🤖 {ai_name} has some follow-up questions:")
        print()
        
        for i, question in enumerate(follow_up_questions, 1):
            try:
                if not _ask_dynamic_question(f"ai_followup_{i}", question, answers):
                    return None
            except KeyboardInterrupt:
                print("\n❌ Follow-up questions cancelled")
                return None
    
    # Show next steps
    next_steps = consultation_data.get("next_steps", [])
    if next_steps:
        print(f"\n📋 {ai_name.upper()} RECOMMENDED NEXT STEPS:")
        for i, step in enumerate(next_steps, 1):
            print(f"   {i}. {step}")
        print()
    
    print(f"🎉 {ai_name} consultation complete! Your answers will guide the project creation.")
    
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
    
    parser.add_argument("--ai-first", action="store_true",
                       help="🤖 AI-FIRST MODE: Complete AI-driven project consultation from the very beginning")
    
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
    
    # Handle AI-first mode - complete AI-driven consultation
    if args.ai_first:
        if args.non_interactive:
            print("❌ --ai-first mode requires interactive input (cannot be used with --non-interactive)")
            return
        
        print("🚀 WELCOME TO AI-FIRST PROJECT CREATION")
        print("=" * 45)
        print("🤖 Your AI consultant will guide you through the entire process")
        print("💫 From initial idea to complete project specification")
        print()
        
        # Complete AI consultation
        project_context = ai_first_consultation(args.non_interactive)
        
        if not project_context:
            logger.info("❌ AI-first consultation cancelled")
            return
            
        # Extract project name from AI consultation
        project_name = project_context.get("project_name")
        if not project_name:
            print("❌ AI consultation didn't provide a project name")
            return
            
        # Validate project name
        project_name = validate_project_name(project_name)
        logger.info(f"🚀 AI-guided project: {project_name}")
        
        # AI suggests directory (for now, use default - could be enhanced)
        base_dir = Path.home() / "Projects"
        print(f"📁 AI recommends creating project at: {base_dir}/{project_name}/")
        
    else:
        # Standard flow - handle project name prompt
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
    
    if not args.ai_first:
        # Standard flow - validate project name and determine directory
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
                        print("💡 Examples: '/home/user/my-projects' or '~/projects' or '../other-projects'")
                        response = input(f"📂 Parent directory [{default_base}]: ").strip()
                        if response:
                            response_path = Path(response).expanduser()
                            if not response_path.is_absolute():
                                # If it's just the project name (like "clicc"), use default parent
                                if '/' not in response and not response.startswith('.') and response == project_name:
                                    print(f"💡 '{response}' matches project name - using default parent directory")
                                    base_dir = default_base
                                else:
                                    # It's a relative path like ../projects
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
            
        except ValueError as e:
            logger.error(f"❌ {e}")
            return
    
    # Continue with project creation (both AI-first and standard flow reach here)
    # If user cancelled during questions, exit completely
    if project_context is None:
        logger.info("❌ Project initialization cancelled by user")
        return
    
    try:
        
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

