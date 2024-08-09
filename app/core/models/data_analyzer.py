from app.core.tools.llm_manager import LLMManager

class DataAnalyzer:
    def __init__(self, config):
        self.llm_manager = LLMManager(config['llms'])

    def analyze_data(self, data):
        prompt = f"Analyze the following data and provide insights: {data}"
        return self.llm_manager.get_text_completion(prompt)

    def generate_data_visualization_code(self, data_description):
        prompt = f"Generate Python code for visualizing this data: {data_description}"
        return self.llm_manager.get_text_completion(prompt)
