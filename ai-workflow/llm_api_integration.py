#!/usr/bin/env python3

"""
🤖 Universal LLM API Integration System
Provides seamless integration with multiple LLM providers for true workflow automation
"""

import json
import os
import sys
import argparse
import logging
import time
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
from enum import Enum
import openai
from anthropic import Anthropic

class LLMProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    AZURE_OPENAI = "azure_openai"
    LOCAL_OLLAMA = "local_ollama"
    GROQ = "groq"
    GOOGLE = "google"

@dataclass
class LLMConfig:
    provider: LLMProvider
    model: str
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    max_tokens: int = 4000
    temperature: float = 0.7
    timeout: int = 60
    max_retries: int = 3
    cost_limit_usd: float = 10.0

@dataclass
class LLMRequest:
    prompt: str
    system_prompt: Optional[str] = None
    context_data: Optional[Dict[str, Any]] = None
    expected_format: str = "markdown"
    validation_criteria: Optional[List[str]] = None

@dataclass
class LLMResponse:
    content: str
    provider: str
    model: str
    tokens_used: int
    cost_usd: float
    execution_time: float
    validated: bool = False
    validation_errors: List[str] = None

class LLMAPIIntegration:
    """Universal LLM API integration for workflow automation"""
    
    def __init__(self, config: LLMConfig, debug: bool = False):
        self.config = config
        self.debug = debug
        self.logger = self._setup_logging()
        self.usage_tracker = {"total_tokens": 0, "total_cost_usd": 0.0}
        
        # Initialize API client based on provider
        self.client = self._initialize_client()
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger('llm_api_integration')
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
    
    def _initialize_client(self):
        """Initialize LLM API client based on provider"""
        
        if self.config.provider == LLMProvider.OPENAI:
            if not self.config.api_key:
                self.config.api_key = os.getenv('OPENAI_API_KEY')
            if not self.config.api_key:
                raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable.")
            
            # Use OpenAI v1.x client
            from openai import OpenAI
            return OpenAI(
                api_key=self.config.api_key,
                base_url=self.config.base_url
            )
            
        elif self.config.provider == LLMProvider.ANTHROPIC:
            if not self.config.api_key:
                self.config.api_key = os.getenv('ANTHROPIC_API_KEY')
            if not self.config.api_key:
                raise ValueError("Anthropic API key required. Set ANTHROPIC_API_KEY environment variable.")
            
            return Anthropic(api_key=self.config.api_key)
            
        elif self.config.provider == LLMProvider.AZURE_OPENAI:
            if not self.config.api_key:
                self.config.api_key = os.getenv('AZURE_OPENAI_API_KEY')
            if not self.config.base_url:
                self.config.base_url = os.getenv('AZURE_OPENAI_ENDPOINT')
            
            from openai import AzureOpenAI
            return AzureOpenAI(
                api_key=self.config.api_key,
                azure_endpoint=self.config.base_url,
                api_version="2023-12-01-preview"
            )
            
        elif self.config.provider == LLMProvider.LOCAL_OLLAMA:
            if not self.config.base_url:
                self.config.base_url = "http://localhost:11434"
            return None  # Use requests directly
            
        elif self.config.provider == LLMProvider.GROQ:
            if not self.config.api_key:
                self.config.api_key = os.getenv('GROQ_API_KEY')
            if not self.config.base_url:
                self.config.base_url = "https://api.groq.com/openai/v1"
            
            from openai import OpenAI
            return OpenAI(
                api_key=self.config.api_key,
                base_url=self.config.base_url
            )
            
        elif self.config.provider == LLMProvider.GOOGLE:
            if not self.config.api_key:
                self.config.api_key = os.getenv('GOOGLE_API_KEY')
            if not self.config.api_key:
                raise ValueError("Google API key required. Set GOOGLE_API_KEY environment variable.")
            
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.config.api_key)
                return genai
            except ImportError:
                raise ValueError("Google GenerativeAI package required. Install with: pip install google-generativeai")
    
    def generate_content(self, request: LLMRequest) -> LLMResponse:
        """Generate content using configured LLM provider"""
        
        self.logger.info(f"🤖 Generating content with {self.config.provider.value} ({self.config.model})")
        
        # Check cost limits
        if self.usage_tracker["total_cost_usd"] >= self.config.cost_limit_usd:
            raise RuntimeError(f"Cost limit exceeded: ${self.usage_tracker['total_cost_usd']:.2f} >= ${self.config.cost_limit_usd}")
        
        start_time = time.time()
        
        for attempt in range(self.config.max_retries):
            try:
                # Generate content based on provider
                if self.config.provider == LLMProvider.OPENAI:
                    response = self._generate_openai(request)
                elif self.config.provider == LLMProvider.ANTHROPIC:
                    response = self._generate_anthropic(request)
                elif self.config.provider == LLMProvider.AZURE_OPENAI:
                    response = self._generate_azure_openai(request)
                elif self.config.provider == LLMProvider.LOCAL_OLLAMA:
                    response = self._generate_ollama(request)
                elif self.config.provider == LLMProvider.GROQ:
                    response = self._generate_groq(request)
                elif self.config.provider == LLMProvider.GOOGLE:
                    response = self._generate_google(request)
                else:
                    raise ValueError(f"Unsupported provider: {self.config.provider}")
                
                # Calculate execution time
                execution_time = time.time() - start_time
                
                # Update usage tracking
                self.usage_tracker["total_tokens"] += response.tokens_used
                self.usage_tracker["total_cost_usd"] += response.cost_usd
                
                # Validate response if criteria provided
                if request.validation_criteria:
                    response = self._validate_response(response, request.validation_criteria)
                
                self.logger.info(f"✅ Content generated successfully ({response.tokens_used} tokens, ${response.cost_usd:.4f})")
                return response
                
            except Exception as e:
                self.logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == self.config.max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
    
    def _generate_openai(self, request: LLMRequest) -> LLMResponse:
        """Generate content using OpenAI API"""
        
        messages = []
        if request.system_prompt:
            messages.append({"role": "system", "content": request.system_prompt})
        
        # Add context data if provided
        user_content = request.prompt
        if request.context_data:
            user_content += f"\n\nContext Data:\n```json\n{json.dumps(request.context_data, indent=2)}\n```"
        
        messages.append({"role": "user", "content": user_content})
        
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=messages,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            timeout=self.config.timeout
        )
        
        content = response.choices[0].message.content
        tokens_used = response.usage.total_tokens
        cost_usd = self._calculate_openai_cost(tokens_used, self.config.model)
        
        return LLMResponse(
            content=content,
            provider=self.config.provider.value,
            model=self.config.model,
            tokens_used=tokens_used,
            cost_usd=cost_usd,
            execution_time=0  # Will be set by caller
        )
    
    def _generate_anthropic(self, request: LLMRequest) -> LLMResponse:
        """Generate content using Anthropic API"""
        
        # Prepare prompt
        full_prompt = request.prompt
        if request.context_data:
            full_prompt += f"\n\nContext Data:\n```json\n{json.dumps(request.context_data, indent=2)}\n```"
        
        response = self.client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=request.system_prompt or "You are a helpful AI assistant.",
            messages=[{"role": "user", "content": full_prompt}]
        )
        
        content = response.content[0].text
        tokens_used = response.usage.input_tokens + response.usage.output_tokens
        cost_usd = self._calculate_anthropic_cost(tokens_used, self.config.model)
        
        return LLMResponse(
            content=content,
            provider=self.config.provider.value,
            model=self.config.model,
            tokens_used=tokens_used,
            cost_usd=cost_usd,
            execution_time=0
        )
    
    def _generate_azure_openai(self, request: LLMRequest) -> LLMResponse:
        """Generate content using Azure OpenAI API"""
        # Similar to OpenAI but with Azure-specific configuration
        return self._generate_openai(request)
    
    def _generate_ollama(self, request: LLMRequest) -> LLMResponse:
        """Generate content using local Ollama API"""
        
        url = f"{self.config.base_url}/api/generate"
        
        # Prepare prompt
        full_prompt = request.prompt
        if request.system_prompt:
            full_prompt = f"System: {request.system_prompt}\n\nUser: {full_prompt}"
        if request.context_data:
            full_prompt += f"\n\nContext Data:\n```json\n{json.dumps(request.context_data, indent=2)}\n```"
        
        payload = {
            "model": self.config.model,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": self.config.temperature,
                "num_predict": self.config.max_tokens
            }
        }
        
        response = requests.post(url, json=payload, timeout=self.config.timeout)
        response.raise_for_status()
        
        result = response.json()
        content = result.get("response", "")
        
        # Estimate tokens (rough approximation)
        tokens_used = len(content.split()) * 1.3  # Rough token estimation
        cost_usd = 0.0  # Local models are free
        
        return LLMResponse(
            content=content,
            provider=self.config.provider.value,
            model=self.config.model,
            tokens_used=int(tokens_used),
            cost_usd=cost_usd,
            execution_time=0
        )
    
    def _generate_groq(self, request: LLMRequest) -> LLMResponse:
        """Generate content using Groq API"""
        # Similar to OpenAI but with Groq-specific pricing
        response = self._generate_openai(request)
        # Adjust cost calculation for Groq pricing
        response.cost_usd = self._calculate_groq_cost(response.tokens_used, self.config.model)
        return response
    
    def _generate_google(self, request: LLMRequest) -> LLMResponse:
        """Generate content using Google Gemini API"""
        
        # Create model instance
        model = self.client.GenerativeModel(self.config.model)
        
        # Prepare prompt
        full_prompt = request.prompt
        if request.system_prompt:
            full_prompt = f"System: {request.system_prompt}\n\nUser: {full_prompt}"
        if request.context_data:
            full_prompt += f"\n\nContext Data:\n```json\n{json.dumps(request.context_data, indent=2)}\n```"
        
        # Configure generation
        generation_config = {
            'temperature': self.config.temperature,
            'max_output_tokens': self.config.max_tokens,
        }
        
        response = model.generate_content(
            full_prompt,
            generation_config=generation_config
        )
        
        content = response.text
        
        # Estimate tokens (rough approximation)
        tokens_used = len(content.split()) * 1.3  # Rough token estimation
        cost_usd = self._calculate_google_cost(tokens_used, self.config.model)
        
        return LLMResponse(
            content=content,
            provider=self.config.provider.value,
            model=self.config.model,
            tokens_used=int(tokens_used),
            cost_usd=cost_usd,
            execution_time=0
        )
    
    def _calculate_openai_cost(self, tokens: int, model: str) -> float:
        """Calculate approximate cost for OpenAI models"""
        cost_per_1k_tokens = {
            "gpt-4": 0.03,
            "gpt-4-turbo": 0.01,
            "gpt-3.5-turbo": 0.002,
            "gpt-3.5-turbo-16k": 0.004
        }
        
        rate = cost_per_1k_tokens.get(model, 0.01)  # Default rate
        return (tokens / 1000) * rate
    
    def _calculate_anthropic_cost(self, tokens: int, model: str) -> float:
        """Calculate approximate cost for Anthropic models"""
        cost_per_1k_tokens = {
            "claude-3-opus-20240229": 0.015,
            "claude-3-sonnet-20240229": 0.003,
            "claude-3-haiku-20240307": 0.00025,
            "claude-3-5-sonnet-20241022": 0.003
        }
        
        rate = cost_per_1k_tokens.get(model, 0.003)  # Default rate
        return (tokens / 1000) * rate
    
    def _calculate_groq_cost(self, tokens: int, model: str) -> float:
        """Calculate approximate cost for Groq models"""
        # Groq often has very competitive pricing
        cost_per_1k_tokens = {
            "llama2-70b-4096": 0.0007,
            "mixtral-8x7b-32768": 0.0006,
            "gemma-7b-it": 0.0001
        }
        
        rate = cost_per_1k_tokens.get(model, 0.0005)  # Default rate
        return (tokens / 1000) * rate
    
    def _calculate_google_cost(self, tokens: int, model: str) -> float:
        """Calculate approximate cost for Google Gemini models"""
        cost_per_1k_tokens = {
            "gemini-pro": 0.0005,
            "gemini-pro-vision": 0.0025,
            "gemini-1.5-pro": 0.0035,
            "gemini-1.5-flash": 0.000075
        }
        
        rate = cost_per_1k_tokens.get(model, 0.0005)  # Default rate
        return (tokens / 1000) * rate
    
    def _validate_response(self, response: LLMResponse, criteria: List[str]) -> LLMResponse:
        """Validate response against criteria"""
        
        validation_errors = []
        
        for criterion in criteria:
            if criterion.lower() == "not_empty" and not response.content.strip():
                validation_errors.append("Content is empty")
            elif criterion.lower() == "contains_markdown" and not any(marker in response.content for marker in ["#", "*", "`", "-"]):
                validation_errors.append("Content does not contain markdown formatting")
            elif criterion.startswith("min_length:"):
                min_length = int(criterion.split(":")[1])
                if len(response.content) < min_length:
                    validation_errors.append(f"Content too short (< {min_length} characters)")
            elif criterion.startswith("contains:"):
                required_text = criterion.split(":", 1)[1]
                if required_text.lower() not in response.content.lower():
                    validation_errors.append(f"Content does not contain required text: {required_text}")
        
        response.validated = len(validation_errors) == 0
        response.validation_errors = validation_errors
        
        if not response.validated:
            self.logger.warning(f"Response validation failed: {validation_errors}")
        
        return response
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """Get current usage statistics"""
        return {
            "total_tokens": self.usage_tracker["total_tokens"],
            "total_cost_usd": round(self.usage_tracker["total_cost_usd"], 4),
            "cost_limit_usd": self.config.cost_limit_usd,
            "remaining_budget_usd": round(self.config.cost_limit_usd - self.usage_tracker["total_cost_usd"], 4),
            "provider": self.config.provider.value,
            "model": self.config.model
        }

