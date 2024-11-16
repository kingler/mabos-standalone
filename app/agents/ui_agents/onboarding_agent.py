"""Agent responsible for conducting the onboarding process for new businesses."""
from typing import Any, Dict, Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict
import logging
import re

from app.agents.core_agents.llm_agent import LLMAgent
from app.services.erp_service import ERPService
from app.services.mabos_service import MABOSService
from app.db.arango_db_client import ArangoDBClient
from app.models.knowledge.question_models import Question, Answer

class OnboardingState(BaseModel):
    """Track the state of the onboarding process."""
    business_name: Optional[str] = None
    industry: Optional[str] = None
    employee_count: Optional[int] = None
    current_question_id: Optional[UUID] = None
    business_id: Optional[UUID] = None
    completed_steps: List[str] = Field(default_factory=list)

class OnboardingAgent(BaseModel):
    """Agent responsible for conducting the onboarding process for new businesses."""

    llm_agent: LLMAgent
    db_client: ArangoDBClient
    erp_service: ERPService
    mabos_service: MABOSService
    state: OnboardingState = Field(default_factory=OnboardingState)
    _test_mode: bool = False
    _test_input: list[str] = []

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def create(cls, llm_agent: LLMAgent, db_client: ArangoDBClient, erp_service: ERPService, mabos_service: MABOSService) -> 'OnboardingAgent':
        return cls(
            llm_agent=llm_agent,
            db_client=db_client,
            erp_service=erp_service,
            mabos_service=mabos_service
        )

    async def conduct_onboarding(self, user_input: str) -> str:
        """Main method to conduct the onboarding process."""
        try:
            # Process the input through LLM for understanding
            processed_input = await self.llm_agent.process_message(user_input)
            
            # Handle the input based on current state
            return await self.handle_user_input(processed_input)
            
        except Exception as e:
            logging.error(f"Error in conduct_onboarding: {str(e)}")
            return f"I apologize, but I encountered an error: {str(e)}"

    async def handle_user_input(self, user_input: str) -> str:
        """Handle user input and generate appropriate responses."""
        try:
            # If this is the first interaction, start onboarding
            if self._is_initial_interaction(user_input):
                return await self._start_onboarding()
            
            # Store the user's response
            await self._store_onboarding_data(user_input)
            
            # Get the next question or action
            return await self._get_next_step()
            
        except ValueError as e:
            # Handle validation errors gracefully
            logging.error(f"Validation error: {str(e)}")
            return str(e)
        except Exception as e:
            logging.error(f"Error handling user input: {str(e)}")
            return f"I apologize, but I encountered an error: {str(e)}"

    def _is_initial_interaction(self, processed_input: str) -> bool:
        """Determine if this is the first interaction in the onboarding process."""
        if not self.state.completed_steps:
            greetings = ['hello', 'hi', 'start', 'begin', 'help']
            return any(greeting in processed_input.lower() for greeting in greetings)
        return False

    async def _start_onboarding(self) -> str:
        """Start the onboarding process."""
        # Initialize or reset the onboarding state
        self.state = OnboardingState(
            business_id=uuid4()  # Generate a new business ID at the start
        )
        
        # Create initial question in database
        question = Question(
            category="General",
            framework="Onboarding",
            text="What is your business name?"
        )
        
        try:
            # Store the question in the database
            collection = self.db_client.db.collection('questions')
            collection.insert(question.dict())
            
            # Store the question ID in the state
            self.state.current_question_id = question.id
            
            return """Welcome to the MABOS business onboarding process! 
            
I'll help you set up your business system by gathering some information. Let's start with the basics:

What is your business name?"""
            
        except Exception as e:
            logging.error(f"Error starting onboarding: {str(e)}")
            return "I apologize, but I encountered an error starting the onboarding process. Please try again."

    def _extract_number(self, text: str) -> Optional[int]:
        """Extract a number from text, handling various formats."""
        # Remove any non-digit characters
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])
        return None

    async def _store_onboarding_data(self, processed_input: str) -> None:
        """Store processed input in the appropriate context."""
        try:
            if not self.state.business_name:
                self.state.business_name = processed_input
                self.state.completed_steps.append('business_name')
            elif not self.state.industry:
                self.state.industry = processed_input
                self.state.completed_steps.append('industry')
            elif not self.state.employee_count:
                # Try to extract a number from the input
                employee_count = self._extract_number(processed_input)
                if employee_count is None:
                    raise ValueError("Please provide a valid number for employee count (must be a positive integer).")
                if employee_count < 1:
                    raise ValueError("Employee count must be at least 1.")
                self.state.employee_count = employee_count
                self.state.completed_steps.append('employee_count')
            
            # Store the answer in the database
            if self.state.current_question_id and self.state.business_id:
                answer = Answer(
                    question_id=self.state.current_question_id,
                    text=processed_input,
                    business_id=self.state.business_id
                )
                
                collection = self.db_client.db.collection('answers')
                collection.insert(answer.dict())
            
        except ValueError as e:
            # Re-raise validation errors to be handled by the caller
            raise
        except Exception as e:
            logging.error(f"Error storing onboarding data: {str(e)}")
            raise

    async def _get_next_step(self) -> str:
        """Determine and return the next step in the onboarding process."""
        try:
            if 'business_name' not in self.state.completed_steps:
                return "What is your business name?"
            elif 'industry' not in self.state.completed_steps:
                return "What industry does your business operate in?"
            elif 'employee_count' not in self.state.completed_steps:
                return "How many employees does your business have? (Please enter a number)"
            else:
                # Create the business profile
                await self.mabos_service.create_agent({
                    'name': self.state.business_name,
                    'type': 'business',
                    'industry': self.state.industry,
                    'employee_count': self.state.employee_count
                }, {})
                
                return f"""Thank you for providing your business information! I've created a profile for {self.state.business_name}.
                
Your business has been successfully onboarded. You can now start using the MABOS system."""
                
        except Exception as e:
            logging.error(f"Error getting next step: {str(e)}")
            return "I apologize, but I encountered an error. Please try again."
