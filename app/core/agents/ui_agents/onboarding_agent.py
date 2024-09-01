import asyncio
from typing import Any, Dict

from pydantic import BaseModel, ConfigDict, Field, SkipValidation

from app.core.agents.core_agents.llm_agent import LLMAgent
from app.core.models.mdd.archimate_model import ArchiMateModel
from app.core.models.mdd.togaf_adm import TOGAFADM
from app.core.services.erp_service import ERPService
from app.core.services.mabos_service import MABOSService
from app.core.utils.file_utils import load_csv, load_markdown
from app.db.arango_db_client import ArangoDBClient
from app.db.togaf_questions import (OnboardingQuestions,
                                    create_database_and_collections,
                                    get_all_questions, seed_questions)
from config.config import CONFIG


class OnboardingAgent(BaseModel):
    """Agent responsible for conducting the onboarding process for new businesses."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    llm_agent: LLMAgent
    db_client: SkipValidation[ArangoDBClient]
    erp_service: ERPService
    mabos_service: MABOSService
    togaf_adm: TOGAFADM = Field(default_factory=TOGAFADM)
    archimate_model: ArchiMateModel = Field(default_factory=ArchiMateModel)
    onboarding_questions: OnboardingQuestions = Field(default_factory=OnboardingQuestions)
    naics_codes: Dict[str, str] = Field(default_factory=dict)
    _test_mode: bool = False
    _test_input: list[str] = []

    @classmethod
    async def create(cls, llm_agent: LLMAgent, db_client: ArangoDBClient, erp_service: ERPService, mabos_service: MABOSService):
        """Asynchronous factory method to create and initialize OnboardingAgent."""
        agent = cls(
            llm_agent=llm_agent,
            db_client=db_client,
            erp_service=erp_service,
            mabos_service=mabos_service
        )
        await agent.initialize()
        return agent

    async def initialize(self):
        """Initialize the agent by loading NAICS codes."""
        try:
            self.naics_codes = await load_csv(CONFIG.NAICS_CODES_PATH)
        except Exception as e:
            print(f"Error loading NAICS codes: {e}")

    async def conduct_onboarding(self, use_example: bool = False) -> Dict[str, Any]:
        if use_example:
            business_data = await self._load_example_business()
        else:
            business_data = await self._collect_business_information()
        
        # Create database and seed questions
        db = create_database_and_collections(business_data['your_business_name'])
        seed_questions(db)
        self.db_client.update_connection(db)
        
        # Now use the new database connection to get questions
        questions = await get_all_questions(db)
        
        business_description = await self.llm_agent.generate_business_description(business_data)
        business_data['business_description'] = business_description

        ontology = await self._generate_ontology(business_data)
        business_data['ontology'] = ontology

        return business_data

    async def _load_example_business(self) -> Dict[str, Any]:
        """Load example business data from markdown file."""
        try:
            description = await load_markdown(CONFIG.BUSINESS_DESCRIPTION_PATH)
            return {'business_description': description}
        except Exception as e:
            print(f"Error loading example business: {e}")
            return {}

    async def _collect_business_information(self) -> Dict[str, Any]:
        """Collect initial business information through manual input."""
        business_data = {}
        print("Please provide the following information about your business:")
        for question in CONFIG.INITIAL_QUESTIONS:
            answer = await self._ask_question(question)
            key = question.replace("What is ", "").replace("?", "").strip().lower().replace(" ", "_")
            business_data[key] = answer
        
        business_data['naics_code'] = self.naics_codes.get(business_data.get('your_business_industry', ''), 'Not found')
        
        await self._ask_togaf_questions(business_data)
        return business_data

    async def _ask_togaf_questions(self, business_data: Dict[str, Any]):
        """Ask TOGAF questions and store answers."""
        try:
            all_questions = await get_all_questions()
            for category, questions in all_questions.items():
                business_data[category] = {}
                for question in questions:
                    answer = await self._ask_question(question, allow_skip=True)
                    if answer.lower() != 'skip':
                        business_data[category][question] = answer
        except Exception as e:
            print(f"Error asking TOGAF questions: {e}")

    async def _generate_business_description(self, business_data: Dict[str, Any]) -> str:
        """Generate business description using LLM manager."""
        try:
            return await self.llm_agent.generate_business_description(business_data)
        except Exception as e:
            print(f"Error generating business description: {e}")
            return ""

    async def _ask_question(self, question: str, allow_skip: bool = False) -> str:
        """Ask a question using the terminal interface and return the answer."""
        skip_text = " (type 'skip' to skip this question)" if allow_skip else ""
        print(f"\n{question}{skip_text}")
        
        if self._test_mode:
            return self._test_input.pop(0) if self._test_input else ""
        
        while True:
            answer = input("Your answer: ").strip()
            if answer or (allow_skip and answer.lower() == 'skip'):
                return answer
            print("Please provide an answer.")

    async def _generate_ontology(self, business_data: Dict[str, Any]):
        """Generate business domain ontology using LLM manager."""
        prompt = f"Based on the following business information, generate a business domain ontology:\n\n{business_data}"
        return await self.llm_agent.generate_response(prompt)

    async def create_mabos_agent(self, initial_config: Dict[str, Any], business_domain_ontology: Dict[str, Any]) -> Any:
        """Create a new MABOS agent using the MABOS service."""
        try:
            return await self.mabos_service.create_agent(initial_config, business_domain_ontology)
        except Exception as e:
            print(f"Error creating MABOS agent: {e}")
            return None