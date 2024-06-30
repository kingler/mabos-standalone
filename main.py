from fastapi import FastAPI
from app.routers import agent_router, goal_router, plan_router, knowledge_base_router

app = FastAPI()

app.include_router(agent_router)
app.include_router(goal_router)
app.include_router(plan_router)
app.include_router(knowledge_base_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)