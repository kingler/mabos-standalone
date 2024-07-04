import os
import openai
from typing import List
import uuid

from pydantic import BaseModel
from app.models.goal import Goal

class LLMDecomposer:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def decompose(self, goal: Goal) -> List[Goal]:
        # Prepare the prompt for the LLM
        prompt = self._create_prompt(goal)

        # Get the response from the LLM
        response = self._get_llm_response(prompt)

        # Parse the response and create subgoals
        subgoals = self._parse_response(response, goal.priority)

        return subgoals

    def _create_prompt(self, goal: Goal) -> str:
        return f"""
        Given the following high-level goal:
        
        "{goal.description}"
        
        Please decompose this goal into 3-5 specific, actionable subgoals. Each subgoal should be a clear, concise step towards achieving the main goal. Format your response as a numbered list, with each subgoal on a new line.
        
        For example:
        1. [Subgoal 1 description]
        2. [Subgoal 2 description]
        3. [Subgoal 3 description]
        ...
        
        Please provide the subgoals now:
        """

    def _get_llm_response(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI assistant tasked with decomposing high-level goals into specific, actionable subgoals."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                n=1,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error in getting LLM response: {e}")
            return ""

    def _parse_response(self, response: str, parent_priority: int) -> List[Goal]:
        subgoals = []
        lines = response.split('\n')
        for line in lines:
            if line.strip() and line[0].isdigit():
                # Remove the number and any leading/trailing whitespace
                description = line.split('.', 1)[1].strip()
                subgoal = Goal(
                    id=str(uuid.uuid4()),
                    description=description,
                    priority=max(1, parent_priority - 1),  # Subgoals have slightly lower priority than parent
                    llm_generated_context="Generated as a subgoal by LLMDecomposer"
                )
                subgoals.append(subgoal)
        return subgoals

    def validate_subgoals(self, main_goal: Goal, subgoals: List[Goal]) -> List[Goal]:
        # Prepare the prompt for validation
        subgoal_descriptions = "\n".join([f"{i+1}. {sg.description}" for i, sg in enumerate(subgoals)])
        validation_prompt = f"""
        Main Goal: {main_goal.description}
        
        Subgoals:
        {subgoal_descriptions}
        
        Please validate these subgoals. Ensure they are:
        1. Relevant to the main goal
        2. Specific and actionable
        3. Collectively comprehensive in achieving the main goal
        
        If any subgoals do not meet these criteria, please suggest improvements or replacements. 
        If all subgoals are valid, simply respond with "All subgoals are valid."
        
        Your response:
        """

        # Get the validation response from the LLM
        validation_response = self._get_llm_response(validation_prompt)

        if "All subgoals are valid" in validation_response:
            return subgoals
        else:
            # If there are suggestions, you might want to process them here
            # For now, we'll just add the suggestions as context to the subgoals
            for subgoal in subgoals:
                subgoal.llm_generated_context += f"\nValidation feedback: {validation_response}"
            
            return subgoals

    def decompose_with_validation(self, goal: Goal) -> List[Goal]:
        initial_subgoals = self.decompose(goal)
        validated_subgoals = self.validate_subgoals(goal, initial_subgoals)
        return validated_subgoals