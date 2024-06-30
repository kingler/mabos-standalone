from fastapi import FastAPI
from app.routers import agent_router, goal_router, plan_router, knowledge_base_router
from app.routers import actions
from app.routers import tasks
from app.routers import planning
from app.routers import communication

app = FastAPI()

app.include_router(agent_router)
app.include_router(goal_router)
app.include_router(plan_router)
app.include_router(knowledge_base_router)
app.include_router(actions.router, prefix="/api/v1", tags=["actions"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(planning.router, prefix="/api/v1/planning", tags=["planning"])
app.include_router(communication.router, prefix="/api/v1/communication", tags=["communication"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)