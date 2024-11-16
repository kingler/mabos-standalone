import pytest
from unittest.mock import patch
from arango.exceptions import DocumentInsertError
from app.models.project_graph import ProjectGraph

@pytest.fixture
def mock_db():
    with patch('app.models.project_graph.ArangoClient') as MockClient:
        yield MockClient.return_value.db.return_value

@pytest.fixture
def project_graph(mock_db):
    return ProjectGraph('localhost', 8529, 'root', 'password', 'test_db')

@pytest.mark.parametrize("problem_id, problem_type, description", [
    ("1", "type1", "description1"),
    ("2", "type2", "description2"),
    ("3", "type3", "description3"),
], ids=["case1", "case2", "case3"])
def test_add_reasoning_problem(project_graph, mock_db, problem_id, problem_type, description):
    mock_collection = mock_db.collection.return_value
    project_graph.add_reasoning_problem(problem_id, problem_type, description)
    mock_collection.insert.assert_called_once_with({
        '_key': problem_id,
        'type': problem_type,
        'description': description
    })

@pytest.mark.parametrize("problem_id, solution_id, method_used, description", [
    ("1", "sol1", "method1", "description1"),
    ("2", "sol2", "method2", "description2"),
    ("3", "sol3", "method3", "description3"),
], ids=["case1", "case2", "case3"])
def test_add_reasoning_solution(project_graph, mock_db, problem_id, solution_id, method_used, description):
    mock_collection = mock_db.collection.return_value
    project_graph.add_reasoning_solution(problem_id, solution_id, method_used, description)
    mock_collection.insert.assert_called_once_with({
        '_key': solution_id,
        'problem_id': problem_id,
        'method': method_used,
        'description': description
    })

@pytest.mark.parametrize("problem_type, expected_result", [
    ("type1", [{"method": "method1", "usage": 1, "avg_effectiveness": 0.9}]),
    ("type2", [{"method": "method2", "usage": 2, "avg_effectiveness": 0.8}]),
], ids=["case1", "case2"])
def test_query_reasoning_effectiveness(project_graph, mock_db, problem_type, expected_result):
    mock_db.aql.execute.return_value = expected_result
    result = project_graph.query_reasoning_effectiveness(problem_type)
    assert result == expected_result
    mock_db.aql.execute.assert_called_once()

@pytest.mark.parametrize("problem_id, problem_type, description", [
    ("1", "type1", "description1"),
], ids=["error_case"])
def test_add_reasoning_problem_error(project_graph, mock_db, problem_id, problem_type, description):
    mock_collection = mock_db.collection.return_value
    mock_collection.insert.side_effect = DocumentInsertError
    with pytest.raises(DocumentInsertError):
        project_graph.add_reasoning_problem(problem_id, problem_type, description)

@pytest.mark.parametrize("problem_id, solution_id, method_used, description", [
    ("1", "sol1", "method1", "description1"),
], ids=["error_case"])
def test_add_reasoning_solution_error(project_graph, mock_db, problem_id, solution_id, method_used, description):
    mock_collection = mock_db.collection.return_value
    mock_collection.insert.side_effect = DocumentInsertError
    with pytest.raises(DocumentInsertError):
        project_graph.add_reasoning_solution(problem_id, solution_id, method_used, description)