import asyncio
import datetime
import json
import logging
from pydantic import BaseModel, Field, SkipValidation
from typing import Dict, Any
import yaml
import os

from app.db.database import SessionLocal

from app.core.models.knowledge.knowledge_graph import KnowledgeGraph, KnowledgeGraphIntegrator
from app.core.models.knowledge.knowledge_base import KnowledgeBase
from app.core.models.knowledge.ontology.ontology import Ontology
from app.core.agents.core_agents.llm_agent import LLMAgent
from app.core.tools.llm_manager import LLMManager
from app.core.services.llm_service import LLMService
from app.core.models.knowledge.ontology.ontology_aligner import OntologyAligner
from app.core.models.knowledge.ontology.ontology_reasoner import OntologyReasoner
from app.core.models.knowledge.vocabulary_manager import VocabularyManager

class OntologyGenerator(BaseModel):
    llm_manager: LLMManager = Field(default_factory=LLMManager)
    llm_service: LLMService = Field(default_factory=LLMService)
    ontology: Ontology = Field(default_factory=Ontology)
    vocabulary: VocabularyManager = Field(default_factory=VocabularyManager)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, config_path: str = 'config/llm_config.yaml', **data):
        super().__init__(**data)
        self.config = self._load_config(config_path)
        api_key = self._get_api_key()  # Ensure API key is retrieved
        self.llm_manager = LLMManager(llms_config=self.config['llms'], api_key=api_key)
        self.llm_service = LLMService(self.llm_manager)# Pass correct arguments
        self.llm_agent = LLMAgent(agent_id="ontology_generator", name="Ontology Generator", 
                                  api_key=self._get_api_key(),
                                  llm_service=self.llm_service,
                                  agent_communication_service=None)

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        if not os.path.exists(config_path):
            print(f"Warning: Config file not found at {config_path}. Using default configuration.")
            return self._get_default_config()
        
        with open(config_path, 'r') as config_file:
            return yaml.safe_load(config_file)

    def _get_default_config(self) -> Dict[str, Any]:
        return {
            'llms': {
                'text_generation': {
                    'default': 'claude-3-opus-20240229',
                    'available': [
                        {
                            'claude-3-opus-20240229': {
                                'url': 'https://api.anthropic.com/v1/messages',
                                'max_tokens': 200000,
                                'output_tokens': 4096,
                                'temperature': 0.7,
                                'capabilities': ['multilingual', 'vision'],
                                'latency': 'moderately_fast',
                                'cost_input': 15.00,
                                'cost_output': 75.00
                            }
                        }
                    ]
                }
            },
            'api_keys': {
                'anthropic': 'ANTHROPIC_API_KEY',
                'openai': 'OPENAI_API_KEY',
                'groq': 'GROQ_API_KEY',
                'gemini': 'GEMINI_API_KEY'
            },
            'default_params': {
                'max_retries': 3,
                'timeout': 30,
                'retry_delay': 1,
                'max_tokens': 2048,
                'temperature': 0.7
            }
        }

    def _get_api_key(self) -> str:
        default_provider = self.config['llms']['text_generation']['default']
        for provider, key_name in self.config['api_keys'].items():
            if provider in default_provider:
                return os.environ.get(key_name, '')
        return ''

    async def generate_ontology(self, business_description: str) -> Ontology:
        prompt = f"""
        Given the following business description, generate an ontology structure:
        
        Business Description: {business_description}
        
        The ontology should include:
        1. Key concepts (classes)
        2. Relationships between concepts
        3. Properties of concepts
        
        Format the output as a JSON structure with the following schema:
        {{
            "concepts": {{
                "ConceptName": "ConceptDescription",
                ...
            }},
            "relationships": {{
                "RelationshipName": {{
                    "domain": "DomainConceptName",
                    "range": "RangeConceptName"
                }},
                ...
            }},
            "properties": {{
                "ConceptName": ["Property1", "Property2", ...],
                ...
            }}
        }}
        """
        
        selected_model = self.llm_manager.select_model("Generate ontology from business description", required_capabilities=["multilingual"])
        response = self.llm_manager.get_text_completion(prompt, model=selected_model)
        ontology_structure = self._parse_llm_response(response)
        
        ontology = Ontology()
        
        for concept, description in ontology_structure.get("concepts", {}).items():
            ontology.add_concept(concept, description)
        
        for relationship, details in ontology_structure.get("relationships", {}).items():
            ontology.add_relationship(relationship, details["domain"], details["range"])
        
        for concept, properties in ontology_structure.get("properties", {}).items():
            for property in properties:
                ontology.add_property(concept, property)
        
        return ontology

    def _parse_llm_response(self, response: str) -> Dict[str, Any]:
        import json
        try:
            # Attempt to parse the response as JSON
            parsed_response = json.loads(response)
            
            # Validate the structure of the parsed response
            required_keys = ["concepts", "relationships", "properties"]
            if not all(key in parsed_response for key in required_keys):
                raise ValueError("Response is missing one or more required keys")
            
            return parsed_response
        except json.JSONDecodeError:
            # If JSON parsing fails, log the error and return an empty dictionary
            logging.error(f"Failed to parse LLM response as JSON: {response}")
            return {}
        except ValueError as e:
            # If the structure is invalid, log the error and return an empty dictionary
            logging.error(f"Invalid response structure: {str(e)}")
            return {}

    async def refine_ontology(self, ontology: Ontology) -> Ontology:
        prompt = f"""
        Refine the following ontology to ensure consistency and completeness:

        {ontology.to_json()}

        Identify and resolve any:
        1. Inconsistencies in relationships
        2. Missing key concepts
        3. Redundant or overlapping concepts

        Provide the refined ontology in the same JSON format.
        """
        
        selected_model = self.llm_manager.select_model("Refine ontology", required_capabilities=["multilingual"])
        response = await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
        refined_ontology = self._parse_llm_response(response)
        return Ontology.from_json(refined_ontology)

    async def validate_ontology(self, ontology: Ontology) -> Dict[str, Any]:
        prompt = f"""
        Validate the following ontology:

        {ontology.to_json()}

        Check for:
        1. Logical consistency
        2. Completeness
        3. Adherence to ontology best practices

        Provide a validation report in JSON format with the following structure:
        {{
            "is_valid": boolean,
            "issues": [
                {{
                    "type": "issue_type",
                    "description": "issue_description",
                    "suggestion": "suggested_fix"
                }},
                ...
            ]
        }}
        """
        
        selected_model = self.llm_manager.select_model("Validate ontology", required_capabilities=["multilingual"])
        response = await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
        return json.loads(response)

