from pydantic import BaseModel, Field
from typing import List

class OnboardingQuestions(BaseModel):
    general_information: List[str] = Field(default_factory=list)
    business_architecture: List[str] = Field(default_factory=list)
    information_systems_architecture: List[str] = Field(default_factory=list)
    technology_architecture: List[str] = Field(default_factory=list)
    goal_modeling: List[str] = Field(default_factory=list)
    business_domain_ontology: List[str] = Field(default_factory=list)
    togaf_integration: List[str] = Field(default_factory=list)
    archimate_notation: List[str] = Field(default_factory=list)

from typing import List, Dict
from arango import ArangoClient

# Connect to ArangoDB
client = ArangoClient(hosts='http://localhost:8529')
db = client.db('mabos_db', username='root', password='password')

# Create collections for questions and answers
questions_collection = db.create_collection('togaf_questions')
answers_collection = db.create_collection('togaf_answers')

# Define the question categories and questions
onboarding_questions = {
    "general_information": [
        "What is the name and description of your organization?",
        "Who are the key stakeholders in your organization?",
        "What are the primary business goals and objectives of your organization?",
        "Can you describe your organizational structure?",
        "What are the core business processes within your organization?"
    ],
    "business_architecture": [
        "What are the key business functions in your organization?",
        "Can you describe the roles and responsibilities within your organization?",
        "What are the primary business services offered by your organization?",
        "What are the critical success factors for your business?",
        "How do you measure business performance (KPIs)?"
    ],
    "information_systems_architecture": [
        "What are the main applications and systems used in your organization?",
        "How are data and information managed within your organization?",
        "What are the key information flows between systems and processes?",
        "Can you describe the integration points between different systems?",
        "What are the data security and privacy requirements?"
    ],
    "technology_architecture": [
        "What is the current technology infrastructure of your organization?",
        "What are the key technology components and platforms used?",
        "How do you manage and maintain your IT infrastructure?",
        "What are the main challenges in your current technology landscape?",
        "What emerging technologies are you considering?"
    ],
    "goal_modeling": [
        "What are the strategic goals of your organization?",
        "What are the tactical and operational goals?",
        "How do these goals align with the overall business objectives?",
        "What are the drivers and motivations behind these goals?",
        "What are the constraints and risks associated with achieving these goals?"
    ],
    "business_domain_ontology": [
        "What are the key concepts and entities in your business domain?",
        "Can you describe the relationships between these entities?",
        "What specific terminology is used in your business domain?",
        "Can you describe the main business processes in your domain?",
        "What are the business rules and policies governing your domain?"
    ],
    "togaf_integration": [
        "How do you currently approach architecture development?",
        "What phases of the TOGAF ADM are most relevant to your organization?",
        "How do you integrate architecture deliverables into your project lifecycle?",
        "What tools and techniques do you use for architecture modeling?"
    ],
    "archimate_notation": [
        "What elements of the ArchiMate language are you familiar with?",
        "How do you use ArchiMate for visualizing architecture models?",
        "What are the common structural, behavioral, and motivational elements you use?",
        "How do you ensure consistency and accuracy in your ArchiMate models?"
    ]
}

# Function to seed the questions into the database
def seed_questions():
    for category, questions in onboarding_questions.items():
        for question in questions:
            questions_collection.insert({'category': category, 'question': question})

# Function to create a new question
def create_question(category: str, question: str):
    questions_collection.insert({'category': category, 'question': question})

# Function to retrieve all questions
def get_all_questions() -> List[Dict]:
    return questions_collection.all()

# Function to retrieve questions by category
def get_questions_by_category(category: str) -> List[Dict]:
    return questions_collection.find({'category': category})

# Function to update a question
def update_question(question_id: str, category: str, question: str):
    questions_collection.update({'_id': question_id}, {'category': category, 'question': question})

# Function to delete a question
def delete_question(question_id: str):
    questions_collection.delete({'_id': question_id})

# Function to create an answer
def create_answer(question_id: str, answer: str):
    answers_collection.insert({'question_id': question_id, 'answer': answer})

# Function to retrieve answers for a question
def get_answers_for_question(question_id: str) -> List[Dict]:
    return answers_collection.find({'question_id': question_id})

# Function to update an answer
def update_answer(answer_id: str, answer: str):
    answers_collection.update({'_id': answer_id}, {'answer': answer})

# Function to delete an answer
def delete_answer(answer_id: str):
    answers_collection.delete({'_id': answer_id})

# Seed the questions into the database
seed_questions()