from typing import Dict, Any
from owlready2 import World
from pydantic import BaseModel

class DomainOntologyGenerator(BaseModel):
    def __init__(self, world: World):
        self.world = world

    def generate_domain_ontology(self, user_data: Dict[str, Any]) -> None:
        """
        Generate a domain ontology based on user data.

        Args:
            user_data (Dict[str, Any]): The user data to generate the ontology.
        """
        domain_onto = self.world.get_ontology("http://example.com/onboarding-ontology")
        with domain_onto:
            class User(domain_onto.Thing): pass
            class BusinessModel(domain_onto.Thing): pass
            class ProductDescription(domain_onto.Thing): pass
            class Stakeholder(domain_onto.Thing): pass  # New class for stakeholders
            
            class hasDescription(domain_onto.ObjectProperty):
                domain = [BusinessModel]
                range = [str]
            class belongsTo(domain_onto.ObjectProperty):
                domain = [ProductDescription]
                range = [BusinessModel]
            class hasStakeholder(domain_onto.ObjectProperty):  # New property for stakeholders
                domain = [BusinessModel]
                range = [Stakeholder]
        
        user = User(f"http://example.com/user/{user_data['user_id']}")
        business_model = BusinessModel(f"http://example.com/business_model/{user_data['user_id']}")
        business_model.hasDescription.append(user_data['business_idea'])
        product = ProductDescription(f"http://example.com/product/{user_data['product_service']}")
        product.belongsTo.append(business_model)
        
        # Add stakeholders
        for stakeholder_data in user_data.get('stakeholders', []):
            stakeholder = Stakeholder(f"http://example.com/stakeholder/{stakeholder_data['id']}")
            business_model.hasStakeholder.append(stakeholder)
        
        self.world.as_rdflib_graph().parse(data=domain_onto.world.as_rdflib_graph().serialize(format='xml'))
