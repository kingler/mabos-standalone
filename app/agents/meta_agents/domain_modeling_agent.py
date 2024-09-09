import logging
import re
import types
import xml.etree.ElementTree as ET
from typing import Any, Dict, List

from owlready2 import DataProperty, ObjectProperty, Thing, World
from pydantic import BaseModel, Field

from app.models.knowledge.ontology.ontology import Ontology
from app.models.knowledge.vocabulary_manager import VocabularyManager
from app.services.llm_service import LLMService
from app.tools.llm_manager import LLMManager


class OntologyGenerator(BaseModel):
    llm_manager: LLMManager = Field(default_factory=LLMManager)
    llm_service: LLMService = Field(default_factory=LLMService)
    ontology: Ontology = Field(default_factory=Ontology)
    vocabulary: VocabularyManager = Field(default_factory=VocabularyManager)

    def _parse_llm_response(self, response: str) -> Dict[str, Any]:
        import json
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Handle parsing error
            logging.error(f"Failed to parse LLM response: {response}")
            # Attempt to extract key-value pairs using regex
            import re
            pattern = r'(\w+):\s*(.+?)(?=\n\w+:|$)'
            matches = re.findall(pattern, response, re.DOTALL)
            parsed_response = {key.strip(): value.strip() for key, value in matches}
            if not parsed_response:
                logging.warning("Could not extract any key-value pairs from the response")
            return parsed_response

    async def generate_ontology(self, business_description: str) -> Ontology:
        # Implement base ontology generation logic
        prompt = f"""
        Given the following business description, generate an ontology with concepts and relationships:
        
        {business_description}
        
        Please provide the output in JSON format with the following structure:
        {{
            "concepts": ["Concept1", "Concept2", ...],
            "relationships": [
                {{
                    "name": "relationship_name",
                    "source": "SourceConcept",
                    "target": "TargetConcept"
                }},
                ...
            ]
        }}
        """
        
        response = await self.llm_service.generate_text(prompt)
        parsed_response = self._parse_llm_response(response)
        
        ontology = Ontology()
        
        if 'concepts' in parsed_response:
            for concept in parsed_response['concepts']:
                ontology.add_concept(concept)
        
        if 'relationships' in parsed_response:
            for relationship in parsed_response['relationships']:
                ontology.add_relationship(
                    relationship['name'],
                    relationship['source'],
                    relationship['target']
                )
        
        return ontology

    async def refine_ontology(self, ontology: Ontology) -> Ontology:
        # Implement ontology refinement logic based on best practices
        
        # 1. Remove redundant concepts and relationships
        redundant_concepts = self._identify_redundant_concepts(ontology)
        for concept in redundant_concepts:
            ontology.remove_concept(concept)
        
        # 2. Normalize relationship names
        self._normalize_relationship_names(ontology)
        
        # 3. Ensure proper hierarchy
        self._refine_concept_hierarchy(ontology)
        
        # 4. Add missing inverse relationships
        self._add_inverse_relationships(ontology)
        
        # 5. Validate and refine cardinalities
        self._refine_cardinalities(ontology)
        
        # 6. Enrich with additional metadata
        await self._enrich_with_metadata(ontology)
        
        return ontology

    def _identify_redundant_concepts(self, ontology: Ontology) -> List[str]:
        # Logic to identify redundant concepts
        # This is a placeholder and should be implemented based on specific criteria
        return []

    def _normalize_relationship_names(self, ontology: Ontology):
        for relationship in ontology.relationships:
            # Normalize relationship names (e.g., convert to snake_case)
            normalized_name = '_'.join(relationship.name.lower().split())
            ontology.update_relationship_name(relationship.name, normalized_name)

    def _refine_concept_hierarchy(self, ontology: Ontology):
        # Logic to refine concept hierarchy
        # This is a placeholder and should be implemented based on domain-specific rules
        pass

    def _add_inverse_relationships(self, ontology: Ontology):
        for relationship in ontology.relationships:
            inverse_name = f"inverse_of_{relationship.name}"
            if not ontology.has_relationship(inverse_name):
                ontology.add_relationship(inverse_name, relationship.target, relationship.source)

    def _refine_cardinalities(self, ontology: Ontology):
        # Logic to refine cardinalities
        # This is a placeholder and should be implemented based on domain-specific rules
        pass

    async def _enrich_with_metadata(self, ontology: Ontology):
        for concept in ontology.concepts:
            prompt = f"Provide a brief description and some example attributes for the concept: {concept}"
            response = await self.llm_service.generate_text(prompt)
            parsed_response = self._parse_llm_response(response)
            if 'description' in parsed_response:
                ontology.add_concept_metadata(concept, 'description', parsed_response['description'])
            if 'attributes' in parsed_response:
                ontology.add_concept_metadata(concept, 'attributes', parsed_response['attributes'])

    async def validate_ontology(self, ontology: Ontology) -> Dict[str, Any]:
        validation_results = {
            "is_valid": True,
            "errors": [],
            "warnings": []
        }

        # Check for unique concept names
        concept_names = set()
        for concept in ontology.concepts:
            if concept.name in concept_names:
                validation_results["errors"].append(f"Duplicate concept name: {concept.name}")
                validation_results["is_valid"] = False
            else:
                concept_names.add(concept.name)

        # Check for unique relationship names
        relationship_names = set()
        for relationship in ontology.relationships:
            if relationship.name in relationship_names:
                validation_results["errors"].append(f"Duplicate relationship name: {relationship.name}")
                validation_results["is_valid"] = False
            else:
                relationship_names.add(relationship.name)

        # Validate relationship integrity
        for relationship in ontology.relationships:
            if relationship.source not in ontology.concepts:
                validation_results["errors"].append(f"Invalid source concept in relationship: {relationship.name}")
                validation_results["is_valid"] = False
            if relationship.target not in ontology.concepts:
                validation_results["errors"].append(f"Invalid target concept in relationship: {relationship.name}")
                validation_results["is_valid"] = False

        # Check for orphan concepts (concepts with no relationships)
        for concept in ontology.concepts:
            if not any(r.source == concept or r.target == concept for r in ontology.relationships):
                validation_results["warnings"].append(f"Orphan concept: {concept.name}")

        # Validate cardinalities
        for relationship in ontology.relationships:
            if not self._is_valid_cardinality(relationship.cardinality):
                validation_results["errors"].append(f"Invalid cardinality for relationship: {relationship.name}")
                validation_results["is_valid"] = False

        # Check for cycles in the concept hierarchy
        if self._has_cycles(ontology):
            validation_results["errors"].append("Cycle detected in concept hierarchy")
            validation_results["is_valid"] = False

        return validation_results

    def _is_valid_cardinality(self, cardinality: str) -> bool:
        # Implement cardinality validation logic
        valid_patterns = [r'^\d+$', r'^\d+\.\.\d+$', r'^\d+\.\.\*$', r'^\*$']
        return any(re.match(pattern, cardinality) for pattern in valid_patterns)

    def _has_cycles(self, ontology: Ontology) -> bool:
        # Implement cycle detection in concept hierarchy
        visited = set()
        path = set()

        def dfs(concept):
            visited.add(concept)
            path.add(concept)
            for child in ontology.get_child_concepts(concept):
                if concept not in visited and dfs(child):
                    return True
            path.remove(concept)
            return False

        for concept in ontology.concepts:
            if concept not in visited and dfs(concept):
                return True
        return False

