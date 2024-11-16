"""LLM Agent for handling natural language processing tasks."""
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, ConfigDict

from app.services.llm_service import LLMService
from app.tools.llm_manager import LLMManager

class LLMAgent(BaseModel):
    """Agent responsible for natural language processing and LLM interactions."""

    llm_manager: Optional[LLMManager] = None
    llm_service: Optional[LLMService] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def create(cls, llm_manager: Optional[LLMManager] = None) -> 'LLMAgent':
        """Create a new LLMAgent instance.
        
        Args:
            llm_manager: Optional LLMManager instance. If not provided, a new one will be created.
            
        Returns:
            A new LLMAgent instance
        """
        # Create LLMManager if not provided
        if not llm_manager:
            llm_manager = LLMManager()
            
        # Create LLMService
        llm_service = LLMService(llm_manager=llm_manager)
        
        # Create and return LLMAgent instance
        return cls(
            llm_manager=llm_manager,
            llm_service=llm_service
        )

    async def process_message(self, message: str) -> str:
        """Process incoming messages using LLM capabilities.
        
        Args:
            message: The input message to process
            
        Returns:
            Processed response from the LLM
        """
        try:
            # For now, just return a simple response
            # In production, this would use the LLM service
            if "hello" in message.lower() or "hi" in message.lower():
                return "Hello! I'm here to help you with the onboarding process."
            return "I understand. Please tell me more about your business."
            
        except Exception as e:
            return f"Error processing message: {str(e)}"

    async def generate_business_description(self, business_data: Dict[str, Any]) -> str:
        """Generate a business description from provided data.
        
        Args:
            business_data: Dictionary containing business information
            
        Returns:
            Generated business description
        """
        try:
            # For now, return a template-based description
            # In production, this would use the LLM service
            return f"""Business Description:
            
{business_data.get('your_business_name', 'Unknown')} is a company in the {business_data.get('your_business_industry', 'Unknown')} industry.
They offer {business_data.get('main_products_services', 'various products and services')}.
Their target market consists of {business_data.get('target_market', 'various customers')}.
"""
        except Exception as e:
            return f"Error generating business description: {str(e)}"
