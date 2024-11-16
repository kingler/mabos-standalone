import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.ontology_reasoner import OntologyReasoner
from app.models.rules.rules import Rules
from app.tools.reasoner import Reasoner, ReasoningStrategy
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.models.agent import Belief, Desire, Intention
from app.tools.llm_manager import LLMManager

class TestReasoningEngine(unittest.TestCase):
    def setUp(self):
        self.mock_knowledge_base = MagicMock(spec=KnowledgeBase)
        self.reasoning_engine = ReasoningEngine(self.mock_knowledge_base, "test_api_key")

    @patch('app.tools.reasoning_engine.Reasoner')
    async def test_reason(self, mock_reasoner):
        mock_reasoner.return_value.update_beliefs = AsyncMock(return_value=[Belief(id="1", content="test belief")])
        context = {"facts": [{"subject": "test", "predicate": "is", "object": "example"}]}
        result = await self.reasoning_engine.reason(context)
        self.assertIn("test", result)
        mock_reasoner.return_value.update_beliefs.assert_called_once()

    @patch('app.tools.reasoning_engine.Reasoner')
    async def test_simulate_action(self, mock_reasoner):
        mock_reasoner.return_value.llm_decomposer.query = AsyncMock(return_value='{"updated": "state"}')
        result = await self.reasoning_engine.simulate_action("test_action", {"initial": "state"})
        self.assertEqual(result, {"updated": "state"})

    @patch('app.tools.reasoning_engine.Reasoner')
    async def test_generate_plan(self, mock_reasoner):
        mock_reasoner.return_value.select_intentions = AsyncMock(return_value=[Intention(id="1", plan_id="test_plan")])
        result = await self.reasoning_engine.generate_plan("test_goal", {"initial": "state"})
        self.assertEqual(result, ["test_plan"])

class TestOntologyReasoner(unittest.TestCase):
    def setUp(self):
        self.mock_llm_manager = MagicMock(spec=LLMManager)
        self.mock_ontology = MagicMock()
        self.ontology_reasoner = OntologyReasoner(self.mock_llm_manager, self.mock_ontology)

    async def test_infer_new_knowledge(self):
        self.mock_llm_manager.generate_text = AsyncMock(return_value="New inferred knowledge")
        result = await self.ontology_reasoner.infer_new_knowledge()
        self.assertEqual(result, "New inferred knowledge")
        self.mock_llm_manager.generate_text.assert_called_once()

    async def test_answer_query(self):
        self.mock_llm_manager.generate_text = AsyncMock(return_value="Query answer")
        result = await self.ontology_reasoner.answer_query("test query")
        self.assertEqual(result, "Query answer")
        self.mock_llm_manager.generate_text.assert_called_once()

class TestRules(unittest.TestCase):
    def setUp(self):
        self.rules = Rules()

    def test_add_rule(self):
        mock_rule = MagicMock()
        self.rules.add_rule(mock_rule)
        self.assertIn(mock_rule, self.rules.rules)

    def test_remove_rule(self):
        mock_rule = MagicMock()
        self.rules.add_rule(mock_rule)
        self.rules.remove_rule(mock_rule)
        self.assertNotIn(mock_rule, self.rules.rules)

    def test_evaluate_rules(self):
        mock_rule1 = MagicMock()
        mock_rule1.condition.return_value = True
        mock_rule2 = MagicMock()
        mock_rule2.condition.return_value = False
        self.rules.add_rule(mock_rule1)
        self.rules.add_rule(mock_rule2)

        mock_agent = MagicMock()
        self.rules.evaluate_rules(mock_agent)
        mock_rule1.action.assert_called_once_with(mock_agent)
        mock_rule2.action.assert_not_called()

class TestReasoner(unittest.TestCase):
    def setUp(self):
        self.mock_knowledge_base = MagicMock(spec=KnowledgeBase)
        self.mock_llm_manager = MagicMock(spec=LLMManager)
        self.reasoner = Reasoner(self.mock_knowledge_base, "test_api_key")
        self.reasoner.llm_manager = self.mock_llm_manager

    @patch('app.tools.reasoner.Reasoner._symbolic_infer')
    async def test_infer_symbolic(self, mock_symbolic_infer):
        mock_symbolic_infer.return_value = [Belief(id="1", content="inferred belief")]
        self.reasoner.strategy = ReasoningStrategy.SYMBOLIC
        result = await self.reasoner.infer([Belief(id="0", content="initial belief")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].content, "inferred belief")

    @patch('app.tools.reasoner.Reasoner._llm_infer')
    async def test_infer_llm(self, mock_llm_infer):
        mock_llm_infer.return_value = [Belief(id="1", content="LLM inferred belief")]
        self.reasoner.strategy = ReasoningStrategy.LLM
        result = await self.reasoner.infer([Belief(id="0", content="initial belief")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].content, "LLM inferred belief")

    async def test_update_beliefs(self):
        self.reasoner._symbolic_infer = MagicMock(return_value=[Belief(id="1", content="new belief")])
        self.reasoner.strategy = ReasoningStrategy.SYMBOLIC
        result = await self.reasoner.update_beliefs([Belief(id="0", content="initial belief")])
        self.assertEqual(len(result), 2)
        self.assertIn(Belief(id="0", content="initial belief"), result)
        self.assertIn(Belief(id="1", content="new belief"), result)

    @patch('app.tools.reasoner.Reasoner._symbolic_generate_desires')
    async def test_generate_desires_symbolic(self, mock_symbolic_generate_desires):
        mock_symbolic_generate_desires.return_value = [Desire(id="1", description="test desire", priority=5)]
        self.reasoner.strategy = ReasoningStrategy.SYMBOLIC
        result = await self.reasoner.generate_desires([Belief(id="0", content="test belief")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].description, "test desire")

    @patch('app.tools.reasoner.Reasoner._llm_generate_desires')
    async def test_generate_desires_llm(self, mock_llm_generate_desires):
        mock_llm_generate_desires.return_value = [Desire(id="1", description="LLM desire", priority=5)]
        self.reasoner.strategy = ReasoningStrategy.LLM
        result = await self.reasoner.generate_desires([Belief(id="0", content="test belief")])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].description, "LLM desire")

    async def test_select_intentions(self):
        desires = [Desire(id="1", description="test desire", priority=5)]
        beliefs = [Belief(id="0", content="test belief")]
        self.mock_knowledge_base.query_applicable_actions.return_value = ["test_action"]
        result = await self.reasoner.select_intentions(desires, beliefs, {})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].plan_id, "test_action")

if __name__ == '__main__':
    unittest.main()