def load_llm_config(config_path: Optional[Path] = None) -> LLMConfig:
    """Load LLM configuration from file or environment"""
    
    if config_path and config_path.exists():
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        
        return LLMConfig(
            provider=LLMProvider(config_data.get("provider", "openai")),
            model=config_data.get("model", "gpt-3.5-turbo"),
            api_key=config_data.get("api_key"),
            base_url=config_data.get("base_url"),
            max_tokens=config_data.get("max_tokens", 4000),
            temperature=config_data.get("temperature", 0.7),
            timeout=config_data.get("timeout", 60),
            max_retries=config_data.get("max_retries", 3),
            cost_limit_usd=config_data.get("cost_limit_usd", 10.0)
        )
    
    # Default configuration from environment
    provider = os.getenv('LLM_PROVIDER', 'openai')
    model = os.getenv('LLM_MODEL', 'gpt-3.5-turbo')
    
    return LLMConfig(
        provider=LLMProvider(provider),
        model=model,
        max_tokens=int(os.getenv('LLM_MAX_TOKENS', '4000')),
        temperature=float(os.getenv('LLM_TEMPERATURE', '0.7')),
        cost_limit_usd=float(os.getenv('LLM_COST_LIMIT', '10.0'))
    )

def main():
    """Main entry point for LLM API integration testing"""
    parser = argparse.ArgumentParser(
        description="🤖 Universal LLM API Integration System"
    )
    
    parser.add_argument("--provider", 
                       choices=[p.value for p in LLMProvider],
                       default="openai",
                       help="LLM provider to use")
    
    parser.add_argument("--model",
                       default="gpt-3.5-turbo",
                       help="Model to use")
    
    parser.add_argument("--prompt",
                       required=True,
                       help="Prompt to send to LLM")
    
    parser.add_argument("--system-prompt",
                       help="System prompt")
    
    parser.add_argument("--config",
                       type=Path,
                       help="Path to LLM configuration file")
    
    parser.add_argument("--debug",
                       action="store_true",
                       help="Enable debug logging")
    
    args = parser.parse_args()
    
    try:
        # Load configuration
        config = load_llm_config(args.config)
        config.provider = LLMProvider(args.provider)
        config.model = args.model
        
        # Initialize LLM integration
        llm = LLMAPIIntegration(config, debug=args.debug)
        
        # Create request
        request = LLMRequest(
            prompt=args.prompt,
            system_prompt=args.system_prompt,
            validation_criteria=["not_empty", "min_length:10"]
        )
        
        # Generate content
        response = llm.generate_content(request)
        
        # Display results
        print(f"\n🤖 LLM Response:")
        print(f"Provider: {response.provider}")
        print(f"Model: {response.model}")
        print(f"Tokens: {response.tokens_used}")
        print(f"Cost: ${response.cost_usd:.4f}")
        print(f"Validated: {response.validated}")
        print(f"\nContent:\n{response.content}")
        
        # Show usage stats
        stats = llm.get_usage_stats()
        print(f"\nUsage Stats: {stats}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
