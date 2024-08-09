from typing import Optional
from app.core.models.agent.belief import Belief

class BeliefService:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def create_belief(self, belief_data: dict) -> Belief:
        belief = Belief(**belief_data)
        self.knowledge_base.add_belief(belief)
        return belief

    def get_belief(self, belief_id: str) -> Optional[Belief]:
        return self.knowledge_base.get_belief(belief_id)

    def update_belief(self, belief_id: str, new_data: dict) -> Optional[Belief]:
        belief = self.knowledge_base.get_belief(belief_id)
        if belief:
            belief.update_belief(**new_data)
            self.knowledge_base.update_belief(belief)
        return belief

    def revise_belief(self, belief_id: str, new_evidence: dict) -> Optional[Belief]:
        belief = self.knowledge_base.get_belief(belief_id)
        if belief:
            belief.revise_belief(new_evidence)
            self.knowledge_base.update_belief(belief)
        return belief

    def delete_belief(self, belief_id: str) -> bool:
        if belief := self.knowledge_base.get_belief(belief_id):
            self.knowledge_base.delete_belief(belief)
            return True
        return False