class SBVROntologyGenerator(OntologyGenerator):
    async def generate_sbvr_ontology(self, business_description: str) -> Ontology:
        prompt = f"""
        Given the following business description, generate an SBVR-compliant ontology structure:
        
        Business Description: {business_description}
        
        The ontology should include:
        1. Business Vocabulary (terms, names, verb concept wordings)
        2. Business Rules (structural and operative)
        3. Concepts and their definitions
        4. Propositions
        
        Format the output as a JSON structure with the following schema:
        {{
            "vocabulary": {{
                "terms": {{"TermName": "Definition"}},
                "names": ["Name1", "Name2"],
                "verb_concept_wordings": ["Wording1", "Wording2"]
            }},
            "rules": {{
                "structural": ["Rule1", "Rule2"],
                "operative": ["Rule3", "Rule4"]
            }},
            "concepts": {{
                "ConceptName": "Definition"
            }},
            "propositions": ["Proposition1", "Proposition2"]
        }}
        """
        
        selected_model = self.llm_manager.select_model("Generate SBVR ontology from business description", required_capabilities=["multilingual"])
        response = await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
        sbvr_structure = self._parse_llm_response(response)
        
        ontology = Ontology()
        
        with self.sbvr_ontology:
            for term, definition in sbvr_structure.get("vocabulary", {}).get("terms", {}).items():
                new_term = Term(term)
                new_concept = Concept(term + "_concept")
                new_term.represents.append(new_concept)
                new_concept.hasDefinition.append(definition)
                ontology.add_concept(term, definition)
            
            for name in sbvr_structure.get("vocabulary", {}).get("names", []):
                Name(name)
            
            for wording in sbvr_structure.get("vocabulary", {}).get("verb_concept_wordings", []):
                VerbConceptWording(wording)
            
            for rule in sbvr_structure.get("rules", {}).get("structural", []):
                StructuralRule(rule)
            
            for rule in sbvr_structure.get("rules", {}).get("operative", []):
                OperativeRule(rule)
            
            for concept, definition in sbvr_structure.get("concepts", {}).items():
                new_concept = Concept(concept)
                new_concept.hasDefinition.append(definition)
                ontology.add_concept(concept, definition)
            
            for proposition in sbvr_structure.get("propositions", []):
                Proposition(proposition)
        
        return ontology

    async def validate_sbvr_ontology(self, ontology: Ontology) -> Dict[str, Any]:
        # Implement SBVR-specific validation
        validation_result = {"is_valid": True, "issues": []}
        
        # Check for required SBVR elements
        required_elements = ["Term", "Concept", "BusinessRule"]
        for element in required_elements:
            if not any(isinstance(entity, getattr(self.sbvr_ontology, element)) for entity in ontology.get_entities()):
                validation_result["is_valid"] = False
                validation_result["issues"].append(f"Missing required SBVR element: {element}")
        
        # Add more SBVR-specific validation checks here
        
        return validation_result

