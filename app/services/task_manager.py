import threading
import uuid
from typing import Dict, List, Optional

from app.models.agent.agent import Agent
from app.models.agent.task import Task


class TaskManager:
    def __init__(self):
        self.tasks: Dict[uuid.UUID, Task] = {}
        self.task_lock = threading.Lock()

    def create_task(self, task_data: dict) -> Task:
        task = Task(**task_data)
        with self.task_lock:
            self.tasks[task.id] = task
        return task

    def get_task(self, task_id: uuid.UUID) -> Optional[Task]:
        return self.tasks.get(task_id)

    def update_task(self, task_id: uuid.UUID, task_data: dict) -> Optional[Task]:
        with self.task_lock:
            if task := self.tasks.get(task_id):
                updated_task = Task(**{**task.dict(), **task_data})
                self.tasks[task_id] = updated_task
                return updated_task
        return None

    def delete_task(self, task_id: uuid.UUID) -> bool:
        with self.task_lock:
            if task_id in self.tasks:
                del self.tasks[task_id]
                return True
        return False

    def assign_task(self, task_id: uuid.UUID, agent: Agent) -> bool:
        with self.task_lock:
            if task := self.tasks.get(task_id):
                task.agent = agent
                return True
        return False

    def execute_task(self, task_id: uuid.UUID) -> Optional[str]:
        if task := self.get_task(task_id):
            return task.execute()
        return None

    def get_agent_tasks(self, agent_id: uuid.UUID) -> List[Task]:
        return [task for task in self.tasks.values() if task.agent and task.agent.id == agent_id]

    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.tasks.values() if task.status == "pending"]

    def check_task_dependencies(self, task: Task) -> bool:
        return all(self.tasks[dep_id].is_completed() for dep_id in task.dependencies if dep_id in self.tasks)

    def process_tasks(self):
        for task in self.get_pending_tasks():
            if self.check_task_dependencies(task) and not task.is_deadline_reached():
                self.execute_task(task.id)