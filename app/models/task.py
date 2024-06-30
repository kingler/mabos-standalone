from pydantic import BaseModel, Field, UUID4
from typing import Optional, List, Any, Dict
from datetime import datetime
import uuid
from .action import Action
from .agent import Agent

class TaskOutput(BaseModel):
    description: str = Field(description="Description of the task")
    summary: Optional[str] = Field(description="Summary of the task", default=None)
    exported_output: Any = Field(description="Output of the task", default=None)
    raw_output: str = Field(description="Result of the task")

    def result(self):
        return self.exported_output

class Task(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, description="Unique identifier for the task")
    description: str = Field(description="Description of the actual task")
    expected_output: str = Field(description="Clear definition of expected output for the task")
    action: Action = Field(description="Action associated with this task")
    agent: Optional[Agent] = Field(description="Agent responsible for executing the task", default=None)
    context: Optional[List["Task"]] = Field(description="Other tasks that will have their output used as context for this task", default=None)
    config: Optional[Dict[str, Any]] = Field(description="Configuration for the task", default=None)
    status: str = Field(default="pending", description="Current status of the task")
    output: Optional[TaskOutput] = Field(description="Task output, its final result after being executed", default=None)
    deadline: Optional[datetime] = Field(description="Deadline for the task", default=None)
    priority: int = Field(default=0, description="Priority of the task")
    dependencies: List[UUID4] = Field(default_factory=list, description="List of task IDs that this task depends on")

    def execute(self, agent: Optional[Agent] = None) -> Optional[str]:
        agent = agent or self.agent
        if not agent:
            raise ValueError("No agent assigned to execute this task")
        
        self.status = "in_progress"
        result = self.action.execute(agent)
        
        if result:
            self.status = "completed"
            self.output = TaskOutput(
                description=self.description,
                exported_output=result,
                raw_output=str(result)
            )
            return result
        else:
            self.status = "failed"
            return None

    def is_completed(self) -> bool:
        return self.status == "completed"

    def is_deadline_reached(self) -> bool:
        if self.deadline:
            return datetime.now() > self.deadline
        return False

    def update_status(self, new_status: str):
        self.status = new_status