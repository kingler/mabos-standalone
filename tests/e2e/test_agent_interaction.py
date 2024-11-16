import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.mabos_service import MABOSService
from app.models.agent import Agent
from app.models.message import Message

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

def test_agent_creation(authenticated_client):
    agent_data = {
        "name": "TestAgent",
        "type": "BusinessAgent",
        "capabilities": ["market_analysis", "financial_planning"]
    }
    response = authenticated_client.post("/api/agents", json=agent_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == agent_data["name"]

def test_agent_communication(authenticated_client):
    # Create two agents
    agent1_data = {"name": "Agent1", "type": "BusinessAgent"}
    agent2_data = {"name": "Agent2", "type": "FinancialAgent"}
    agent1_response = authenticated_client.post("/api/agents", json=agent1_data)
    agent2_response = authenticated_client.post("/api/agents", json=agent2_data)
    
    agent1_id = agent1_response.json()["id"]
    agent2_id = agent2_response.json()["id"]

    # Send a message from Agent1 to Agent2
    message_data = {
        "sender_id": agent1_id,
        "receiver_id": agent2_id,
        "content": "Hello from Agent1",
        "type": "INFORM"
    }
    response = authenticated_client.post("/api/messages", json=message_data)
    assert response.status_code == 201

    # Check if Agent2 received the message
    messages_response = authenticated_client.get(f"/api/agents/{agent2_id}/messages")
    assert messages_response.status_code == 200
    assert len(messages_response.json()) > 0
    assert messages_response.json()[0]["content"] == message_data["content"]

def test_agent_collaboration(authenticated_client):
    # Create a business plan
    business_plan_data = {
        "name": "Collaboration Test Business",
        "industry": "Technology",
        "description": "A test business for agent collaboration"
    }
    business_plan_response = authenticated_client.post("/api/business-plans", json=business_plan_data)
    business_plan_id = business_plan_response.json()["id"]

    # Create multiple agents for collaboration
    agents = []
    for agent_type in ["MarketAnalysisAgent", "FinancialPlanningAgent", "OperationsAgent"]:
        agent_data = {"name": f"Test{agent_type}", "type": agent_type}
        agent_response = authenticated_client.post("/api/agents", json=agent_data)
        agents.append(agent_response.json())

    # Trigger collaboration on the business plan
    collaboration_data = {
        "business_plan_id": business_plan_id,
        "agent_ids": [agent["id"] for agent in agents]
    }
    response = authenticated_client.post("/api/agents/collaborate", json=collaboration_data)
    assert response.status_code == 200

    # Check the results of the collaboration
    results = response.json()
    assert "market_analysis" in results
    assert "financial_projections" in results
    assert "operational_recommendations" in results
