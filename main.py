from fastapi import FastAPI
from app.routers import agents as agent_router
from app.routers import goals as goal_router
from app.routers import plans as plan_router
from app.routers import knowledge_bases as knowledge_base_router
from app.routers import actions, tasks, planning, communication
from app.routers import mas_router
from app.routers import version_control

app = FastAPI()

app.include_router(agent_router.router, prefix="/api/v1/agents", tags=["agents"])
app.include_router(goal_router.router, prefix="/api/v1/goals", tags=["goals"])
app.include_router(plan_router.router, prefix="/api/v1/plans", tags=["plans"])
app.include_router(knowledge_base_router.router, prefix="/api/v1/knowledge_bases", tags=["knowledge_bases"])
app.include_router(actions.router, prefix="/api/v1", tags=["actions"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(planning.router, prefix="/api/v1/planning", tags=["planning"])
app.include_router(communication.router, prefix="/api/v1/communication", tags=["communication"])
app.include_router(mas_router.router, prefix="/api/v1", tags=["MAS"])
app.include_router(version_control.router, prefix="/api/v1/vc", tags=["Version Control"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)