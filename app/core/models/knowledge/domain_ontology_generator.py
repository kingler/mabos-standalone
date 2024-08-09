from typing import Dict, Any
from owlready2 import World
from app.core.models.knowledge.domain_ontology_generator import DomainOntologyGenerator

class SBVRDomainOntologyGenerator(DomainOntologyGenerator):
    def __init__(self, world: World, sbvr_ontology):
        super().__init__(world)
        self.sbvr_ontology = sbvr_ontology

    def generate_domain_ontology(self, user_data: Dict[str, Any]) -> None:
        domain_onto = self.world.get_ontology("http://example.com/sbvr-domain-ontology")
        domain_onto.imported_ontologies.append(self.sbvr_ontology)
        
        with domain_onto:
            class User(self.sbvr_ontology.Concept): pass
            class BusinessModel(self.sbvr_ontology.Concept): pass
            class ProductDescription(self.sbvr_ontology.Concept): pass
            class Stakeholder(self.sbvr_ontology.Concept): pass
            
            class hasDescription(self.sbvr_ontology.ObjectProperty):
                domain = [BusinessModel]
                range = [str]
            class belongsTo(self.sbvr_ontology.ObjectProperty):
                domain = [ProductDescription]
                range = [BusinessModel]
            class hasStakeholder(self.sbvr_ontology.ObjectProperty):
                domain = [BusinessModel]
                range = [Stakeholder]
            
            user = User(f"http://example.com/user/{user_data['user_id']}")
            business_model = BusinessModel(f"http://example.com/business_model/{user_data['user_id']}")
            business_model.hasDescription.append(user_data['business_idea'])
            product = ProductDescription(f"http://example.com/product/{user_data['product_service']}")
            product.belongsTo.append(business_model)
            
            for stakeholder_data in user_data.get('stakeholders', []):
                stakeholder = Stakeholder(f"http://example.com/stakeholder/{stakeholder_data['id']}")
                business_model.hasStakeholder.append(stakeholder)
            
            business_vocabulary = self.sbvr_ontology.BusinessVocabulary("DomainVocabulary")
            for term in [User, BusinessModel, ProductDescription, Stakeholder]:
                business_vocabulary.hasComponent.append(term)
            
            rule = self.sbvr_ontology.OperativeRule("EachBusinessModelMustHaveAtLeastOneStakeholder")
            rule.hasModality.append("obligation")
        
        self.world.save()

    def validate_domain_ontology(self) -> Dict[str, Any]:
        validation_result = {"is_valid": True, "issues": []}
        
        # Check if all required concepts are present
        required_concepts = ["User", "BusinessModel", "ProductDescription", "Stakeholder"]
        for concept in required_concepts:
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