class OntologyVersionControl:
       def __init__(self, storage_backend):
           self.storage = storage_backend

       def save_version(self, ontology: Ontology, version: str, metadata: Dict[str, Any]):
           # Save ontology version with metadata
           serialized_ontology = ontology.to_json()
           version_data = {
               'ontology': serialized_ontology,
               'metadata': metadata,
               'version': version,
               'timestamp': datetime.now().isoformat()
           }
           self.storage.save(f'ontology_v{version}', json.dumps(version_data))
           logging.info(f"Saved ontology version {version} with metadata")

       def get_version(self, version: str) -> Ontology:
           # Retrieve specific version of ontology
           version_data = self.storage.load(f'ontology_v{version}')
           if version_data:
               data = json.loads(version_data)
               ontology = Ontology()
               ontology.from_json(data['ontology'])
               return ontology
           else:
               logging.warning(f"Ontology version {version} not found")
               return None

       def compare_versions(self, version1: str, version2: str) -> Dict[str, Any]:
           # Compare two versions and return differences
           ontology1 = self.get_version(version1)
           ontology2 = self.get_version(version2)
           
           if not ontology1 or not ontology2:
               return {"error": "One or both versions not found"}
           
           differences = {
               "concepts": {
                   "added": [],
                   "removed": [],
                   "modified": []
               },
               "relationships": {
                   "added": [],
                   "removed": [],
                   "modified": []
               },
               "properties": {
                   "added": [],
                   "removed": [],
                   "modified": []
               }
           }
           
           # Compare concepts
           concepts1 = set(ontology1.concepts.keys())
           concepts2 = set(ontology2.concepts.keys())
           differences["concepts"]["added"] = list(concepts2 - concepts1)
           differences["concepts"]["removed"] = list(concepts1 - concepts2)
           for concept in concepts1.intersection(concepts2):
               if ontology1.concepts[concept] != ontology2.concepts[concept]:
                   differences["concepts"]["modified"].append(concept)
           
           # Compare relationships
           relationships1 = set((r.source, r.target, r.type) for r in ontology1.relationships)
           relationships2 = set((r.source, r.target, r.type) for r in ontology2.relationships)
           differences["relationships"]["added"] = list(relationships2 - relationships1)
           differences["relationships"]["removed"] = list(relationships1 - relationships2)
           
           # Compare properties
           properties1 = set((p.name, p.concept, p.range) for p in ontology1.properties)
           properties2 = set((p.name, p.concept, p.range) for p in ontology2.properties)
           differences["properties"]["added"] = list(properties2 - properties1)
           differences["properties"]["removed"] = list(properties1 - properties2)
           
           return differences
       
