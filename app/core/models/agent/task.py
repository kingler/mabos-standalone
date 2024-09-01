import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import UUID4, BaseModel, Field


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
    action_id: str = Field(description="ID of the action associated with this task")
    context: Optional[List[UUID4]] = Field(description="IDs of other tasks that will have their output used as context for this task", default=None)
    config: Optional[Dict[str, Any]] = Field(description="Configuration for the task", default=None)
    status: str = Field(default="pending", description="Current status of the task")
    output: Optional[TaskOutput] = Field(description="Task output, its final result after being executed", default=None)
    deadline: Optional[datetime] = Field(description="Deadline for the task", default=None)
    priority: int = Field(default=0, description="Priority of the task")
    dependencies: List[UUID4] = Field(default_factory=list, description="List of task IDs that this task depends on")

    def execute(self, execute_action) -> Optional[str]:
        self.status = "in_progress"
        if result := execute_action(self.action_id):
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
        return self.deadline and datetime.now() > self.deadline

    def update_status(self, new_status: str):
        self.status = new_status

Task.model_rebuild()