class SBVROntologyGenerator(OntologyGenerator):
    def __init__(self, llm_manager: LLMManager, **data):
        super().__init__(llm_manager=llm_manager, **data)
        self.sbvr_ontology = self.create_sbvr_base_ontology()

    def create_sbvr_base_ontology(self):
        world = World()
        sbvr_onto = world.get_ontology("http://example.com/sbvr-metamodel")

        with sbvr_onto:
            class SBVRConcept(Thing): pass
            class Noun(SBVRConcept): pass
            class VerbConcept(SBVRConcept): pass
            class Fact(SBVRConcept): pass
            class Rule(SBVRConcept): pass
            class Meaning(SBVRConcept): pass
            class Representation(SBVRConcept): pass
            class Expression(SBVRConcept): pass
            class Designation(Representation): pass
            class Definition(Representation): pass
            class Statement(Representation): pass
            class Text(Expression): pass
            class Name(Designation): pass
            class Term(Designation): pass
            class FactType(Meaning): pass
            class ObjectType(Noun): pass
            class IndividualConcept(Noun): pass
            class Characteristic(Fact): pass
            class AssociativeFactType(FactType): pass
            class Concept(Meaning): pass
            class ReferenceScheme(SBVRConcept): pass
            class Vocabulary(SBVRConcept): pass
            class GeneralConcept(Noun): pass
            class CategorizationScheme(SBVRConcept): pass
            class CategorizationType(SBVRConcept): pass
            class Variable(SBVRConcept): pass
            class LogicalFormulation(SBVRConcept): pass
            class Projection(SBVRConcept): pass
            class AuxiliaryVariable(Variable): pass

            class hasDefinition(ObjectProperty):
                domain = [SBVRConcept]
                range = [Definition]

            class hasFactType(ObjectProperty):
                domain = [Fact]
                range = [VerbConcept]

            class hasRole(ObjectProperty):
                domain = [VerbConcept]
                range = [Noun]

            class represents(ObjectProperty):
                domain = [Representation]
                range = [Meaning]

            class hasExpression(ObjectProperty):
                domain = [Representation]
                range = [Expression]

            class designates(ObjectProperty):
                domain = [Designation]
                range = [Meaning]

            class defines(ObjectProperty):
                domain = [Definition]
                range = [Meaning]

            class hasReferenceScheme(ObjectProperty):
                domain = [ObjectType]
                range = [ReferenceScheme]

            class usesCharacteristic(ObjectProperty):
                domain = [ReferenceScheme]
                range = [Characteristic]

            class isInVocabulary(ObjectProperty):
                domain = [SBVRConcept]
                range = [Vocabulary]

            class hasText(DataProperty):
                domain = [Text]
                range = [str]

            class hasName(DataProperty):
                domain = [SBVRConcept]
                range = [str]

            class hasCategorizationScheme(ObjectProperty):
                domain = [GeneralConcept]
                range = [CategorizationScheme]

            class hasCategorizationType(ObjectProperty):
                domain = [GeneralConcept]
                range = [CategorizationType]

            class hasObjectifiedVerbConcept(ObjectProperty):
                domain = [GeneralConcept]
                range = [VerbConcept]

            class hasConstrainingFormulation(ObjectProperty):
                domain = [Projection]
                range = [LogicalFormulation]

            class hasAuxiliaryVariable(ObjectProperty):
                domain = [Projection]
                range = [AuxiliaryVariable]

            class hasProjectionVariable(ObjectProperty):
                domain = [Projection]
                range = [Variable]

            class hasStatement(ObjectProperty):
                domain = [Meaning]
                range = [Statement]

            class incorporatesVocabulary(ObjectProperty):
                domain = [Vocabulary]
                range = [Vocabulary]

            class hasEnforcementLevel(ObjectProperty):
                domain = [Rule]
                range = [SBVRConcept]  # Assuming EnforcementLevel is a concept

            class hasModalFormulation(ObjectProperty):
                domain = [Rule]
                range = [LogicalFormulation]

            class hasProjectionPosition(DataProperty):
                domain = [Variable]
                range = [int]

            # Add more properties as needed based on the SBVR metamodel

        # Load SBVR metamodel from XML file
        tree = ET.parse('app/core/models/knowledge/ontology/sbvr.metamodel.xml')
        root = tree.getroot()

        for elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces={'xmi': 'http://www.omg.org/spec/XMI/20110701'}):
            class_name = elem.get('name')
            with sbvr_onto:
                new_class = types.new_class(class_name, (SBVRConcept,))

        return sbvr_onto

    async def generate_sbvr_ontology(self, business_description: str) -> Ontology:
        # Use the LLM to extract SBVR concepts from the business description
        prompt = f"Extract SBVR concepts, fact types, and rules from the following business description:\n\n{business_description}"
        response = await self.llm_service.get_completion(prompt)
        parsed_response = self._parse_llm_response(response)

        # Create a new ontology based on the SBVR metamodel
        world = World()
        domain_onto = world.get_ontology("http://example.com/domain-ontology")
        domain_onto.imported_ontologies.append(self.sbvr_ontology)

        with domain_onto:
            for concept in parsed_response.get('concepts', []):
                new_class = types.new_class(concept, (self.sbvr_ontology.Noun,))
                new_class.hasDefinition.append(parsed_response['definitions'].get(concept, ''))

            for fact_type in parsed_response.get('fact_types', []):
                new_fact = types.new_class(fact_type['name'], (self.sbvr_ontology.Fact,))
                verb_concept = types.new_class(fact_type['verb'], (self.sbvr_ontology.VerbConcept,))
                new_fact.hasFactType.append(verb_concept)
                for role in fact_type['roles']:
                    verb_concept.hasRole.append(domain_onto[role])

            for rule in parsed_response.get('rules', []):
                new_rule = types.new_class(rule['name'], (self.sbvr_ontology.Rule,))
                new_rule.hasDefinition.append(rule['definition'])

        return Ontology(world=world, ontology=domain_onto)

    async def validate_sbvr_ontology(self, ontology: Ontology) -> Dict[str, Any]:
        validation_result = {"is_valid": True, "issues": []}

        # Check if all required SBVR concepts are present
        required_concepts = ["Noun", "VerbConcept", "Fact", "Rule"]
        for concept in required_concepts:
            if not ontology.ontology.search_one(iri=f"*{concept}"):
                validation_result["is_valid"] = False
                validation_result["issues"].append(f"Required SBVR concept '{concept}' not found in the ontology")

        # Additional SBVR-specific validation checks
        # Check for presence of key SBVR elements
        key_elements = ["ObjectType", "IndividualConcept", "Characteristic", "AssociativeFactType", "AttributiveFactType"]
        for element in key_elements:
            if not ontology.ontology.search_one(iri=f"*{element}"):
                validation_result["issues"].append(f"Key SBVR element '{element}' not found in the ontology")

        # Validate VerbConcept structure
        verb_concepts = ontology.ontology.search(type=ontology.ontology.VerbConcept)
        for vc in verb_concepts:
            if not hasattr(vc, 'verbConceptWording') or not vc.verbConceptWording:
                validation_result["issues"].append(f"VerbConcept '{vc.name}' is missing verbConceptWording")
            if not hasattr(vc, 'verbConceptRole') or not vc.verbConceptRole:
                validation_result["issues"].append(f"VerbConcept '{vc.name}' is missing verbConceptRole")

        # Validate Rule structure
        rules = ontology.ontology.search(type=ontology.ontology.Rule)
        for rule in rules:
            if not hasattr(rule, 'hasDefinition') or not rule.hasDefinition:
                validation_result["issues"].append(f"Rule '{rule.name}' is missing definition")

        # Check for proper relationships
        if not ontology.ontology.search(type=ontology.ontology.hasFactType):
            validation_result["issues"].append("Missing 'hasFactType' relationship in the ontology")
        if not ontology.ontology.search(type=ontology.ontology.hasRole):
            validation_result["issues"].append("Missing 'hasRole' relationship in the ontology")

        # Validate cardinality constraints
        quantifications = ontology.ontology.search(type=ontology.ontology["at-least-nQuantification"]) + \
                          ontology.ontology.search(type=ontology.ontology["at-most-nQuantification"])
        for quant in quantifications:
            if not hasattr(quant, 'minimumCardinality') and not hasattr(quant, 'maximumCardinality'):
                validation_result["issues"].append(f"Quantification '{quant.name}' is missing cardinality constraint")

        if validation_result["issues"]:
            validation_result["is_valid"] = False

        return validation_result