import yaml
from dotenv import load_dotenv
import os
from typing import List, Any, Dict
from pydantic import BaseModel, Field, SkipValidation
from app.core.models.agent.goal import Goal
from app.core.tools.llm_manager import LLMManager

load_dotenv()

class LLMDecomposer(BaseModel):
    config: Dict[str, Any] = Field(default_factory=SkipValidation)
    llm_manager: LLMManager = Field(default_factory=SkipValidation)

    def __init__(self, config_path='/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/config/llm_config.yaml'):
        super().__init__()
        # Load environment variables
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError("API_KEY not found in environment variables")
        
        # Load configuration file
        self.config = self.load_config(config_path)
        
        # Debugging: Print the configuration before using it
        print("Loaded configuration in LLMDecomposer:", self.config)
        
        # Check if 'llms' key exists in the config
        if 'llms' not in self.config:
            raise KeyError("'llms' key not found in the configuration file")
        
        # Initialize LLMManager
        self.llm_manager = LLMManager(llms_config=self.config['llms'], api_key=api_key)

    def load_config(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        
        # Debugging: Print the configuration
        print("Loaded configuration:", config)
        
        # Check if 'llms' key exists in the config
        if 'llms' not in config:
            raise KeyError("'llms' key not found in the configuration file")
        
        return config
