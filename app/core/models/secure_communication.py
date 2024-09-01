from cryptography.fernet import Fernet


class SecureCommunication:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_message(self, message: str) -> bytes:
        return self.cipher_suite.encrypt(message.encode())

    def decrypt_message(self, encrypted_message: bytes) -> str:
        return self.cipher_suite.decrypt(encrypted_message).decode()