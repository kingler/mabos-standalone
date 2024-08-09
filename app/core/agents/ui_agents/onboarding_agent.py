from arango import ArangoClientError
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from uuid import UUID, uuid4
from app.core.agents.core_agents.llm_agent import LLMAgent
from app.core.models.mdd.togaf_adm import TOGAFADM
from app.core.models.mdd.archimate_model import ArchiMateModel
from app.db.arango_db_client import ArangoDBClient

from app.core.services.mabos_service import MABOSService
from app.core.services.erp_service import ERPService
from app.core.models.erp.erp_models import ERPSystem, FinancialModule, HRModule, CRMModule, SupplyChainModule, InventoryModule, ProjectManagementModule, ManufacturingModule

class OnboardingQuestions(BaseModel):
    general_information: List[str] = Field(default_factory=list)
    business_architecture: List[str] = Field(default_factory=list)
    information_systems_architecture: List[str] = Field(default_factory=list)
    technology_architecture: List[str] = Field(default_factory=list)
    goal_modeling: List[str] = Field(default_factory=list)
    business_domain_ontology: List[str] = Field(default_factory=list)
    togaf_integration: List[str] = Field(default_factory=list)
    archimate_notation: List[str] = Field(default_factory=list)
    
class OnboardingAgent:
    def __init__(self, llm_agent: LLMAgent, db_client: ArangoDBClient, erp_service: ERPService, mabos_service: MABOSService):
        self.llm_agent = llm_agent
        self.togaf_adm = TOGAFADM()
        self.mabos_service = mabos_service
        self.erp_service = erp_service
        self.archimate_model = ArchiMateModel()
        self.db_client = db_client
        self.onboarding_questions = self._generate_onboarding_questions()
        self.answers = {}

    async def _retrieve_onboarding_questions(self) -> OnboardingQuestions:
        query = """
        FOR category IN togaf_questions
        COLLECT category_name = category.category INTO questions
        RETURN {
            [category_name]: questions[*].category.question
        }
        """ 
        result = await self.db_client.execute_query(query)
        
        questions = OnboardingQuestions()
        for category_dict in result:
            for category, category_questions in category_dict.items():
                setattr(questions, category, category_questions)
        
        return questions

    async def conduct_onboarding(self) -> Dict[str, Any]:
        business_type = await self._get_business_type()
        industry = await self._infer_industry(business_type)
    
        onboarding_data = {}
        for category, questions in self.onboarding_questions:
            category_data = await self._process_category(category, questions, industry)
        human_friendly_data = await self.llm_agent.generate_human_message(category_data)
        onboarding_data[category] = await self.llm_agent.interpret_human_message(human_friendly_data)

        processed_data = self._process_onboarding_data(onboarding_data)
        
        # Generate a human-friendly summary of the onboarding process
        summary = await self.llm_agent.generate_human_message(processed_data)
        print("Onboarding Summary:", summary)

        return processed_data

    async def _get_business_type(self) -> str:
        return await self.llm_agent.ask_question("What type of business are you onboarding?")

    async def _infer_industry(self, business_type: str) -> str:
        return await self.llm_agent.ask_question(f"Based on the business type '{business_type}', what industry does this belong to?")

    async def _process_category(self, category: str, questions: List[str], industry: str) -> Dict[str, str]:
        responses = {}
        for question in questions:
            initial_answer = await self._generate_initial_answer(category, question, industry)
            final_answer = await self._refine_answer(category, question, initial_answer)
            responses[question] = final_answer
        return responses

    async def _generate_initial_answer(self, category: str, question: str, industry: str) -> str:
        prompt = f"Given a {industry} business, provide an initial answer to the following {category} question: {question}"
        return await self.llm_agent.ask_question(prompt)

    async def _refine_answer(self, category: str, question: str, initial_answer: str) -> str:
        prompt = f"Review and refine the following answer to the {category} question '{question}': {initial_answer}"
        refined_answer = await self.llm_agent.ask_question(prompt)
        
        # Allow for manual editing or regeneration
        while True:
            user_choice = input(f"Accept this answer? (Y/N/R for regenerate): {refined_answer}\n")
            if user_choice.lower() == 'y':
                return refined_answer
            elif user_choice.lower() == 'n':
                manual_edit = input("Enter your edited answer: ")
                return manual_edit
            elif user_choice.lower() == 'r':
                refined_answer = await self._generate_initial_answer(category, question, self.answers.get('industry', ''))
            else:
                print("Invalid choice. Please enter Y, N, or R.")

    async def _ask_questions(self, category: str, questions: List[str]) -> Dict[str, str]:
        responses = {}
        for question in questions:
            response = await self.llm_agent.ask_question(f"{category}: {question}")
            responses[question] = response
        return responses

    def _process_onboarding_data(self, onboarding_data: Dict[str, Any]) -> Dict[str, Any]:
        processed_data = {
            "business_motivation_model": self._create_business_motivation_model(onboarding_data),
            "business_layer": self._create_business_layer(onboarding_data),
            "application_layer": self._create_application_layer(onboarding_data),
            "technology_layer": self._create_technology_layer(onboarding_data),
            "implementation_layer": self._create_implementation_layer(onboarding_data),
        }

        self.archimate_model.update(processed_data)
        self.togaf_adm.execute_phase("Preliminary", processed_data)
        self.togaf_adm.execute_phase("Vision", processed_data)

        return processed_data

    def _create_business_motivation_model(self, data: Dict[str, Any]) -> Dict[str, Any]:
        strategy_data = data["business_strategy"]
        return {
            "vision": strategy_data["What is the overall vision for your business?"],
            "goals": strategy_data["What are your key business goals and objectives?"],
            "stakeholders": strategy_data["Who are your main stakeholders?"],
            "drivers": strategy_data["What are the primary drivers for your business?"],
        }
        
    async def _process_onboarding_data(self, onboarding_data: Dict[str, Any]) -> Dict[str, Any]:
        processed_data = {
            "business_motivation_model": self._create_business_motivation_model(onboarding_data),
            "business_layer": self._create_business_layer(onboarding_data),
            "application_layer": self._create_application_layer(onboarding_data),
            "technology_layer": self._create_technology_layer(onboarding_data),
            "implementation_layer": self._create_implementation_layer(onboarding_data),
        }

        self.archimate_model.update(processed_data)
        self.togaf_adm.execute_phase("Preliminary", processed_data)
        self.togaf_adm.execute_phase("Vision", processed_data)

        # Create ERP system and modules
        erp_system = await self._create_erp_system(processed_data)

        return {**processed_data, "erp_system": erp_system.dict()}

    async def _create_erp_system(self, processed_data: Dict[str, Any]) -> ERPSystem:
        business_name = self.get_business_name()
        erp_system = await self.erp_service.create_erp_system(business_name)

        # Create and add ERP modules
        financial_module = await self._create_financial_module(processed_data)
        await self.erp_service.add_module(erp_system.id, financial_module)

        hr_module = await self._create_hr_module(processed_data)
        await self.erp_service.add_module(erp_system.id, hr_module)

        crm_module = await self._create_crm_module(processed_data)
        await self.erp_service.add_module(erp_system.id, crm_module)

        supply_chain_module = await self._create_supply_chain_module(processed_data)
        await self.erp_service.add_module(erp_system.id, supply_chain_module)

        inventory_module = await self._create_inventory_module(processed_data)
        await self.erp_service.add_module(erp_system.id, inventory_module)

        project_module = await self._create_project_module(processed_data)
        await self.erp_service.add_module(erp_system.id, project_module)

        manufacturing_module = await self._create_manufacturing_module(processed_data)
        await self.erp_service.add_module(erp_system.id, manufacturing_module)

        return await self.erp_service.get_erp_system(erp_system.id)

    async def _create_financial_module(self, processed_data: Dict[str, Any]) -> FinancialModule:
        business_layer = processed_data["business_layer"]
        return await self.erp_service.generate_module("financial", {
            "accounting_method": business_layer.get("accounting_method", "accrual"),
            "reporting_frequency": business_layer.get("financial_reporting_frequency", "monthly"),
            "description": "Financial management module"
        })

    async def _create_hr_module(self, processed_data: Dict[str, Any]) -> HRModule:
        business_layer = processed_data["business_layer"]
        return await self.erp_service.generate_module("hr", {
            "employee_count": business_layer.get("employee_count", 0),
            "payroll_frequency": business_layer.get("payroll_frequency", "monthly"),
            "description": "Human Resources management module"
        })    

    def _create_business_layer(self, data: Dict[str, Any]) -> Dict[str, Any]:
        business_data = data["business_layer"]
        return {
            "processes": business_data["What are the main business processes in your organization?"],
            "structure": business_data["Can you describe your organizational structure?"],
            "rules": business_data["What are the key business rules that govern your operations?"],
            "products_services": business_data["What are the main products or services you offer?"],
            "accounting_method": business_data.get("What accounting method do you use?", "accrual"),
            "financial_reporting_frequency": business_data.get("How often do you prepare financial reports?", "monthly"),
            "employee_count": business_data.get("How many employees do you have?", 0),
            "payroll_frequency": business_data.get("How often do you process payroll?", "monthly"),
        }

    def _create_application_layer(self, data: Dict[str, Any]) -> Dict[str, Any]:
        app_data = data["application_layer"]
        return {
            "applications": app_data["What are the main software applications used in your business?"],
            "support": app_data["How do these applications support your business processes?"],
            "integrations": app_data["Are there any integration points between your applications?"],
            "data_entities": app_data["What are the key data entities managed by your applications?"],
        }

    def _create_technology_layer(self, data: Dict[str, Any]) -> Dict[str, Any]:
        tech_data = data["technology_layer"]
        return {
            "infrastructure": tech_data["What is your current IT infrastructure?"],
            "cloud_services": tech_data["Are you using any cloud services? If so, which ones?"],
            "networking": tech_data["What networking technologies are you using?"],
            "data_management": tech_data["How do you manage data storage and backups?"],
        }

    def _create_implementation_layer(self, data: Dict[str, Any]) -> Dict[str, Any]:
        impl_data = data["implementation_layer"]
        return {
            "projects": impl_data["Do you have any ongoing or planned IT projects?"],
            "implementation_approach": impl_data["What is your approach to system implementation and deployment?"],
            "change_management": impl_data["How do you manage changes in your IT environment?"],
            "adoption_considerations": impl_data["What are your key considerations for technology adoption?"],
        }
    
    def create_mabos_agent(self, initial_config, business_domain_ontology):
        # Create a new MABOS agent using the MABOS API
        mabos_agent = self.mabos_api.create_agent(initial_config,business_domain_ontology)
        return mabos_agent

    def get_business_name(self):
        # Use a conversational interface to get the business name
        # Example:
        business_name = input("Enter your business name: ")
        return business_name

    def get_business_type(self):
        # Use a conversational interface to get the business type
        # Example:
        business_type = input("Enter your business type: ")
        return business_type

    def get_business_address(self):
        # Use a conversational interface to get the business address
        # Example:
        business_address = input("Enter your business address: ")
        return business_address

    def get_business_phone(self):
        # Use a conversational interface to get the business phone number
        # Example:
        business_phone = input("Enter your business phone number: ")
        return business_phone

    def get_business_email(self):
        # Use a conversational interface to get the business email    
        business_email = input("Enter your business email: ")
        return business_email