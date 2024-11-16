import asyncio
import pytest
from unittest.mock import Mock, AsyncMock, PropertyMock
from owlready2 import World
from app.models.knowledge.knowledge_graph import EnhancedKnowledgeGraph, KnowledgeInference
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.models.knowledge.ontology.ontology import Ontology
from app.models.knowledge.ontology.domain_ontology_generator import DomainOntologyGenerator
from app.tools.llm_manager import LLMManager
from app.db.arango_db_client import ArangoDBClient

@pytest.fixture
def db_client():
    # Mock ArangoDBClient
    mock_client = Mock(spec=ArangoDBClient)
    mock_client.insert_business_goal = AsyncMock()
    mock_client.get_business_goal = AsyncMock(return_value={"id": "test_goal", "name": "Test Goal"})
    mock_client.update_business_goal = AsyncMock()
    mock_client.delete_business_goal = AsyncMock()
    return mock_client

@pytest.fixture
def llm_manager():
    # Mock LLMManager
    mock_manager = Mock(spec=LLMManager)
    
    # Set up different responses for different calls
    async def mock_get_structured_output(prompt, output_schema):
        if "Validate the following inference" in prompt:
            return {"is_valid": True, "confidence": 0.9}
        else:
            return [
                KnowledgeInference(
                    source_nodes=["node1", "node2"],
                    inference_type="logical",
                    inferred_fact="Test inference",
                    confidence=0.9,
                    reasoning_chain=["step1", "step2"]
                )
            ]
    
    mock_manager.get_structured_output = AsyncMock(side_effect=mock_get_structured_output)
    mock_manager.get_text_completion = AsyncMock(return_value="Test explanation")
    return mock_manager

@pytest.fixture
def knowledge_base():
    mock_kb = Mock(spec=KnowledgeBase)
    mock_kb.ontology = Mock()
    mock_kb.ontology.to_json = Mock(return_value='{"test": "ontology"}')
    return mock_kb

@pytest.fixture
def mock_ontology():
    mock = Mock(spec=Ontology)
    mock.concepts = {
        "TestConcept": {"description": "A test concept"},
        "AnotherConcept": {"description": "Another test concept"}
    }
    mock.relationships = {
        "hasRelation": {"domain": "TestConcept", "range": "AnotherConcept"}
    }
    return mock

@pytest.fixture
def ontology_generator(llm_manager, mock_ontology):
    mock_generator = Mock(spec=DomainOntologyGenerator)
    mock_generator.generate_domain_ontology = AsyncMock(return_value=mock_ontology)
    mock_generator.validate_domain_ontology = AsyncMock(return_value={"is_valid": True})
    return mock_generator

@pytest.fixture
def enhanced_graph(db_client, llm_manager, ontology_generator, knowledge_base):
    return EnhancedKnowledgeGraph(
        db_client=db_client,
        llm_manager=llm_manager,
        ontology_generator=ontology_generator,
        knowledge_base=knowledge_base
    )

@pytest.mark.asyncio
async def test_knowledge_inference(enhanced_graph):
    # Test context
    context = {
        "business_idea": "Online Bookstore",
        "product_service": "Digital and physical books",
        "target_market": "Book readers worldwide"
    }
    
    # Test inference
    inferences = await enhanced_graph.infer_knowledge(context)
    assert len(inferences) > 0
    
    # Validate first inference
    first_inference = inferences[0]
    assert isinstance(first_inference, KnowledgeInference)
    assert first_inference.confidence >= 0 and first_inference.confidence <= 1
    assert len(first_inference.reasoning_chain) > 0
    
    # Test inference validation
    validation = await enhanced_graph.validate_inference(first_inference)
    assert "is_valid" in validation
    assert validation["is_valid"] is True
    
    # Test inference explanation
    explanation = await enhanced_graph.explain_inference(str(first_inference.id))
    assert len(explanation) > 0

@pytest.mark.asyncio
async def test_ontology_generation(enhanced_graph, mock_ontology):
    # Test data
    user_data = {
        "business_idea": "Online Bookstore",
        "product_service": "Digital and physical books",
        "user_id": "test_user_1",
        "stakeholders": [
            {"id": "1", "role": "owner"},
            {"id": "2", "role": "manager"}
        ]
    }
    
    # Generate ontology
    ontology = await enhanced_graph.generate_domain_ontology(user_data)
    assert ontology is not None
    
    # Validate ontology
    validation = await enhanced_graph.validate_ontology(ontology)
    assert validation["is_valid"]
    
    # Test ontology merging
    enhanced_graph.merge_ontology(mock_ontology)
    
    # Verify merged concepts
    node_data = enhanced_graph.get_node("TestConcept")
    assert node_data is not None

@pytest.mark.asyncio
async def test_graph_operations(enhanced_graph):
    # Test node operations
    test_data = {"property": "value"}
    enhanced_graph.add_node("test_node", test_data)
    node_data = enhanced_graph.get_node("test_node")
    assert test_data["property"] == node_data["property"]
    
    # Test edge operations
    enhanced_graph.add_edge("test_node", "related_node", {"relation": "connects_to"})
    neighbors = enhanced_graph.get_neighbors("test_node")
    assert "related_node" in neighbors

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--asyncio-mode=strict"])
