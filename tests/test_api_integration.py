import pytest
from fastapi.testclient import TestClient
from src.api.main import app
from datetime import datetime, timedelta

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "database_connected" in response.json()

def test_create_goal():
    goal_data = {
        "name": "Increase Sales",
        "description": "Increase total sales by 20% in Q3",
        "target_value": 120000,
        "current_value": 100000,
        "start_date": datetime.now().isoformat(),
        "end_date": (datetime.now() + timedelta(days=90)).isoformat()
    }
    response = client.post("/goals", json=goal_data)
    assert response.status_code == 200
    assert "goal_id" in response.json()
    return response.json()["goal_id"]

def test_get_goal(goal_id):
    response = client.get(f"/goals/{goal_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Increase Sales"
    assert response.json()["status"] == "Not Started"

def test_update_goal(goal_id):
    update_data = {
        "current_value": 110000,
        "status": "In Progress"
    }
    response = client.put(f"/goals/{goal_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Goal updated successfully"

def test_list_goals():
    response = client.get("/goals")
    assert response.status_code == 200
    assert "goals" in response.json()
    assert len(response.json()["goals"]) > 0

def test_update_goal_progress(goal_id):
    response = client.put(f"/goals/{goal_id}/progress", params={"current_value": 115000})
    assert response.status_code == 200
    assert response.json()["message"] == "Goal progress updated successfully"

def test_get_goal_recommendations(goal_id):
    response = client.get(f"/goals/{goal_id}/recommendations")
    assert response.status_code == 200
    assert "recommendations" in response.json()

def test_delete_goal(goal_id):
    response = client.delete(f"/goals/{goal_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Goal deleted successfully"

def test_goal_lifecycle():
    # Create a goal
    goal_id = test_create_goal()

    # Get the created goal
    test_get_goal(goal_id)

    # Update the goal
    test_update_goal(goal_id)

    # List goals
    test_list_goals()

    # Update goal progress
    test_update_goal_progress(goal_id)

    # Get goal recommendations
    test_get_goal_recommendations(goal_id)

    # Delete the goal
    test_delete_goal(goal_id)

    # Verify the goal is deleted
    response = client.get(f"/goals/{goal_id}")
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main()