"""Terminal interface for interacting with the MABOS OnboardingAgent."""
from typing import Optional
from colorama import init, Fore, Style
from app.agents.ui_agents.onboarding_agent import OnboardingAgent
from app.agents.core_agents.llm_agent import LLMAgent
from app.services.mabos_service import MABOSService
from app.db.arango_db_client import ArangoDBClient
from app.services.erp_service import ERPService

class TerminalInterface:
    """Handles terminal-based interaction with the MABOS OnboardingAgent."""
    
    def __init__(self, db_client: ArangoDBClient, erp_service: ERPService, mabos_service: MABOSService):
        """Initialize the terminal interface with required services.
        
        Args:
            db_client: Database client for ArangoDB
            erp_service: ERP service instance
            mabos_service: MABOS service instance
        """
        # Initialize colorama for cross-platform color support
        init()
        
        # Create LLM agent using factory method
        self.llm_agent = LLMAgent.create()
        
        # Create onboarding agent using factory method
        self.onboarding_agent = OnboardingAgent.create(
            llm_agent=self.llm_agent,
            db_client=db_client,
            erp_service=erp_service,
            mabos_service=mabos_service
        )
        
        self.mabos_service = mabos_service
        
    def print_agent_message(self, message: str) -> None:
        """Print agent messages in blue color.
        
        Args:
            message: The message to print
        """
        print(f"\n{Fore.BLUE}MABOS: {message}{Style.RESET_ALL}")
        
    def print_user_prompt(self) -> str:
        """Print user prompt in green color and get input.
        
        Returns:
            The user's input string
        """
        return input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
        
    def print_error(self, error: str) -> None:
        """Print error messages in red color.
        
        Args:
            error: The error message to print
        """
        print(f"\n{Fore.RED}Error: {error}{Style.RESET_ALL}")
        
    async def start_conversation(self) -> None:
        """Start the conversation loop with the user."""
        try:
            # Initialize MABOS service
            await self.mabos_service.initialize()
            
            self.print_agent_message("Welcome to MABOS! I'm your onboarding assistant.")
            self.print_agent_message("I'll help you set up your business system. Type 'exit' at any time to end the conversation.")
            
            while True:
                try:
                    user_input = self.print_user_prompt()
                    
                    if user_input.lower() == 'exit':
                        self.print_agent_message("Thank you for using MABOS. Goodbye!")
                        break
                    
                    if not user_input:
                        self.print_error("Please enter a message.")
                        continue
                        
                    # Process user input through LLM for natural language understanding
                    processed_input = await self.llm_agent.process_message(user_input)
                    
                    # Get response from onboarding agent
                    response = await self.onboarding_agent.conduct_onboarding(processed_input)
                    
                    self.print_agent_message(response)
                    
                except KeyboardInterrupt:
                    self.print_agent_message("\nConversation terminated by user. Goodbye!")
                    break
                except Exception as e:
                    self.print_error(f"An unexpected error occurred: {str(e)}")
                    self.print_error("Please try again or type 'exit' to end the conversation.")
        except Exception as e:
            self.print_error(f"Failed to initialize MABOS service: {str(e)}")
            self.print_error("Please try restarting the application.")
