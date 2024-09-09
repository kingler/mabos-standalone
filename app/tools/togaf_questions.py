from typing import Dict, List

from arango import ArangoClient
from pydantic import BaseModel, ConfigDict, Field

from app.config.config import CONFIG
from app.agents.core_agents.llm_agent import LLMAgent  # Assuming you have this import

from datetime import datetime

class OnboardingQuestions(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    general_information: List[str] = Field(default_factory=list)
    business_architecture: List[str] = Field(default_factory=list)
    information_systems_architecture: List[str] = Field(default_factory=list)
    technology_architecture: List[str] = Field(default_factory=list)
    goal_modeling: List[str] = Field(default_factory=list)
    business_domain_ontology: List[str] = Field(default_factory=list)
    togaf_integration: List[str] = Field(default_factory=list)
    archimate_notation: List[str] = Field(default_factory=list)

onboarding_questions = OnboardingQuestions(
    general_information=[
        "What is your organization's name?",
        "What industry does your organization operate in?",
        "How many employees does your organization have?",
    ],
    # ... (other categories of questions)
)

async def generate_db_name(business_name: str, llm_agent: LLMAgent) -> str:
    # Generate a shortened version of the business name
    prompt = f"Generate a short, alphanumeric abbreviation (max 10 characters) for the business name: {business_name}"
    business_name_shorthand = await llm_agent.generate_response(prompt)
    business_name_shorthand = ''.join(e for e in business_name_shorthand if e.isalnum())[:10]
    
    # Get current date for onboarding
    onboarding_date = datetime.now().strftime("%Y%m%d")
    
    # Construct the database name
    db_name = f"{business_name_shorthand}_{onboarding_date}_db"
    return db_name.lower()

async def create_database_and_collections(business_name: str, llm_agent: LLMAgent):
    client = ArangoClient(hosts=CONFIG.ARANGO_HOST)
    sys_db = client.db('_system', username=CONFIG.ARANGO_USERNAME, password=CONFIG.ARANGO_PASSWORD)
    
    db_name = await generate_db_name(business_name, llm_agent)
    if not sys_db.has_database(db_name):
        sys_db.create_database(db_name)
    
    db = client.db(db_name, username=CONFIG.ARANGO_USERNAME, password=CONFIG.ARANGO_PASSWORD)
    
    if not db.has_collection('togaf_questions'):
        db.create_collection('togaf_questions')
    if not db.has_collection('togaf_answers'):
        db.create_collection('togaf_answers')
    
    return db

def seed_questions(db):
    questions_collection = db.collection('togaf_questions')
    for category, questions in onboarding_questions.dict().items():
        for question in questions:
            questions_collection.insert({'category': category, 'question': question})

async def get_all_questions(db) -> Dict[str, List[str]]:
    questions_collection = db.collection('togaf_questions')
    cursor = await questions_collection.all()
    questions = {}
    async for doc in cursor:
        category = doc['category']
        question = doc['question']
        if category not in questions:
            questions[category] = []
        questions[category].append(question)
    return questions