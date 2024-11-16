import unittest
from unittest.mock import Mock, patch
from pade.acl.aid import AID
from pade.acl.messages import ACLMessage
from src.agents.base_agent import BaseAgent, RequestInitiator, RequestResponder

class TestBaseAgent(unittest.TestCase):
    def setUp(self):
        self.agent = BaseAgent(AID("test_agent@localhost:5000"))

    def test_add_behaviour(self):
        mock_behaviour = Mock()
        self.agent.add_behaviour(mock_behaviour)
        self.assertIn(mock_behaviour, self.agent.behaviours)

    def test_on_start(self):
        mock_behaviour1 = Mock()
        mock_behaviour2 = Mock()
        self.agent.add_behaviour(mock_behaviour1)
        self.agent.add_behaviour(mock_behaviour2)

        with patch.object(self.agent, 'add_behaviour') as mock_add:
            self.agent.on_start()
            mock_add.assert_any_call(mock_behaviour1)
            mock_add.assert_any_call(mock_behaviour2)

    @patch('src.agents.base_agent.ACLMessage')
    def test_send_message(self, mock_acl_message):
        receiver_aid = AID("receiver@localhost:5000")
        content = {"key": "value"}
        performative = ACLMessage.REQUEST

        self.agent.send_message(receiver_aid, content, performative)

        mock_acl_message.assert_called_once_with(performative)
        mock_message = mock_acl_message.return_value
        mock_message.add_receiver.assert_called_once_with(receiver_aid)
        mock_message.set_content.assert_called_once_with(str(content))
        self.agent.send.assert_called_once_with(mock_message)

class TestRequestInitiator(unittest.TestCase):
    def setUp(self):
        self.agent = Mock()
        self.message = Mock()
        self.initiator = RequestInitiator(self.agent, self.message)

    def test_handle_agree(self):
        mock_message = Mock()
        mock_message.sender.name = "sender"
        self.agent.aid.name = "agent"

        with patch('builtins.print') as mock_print:
            self.initiator.handle_agree(mock_message)
            mock_print.assert_called_once_with("agent received agree from sender")

    def test_handle_refuse(self):
        mock_message = Mock()
        mock_message.sender.name = "sender"
        self.agent.aid.name = "agent"

        with patch('builtins.print') as mock_print:
            self.initiator.handle_refuse(mock_message)
            mock_print.assert_called_once_with("agent received refuse from sender")

    def test_handle_inform(self):
        mock_message = Mock()
        mock_message.sender.name = "sender"
        self.agent.aid.name = "agent"

        with patch('builtins.print') as mock_print:
            self.initiator.handle_inform(mock_message)
            mock_print.assert_called_once_with("agent received inform from sender")

class TestRequestResponder(unittest.TestCase):
    def setUp(self):
        self.agent = Mock()
        self.responder = RequestResponder(self.agent)

    def test_handle_request(self):
        mock_message = Mock()
        self.responder.handle_request(mock_message)
        # As the handle_request method is empty, we just ensure it doesn't raise an exception
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()