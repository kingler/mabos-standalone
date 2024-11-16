import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.mabos_service import MABOSService
from app.models.business.business_model import BusinessModel
from app.models.goal import Goal
from app.models.rule import Rule
from app.models.business.business_plan import BusinessPlan
from app.models.agent import Agent
from app.models.business.erp_models import ERPModule

client = TestClient(app)
mabos_service = MABOSService()

@pytest.fixture
def authenticated_client():
    login_data = {
        "username": "testuser",
        "password": "securepassword123"
    }
    login_response = client.post("/api/users/login", data=login_data)
    token = login_response.json()["access_token"]
    return TestClient(app, headers={"Authorization": f"Bearer {token}"})

def test_business_model_to_erp_integration(authenticated_client):
    # Create a business model
    business_model_data = {
        "name": "TechInnovate Solutions",
        "industry": "Software",
        "description": "AI-powered software for SMBs",
        "business_architecture": {
            "key_activities": ["Software Development", "AI Research", "Customer Support"],
            "value_propositions": ["Affordable AI Solutions", "Increased Efficiency"],
            "customer_segments": ["Small Businesses", "Medium Enterprises"]
        }
    }
    response = authenticated_client.post("/api/business-models", json=business_model_data)
    assert response.status_code == 201
    business_model_id = response.json()["id"]

    # Generate ERP modules based on the business model
    response = authenticated_client.post(f"/api/business-models/{business_model_id}/generate-erp-modules")
    assert response.status_code == 201
    erp_modules = response.json()["modules"]

    # Verify that appropriate ERP modules were generated
    module_names = [module["name"] for module in erp_modules]
    assert "Finance" in module_names
    assert "CRM" in module_names
    assert "Human Resources" in module_names
    assert "Project Management" in module_names

    # Verify that ERP modules reflect the business model
    for module in erp_modules:
        if module["name"] == "CRM":
            assert "Small Businesses" in module["features"]
            assert "Medium Enterprises" in module["features"]

def test_goal_to_agent_task_integration(authenticated_client):
    # Create a business model
    business_model_response = authenticated_client.post("/api/business-models", json={"name": "Test Model"})
    business_model_id = business_model_response.json()["id"]

    # Create a goal
    goal_data = {
        "name": "Increase Market Share",
        "description": "Expand market share by 10% in the next quarter",
        "category": "Growth",
        "kpis": ["Market Share Percentage", "New Customer Acquisition Rate"]
    }
    goal_response = authenticated_client.post(f"/api/business-models/{business_model_id}/goals", json=goal_data)
    assert goal_response.status_code == 201
    goal_id = goal_response.json()["id"]

    # Verify that agents are assigned tasks based on the goal
    response = authenticated_client.get(f"/api/agents/tasks")
    assert response.status_code == 200
    tasks = response.json()["tasks"]

    goal_related_tasks = [task for task in tasks if task["related_goal_id"] == goal_id]
    assert len(goal_related_tasks) > 0
    
    # Verify that tasks are appropriate for the goal
    task_names = [task["name"] for task in goal_related_tasks]
    assert any("market analysis" in name.lower() for name in task_names)
    assert any("customer acquisition" in name.lower() for name in task_names)

def test_rule_enforcement_in_agent_actions(authenticated_client):
    # Create a business rule
    rule_data = {
        "type": "OperativeRule",
        "statement": "All customer data must be encrypted at rest",
        "enforcement_level": "Strict"
    }
    rule_response = authenticated_client.post("/api/rules", json=rule_data)
    assert rule_response.status_code == 201
    rule_id = rule_response.json()["id"]

    # Simulate an agent action that would violate the rule
    action_data = {
        "agent_id": "test_agent",
        "action": "store_customer_data",
        "parameters": {"encryption": False}
    }
    action_response = authenticated_client.post("/api/agents/actions", json=action_data)
    assert action_response.status_code == 403
    assert "rule violation" in action_response.json()["detail"].lower()

    # Simulate an agent action that complies with the rule
    compliant_action_data = {
        "agent_id": "test_agent",
        "action": "store_customer_data",
        "parameters": {"encryption": True}
    }
    compliant_response = authenticated_client.post("/api/agents/actions", json=compliant_action_data)
    assert compliant_response.status_code == 200

def test_business_plan_to_financial_projection_integration(authenticated_client):
    # Create a business plan
    business_plan_data = {
        "name": "TechInnovate Growth Plan",
        "revenue_model": "SaaS",
        "pricing_strategy": "Tiered Pricing",
        "target_market_size": 1000000,
        "expected_market_penetration": 0.05
    }
    plan_response = authenticated_client.post("/api/business-plans", json=business_plan_data)
    assert plan_response.status_code == 201
    plan_id = plan_response.json()["id"]

    # Generate financial projections based on the business plan
    projection_response = authenticated_client.post(f"/api/business-plans/{plan_id}/financial-projections")
    assert projection_response.status_code == 201
    projections = projection_response.json()["projections"]

    # Verify that projections are consistent with the business plan
    assert "revenue" in projections
    assert "expenses" in projections
    assert "cash_flow" in projections

    # Check if the revenue projection aligns with the target market and penetration
    expected_customers = business_plan_data["target_market_size"] * business_plan_data["expected_market_penetration"]
    assert abs(projections["revenue"]["year_1"] / expected_customers - 100) < 20  # Allowing for some variation

def test_agent_collaboration_on_business_task(authenticated_client):
    # Create a complex business task
    task_data = {
        "name": "Develop New Product Strategy",
        "description": "Create a comprehensive strategy for our next flagship product",
        "required_skills": ["market_analysis", "product_development", "financial_planning"]
    }
    task_response = authenticated_client.post("/api/tasks", json=task_data)
    assert task_response.status_code == 201
    task_id = task_response.json()["id"]

    # Trigger agent collaboration on the task
    collab_response = authenticated_client.post(f"/api/tasks/{task_id}/collaborate")
    assert collab_response.status_code == 200
    collaboration_result = collab_response.json()

    # Verify that multiple agents contributed to the task
    assert len(collaboration_result["contributing_agents"]) >= 3
    
    # Check that the collaboration output covers all required aspects
    assert "market_analysis" in collaboration_result["output"]
    assert "product_features" in collaboration_result["output"]
    assert "financial_projections" in collaboration_result["output"]

    # Verify that the agents' actions were logged
    logs_response = authenticated_client.get(f"/api/tasks/{task_id}/logs")
    assert logs_response.status_code == 200
    action_logs = logs_response.json()["logs"]
    assert len(action_logs) > 0
    assert all(log["task_id"] == task_id for log in action_logs)

if __name__ == "__main__":
    pytest.main([__file__])


