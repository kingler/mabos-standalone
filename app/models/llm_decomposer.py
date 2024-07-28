import openai
from typing import List
import uuid

from pydantic import BaseModel
from app.models.goal import Goal

class LLMDecomposer:
    """
    A class for decomposing high-level goals into specific, actionable subgoals using a language model.
    """

    def __init__(self, api_key: str):
        """
        Initialize the LLMDecomposer with an API key.

        Args:
            api_key (str): The API key for accessing the language model service.
        """
        self.api_key = api_key
        openai.api_key = self.api_key  # Set the API key for the openai module

    def decompose(self, goal: Goal) -> List[Goal]:
        """
        Decompose a high-level goal into subgoals.

        Args:
            goal (Goal): The high-level goal to decompose.

        Returns:
            List[Goal]: A list of subgoals derived from the main goal.
        """
        prompt = self._create_prompt(goal)
        response = self._get_llm_response(prompt)
        subgoals = self._parse_response(response, goal.priority)
        return subgoals

    def _create_prompt(self, goal: Goal) -> str:
        """
        Create a prompt for the language model to decompose the goal.

        Args:
            goal (Goal): The goal to be decomposed.

        Returns:
            str: The formatted prompt for the language model.
        """
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
        """
        Get a response from the language model.

        Args:
            prompt (str): The prompt to send to the language model.

        Returns:
            str: The response from the language model.

        Raises:
            Exception: If there's an error in getting the LLM response.
        """
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
            raise Exception(f"Error in getting LLM response: {e}")

    def _parse_response(self, response: str, parent_priority: int) -> List[Goal]:
        """
        Parse the LLM response and create subgoals.

        Args:
            response (str): The response from the language model.
            parent_priority (int): The priority of the parent goal.

        Returns:
            List[Goal]: A list of parsed subgoals.
        """
        subgoals = []
        lines = response.split('\n')
        for line in lines:
            if line.strip() and line[0].isdigit():
                description = line.split('.', 1)[1].strip()
                subgoal = Goal(
                    id=str(uuid.uuid4()),
                    description=description,
                    priority=max(1, parent_priority - 1),
                    llm_generated_context="Generated as a subgoal by LLMDecomposer"
                )
                subgoals.append(subgoal)
        return subgoals

    def validate_subgoals(self, main_goal: Goal, subgoals: List[Goal]) -> List[Goal]:
        """
        Validate the generated subgoals against the main goal.

        Args:
            main_goal (Goal): The main goal.
            subgoals (List[Goal]): The list of subgoals to validate.

        Returns:
            List[Goal]: The validated (and possibly modified) list of subgoals.
        """
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

        validation_response = self._get_llm_response(validation_prompt)

        if "All subgoals are valid" in validation_response:
            return subgoals
        else:
            for subgoal in subgoals:
                subgoal.llm_generated_context += f"\nValidation feedback: {validation_response}"
            
            return subgoals

    def decompose_with_validation(self, goal: Goal) -> List[Goal]:
        """
        Decompose a goal into subgoals and validate them.

        Args:
            goal (Goal): The main goal to decompose and validate.

        Returns:
            List[Goal]: A list of validated subgoals.
        """
        initial_subgoals = self.decompose(goal)
        validated_subgoals = self.validate_subgoals(goal, initial_subgoals)
        return validated_subgoals