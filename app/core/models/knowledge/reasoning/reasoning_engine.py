from typing import Any, Dict, List

import sympy
from pydantic import BaseModel
from pyres import *
from pysmt.shortcuts import *
from z3 import *

from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.knowledge.reasoning.reasoner import Reasoner
from app.core.models.agent.plan import Plan
from app.core.models.agent import Goal


class SymbolicPlanner:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def create_plan(self, goal: Goal, initial_state: Dict[str, Any]) -> Plan:
        actions = self._backward_chaining(goal, initial_state)
        return Plan(steps=actions, goal=goal)

    def _backward_chaining(self, goal: Goal, state: Dict[str, Any]) -> List[str]:
        if self._goal_achieved(goal, state):
            return []

        applicable_actions = self._find_applicable_actions(goal, state)
        for action in applicable_actions:
            new_state = self._apply_action(action, state)
            subplan = self._backward_chaining(goal, new_state)
            if subplan is not None:
                return [action] + subplan

        return None

    def _goal_achieved(self, goal: Goal, state: Dict[str, Any]) -> bool:
        return self.knowledge_base.query_goal_state(goal, state)

    def _find_applicable_actions(self, goal: Goal, state: Dict[str, Any]) -> List[str]:
        return self.knowledge_base.query_applicable_actions(goal, state)

    def _apply_action(self, action: str, state: Dict[str, Any]) -> Dict[str, Any]:
        return self.knowledge_base.query_action_effects(action, state)

    def validate_plan(self, plan: Plan, initial_state: Dict[str, Any]) -> bool:
        current_state = initial_state.copy()
        for action in plan.steps:
            current_state = self._apply_action(action, current_state)
        return self._goal_achieved(plan.goal, current_state)


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
        self.z3_solver = Solver()
        self.pysmt_solver = Solver()
        self.pyres_kb = KnowledgeBase()
        
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
        
        return {**rule_based_results, **probabilistic_results}

    def _rule_based_reasoning(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform rule-based reasoning using the rules engine.
        
        Args:
            context (Dict[str, Any]): The context for reasoning.
        
        Returns:
            Dict[str, Any]: The results of rule-based reasoning.
        """
        def post(category: str, fact: Dict[str, Any]):
            # Placeholder for the actual implementation of the post function
            print(f"Posting to {category}: {fact}")
            
        results = {}
        for fact in context.get('facts', []):
            post('business', fact)
            # Collect results from the rules engine
            # This is a placeholder for actual implementation
            results[fact['subject']] = 'processed'
        return results

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
        return self._safe_eval(response)

    def generate_plan(self, goal: str, initial_state: Dict[str, Any]) -> List[str]:
        """
        Generate a plan to achieve a goal from an initial state using the knowledge base.
        
        Args:
            goal (str): The goal to achieve.
            initial_state (Dict[str, Any]): The initial state.
        
        Returns:
            List[str]: The generated plan as a list of actions.
        """
        return self._goal_oriented_reasoning(goal, initial_state)

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
        return [i.plan_id for i in intentions if i.plan_id]

    def _case_based_reasoning(self, current_case: Dict[str, Any]) -> Dict[str, Any]:
        return self._reason_with_llm(
            {"current_case": current_case},
            """
            Given the current case:
            {current_case}
            
            Retrieve the most similar case from the knowledge base and provide the solution.
            Provide the solution in the same format as the input case.
            """
        )

    def _temporal_reasoning(self, timeline: List[Dict[str, Any]]) -> Dict[str, Any]:
        return self._reason_with_llm(
            {"timeline": timeline},
            """
            Given the timeline of events:
            {timeline}
            
            Analyze the timeline and provide insights or predictions.
            Provide the output as a dictionary with 'insights' and 'predictions' as keys.
            """
        )

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
        return self._safe_eval(response)
        
    def _query_llm(self, prompt: str) -> str:
        """
        Query the LLM with a given prompt.
        
        Args:
            prompt (str): The prompt to query the LLM.
        
        Returns:
            str: The response from the LLM.
        """
        try:
            return self.reasoner.llm_decomposer.query(prompt)
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

    def _reason_with_llm(self, context: Dict[str, Any], prompt_template: str) -> Dict[str, Any]:
        prompt = prompt_template.format(**context)
        response = self._query_llm(prompt)
        return self._safe_eval(response)

    def solve_constraint(self, constraints):
        self.z3_solver.reset()
        for constraint in constraints:
            self.z3_solver.add(constraint)
        return self.z3_solver.model() if self.z3_solver.check() == sat else None
    
    def prove_theorem(self, axioms, theorem):
        with self.pysmt_solver:
            for axiom in axioms:
                self.pysmt_solver.add_assertion(axiom)
            return self.pysmt_solver.solve([Not(theorem)])
    
    def prove_fol(self, premises, conclusion):
        for premise in premises:
            self.pyres_kb.tell(premise)
        return self.pyres_kb.ask(conclusion)
    
    def symbolic_math(self, expression):
        return sympy.simplify(expression)
    
    def select_reasoning_method(self, problem_type):
        if problem_type == "constraint":
            return self.solve_constraint
        elif problem_type == "theorem":
            return self.prove_theorem
        elif problem_type == "fol":
            return self.prove_fol
        elif problem_type == "symbolic":
            return self.symbolic_math
        else:
            raise ValueError("Unknown problem type")