class NaturalLanguageOntologyInterface:
       def __init__(self, llm_manager: LLMManager, ontology: Ontology):
           self.llm_manager = llm_manager
           self.ontology = ontology

       async def process_command(self, command: str) -> str:
           prompt = f"""
           Given the following ontology:

           {self.ontology.to_json()}

           Execute the following natural language command on the ontology:

           {command}

           Provide a description of the changes made or information retrieved, and return the updated ontology if applicable.
           """

           selected_model = self.llm_manager.select_model("Natural language ontology interface", required_capabilities=["multilingual"])
           response = await self.llm_manager.get_text_completion_async(prompt, model=selected_model)
           
           # Parse the response and update the ontology if necessary
           # Return a user-friendly message describing the action taken
           pass 
       
class OntologyManager(BaseModel):
    def __init__(self, llm_manager: LLMManager, storage_backend, graph_database, use_sbvr: bool = False):
        self.llm_manager = llm_manager
        self.generator = SBVROntologyGenerator(llm_manager) if use_sbvr else OntologyGenerator(llm_manager)
        self.version_control = OntologyVersionControl(storage_backend)
        self.graph_integrator = KnowledgeGraphIntegrator(graph_database)
        self.aligner = OntologyAligner(llm_manager)
        self.nl_interface = None
        self.reasoner = None

    async def create_ontology(self, business_description: str) -> Ontology:
        ontology = await self.generator.generate_ontology(business_description)
        refined_ontology = await self.generator.refine_ontology(ontology)
        validation_report = await self.generator.validate_ontology(refined_ontology)
        
        if validation_report['is_valid']:
            self.version_control.save_version(refined_ontology, "1.0", {"source": "initial_generation"})
            self.graph_integrator.ontology_to_graph(refined_ontology)
            self.nl_interface = NaturalLanguageOntologyInterface(self.llm_manager, refined_ontology)
            self.reasoner = OntologyReasoner(self.llm_manager, refined_ontology)
            return refined_ontology
        else:
            raise ValueError("Generated ontology failed validation")

    async def update_ontology(self, updates: Dict[str, Any]) -> Ontology:
        current_ontology = self.version_control.get_version("latest")
        updated_ontology = current_ontology.apply_updates(updates)
        validation_report = await self.generator.validate_ontology(updated_ontology)
        
        if validation_report['is_valid']:
            new_version = self.version_control.save_version(updated_ontology, "increment", {"source": "manual_update"})
            self.graph_integrator.update_graph_from_ontology(updated_ontology)
            self.nl_interface.ontology = updated_ontology
            self.reasoner.ontology = updated_ontology
            return updated_ontology
        else:
            raise ValueError("Updated ontology failed validation")

    async def process_nl_command(self, command: str) -> str:
        return await self.nl_interface.process_command(command)

    async def perform_reasoning(self, query: str) -> str:
        return await self.reasoner.answer_query(query)

# Usage example:
async def main():
    llm_manager = LLMManager()
    storage_backend = SessionLocal()  # Using the database session from database.py
    graph_database = KnowledgeGraph(KnowledgeBase())  # Using KnowledgeGraph from knowledge_graph.py with a KnowledgeBase from knowledge_base.py
    
    ontology_manager = OntologyManager(llm_manager, storage_backend, graph_database)
    
    initial_ontology = await ontology_manager.create_ontology("An e-commerce platform selling electronics")
    print("Initial ontology created:", initial_ontology)
    
    update_result = await ontology_manager.process_nl_command("Add a new concept 'Smartphone' as a subclass of 'Electronics'")
    print("Ontology updated:", update_result)
    
    reasoning_result = await ontology_manager.perform_reasoning("What are the potential relationships between 'Smartphone' and 'Customer'?")
    print("Reasoning result:", reasoning_result)

if __name__ == "__main__":
    asyncio.run(main())      