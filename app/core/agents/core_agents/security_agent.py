from cryptography.fernet import Fernet

from app.core.models.agent.agent import Agent
from app.core.models.agent.agent_role import AgentRole


class SecureCommunicationService:
    def __init__(self, key: str):
        self.cipher_suite = Fernet(key)

    def encrypt_message(self, message: str) -> str:
        return self.cipher_suite.encrypt(message.encode()).decode()

    def decrypt_message(self, encrypted_message: str) -> str:
        return self.cipher_suite.decrypt(encrypted_message.encode()).decode()


class SecurityAgent(Agent):
    def __init__(self, agent_id: str, name: str, secure_comm_service: SecureCommunicationService):
        super().__init__(agent_id, name)
        self.secure_comm_service = secure_comm_service
        self.add_role(AgentRole(name="Security", responsibilities=["monitor_traffic"]))

    def monitor_traffic(self, message: str):
        return self.secure_comm_service.encrypt_message(message)