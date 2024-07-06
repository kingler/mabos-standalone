from fastapi import FastAPI
from app.routers.agents import router as agent_router
from app.routers.goals import router as goal_router
from app.routers.plans import router as plan_router
from app.routers.knowledge_bases import router as knowledge_base_router
from app.routers import actions, tasks, planning, communication
from app.routers import version_control
from app.routers.ontology import router as ontology_router
from app.routers.rules_engine import router as rules_engine_router
from app.routers.agent_roles import router as agent_roles_router
from app.routers.intentions import router as intentions_router
from app.routers.organization import router as organization_router
from app.routers.environment import router as environment_router
# from app.routers.world_model_router import router as world_model_router

app = FastAPI()

app.include_router(agent_router, prefix="/api/v1/agents", tags=["agents"])
app.include_router(goal_router, prefix="/api/v1/goals", tags=["goals"])
app.include_router(plan_router, prefix="/api/v1/plans", tags=["plans"])
app.include_router(knowledge_base_router, prefix="/api/v1/knowledge_bases", tags=["knowledge_bases"])
app.include_router(actions.router, prefix="/api/v1", tags=["actions"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
app.include_router(planning.router, prefix="/api/v1/planning", tags=["planning"])
app.include_router(communication.router, prefix="/api/v1/communication", tags=["communication"])
app.include_router(version_control.router, prefix="/api/v1/vc", tags=["Version Control"])
app.include_router(ontology_router, prefix="/ontology", tags=["ontology"])
app.include_router(rules_engine_router, prefix="/rule_engine", tags=["rules_engine"])
app.include_router(agent_roles_router, prefix="/agent_roles", tags=["agent_roles"])
app.include_router(intentions_router, prefix="/intentions", tags=["intentions"])
app.include_router(organization_router, prefix="/organization", tags=["organization"])
app.include_router(environment_router, prefix="/environment", tags=["environment"])
# app.include_router(world_model_router, prefix="/world_model", tags=["world_model"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)