from owlready2 import World, FunctionalProperty, InverseFunctionalProperty
from pydantic import BaseModel, Field, SkipValidation
from typing import Optional
from rdflib import Graph

class CustomInference(BaseModel):
    Graph: SkipValidation[Graph] = Field(default=None)
    world: SkipValidation[World] = Field(..., description="The owlready2 World instance")
    knowledge_graph: SkipValidation[Graph] = Field(..., description="RDFLib Graph for storing knowledge")
    reasoning_engine: Optional[object] = Field(None, description="Reasoning engine for inference")

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        print("CustomInference initialized with data:", data)
        

    def apply_custom_inference_rules(self) -> None:
        """
        Apply custom inference rules to the ontology and knowledge graph.

        This method defines custom object properties and their relationships
        within the ontology, applies reasoning, and updates the knowledge graph.

        Raises:
            ValueError: If the ontology URL is not found in the world.
        """
        ontology_url = "http://example.com/mabos-ontology"
        onto = self.world.get_ontology(ontology_url)
        
        if not onto:
            raise ValueError(f"Ontology {ontology_url} not found in the world.")

        with onto:
            class hasPrimaryGoal(onto.ObjectProperty, FunctionalProperty):
                """
                Represents a functional property indicating the primary goal of an entity.
                """
                pass

            class isGoalOf(onto.ObjectProperty, InverseFunctionalProperty):
                """
                Represents an inverse functional property indicating which entity a goal belongs to.
                """
                inverse_property = hasPrimaryGoal

            class hasSubGoal(onto.ObjectProperty):
                """
                Represents a property indicating a sub-goal of a primary goal.
                """
                domain = [onto.Thing]  # Specify the appropriate domain class
                range = [onto.Thing]   # Specify the appropriate range class

        # Apply reasoning
        if self.reasoning_engine:
            inferred_facts = self.reasoning_engine.reason(self.world.as_rdflib_graph())
            self.update_knowledge_graph(inferred_facts)
        else:
            print("Warning: No reasoning engine provided. Skipping reasoning step.")

        # Sync the ontology to ensure changes are saved
        onto.sync_reasoner()

    def update_knowledge_graph(self, inferred_facts: Graph) -> None:
        """
        Update the knowledge graph with newly inferred facts.

        Args:
            inferred_facts (Graph): RDFLib Graph containing newly inferred facts.
        """
        self.knowledge_graph += inferred_facts

    def query_knowledge_base(self, query: str) -> list:
        """
        Query the knowledge base (ontology and knowledge graph).

        Args:
            query (str): SPARQL query string.

        Returns:
            list: Query results.
        """
        return list(self.knowledge_graph.query(query))