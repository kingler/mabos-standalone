from fastapi import APIRouter, HTTPException
from app.core.services.rule_engine_service import RuleEngineService
from app.core.services.agent_role_service import AgentRolesService

router = APIRouter()  # Added this line

@router.get("/rules")
def get_rules():
    return RuleEngineService.get_all_rules()

@router.post("/rules")
def create_rule(rule: dict):
    return RuleEngineService.create_rule(rule)

@router.post("/execute")
def execute_rule_engine(context: dict):
    return RuleEngineService.execute(context)

@router.get("/agent_roles")
def get_agent_roles():
    return AgentRolesService.get_all_roles()
