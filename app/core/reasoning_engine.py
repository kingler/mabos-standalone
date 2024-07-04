from typing import Dict, Any, List

from pydantic import BaseModel
from app.models.knowledge_base import KnowledgeBase
from app.core.reasoner import Reasoner

class ReasoningEngine(BaseModel):
    """
    A reasoning engine that performs various types of reasoning using a knowledge base and a reasoner.
    """
    def __init__(self, knowledge_base: KnowledgeBase, api_key: str):
        """
        Initialize the ReasoningEngine with a knowledge base and an API key.
        
        Args:
            knowledge_base (KnowledgeBase): The knowledge base to use for reasoning.
            api_key (str): The API key for the reasoner.
        """
        self.reasoner = Reasoner(knowledge_base, api_key)

    def reason(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform reasoning using the knowledge base and context.
        
        Args:
            context (Dict[str, Any]): The context for reasoning.
        
        Returns:
            Dict[str, Any]: The combined results of rule-based and probabilistic reasoning.
        """
        # Rule-based reasoning
        rule_based_results = self._rule_based_reasoning(context)
        
        # Probabilistic reasoning
        probabilistic_results = self._probabilistic_reasoning(context)
        
        # Combine results
        combined_results = {**rule_based_results, **probabilistic_results}
        return combined_results

    def simulate_action(self, action: str, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate the outcome of performing an action in a given state using the knowledge base.
        
        Args:
            action (str): The action to simulate.
            state (Dict[str, Any]): The current state.
        
        Returns:
            Dict[str, Any]: The updated state after simulating the action.
        """
        prompt = f"""
        Given the current state:
        {state}
        
        Simulate the outcome of performing the action: {action}
        Provide the updated state in the same format as the input state.
        """
        response = self._query_llm(prompt)
        updated_state = self._safe_eval(response)
        return updated_state

    def generate_plan(self, goal: str, initial_state: Dict[str, Any]) -> List[str]:
        """
        Generate a plan to achieve a goal from an initial state using the knowledge base.
        
        Args:
            goal (str): The goal to achieve.
            initial_state (Dict[str, Any]): The initial state.
        
        Returns:
            List[str]: The generated plan as a list of actions.
        """
        plan = self._goal_oriented_reasoning(goal, initial_state)
        return plan

    def _bdi_reasoning(self, beliefs: Dict[str, Any], desires: List[str], intentions: List[str]) -> Dict[str, Any]:
        """
        Perform BDI (Belief-Desire-Intention) reasoning using the knowledge base.
        
        Args:
            beliefs (Dict[str, Any]): The current beliefs.
            desires (List[str]): The current desires.
            intentions (List[str]): The current intentions.
        
        Returns:
            Dict[str, Any]: The updated beliefs, desires, and intentions after BDI reasoning.
        """
        updated_beliefs = self.reasoner.update_beliefs(beliefs)
        updated_desires = self.reasoner.generate_desires(updated_beliefs)
        updated_intentions = self.reasoner.select_intentions(updated_desires, updated_beliefs, {})
        return {
            "beliefs": updated_beliefs,
            "desires": updated_desires,
            "intentions": updated_intentions
        }

    def _goal_oriented_reasoning(self, goal: str, current_state: Dict[str, Any]) -> List[str]:
        """
        Perform goal-oriented reasoning using the knowledge base to generate a plan.
        
        Args:
            goal (str): The goal to achieve.
            current_state (Dict[str, Any]): The current state.
        
        Returns:
            List[str]: The generated plan as a list of actions.
        """
        beliefs = [{"content": f"{k}: {v}"} for k, v in current_state.items()]
        desires = [{"description": goal, "priority": 1}]
        intentions = self.reasoner.select_intentions(desires, beliefs, {})
        plan = [i.plan_id for i in intentions if i.plan_id]
        return plan

    def _case_based_reasoning(self, current_case: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform case-based reasoning using the knowledge base to find a solution for the current case.
        
        Args:
            current_case (Dict[str, Any]): The current case.
        
        Returns:
            Dict[str, Any]: The solution for the current case.
        """
        prompt = f"""
        Given the current case:
        {current_case}
        
        Retrieve the most similar case from the knowledge base and provide the solution.
        Provide the solution in the same format as the input case.
        """
        response = self._query_llm(prompt)
        solution = self._safe_eval(response)
        return solution

    def _temporal_reasoning(self, timeline: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform temporal reasoning using the knowledge base to analyze a timeline of events.
        
        Args:
            timeline (List[Dict[str, Any]]): The timeline of events.
        
        Returns:
            Dict[str, Any]: The insights and predictions based on the temporal reasoning.
        """
        prompt = f"""
        Given the timeline of events:
        {timeline}
        
        Analyze the timeline and provide insights or predictions.
        Provide the output as a dictionary with 'insights' and 'predictions' as keys.
        """
        response = self._query_llm(prompt)
        output = self._safe_eval(response)
        return output

    def _uncertainty_reasoning(self, uncertain_facts: List[Dict[str, float]]) -> Dict[str, Any]:
        """
        Perform reasoning under uncertainty using the knowledge base.
        
        Args:
            uncertain_facts (List[Dict[str, float]]): The uncertain facts with their probabilities.
        
        Returns:
            Dict[str, Any]: The conclusions based on reasoning under uncertainty.
        """
        prompt = f"""
        Given the uncertain facts:
        {uncertain_facts}
        
        Perform reasoning considering the uncertainty and provide the most likely conclusions.
        Provide the output as a dictionary with 'conclusions' as the key.
        """
        response = self._query_llm(prompt)
        output = self._safe_eval(response)
        return output
        
    def _rule_based_reasoning(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform rule-based reasoning using the knowledge base and context.
        
        Args:
            context (Dict[str, Any]): The context for reasoning.
        
        Returns:
            Dict[str, Any]: The results of rule-based reasoning.
        """
        # Extract relevant facts from the context
        facts = [fact for fact in context.keys() if not isinstance(context[fact], float)]
        
        # Construct a prompt for rule-based reasoning
        prompt = f"""
        Given the following facts:
        {facts}
        
        Perform rule-based reasoning using the knowledge base to infer new knowledge or derive conclusions.
        Provide the output as a dictionary with 'inferred_knowledge' and 'conclusions' as keys.
        """
        
        # Query the LLM with the rule-based reasoning prompt
        response = self._query_llm(prompt)
        
        # Evaluate the LLM response and extract the results
        output = self._safe_eval(response)
        inferred_knowledge = output.get("inferred_knowledge", {})
        conclusions = output.get("conclusions", {})
        
        return {
            "inferred_knowledge": inferred_knowledge,
            "conclusions": conclusions
        }
    
    def _probabilistic_reasoning(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform probabilistic reasoning using the knowledge base and context.
        
        Args:
            context (Dict[str, Any]): The context for reasoning.
        
        Returns:
            Dict[str, Any]: The results of probabilistic reasoning.
        """
        # Extract relevant facts and their probabilities from the context
        facts_with_probs = [(fact, prob) for fact, prob in context.items() if isinstance(prob, float)]
        
        # Construct a prompt for probabilistic reasoning
        prompt = f"""
        Given the following facts with their probabilities:
        {facts_with_probs}
        
        Perform probabilistic reasoning to infer new knowledge or update existing beliefs.
        Provide the output as a dictionary with 'inferred_knowledge' and 'updated_beliefs' as keys.
        """
        
        # Query the LLM with the probabilistic reasoning prompt
        response = self._query_llm(prompt)
        
        # Evaluate the LLM response and extract the results
        output = self._safe_eval(response)
        inferred_knowledge = output.get("inferred_knowledge", {})
        updated_beliefs = output.get("updated_beliefs", {})
        
        return {
            "inferred_knowledge": inferred_knowledge,
            "updated_beliefs": updated_beliefs
        }

    def _query_llm(self, prompt: str) -> str:
        """
        Query the LLM with a given prompt.
        
        Args:
            prompt (str): The prompt to query the LLM.
        
        Returns:
            str: The response from the LLM.
        """
        try:
            response = self.reasoner.llm_decomposer.query(prompt)
            return response
        except Exception as e:
            print(f"Error querying LLM: {e}")
            return "{}"

    def _safe_eval(self, response: str) -> Dict[str, Any]:
        """
        Safely evaluate the LLM response.
        
        Args:
            response (str): The response from the LLM.
        
        Returns:
            Dict[str, Any]: The evaluated response as a dictionary.
        """
        try:
            return eval(response)
        except Exception as e:
            print(f"Error evaluating response: {e}")
            return {}