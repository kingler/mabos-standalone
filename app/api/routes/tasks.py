from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.models.agent.task import Task
from app.core.services.agent_service import AgentService
from app.core.services.task_manager import TaskManager

router = APIRouter()

def get_task_manager():
    return TaskManager()

def get_agent_service():
    return AgentService()

@router.post("/tasks/", response_model=Task)
async def create_task(task_data: dict, task_manager: TaskManager = Depends(get_task_manager)):
    return task_manager.create_task(task_data)

@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: UUID, task_manager: TaskManager = Depends(get_task_manager)):
    if task := task_manager.get_task(task_id):
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, task_data: dict, task_manager: TaskManager = Depends(get_task_manager)):
    if task := task_manager.update_task(task_id, task_data):
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: UUID, task_manager: TaskManager = Depends(get_task_manager)):
    if task_manager.delete_task(task_id):
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/tasks/{task_id}/assign/{agent_id}")
async def assign_task(
    task_id: UUID, 
    agent_id: UUID, 
    task_manager: TaskManager = Depends(get_task_manager),
    agent_service: AgentService = Depends(get_agent_service)
):
    agent = agent_service.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    if task_manager.assign_task(task_id, agent):
        return {"message": "Task assigned successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/tasks/{task_id}/execute")
async def execute_task(task_id: UUID, task_manager: TaskManager = Depends(get_task_manager)):
    result = task_manager.execute_task(task_id)
    if result is not None:
        return {"message": "Task executed successfully", "result": result}
    raise HTTPException(status_code=404, detail="Task not found or execution failed")

@router.get("/agents/{agent_id}/tasks", response_model=List[Task])
async def get_agent_tasks(
    agent_id: UUID,
    task_manager: TaskManager = Depends(get_task_manager),
    agent_service: AgentService = Depends(get_agent_service)
):
    if not agent_service.get_agent(agent_id):
        raise HTTPException(status_code=404, detail="Agent not found")
    return task_manager.get_agent_tasks(agent_id)

@router.get("/tasks/pending", response_model=List[Task])
async def get_pending_tasks(task_manager: TaskManager = Depends(get_task_manager)):
    return task_manager.get_pending_tasks()

@router.post("/tasks/process")
async def process_tasks(task_manager: TaskManager = Depends(get_task_manager)):
    task_manager.process_tasks()
    return {"message": "Tasks processed successfully"}