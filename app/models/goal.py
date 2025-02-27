from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional, Dict

class SoftGoal(BaseModel):
    id: str
    description: str
    contribution: str  # e.g., "positive", "negative"

class Goal(BaseModel):
    """
    Represents a goal in the multi-agent business operating system.

    Attributes:
        id (str): The unique identifier of the goal.
        description (str): A description of the goal.
        priority (int): The priority level of the goal.
        status (str): The current status of the goal.
        subgoals (List[str]): A list of subgoals associated with the goal.
        llm_generated_context (Optional[str]): Additional context generated by the language model.
        is_achieved (bool): Indicates whether the goal has been achieved.
        metadata (Dict[str, any]): Additional metadata associated with the goal.
        parent_goal (Optional['Goal']): The parent goal of the current goal.
        child_goals (List['Goal']): A list of child goals associated with the current goal.
        soft_goals (List[SoftGoal]): A list of soft goals associated with the goal.
        contributions (Dict[str, float]): Contributions to parent goals.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: str = Field(..., description="The unique identifier of the goal")
    description: str = Field(..., description="A description of the goal")
    priority: int = Field(..., description="The priority level of the goal")
    status: str = Field(..., description="The current status of the goal")
    subgoals: List[str] = Field(default_factory=list, description="A list of subgoals associated with the goal")
    llm_generated_context: Optional[str] = Field(default=None, description="Additional context generated by the language model")
    is_achieved: bool = Field(default=False, description="Indicates whether the goal has been achieved")
    metadata: Dict[str, any] = Field(default_factory=dict, description="Additional metadata associated with the goal")
    parent_goal: Optional['Goal'] = Field(default=None, description="The parent goal of the current goal")
    child_goals: List['Goal'] = Field(default_factory=list, description="A list of child goals associated with the current goal")
    soft_goals: List[SoftGoal] = Field(default_factory=list, description="A list of soft goals associated with the goal")
    contributions: Dict[str, float] = Field(default_factory=dict, description="Contributions to parent goals")

    def decompose(self, llm_decomposer, sub_goals: List['Goal']):
        """
        Decomposes the goal into subgoals using the provided language model decomposer.

        Args:
            llm_decomposer: The language model decomposer used to decompose the goal.
            sub_goals (List['Goal']): A list of subgoals to be added as child goals.
        """
        self.subgoals = llm_decomposer.decompose(self)
        self.child_goals.extend(sub_goals)
        self.validate_subgoals()
        for sub_goal in sub_goals:
            sub_goal.parent_goal = self

    def validate_subgoals(self):
        """
        Validates the subgoals associated with the goal.

        Raises:
            TypeError: If the subgoals are not a list or if any subgoal is not a string.
            ValueError: If any subgoal is empty or whitespace, or if there are no subgoals.
        """
        if not isinstance(self.subgoals, list):
            raise TypeError("Subgoals must be a list")
        
        for subgoal in self.subgoals:
            if not isinstance(subgoal, str):
                raise TypeError("Each subgoal must be a string")
            
            if len(subgoal.strip()) == 0:
                raise ValueError("Subgoals cannot be empty or whitespace")
        
        if len(self.subgoals) == 0:
            raise ValueError("Goal must have at least one subgoal")

    def update_status(self, is_achieved: bool):
        """
        Updates the achievement status of the goal.

        Args:
            is_achieved (bool): Indicates whether the goal has been achieved.
        """
        self.is_achieved = is_achieved

    def add_metadata(self, key: str, value: any):
        """
        Adds metadata to the goal.

        Args:
            key (str): The key of the metadata.
            value (any): The value of the metadata.
        """
        self.metadata[key] = value
        
    def add_soft_goal(self, soft_goal: SoftGoal):
        self.soft_goals.append(soft_goal)

    def update_contribution(self, parent_goal_id: str, contribution: float):
        self.contributions[parent_goal_id] = contribution

    def propagate_changes(self):
        for child_goal in self.child_goals:
            child_goal.update_contribution(self.id, self.contributions.get(child_goal.id, 0))
            child_goal.propagate_changes()
