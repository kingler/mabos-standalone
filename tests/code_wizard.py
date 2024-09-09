from pydantic import BaseModel
import json
import os
from typing import List, Dict, Any

from app.agents.core_agents.llm_agent import LLMAgent
from app.services.llm_service import LLMService
from app.services.agent_communication_service import AgentCommunicationService

class CodeEvaluationReport(BaseModel):
    analysis: str
    suggestions: List[str]

class ImprovedCode(BaseModel):
    code: str
    explanation: str

class CodeRatingReport(BaseModel):
    score: float
    feedback: str

class CodeWizardLLMAgent(LLMAgent):
    def __init__(self, agent_id: str, name: str, llm_service: LLMService, agent_communication_service: AgentCommunicationService):
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'llm_config.json')
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        
        api_key = os.environ.get(config['api_keys']['anthropic'])
        super().__init__(agent_id, name, api_key, llm_service, agent_communication_service)

    async def generate_evaluation_report(self, code: str) -> CodeEvaluationReport:
        prompt = f"Evaluate the following code and provide an analysis with suggestions for improvement:\n\n{code}"
        response = await self.generate_response(prompt)
        return CodeEvaluationReport.parse_raw(response)

    async def generate_improved_code(self, code: str, suggestions: List[str]) -> ImprovedCode:
        prompt = f"Improve the following code based on these suggestions:\n\nCode:\n{code}\n\nSuggestions:\n{', '.join(suggestions)}"
        response = await self.generate_response(prompt)
        return ImprovedCode.parse_raw(response)

    async def generate_rating_report(self, code: str) -> CodeRatingReport:
        prompt = f"Rate the following code on a scale of 0 to 10 and provide feedback:\n\n{code}"
        response = await self.generate_response(prompt)
        return CodeRatingReport.parse_raw(response)

class CodeWizard:
    def __init__(self, llm_service: LLMService, agent_communication_service: AgentCommunicationService):
        self.llm_agent = CodeWizardLLMAgent("code_wizard", "Code Wizard", llm_service, agent_communication_service)

    async def optimize_code(self, initial_code: str, max_iterations: int = 5, target_score: float = 9.0) -> str:
        current_code = initial_code
        iterations = 0

        while iterations < max_iterations:
            evaluation_report = await self.llm_agent.generate_evaluation_report(current_code)
            improved_code = await self.llm_agent.generate_improved_code(current_code, evaluation_report.suggestions)
            rating_report = await self.llm_agent.generate_rating_report(improved_code.code)

            print(f"Iteration {iterations + 1}: Score = {rating_report.score}")
            print(f"Feedback: {rating_report.feedback}")

            if rating_report.score >= target_score:
                print("Target score reached!")
                return improved_code.code

            current_code = improved_code.code
            iterations += 1

        print("Max iterations reached.")
        return current_code

# Usage
async def main():
    # You'll need to implement these services
    llm_service = LLMService()
    agent_communication_service = AgentCommunicationService()

    wizard = CodeWizard(llm_service, agent_communication_service)
    initial_code = """
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    """
    optimized_code = await wizard.optimize_code(initial_code)
    print("Optimized Code:")
    print(optimized_code)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())