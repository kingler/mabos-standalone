import json
from typing import Dict, Any, List, Union

from pydantic import BaseModel
from app.models.sentence_transformer import SentenceTransformerWrapper

class KnowledgeConverter(BaseModel):
    """
    A class for converting knowledge between symbolic and neural representations.
    """

    transformer: SentenceTransformerWrapper

    def __init__(self, **data):
        """
        Initialize the KnowledgeConverter with a SentenceTransformerWrapper.
        """
        super().__init__(**data)
        self.transformer = SentenceTransformerWrapper()

    def to_symbolic(self, knowledge: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert knowledge to symbolic representation.

        Args:
            knowledge (Dict[str, Any]): The input knowledge.

        Returns:
            Dict[str, Any]: The symbolic representation of the knowledge.
        """
        def convert_value(value: Any) -> Any:
            if isinstance(value, (str, int, float, bool)):
                return value
            elif isinstance(value, (list, dict)):
                return json.dumps(value)
            else:
                return str(value)
        return {key: convert_value(value) for key, value in knowledge.items()}

    def to_neural(self, knowledge: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert knowledge to neural representation.

        Args:
            knowledge (Dict[str, Any]): The input knowledge.

        Returns:
            Dict[str, Any]: The neural representation of the knowledge.
        """
        def convert_value(value: Any) -> Union[List[float], Any]:
            if isinstance(value, str):
                return self.transformer.embed_text(value).tolist()
            elif isinstance(value, (int, float, bool)):
                return value
            elif isinstance(value, list):
                return [convert_value(item) for item in value]
            elif isinstance(value, dict):
                return {k: convert_value(v) for k, v in value.items()}
            else:
                return self.transformer.embed_text(str(value)).tolist()
        return {key: convert_value(value) for key, value in knowledge.items()}

    def symbolic_to_text(self, symbolic_knowledge: Dict[str, Any]) -> str:
        """
        Convert symbolic knowledge to text representation.

        Args:
            symbolic_knowledge (Dict[str, Any]): The symbolic knowledge.

        Returns:
            str: The text representation of the symbolic knowledge.
        """
        return "\n".join(f"{key}: {json.dumps(value)}" for key, value in symbolic_knowledge.items())

    def text_to_symbolic(self, text: str) -> Dict[str, Any]:
        """
        Convert text to symbolic knowledge representation.

        Args:
            text (str): The input text.

        Returns:
            Dict[str, Any]: The symbolic knowledge representation.
        """
        symbolic_knowledge = {}
        for line in text.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                try:
                    symbolic_knowledge[key] = json.loads(value)
                except json.JSONDecodeError:
                    symbolic_knowledge[key] = value
        return symbolic_knowledge

    def neural_to_text(self, neural_knowledge: Dict[str, Any]) -> str:
        """
        Convert neural knowledge to text representation.

        Args:
            neural_knowledge (Dict[str, Any]): The neural knowledge.

        Returns:
            str: The text representation of the neural knowledge.
        """
        def format_value(value: Any) -> str:
            if isinstance(value, list) and all(isinstance(item, float) for item in value):
                return f"[embedding of size {len(value)}]"
            elif isinstance(value, (int, float, bool)):
                return str(value)
            elif isinstance(value, dict):
                return json.dumps({k: format_value(v) for k, v in value.items()})
            else:
                return str(value)
        return "\n".join(f"{key}: {format_value(value)}" for key, value in neural_knowledge.items())

def to_symbolic(knowledge: Dict[str, Any]) -> Dict[str, Any]:
    """
    Standalone function to convert knowledge to symbolic representation.

    Args:
        knowledge (Dict[str, Any]): The input knowledge.

    Returns:
        Dict[str, Any]: The symbolic representation of the knowledge.
    """
    converter = KnowledgeConverter()
    return converter.to_symbolic(knowledge)

def to_neural(knowledge: Dict[str, Any]) -> Dict[str, Any]:
    """
    Standalone function to convert knowledge to neural representation.

    Args:
        knowledge (Dict[str, Any]): The input knowledge.

    Returns:
        Dict[str, Any]: The neural representation of the knowledge.
    """
    converter = KnowledgeConverter()
    return converter.to_neural(knowledge)