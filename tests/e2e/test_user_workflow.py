import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.mabos_service import MABOSService
from app.models.business_model import BusinessModel
from app.models.erp_module import ERPModule

client = TestClient(app)
mabos_service = MABOSService()

def test_user_registration():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword123"
    }
    response = client.post("/api/users/register", json=user_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["username"] == user_data["username"]

def test_business_plan_creation():
    # First, login to get the authentication token
    login_data = {
        "username": "testuser",
        "password": "securepassword123"
    }
    login_response = client.post("/api/users/login", data=login_data)
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    # Create a business plan
    business_plan_data = {
        "name": "Test Business",
        "industry": "Technology",
        "description": "A test business for e2e testing",
        "target_market": "Small businesses",
        "revenue_model": "SaaS"
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/business-plans", json=business_plan_data, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == business_plan_data["name"]

def test_erp_module_generation():
    # Login and get the token
    login_data = {
        "username": "testuser",
        "password": "securepassword123"
    }
    login_response = client.post("/api/users/login", data=login_data)
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get the business plan ID (assuming it's the first one for this user)
    business_plans_response = client.get("/api/business-plans", headers=headers)
    assert business_plans_response.status_code == 200
    business_plan_id = business_plans_response.json()[0]["id"]

    # Generate ERP modules
    erp_generation_data = {
        "business_plan_id": business_plan_id,
        "modules": ["finance", "inventory", "crm"]
    }
    response = client.post("/api/erp/generate", json=erp_generation_data, headers=headers)
    assert response.status_code == 201
    assert "modules" in response.json()
    assert len(response.json()["modules"]) == 3

    # Verify that the modules were created
    for module in response.json()["modules"]:
        module_response = client.get(f"/api/erp/modules/{module['id']}", headers=headers)
        assert module_response.status_code == 200
        assert module_response.json()["name"] in erp_generation_data["modules"]