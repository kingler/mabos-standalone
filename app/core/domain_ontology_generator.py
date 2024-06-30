from typing import Dict, Any
from owlready2 import World

class DomainOntologyGenerator:
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
            
            class hasDescription(domain_onto.ObjectProperty):
                domain = [BusinessModel]
                range = [str]
            class belongsTo(domain_onto.ObjectProperty):
                domain = [ProductDescription]
                range = [BusinessModel]
        
        user = User(f"http://example.com/user/{user_data['user_id']}")
        business_model = BusinessModel(f"http://example.com/business_model/{user_data['user_id']}")
        business_model.hasDescription.append(user_data['business_idea'])
        product = ProductDescription(f"http://example.com/product/{user_data['product_service']}")
        product.belongsTo.append(business_model)
        
        self.world.as_rdflib_graph().parse(data=domain_onto.world.as_rdflib_graph().serialize(format='xml'))
