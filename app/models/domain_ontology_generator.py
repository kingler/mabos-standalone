from typing import Dict, Any
from owlready2 import World, Ontology
from pydantic import BaseModel, Field

class DomainOntologyGenerator(BaseModel):
    world: World = Field(..., description="The owlready2 World instance")

    class Config:
        arbitrary_types_allowed = True

    def generate_domain_ontology(self, user_data: Dict[str, Any]) -> Ontology:
        """
        Generate a domain ontology based on user data.

        Args:
            user_data (Dict[str, Any]): The user data to generate the ontology.

        Returns:
            Ontology: The generated domain ontology.

        Raises:
            KeyError: If required keys are missing in user_data.
        """
        domain_onto = self.world.get_ontology("http://example.com/onboarding-ontology")

        with domain_onto:
            class User(domain_onto.Thing): pass
            class BusinessModel(domain_onto.Thing): pass
            class ProductDescription(domain_onto.Thing): pass
            class Stakeholder(domain_onto.Thing): pass

            class hasDescription(domain_onto.DataProperty):
                domain = [BusinessModel]
                range = [str]
            class belongsTo(domain_onto.ObjectProperty):
                domain = [ProductDescription]
                range = [BusinessModel]
            class hasStakeholder(domain_onto.ObjectProperty):
                domain = [BusinessModel]
                range = [Stakeholder]
            class hasUser(domain_onto.ObjectProperty):
                domain = [BusinessModel]
                range = [User]

        try:
            user = User(f"http://example.com/user/{user_data['user_id']}")
            business_model = BusinessModel(f"http://example.com/business_model/{user_data['user_id']}")
            business_model.hasDescription = user_data['business_idea']
            business_model.hasUser.append(user)

            product = ProductDescription(f"http://example.com/product/{user_data['product_service']}")
            product.belongsTo.append(business_model)

            for stakeholder_data in user_data.get('stakeholders', []):
                stakeholder = Stakeholder(f"http://example.com/stakeholder/{stakeholder_data['id']}")
                business_model.hasStakeholder.append(stakeholder)

        except KeyError as e:
            raise KeyError(f"Missing required key in user_data: {str(e)}")

        # Explicitly access the properties to avoid warnings
        _ = hasDescription, belongsTo, hasStakeholder, hasUser

        domain_onto.save()
        return domain_onto