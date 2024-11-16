import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.mabos_service import MABOSService
from app.models.business_model import BusinessModel
from app.models.goal import Goal
from app.models.rule import Rule
from app.models.business_plan import BusinessPlan

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

def test_end_to_end_business_onboarding(authenticated_client):
    # Step 1: Submit business description
    business_description = """
    TechInnovate Solutions develops cutting-edge AI-powered software for small to medium-sized businesses. 
    Our flagship product is an intelligent CRM system that provides predictive analytics and automated workflow optimization.
    We aim to revolutionize how SMBs operate by providing enterprise-level AI capabilities at an affordable price point.
    """
    response = authenticated_client.post("/api/onboarding/description", json={"description": business_description})
    assert response.status_code == 202
    job_id = response.json()["job_id"]

    # Step 2: Generate Business Model
    response = authenticated_client.get(f"/api/onboarding/status/{job_id}")
    assert response.status_code == 200
    while response.json()["status"] != "completed":
        response = authenticated_client.get(f"/api/onboarding/status/{job_id}")
    
    business_model_id = response.json()["result"]["business_model_id"]
    response = authenticated_client.get(f"/api/business-models/{business_model_id}")
    assert response.status_code == 200
    business_model = response.json()
    
    assert "Business Architecture" in business_model
    assert "Data Architecture" in business_model
    assert "Application Architecture" in business_model
    assert "Technology Architecture" in business_model
    assert "SBVR Vocabulary" in business_model
    assert "SBVR Business Rules" in business_model

    # Step 3: Generate Initial Goals
    response = authenticated_client.post(f"/api/business-models/{business_model_id}/generate-goals")
    assert response.status_code == 201
    goals = response.json()["goals"]
    
    assert len(goals) > 0
    for goal in goals:
        assert "name" in goal
        assert "description" in goal
        assert "category" in goal
        assert "kpis" in goal
        assert "alignment" in goal

    # Step 4: Generate Business Rules
    response = authenticated_client.post(f"/api/business-models/{business_model_id}/generate-rules")
    assert response.status_code == 201
    rules = response.json()["rules"]
    
    assert len(rules) > 0
    for rule in rules:
        assert "id" in rule
        assert "type" in rule
        assert "statement" in rule
        assert "related_goals" in rule
        assert "enforcement_level" in rule

    # Step 5: Generate Business Plan
    response = authenticated_client.post(f"/api/business-models/{business_model_id}/generate-plan")
    assert response.status_code == 201
    business_plan = response.json()["business_plan"]
    
    assert "executive_summary" in business_plan
    assert "company_description" in business_plan
    assert "market_analysis" in business_plan
    assert "organization_and_management" in business_plan
    assert "service_or_product_line" in business_plan
    assert "marketing_and_sales_strategy" in business_plan
    assert "financial_projections" in business_plan
    assert "appendix" in business_plan

    # Step 6: Verify Multi-Agent System Creation
    response = authenticated_client.get(f"/api/business-models/{business_model_id}/mas")
    assert response.status_code == 200
    mas = response.json()["multi_agent_system"]
    
    assert "agents" in mas
    assert len(mas["agents"]) > 0
    for agent in mas["agents"]:
        assert "id" in agent
        assert "type" in agent
        assert "beliefs" in agent
        assert "desires" in agent
        assert "intentions" in agent

    # Step 7: Verify Alignment Between Components
    for rule in rules:
        assert any(goal["name"] in rule["related_goals"] for goal in goals)

    for goal in goals:
        assert any(goal["name"] in business_plan["appendix"])

    print("End-to-end business onboarding test passed successfully!")

def test_business_model_update_propagation(authenticated_client):
    # Get an existing business model
    response = authenticated_client.get("/api/business-models")
    assert response.status_code == 200
    business_model_id = response.json()[0]["id"]

    # Update the business model
    update_data = {
        "Business Architecture": {
            "target_market": "Expanded to include medium-sized enterprises"
        }
    }
    response = authenticated_client.patch(f"/api/business-models/{business_model_id}", json=update_data)
    assert response.status_code == 200

    # Verify that goals are updated
    response = authenticated_client.get(f"/api/business-models/{business_model_id}/goals")
    assert response.status_code == 200
    updated_goals = response.json()["goals"]
    assert any("medium-sized enterprises" in goal["description"] for goal in updated_goals)

    # Verify that rules are updated
    response = authenticated_client.get(f"/api/business-models/{business_model_id}/rules")
    assert response.status_code == 200
    updated_rules = response.json()["rules"]
    assert any("medium-sized enterprises" in rule["statement"] for rule in updated_rules)

    # Verify that the business plan is updated
    response = authenticated_client.get(f"/api/business-models/{business_model_id}/business-plan")
    assert response.status_code == 200
    updated_plan = response.json()["business_plan"]
    assert "medium-sized enterprises" in updated_plan["market_analysis"]

    print("Business model update propagation test passed successfully!")

if __name__ == "__main__":
    pytest.main([__file__])