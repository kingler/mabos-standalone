from typing import Dict, List, Any
import re
import uuid
from app.core.models.knowledge.reasoning.reasoner import Reasoner
import numpy as np
from app.core.models.sentence_transformer import SentenceTransformer
from app.core.models.knowledge.knowledge_base import KnowledgeBase, KnowledgeItem
from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.knowledge.reasoning.reasoning_engine import ReasoningEngine

class KnowledgeBaseService:
    def __init__(self):
        self.knowledge_base = KnowledgeBase(id=str(uuid.uuid4()))  # Ensure this is correctly initialized
        api_key = "your_api_key"  # Replace with your actual API key
        self.reasoning_engine = Reasoner(knowledge_base=self.knowledge_base, api_key=api_key)

    def create_knowledge_base(self) -> KnowledgeBase:
        kb_id = str(uuid.uuid4())
        new_kb = KnowledgeBase(id=kb_id)
        self.knowledge_bases[kb_id] = new_kb
        return new_kb

    def get_knowledge_base(self, kb_id: str) -> KnowledgeBase:
        return self.knowledge_bases.get(kb_id)

    def list_knowledge_bases(self) -> List[KnowledgeBase]:
        return list(self.knowledge_bases.values())

    def add_symbolic_knowledge(self, kb_id: str, item: KnowledgeItem) -> KnowledgeBase:
        kb = self.knowledge_bases.get(kb_id)
        if kb:
            kb.add_symbolic_knowledge(item)
        return kb

    def add_neural_knowledge(self, kb_id: str, item: KnowledgeItem) -> KnowledgeBase:
        kb = self.knowledge_bases.get(kb_id)
        if kb:
            kb.add_neural_knowledge(item)
        return kb

    def query_knowledge_base(self, kb_id: str, query: str) -> Dict[str, Any]:
        kb = self.knowledge_bases.get(kb_id)
        if not kb:
            return None
        return kb.query(query)

    def reason(self, kb_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        kb = self.knowledge_bases.get(kb_id)
        if not kb:
            return None
        return self.reasoning_engine.reason(kb, context)

    def simulate_action(self, kb_id: str, action: str, state: Dict[str, Any]) -> Dict[str, Any]:
        kb = self.knowledge_bases.get(kb_id)
        if not kb:
            return None
        return self.reasoning_engine.simulate_action(kb, action, state)

    def generate_plan(self, kb_id: str, goal: str, initial_state: Dict[str, Any]) -> List[str]:
        kb = self.knowledge_bases.get(kb_id)
        if not kb:
            return None
        return self.reasoning_engine.generate_plan(kb, goal, initial_state)