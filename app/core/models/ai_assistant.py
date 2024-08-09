from app.core.tools.llm_manager import LLMManager

class AIAssistant:
    def __init__(self, config):
        self.llm_manager = LLMManager(config['llms'])

    def generate_response(self, user_input):
        prompt = f"Generate a response to the following user input: {user_input}"
        return self.llm_manager.get_text_completion(prompt)

    def generate_follow_up_question(self, context):
        prompt = f"Generate a follow-up question based on this context: {context}"
        return self.llm_manager.get_text_completion(prompt)
