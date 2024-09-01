from app.core.tools.llm_manager import LLMManager


class CodeGenerator:
    def __init__(self, config):
        self.llm_manager = LLMManager(config['llms'])

    def generate_code(self, specification):
        prompt = f"Generate code based on the following specification: {specification}"
        return self.llm_manager.get_text_completion(prompt)

    def refactor_code(self, code):
        prompt = f"Refactor the following code: {code}"
        return self.llm_manager.get_text_completion(prompt)
