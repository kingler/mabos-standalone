import unittest
from unittest.mock import patch, MagicMock
from app.agents.core_agents.llm_agent import LLMAgent
from app.models.agent.goal import Goal
from app.models.message import ACLMessage, Performative

class TestLLMAgent(unittest.TestCase):

    def setUp(self):
        self.llm_service = MagicMock()
        self.agent_communication_service = MagicMock()
        self.agent = LLMAgent(
            agent_id="123",
            name="LLMAgent",
            api_key="test_api_key",
            llm_service=self.llm_service,
            agent_communication_service=self.agent_communication_service
        )

    @patch('app.agents.core_agents.llm_agent.LLMAgent.handle_request')
    def test_process_message_request(self, mock_handle_request):
        message = ACLMessage(
            sender_id="sender",
            receiver_id="123",
            performative=Performative.REQUEST,
            content="Test request"
        )
        self.agent.process_message(message)
        mock_handle_request.assert_called_with("Test request")

    @patch('app.agents.core_agents.llm_agent.LLMAgent.process_information')
    def test_process_message_inform(self, mock_process_information):
        message = ACLMessage(
            sender_id="sender",
            receiver_id="123",
            performative=Performative.INFORM,
            content="Test information"
        )
        self.agent.process_message(message)
        mock_process_information.assert_called_with("Test information")

    @patch('app.agents.core_agents.llm_agent.LLMAgent.handle_query')
    def test_process_message_query(self, mock_handle_query):
        message = ACLMessage(
            sender_id="sender",
            receiver_id="123",
            performative=Performative.QUERY,
            content="Test query"
        )
        self.agent.process_message(message)
        mock_handle_query.assert_called_with("Test query")

    def test_decompose_goal(self):
        goal = Goal(description="Test goal", priority=1)
        self.agent.decompose_goal(goal)
        self.llm_service.decompose_with_validation.assert_called_with(goal)

if __name__ == '__main__':
    unittest.main()