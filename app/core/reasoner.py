import os
from typing import List, Dict, Any

from pydantic import BaseModel
from app.core.llm_decomposer import LLMDecomposer
from app.models.agent import Belief, Desire, Intention
from app.models.knowledge_base import KnowledgeBase
import openai  # Assuming we're using OpenAI's GPT for LLM capabilities

class SymbolicReasoner:
    """
    A symbolic reasoner that performs inference and generates desires based on symbolic rules.
    """
    def __init__(self, knowledge_base: KnowledgeBase):
        """
        Initialize the SymbolicReasoner with a knowledge base.

        Args:
            knowledge_base (KnowledgeBase): The knowledge base to use for reasoning.
        """
        self.knowledge_base = knowledge_base

    def infer(self, beliefs: List[Belief]) -> List[Belief]:
        """
        Perform symbolic inference based on the given beliefs and the knowledge base.

        Args:
            beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Belief]: The inferred beliefs based on symbolic rules.
        """
        new_beliefs = []
        for belief in beliefs:
            if belief.content == "A" and self.knowledge_base.symbolic_kb.get("A_implies_B"):
                new_beliefs.append(Belief(id="inferred_B", content="B"))
            # Add more symbolic inference rules here
        return new_beliefs

    def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        """
        Generate desires based on the given beliefs and symbolic rules.

        Args:
            beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Desire]: The generated desires based on symbolic rules.
        """
        desires = []
        for belief in beliefs:
            if belief.content == "hungry":
                desires.append(Desire(id="eat_desire", description="Find food", priority=5))
            # Add more symbolic desire generation rules here
        return desires

class LLMReasoner:
    """
    A reasoner that uses a large language model (LLM) to perform inference and generate desires.
    """
    def __init__(self):
        """
        Initialize the LLMReasoner with the OpenAI API key.
        """
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def infer(self, beliefs: List[Belief]) -> List[Belief]:
        """
        Perform inference using the LLM based on the given beliefs.

        Args:
            beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Belief]: The inferred beliefs based on the LLM's response.
        """
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What new beliefs can be inferred?"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        new_belief_texts = response.choices[0].text.strip().split(", ")
        return [Belief(id=f"llm_inferred_{i}", content=text) for i, text in enumerate(new_belief_texts)]

    def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        """
        Generate desires using the LLM based on the given beliefs.

        Args:
            beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Desire]: The generated desires based on the LLM's response.
        """
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What desires should the agent have?"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        desire_texts = response.choices[0].text.strip().split(", ")
        return [Desire(id=f"llm_desire_{i}", description=text, priority=5) for i, text in enumerate(desire_texts)]

class RDFSReasoner:
    """
    A reasoner that uses RDFS to perform inference and generate desires.
    """
    def __init__(self):
        """
        Initialize the RDFSReasoner.
        """

class OWLReasoner:
    """
    A reasoner that uses OWL to perform inference and generate desires.
    """
    def __init__(self):
        """
        Initialize the OWLReasoner.
        """
        

class Reasoner:
    """
    A reasoner that combines symbolic reasoning and LLM-based reasoning to update beliefs, generate desires, select intentions, and make decisions.
    """
    def __init__(self, knowledge_base: KnowledgeBase, api_key: str):
        """
        Initialize the Reasoner with a knowledge base and an API key.

        Args:
            knowledge_base (KnowledgeBase): The knowledge base to use for reasoning.
            api_key (str): The API key for the LLM.
        """
        self.knowledge_base = knowledge_base
        self.api_key = api_key
        self.llm_decomposer = LLMDecomposer(api_key=api_key)
        self.symbolic_reasoner = SymbolicReasoner(knowledge_base=knowledge_base)
        self.llm_reasoner = LLMReasoner()

    def update_beliefs(self, current_beliefs: List[Belief]) -> List[Belief]:
        """
        Update the agent's beliefs using both symbolic reasoning and LLM-based reasoning.

        Args:
            current_beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Belief]: The updated beliefs after reasoning.
        """
        symbolic_inferences = self.symbolic_reasoner.infer(current_beliefs)
        llm_inferences = self.llm_reasoner.infer(current_beliefs)
        return list(set(current_beliefs + symbolic_inferences + llm_inferences))

    def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        """
        Generate desires using both symbolic reasoning and LLM-based reasoning.

        Args:
            beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Desire]: The generated desires after reasoning.
        """
        symbolic_desires = self.symbolic_reasoner.generate_desires(beliefs)
        llm_desires = self.llm_reasoner.generate_desires(beliefs)
        return list(set(symbolic_desires + llm_desires))

    def select_intentions(self, desires: List[Desire], beliefs: List[Belief], resources: Dict[str, float]) -> List[Intention]:
        """
        Select intentions based on the agent's desires, beliefs, and available resources.

        Args:
            desires (List[Desire]): The current desires of the agent.
            beliefs (List[Belief]): The current beliefs of the agent.
            resources (Dict[str, float]): The available resources of the agent.

        Returns:
            List[Intention]: The selected intentions.
        """
        intentions = []
        for desire in sorted(desires, key=lambda d: d.priority, reverse=True):
            if len(intentions) < 3:
                intentions.append(Intention(id=f"intention_{desire.id}", desire_id=desire.id, plan_id=None))
        return intentions

    def make_decision(self, agent_id: str, beliefs: List[Belief], desires: List[Desire], intentions: List[Intention], resources: Dict[str, float]) -> Dict[str, Any]:
        """
        Make a decision based on the agent's beliefs, desires, intentions, and resources using an LLM.

        Args:
            agent_id (str): The ID of the agent.
            beliefs (List[Belief]): The current beliefs of the agent.
            desires (List[Desire]): The current desires of the agent.
            intentions (List[Intention]): The current intentions of the agent.
            resources (Dict[str, float]): The available resources of the agent.

        Returns:
            Dict[str, Any]: The decision made by the agent, including the action, reasoning, and updated mental states.
        """
        updated_beliefs = self.update_beliefs(beliefs)
        updated_desires = self.generate_desires(updated_beliefs)
        updated_intentions = self.select_intentions(updated_desires, updated_beliefs, resources)
        
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
