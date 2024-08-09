from app.core.tools.llm_manager import LLMManager

class NLPUtils:
    def __init__(self, config):
        self.llm_manager = LLMManager(config['llms'])

    def sentiment_analysis(self, text):
        prompt = f"Perform sentiment analysis on the following text: {text}"
        return self.llm_manager.get_text_completion(prompt)

    def entity_extraction(self, text):
        prompt = f"Extract entities from the following text: {text}"
        return self.llm_manager.get_text_completion(prompt)
