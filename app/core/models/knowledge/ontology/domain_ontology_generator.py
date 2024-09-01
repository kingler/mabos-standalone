from typing import Any, Dict

from owlready2 import World

from app.core.models.knowledge.ontology.ontology import Ontology
from app.core.models.knowledge.ontology.ontology_generator import (
    OntologyGenerator, SBVROntologyGenerator)
from app.core.tools.llm_manager import LLMManager


class DomainOntologyGenerator:
    def __init__(self, world: World, llm_manager: LLMManager):
        self.world = world
        self.ontology_generator = OntologyGenerator(llm_manager=llm_manager)

    async def generate_domain_ontology(self, user_data: Dict[str, Any]) -> Ontology:
        business_description = f"A business model for {user_data['business_idea']} with product/service: {user_data['product_service']}"
        ontology = await self.ontology_generator.generate_ontology(business_description)
        return await self.ontology_generator.refine_ontology(ontology)

    async def validate_domain_ontology(self, ontology: Ontology) -> Dict[str, Any]:
        return await self.ontology_generator.validate_ontology(ontology)

class SBVRDomainOntologyGenerator(DomainOntologyGenerator):
    def __init__(self, world: World, llm_manager: LLMManager, sbvr_ontology):
        super().__init__(world, llm_manager)
        self.sbvr_ontology = sbvr_ontology
        self.sbvr_ontology_generator = SBVROntologyGenerator(llm_manager=llm_manager)

    async def generate_domain_ontology(self, user_data: Dict[str, Any]) -> Ontology:
        business_description = f"A business model for {user_data['business_idea']} with product/service: {user_data['product_service']}"
        sbvr_ontology = await self.sbvr_ontology_generator.generate_sbvr_ontology(business_description)
        
        # Enhance the SBVR ontology with user-specific data
        with sbvr_ontology:
            sbvr_ontology.add_concept("User", f"User with ID {user_data['user_id']}")
            sbvr_ontology.add_concept("BusinessModel", f"Business model for {user_data['business_idea']}")
            sbvr_ontology.add_concept("ProductDescription", f"Description of {user_data['product_service']}")
            sbvr_ontology.add_concept("Stakeholder", "A person or entity with interest in the business")
            
            sbvr_ontology.add_relationship("hasDescription", "BusinessModel", "string")
            sbvr_ontology.add_relationship("belongsTo", "ProductDescription", "BusinessModel")
            sbvr_ontology.add_relationship("hasStakeholder", "BusinessModel", "Stakeholder")
            
            for stakeholder_data in user_data.get('stakeholders', []):
                sbvr_ontology.add_concept(f"Stakeholder_{stakeholder_data['id']}", f"Stakeholder with ID {stakeholder_data['id']}")
        
        return sbvr_ontology

    async def validate_domain_ontology(self, ontology: Ontology) -> Dict[str, Any]:
        validation_result = await self.sbvr_ontology_generator.validate_sbvr_ontology(ontology)
        
        # Additional domain-specific validation
        required_concepts = ["User", "BusinessModel", "ProductDescription", "Stakeholder"]
        for concept in required_concepts:
            if concept not in ontology.concepts:
                validation_result["is_valid"] = False
                validation_result["issues"].append(f"Required concept '{concept}' not found in the ontology")
        
        return validation_result