import os
from enum import Enum
from typing import Any, Dict, List, Union

import openai  # Assuming we're using OpenAI's GPT for LLM capabilities
from owlready2 import *
from pydantic import BaseModel, Field
from rdflib import Graph, Literal, URIRef

from app.models.agent import Belief, Desire, Intention
from app.models.agent.plan import Plan
from app.models.knowledge.knowledge_base import KnowledgeBase
from app.models.llm_decomposer import LLMDecomposer
from app.tools.llm_manager import LLMManager
from app.models.knowledge.reasoning.inference_result import InferenceResult


class ReasoningStrategy(Enum):
    SYMBOLIC = "symbolic"
    LLM = "llm"
    RDFS = "rdfs"
    OWL = "owl"
    SBVR = "sbvr"
    PROBABILISTIC = "probabilistic"
    CAUSAL = "causal"
    ANALOGICAL = "analogical"
    ETHICAL = "ethical"
    META = "meta"

class Reasoner(BaseModel):
    """
    A reasoner that combines different reasoning strategies to update beliefs, generate desires, select intentions, and make decisions.
    """
    knowledge_base: KnowledgeBase = Field(...)
    strategy: ReasoningStrategy = Field(default=ReasoningStrategy.SYMBOLIC)
    llm_manager: LLMManager = Field(default_factory=LLMManager)
    llm_decomposer: LLMDecomposer = Field(default=None)

    def __init__(self, knowledge_base: KnowledgeBase, strategy: ReasoningStrategy = ReasoningStrategy.SYMBOLIC, **data):
        super().__init__(knowledge_base=knowledge_base, strategy=strategy, **data)
        self.llm_manager = LLMManager()
        self.llm_decomposer = LLMDecomposer(llm_manager=self.llm_manager)

    async def infer(self, beliefs: List[Belief]) -> List[Belief]:
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
            return await self._llm_infer(beliefs)
        elif self.strategy == ReasoningStrategy.RDFS:
            return self._rdfs_infer(beliefs)
        elif self.strategy == ReasoningStrategy.OWL:
            return self._owl_infer(beliefs)
        elif self.strategy == ReasoningStrategy.SBVR:
            return self._sbvr_vocabulary_utilization(beliefs)
        elif self.strategy == ReasoningStrategy.PROBABILISTIC:
            return self._fuzzy_logic_reasoning(beliefs)
        elif self.strategy == ReasoningStrategy.CAUSAL:
            return self._counterfactual_reasoning(beliefs)
        elif self.strategy == ReasoningStrategy.ANALOGICAL:
            return self._cross_domain_mapping(beliefs)
        elif self.strategy == ReasoningStrategy.ETHICAL:
            return self._ethical_impact_assessment(beliefs)
        elif self.strategy == ReasoningStrategy.META:
            return self._self_evaluation(beliefs)
        else:
            raise ValueError(f"Unknown reasoning strategy: {self.strategy}")

    async def generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
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
            return await self._llm_generate_desires(beliefs)
        elif self.strategy == ReasoningStrategy.RDFS:
            return self._rdfs_generate_desires(beliefs)
        elif self.strategy == ReasoningStrategy.OWL:
            return self._owl_generate_desires(beliefs)
        else:
            raise ValueError(f"Unknown reasoning strategy: {self.strategy}")

    def _symbolic_infer(self, beliefs: List[Belief]) -> List[Belief]:
        return [Belief(id="inferred_B", content="B") 
                for belief in beliefs 
                if belief.content == "A" and self.knowledge_base.symbolic_kb.get("A_implies_B")]

    async def _llm_infer(self, beliefs: List[Belief]) -> List[Belief]:
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What new beliefs can be inferred?"
        response = await self.llm_manager.generate_text(prompt)
        new_belief_texts = response.strip().split(", ")
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

    def _sbvr_vocabulary_utilization(self, beliefs: List[Belief]) -> List[Belief]:
        sbvr_vocabulary = self.knowledge_base.get_sbvr_vocabulary() # Utilize SBVR vocabulary for consistent interpretation of business concepts
        return [Belief(id=f"sbvr_voc_{belief.id}", content=sbvr_vocabulary[belief.content]) 
                for belief in beliefs if belief.content in sbvr_vocabulary]

    def _fuzzy_logic_reasoning(self, beliefs: List[Belief]) -> List[Belief]:
        return [Belief(id=f"fuzzy_{belief.id}", content=f"Fuzzy interpretation of {belief.content}")
                for belief in beliefs if "approximately" in belief.content]

    def _counterfactual_reasoning(self, query: str) -> InferenceResult:
        # Implement counterfactual reasoning for "what-if" analyses
        counterfactual_scenario = f"Counterfactual scenario for {query}"
        return InferenceResult(conclusion=counterfactual_scenario, confidence=0.7, explanation="Based on counterfactual reasoning")

    def _cross_domain_mapping(self, query: str) -> InferenceResult:
        # Implement cross-domain mapping for creative problem-solving
        cross_domain_result = f"Cross-domain mapping result for {query}"
        return InferenceResult(conclusion=cross_domain_result, confidence=0.8, explanation="Based on cross-domain mapping")

    def _ethical_impact_assessment(self, query: str) -> InferenceResult:
        # Implement ethical impact assessment for decisions and actions
        ethical_assessment = f"Ethical impact assessment for {query}"
        return InferenceResult(conclusion=ethical_assessment, confidence=0.9, explanation="Based on ethical impact assessment")

    def _self_evaluation(self, query: str) -> InferenceResult:
        # Implement self-evaluation for assessing reasoning processes
        self_evaluation_result = f"Self-evaluation result for {query}"
        return InferenceResult(conclusion=self_evaluation_result, confidence=0.85, explanation="Based on self-evaluation")

    def _symbolic_generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        return [Desire(id="eat_desire", description="Find food", priority=5) 
                for belief in beliefs if belief.content == "hungry"]

    async def _llm_generate_desires(self, beliefs: List[Belief]) -> List[Desire]:
        belief_texts = [b.content for b in beliefs]
        prompt = f"Given these beliefs: {', '.join(belief_texts)}. What desires should the agent have?"
        response = await self.llm_manager.generate_text(prompt)
        desire_texts = response.strip().split(", ")
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

    async def update_beliefs(self, current_beliefs: List[Belief]) -> List[Belief]:
        """
        Update the agent's beliefs using the selected reasoning strategy.

        Args:
            current_beliefs (List[Belief]): The current beliefs of the agent.

        Returns:
            List[Belief]: The updated beliefs after reasoning.
        """
        inferred_beliefs = await self.infer(current_beliefs)
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

    async def make_decision(self, agent_id: str, beliefs: List[Belief], desires: List[Desire], intentions: List[Intention], resources: Dict[str, float]) -> Dict[str, Any]:
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
        updated_beliefs = await self.update_beliefs(beliefs)
        updated_desires = await self.generate_desires(updated_beliefs)
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
        
        response = await self.llm_manager.generate_text(prompt)
        
        action_line, reasoning_line = response.strip().split("\n")
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
        return self.llm_decomposer.translate_to_formal(natural_language)

    def formal_to_natural(self, formal_logic: str) -> str:
        return self.llm_decomposer.translate_to_natural(formal_logic)

    def combine_symbolic_and_formal(self, symbolic_insights: Dict[str, Any], formal_results: Dict[str, Any]) -> Dict[str, Any]:
        # Combine symbolic AI insights with formal reasoning results
        return symbolic_insights | formal_results

    def plan(self, goal: Any, current_state: Dict[str, Any]) -> Plan:
        # Use the planning service to generate a plan
        formal_goal = self.natural_to_formal(str(goal))
        formal_state = {k: self.natural_to_formal(str(v)) for k, v in current_state.items()}
        
        plan = self.planning_service.generate_plan(formal_goal, formal_state)
        
        if isinstance(plan, Plan):
            # Translate the plan steps back to natural language if needed
            return Plan(
                steps=[self.formal_to_natural(step) for step in plan.steps],
                goal=self.formal_to_natural(plan.goal)
            )
        else:
            raise ValueError("Failed to generate a valid plan")

    def reason_and_plan(self, goal: Any, current_state: Dict[str, Any]) -> Dict[str, Any]:
        # Combine symbolic reasoning with planning
        symbolic_insights = self.llm_decomposer.generate_insights(goal, current_state)
        plan = self.plan(goal, current_state)
        formal_results = {"plan": plan}
        
        return self.combine_symbolic_and_formal(symbolic_insights, formal_results)

    def get_current_state(self) -> Dict[str, Any]:
        return {
            'beliefs': [belief.to_dict() for belief in self.knowledge_base.get_beliefs()],
            'desires': [desire.to_dict() for desire in self.knowledge_base.get_desires()],
            'intentions': [intention.to_dict() for intention in self.knowledge_base.get_intentions()],
            'current_plan': self.planning_service.get_current_plan().to_dict() if self.planning_service.get_current_plan() else None,
        }
