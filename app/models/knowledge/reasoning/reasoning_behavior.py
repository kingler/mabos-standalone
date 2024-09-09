from app.models.knowledge.knowledge_base import KnowledgeBase
from app.tools.reasoner import Reasoner


class ReasoningBehavior:
    def __init__(self, knowledge_base: KnowledgeBase, reasoner: Reasoner):
        self.knowledge_base = knowledge_base
        self.reasoner = reasoner

    def identify_problem(self, agent):
        # Use ontology to identify problems requiring complex reasoning
        query = """
        SELECT ?problem
        WHERE {
            ?problem rdf:type :ComplexProblem .
            ?problem :requiresReasoning true .
        }
        """
        results = self.knowledge_base.reason(query)
        return results[0]['problem'] if results else None

    def formulate_problem(self, agent, problem_data):
        if problem_class := self.knowledge_base.ontology.get_concept_hierarchy().get(problem_data):
            properties = self.knowledge_base.ontology.get_properties()
            return {
                'type': problem_class,
                'data': {prop: getattr(agent, prop, None) for prop in properties if hasattr(agent, prop)}
            }
        return None

    def interpret_results(self, agent, results):
        # Use ontology to interpret and act on reasoning results
        for result in results:
            action_query = f"""
            SELECT ?action
            WHERE {{
                :{result} :hasRecommendedAction ?action .
            }}
            """
            actions = self.knowledge_base.reason(action_query)
            for action in actions:
                agent.perform_action(action['action'])

    def execute(self, agent):
        if problem := self.identify_problem(agent):
            if formulated_problem := self.formulate_problem(agent, problem):
                results = self.reasoner.reason(formulated_problem, strategy="symbolic")
                self.interpret_results(agent, results)