import os
from typing import List, Dict, Any, Union
from enum import Enum

from pydantic import BaseModel
from owlready2 import *
from rdflib import Graph, Literal, URIRef
from app.core.models.llm_decomposer import LLMDecomposer
from app.core.models.agent import Belief, Desire, Intention
from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.agent.plan import Plan
import openai  # Assuming we're using OpenAI's GPT for LLM capabilities

class ReasoningStrategy(Enum):
    SYMBOLIC = "symbolic"
    LLM = "llm"
    RDFS = "rdfs"
    OWL = "owl"

class Reasoner(BaseModel):
    """
    A reasoner that combines different reasoning strategies to update beliefs, generate desires, select intentions, and make decisions.
    """
    knowledge_base: KnowledgeBase
    api_key: str
    strategy: ReasoningStrategy

    def __init__(self, knowledge_base: KnowledgeBase, api_key: str, strategy: ReasoningStrategy = ReasoningStrategy.SYMBOLIC):
        super().__init__(knowledge_base=knowledge_base, api_key=api_key, strategy=strategy)
        self.knowledge_base = knowledge_base
        self.llm_decomposer = LLMDecomposer(api_key=api_key)
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def infer(self, beliefs: List[Belief]) -> List[Belief]:
        """
        Perform inference based on the given beliefs and the selected reasoning strategy.

        Args:
            beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Belief]: The inferred beliefs based on the selected strategy.
        """
        if self.strategy == ReasoningStrategy.SYMBOLIC:
            return self._symbolic_infer(beliefs)
        elif self.strategy == ReasoningStrategy.LLM:
            return self._llm_infer(beliefs)
        elif self.strategy == ReasoningStrategy.RDFS:
            return self._rdfs_infer(beliefs)
        elif self.strategy == ReasoningStrategy.OWL:
            return self._owl_infer(beliefs)
        else:
            raise ValueError(f"Unknown reasoning strategy: {self.strategy}")

    def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        """
        Generate desires based on the given beliefs and the selected reasoning strategy.

        Args:
            beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Desire]: The generated desires based on the selected strategy.
        """
        if self.strategy == ReasoningStrategy.SYMBOLIC:
            return self._symbolic_generate_desires(beliefs)
        elif self.strategy == ReasoningStrategy.LLM:
            return self._llm_generate_desires(beliefs)
        elif self.strategy == ReasoningStrategy.RDFS:
            return self._rdfs_generate_desires(beliefs)
        elif self.strategy == ReasoningStrategy.OWL:
            return self._owl_generate_desires(beliefs)
        else:
            raise ValueError(f"Unknown reasoning strategy: {self.strategy}")

    def _symbolic_infer(self, beliefs: List[Belief]) -> List[Belief]:
        new_beliefs = []
        for belief in beliefs:
            if belief.content == "A" and self.knowledge_base.symbolic_kb.get("A_implies_B"):
                new_beliefs.append(Belief(id="inferred_B", content="B"))
        return new_beliefs

    def _llm_infer(self, beliefs: List[Belief]) -> List[Belief]:
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What new beliefs can be inferred?"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        new_belief_texts = response.choices[0].text.strip().split(", ")
        return [Belief(id=f"llm_inferred_{i}", content=text) for i, text in enumerate(new_belief_texts)]

    def _rdfs_infer(self, beliefs: List[Belief]) -> List[Belief]:
        # Create an RDF graph from the beliefs
        graph = Graph()
        for belief in beliefs:
            subject = URIRef(f"http://example.com/{belief.id}")
            predicate = URIRef("http://example.com/hasContent")
            obj = Literal(belief.content)
            graph.add((subject, predicate, obj))

        # Apply RDFS reasoning
        rdfs_reasoner = graph.rdfs_closure()
        rdfs_reasoner.run()

        # Extract new beliefs from the inferred triples
        new_beliefs = []
        for s, p, o in graph:
            if (s, p, o) not in [(URIRef(f"http://example.com/{b.id}"), URIRef("http://example.com/hasContent"), Literal(b.content)) for b in beliefs]:
                new_belief_id = f"rdfs_inferred_{len(new_beliefs)}"
                new_belief_content = f"{s} {p} {o}"
                new_beliefs.append(Belief(id=new_belief_id, content=new_belief_content))

        return new_beliefs
    def _owl_infer(self, beliefs: List[Belief]) -> List[Belief]:
        # Create an OWL ontology from the beliefs
        onto = get_ontology("http://example.com/owl-inference/")

        with onto:
            class HasContent(DataProperty):
                domain = [Thing]
                range = [str]

            for belief in beliefs:
                new_class = types.new_class(belief.id, (Thing,))
                individual = new_class()
                individual.HasContent = belief.content

        # Run the reasoner
        with onto:
            sync_reasoner()

        # Extract new beliefs from the inferred axioms
        new_beliefs = []
        for cls in onto.classes():
            for instance in cls.instances():
                if hasattr(instance, 'HasContent'):
                    content = instance.HasContent
                    if content not in [b.content for b in beliefs]:
                        new_belief_id = f"owl_inferred_{len(new_beliefs)}"
                        new_beliefs.append(Belief(id=new_belief_id, content=content))

        return new_beliefs

    def _symbolic_generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        desires = []
        for belief in beliefs:
            if belief.content == "hungry":
                desires.append(Desire(id="eat_desire", description="Find food", priority=5))
        return desires

    def _llm_generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What desires should the agent have?"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        desire_texts = response.choices[0].text.strip().split(", ")
        return [Desire(id=f"llm_desire_{i}", description=text, priority=5) for i, text in enumerate(desire_texts)]

    def _rdfs_generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        # Create an RDF graph from the beliefs
        graph = Graph()
        for belief in beliefs:
            subject = URIRef(f"http://example.com/{belief.id}")
            predicate = URIRef("http://example.com/hasContent")
            obj = Literal(belief.content)
            graph.add((subject, predicate, obj))

        # Define RDFS rules for desire generation
        rules = """
            @prefix ex: <http://example.com/> .
            @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

            ex:hungry rdfs:subClassOf ex:NeedsFood .
            ex:NeedsFood rdfs:subClassOf ex:GeneratesDesire .
            ex:GeneratesDesire rdfs:subClassOf ex:Desire .
        """
        graph.parse(data=rules, format="turtle")

        # Apply RDFS reasoning
        rdfs_reasoner = graph.rdfs_closure()
        rdfs_reasoner.run()

        # Query for generated desires
        desires = []
        query = """
            PREFIX ex: <http://example.com/>
            SELECT ?content
            WHERE {
                ?belief ex:hasContent ?content .
                ?content a ex:Desire .
            }
        """
        results = graph.query(query)

        for row in results:
            desire_content = str(row['content'])
            desire_id = f"rdfs_desire_{len(desires)}"
            desires.append(Desire(id=desire_id, description=desire_content, priority=5))

        return desires

    def _owl_generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        # Create an OWL ontology from the beliefs
        onto = get_ontology("http://example.com/owl-desires.owl")

        with onto:
            class HasContent(DataProperty):
                domain = [Thing]
                range = [str]

            class GeneratesDesire(ObjectProperty):
                domain = [Thing]
                range = [Thing]

            class Desire(Thing):
                pass

            # Define OWL rules for desire generation
            class NeedsFood(Thing):
                equivalent_to = [Thing & HasContent.value("hungry")]

            class WantsExercise(Thing):
                equivalent_to = [Thing & HasContent.value("inactive")]

            NeedsFood.is_a.append(GeneratesDesire.some(Desire))
            WantsExercise.is_a.append(GeneratesDesire.some(Desire))

            # Add beliefs to the ontology
            for belief in beliefs:
                belief_instance = Thing(belief.id)
                belief_instance.HasContent.append(belief.content)

        # Run the reasoner
        with onto:
            sync_reasoner()

        # Query for generated desires
        desires = []
        for desire in onto.search(type=Desire):
            for belief in onto.search(GeneratesDesire.some(desire)):
                desire_content = f"Desire generated from belief: {belief.HasContent[0]}"
                desire_id = f"owl_desire_{len(desires)}"
                desires.append(Desire(id=desire_id, description=desire_content, priority=5))

        return desires

    def update_beliefs(self, current_beliefs: List[Belief]) -> List[Belief]:
        """
        Update the agent's beliefs using the selected reasoning strategy.

        Args:
            current_beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Belief]: The updated beliefs after reasoning.
        """
        inferred_beliefs = self.infer(current_beliefs)
        return list(set(current_beliefs + inferred_beliefs))

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

    def natural_to_formal(self, natural_language: str) -> str:
        # Translate natural language to formal logic
        # This could use the LLM model for translation
        formal_logic = self.llm_decomposer.translate_to_formal(natural_language)
        return formal_logic

    def formal_to_natural(self, formal_logic: str) -> str:
        # Translate formal logic to natural language
        # This could use the LLM model for translation
        natural_language = self.llm_decomposer.translate_to_natural(formal_logic)
        return natural_language

    def combine_symbolic_and_formal(self, symbolic_insights: Dict[str, Any], formal_results: Dict[str, Any]) -> Dict[str, Any]:
        # Combine symbolic AI insights with formal reasoning results
        # This method would implement logic to merge the two types of results
        combined_results = {**symbolic_insights, **formal_results}
        # Add any additional logic to resolve conflicts or synthesize information
        return combined_results

    def plan(self, goal: Any, current_state: Dict[str, Any]) -> Plan:
        # Use the planning service to generate a plan
        formal_goal = self.natural_to_formal(str(goal))
        formal_state = {k: self.natural_to_formal(str(v)) for k, v in current_state.items()}
        
        plan = self.planning_service.generate_plan(formal_goal, formal_state)
        
        if isinstance(plan, Plan):
            # Translate the plan steps back to natural language if needed
            natural_language_plan = Plan(
                steps=[self.formal_to_natural(step) for step in plan.steps],
                goal=self.formal_to_natural(plan.goal)
            )
            return natural_language_plan
        else:
            raise ValueError("Failed to generate a valid plan")

    def reason_and_plan(self, goal: Any, current_state: Dict[str, Any]) -> Dict[str, Any]:
        # Combine symbolic reasoning with planning
        symbolic_insights = self.llm_decomposer.generate_insights(goal, current_state)
        plan = self.plan(goal, current_state)
        formal_results = {"plan": plan}
        
        combined_results = self.combine_symbolic_and_formal(symbolic_insights, formal_results)
        return combined_results

    def get_current_state(self) -> Dict[str, Any]:
        current_state = {}

        # Query the knowledge base for current beliefs
        beliefs = self.knowledge_base.get_beliefs()
        current_state['beliefs'] = [belief.to_dict() for belief in beliefs]

        # Query the knowledge base for current desires
        desires = self.knowledge_base.get_desires()
        current_state['desires'] = [desire.to_dict() for desire in desires]

        # Query the knowledge base for current intentions
        intentions = self.knowledge_base.get_intentions()
        current_state['intentions'] = [intention.to_dict() for intention in intentions]

        # Query external data sources if necessary
        # For example, if we have an environment state:
        # current_state['environment'] = self.knowledge_base.get_environment_state()

        # If we have any ongoing plans, include them in the current state
        current_plan = self.planning_service.get_current_plan()
        if current_plan:
            current_state['current_plan'] = current_plan.to_dict()

        # Include any other relevant information from the knowledge base
        # For example, if we have a concept of time or resources:
        # current_state['time'] = self.knowledge_base.get_current_time()
        # current_state['resources'] = self.knowledge_base.get_available_resources()

        return current_state
