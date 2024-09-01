import os
import uuid
from typing import Any, Dict, List
import logging

import json
from pydantic import BaseModel, Field
from app.core.models.agent.goal import Goal
from app.core.tools.llm_manager import LLMManager

class LLMDecomposer(BaseModel):
    llm_manager: LLMManager = Field(...)
    config: Dict[str, Any] = Field(default_factory=dict)

    def __init__(self, llm_manager: LLMManager, config_path: str = '/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/config/llm_config.json', **data):
        super().__init__(llm_manager=llm_manager, **data)
        self.config = self.load_config(config_path)

    def load_config(self, config_path: str) -> Dict[str, Any]:
        try:
            with open(config_path, 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            print(f"Config file not found at {config_path}. Using default empty configuration.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {config_path}. Using default empty configuration.")
            return {}

    async def decompose(self, goal: Goal) -> List[Goal]:
        prompt = self._create_prompt(goal)
        response = await self.llm_manager.generate_text(prompt)
        return self._parse_response(response, goal.priority)

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

    def _parse_response(self, response: str, parent_priority: int) -> List[Goal]:
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

        validation_response = self.llm_manager.generate_text(validation_prompt)

        if "All subgoals are valid" not in validation_response:
            for subgoal in subgoals:
                subgoal.llm_generated_context += f"\nValidation feedback: {validation_response}"
        return subgoals

    def decompose_with_validation(self, goal: Goal) -> List[Goal]:
        return self.validate_subgoals(goal, self.decompose(goal))