import os
from typing import List, Dict, Any
from app.core.llm_decomposer import LLMDecomposer
from app.models.agent import Belief, Desire, Intention
from app.models.knowledge_base import KnowledgeBase
import openai  # Assuming we're using OpenAI's GPT for LLM capabilities

class SymbolicReasoner:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def infer(self, beliefs: List[Belief]) -> List[Belief]:
        # Placeholder for symbolic inference
        # This could involve rule-based reasoning, logical inference, etc.
        new_beliefs = []
        for belief in beliefs:
            # Example: If we believe A and we know A implies B, then we believe B
            if belief.content == "A" and self.knowledge_base.symbolic_kb.get("A_implies_B"):
                new_beliefs.append(Belief(id="inferred_B", content="B"))
        return new_beliefs

    def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        # Placeholder for desire generation based on symbolic rules
        desires = []
        for belief in beliefs:
            if belief.content == "hungry":
                desires.append(Desire(id="eat_desire", description="Find food", priority=5))
        return desires

class LLMReasoner:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def infer(self, beliefs: List[Belief]) -> List[Belief]:
        # Use LLM to generate new beliefs based on current beliefs
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What new beliefs can be inferred?"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        new_belief_texts = response.choices[0].text.strip().split(", ")
        return [Belief(id=f"llm_inferred_{i}", content=text) for i, text in enumerate(new_belief_texts)]

    def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        # Use LLM to generate desires based on current beliefs
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What desires should the agent have?"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        desire_texts = response.choices[0].text.strip().split(", ")
        return [Desire(id=f"llm_desire_{i}", description=text, priority=5) for i, text in enumerate(desire_texts)]

class Reasoner:
    def __init__(self, knowledge_base: KnowledgeBase, api_key: str):
        self.knowledge_base = knowledge_base
        self.llm_decomposer = LLMDecomposer(api_key)
        self.symbolic_reasoner = SymbolicReasoner(knowledge_base)
        self.llm_reasoner = LLMReasoner()

    def update_beliefs(self, current_beliefs: List[Belief]) -> List[Belief]:
        symbolic_inferences = self.symbolic_reasoner.infer(current_beliefs)
        llm_inferences = self.llm_reasoner.infer(current_beliefs)
        return list(set(current_beliefs + symbolic_inferences + llm_inferences))

    def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        symbolic_desires = self.symbolic_reasoner.generate_desires(beliefs)
        llm_desires = self.llm_reasoner.generate_desires(beliefs)
        return list(set(symbolic_desires + llm_desires))

    def select_intentions(self, desires: List[Desire], beliefs: List[Belief], resources: Dict[str, float]) -> List[Intention]:
        # Placeholder for intention selection
        # This could involve more complex logic, possibly using both symbolic and LLM-based approaches
        intentions = []
        for desire in sorted(desires, key=lambda d: d.priority, reverse=True):
            if len(intentions) < 3:  # Limit to top 3 intentions for now
                intentions.append(Intention(id=f"intention_{desire.id}", desire_id=desire.id, plan_id=None))
        return intentions

    def make_decision(self, agent_id: str, beliefs: List[Belief], desires: List[Desire], intentions: List[Intention], resources: Dict[str, float]) -> Dict[str, Any]:
        updated_beliefs = self.update_beliefs(beliefs)
        updated_desires = self.generate_desires(updated_beliefs)
        updated_intentions = self.select_intentions(updated_desires, updated_beliefs, resources)
        
        # Use LLM to make a final decision based on the updated BDI state
        belief_texts = [b.content for b in updated_beliefs]
        desire_texts = [d.description for d in updated_desires]
        intention_texts = [f"Intend to: {d.description}" for i in updated_intentions for d in updated_desires if d.id == i.desire_id]
        
        prompt = f"""
        Agent ID: {agent_id}
        Beliefs: {', '.join(belief_texts)}
        Desires: {', '.join(desire_texts)}
        Intentions: {', '.join(intention_texts)}
        Resources: {resources}
        
        Based on this information, what action should the agent take next? Provide your answer in the format:
        Action: [action description]
        Reasoning: [brief explanation]
        """
        
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
        decision = response.choices[0].text.strip()
        
        # Parse the decision
        action_line, reasoning_line = decision.split("\n")
        action = action_line.split(": ")[1]
        reasoning = reasoning_line.split(": ")[1]
        
        return {
            "action": action,
            "reasoning": reasoning,
            "updated_beliefs": updated_beliefs,
            "updated_desires": updated_desires,
            "updated_intentions": updated_intentions
        }