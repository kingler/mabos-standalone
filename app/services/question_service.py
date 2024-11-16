# app/services/question_service.py
from typing import List, Optional
from uuid import UUID

from app.models.knowledge.question_models import Answer, Question
from app.db.arango_db_client import ArangoDBClient


class QuestionService:
    def __init__(self, db_client: ArangoDBClient):
        self.db_client = db_client

    def create_question(self, question: Question) -> Question:
        """Create a new question."""
        collection = self.db_client.db.collection('questions')
        result = collection.insert(question.dict())
        return Question.from_db({'_key': result['_key'], **question.dict()})

    def get_question(self, question_id: UUID) -> Optional[Question]:
        """Get a question by ID."""
        collection = self.db_client.db.collection('questions')
        result = collection.get(str(question_id))
        return Question.from_db(result) if result else None

    def update_question(self, question: Question) -> Question:
        """Update an existing question."""
        collection = self.db_client.db.collection('questions')
        collection.update_match({'_key': str(question.id)}, question.dict())
        return question

    def delete_question(self, question_id: UUID) -> bool:
        """Delete a question by ID."""
        collection = self.db_client.db.collection('questions')
        try:
            collection.delete(str(question_id))
            return True
        except:
            return False

    def list_questions(self, framework: Optional[str] = None, category: Optional[str] = None) -> List[Question]:
        """List questions with optional filtering."""
        collection = self.db_client.db.collection('questions')
        
        # Build AQL query based on filters
        aql = "FOR q IN questions"
        filters = []
        if framework:
            filters.append(f"q.framework == '{framework}'")
        if category:
            filters.append(f"q.category == '{category}'")
            
        if filters:
            aql += " FILTER " + " AND ".join(filters)
            
        aql += " RETURN q"
        
        cursor = self.db_client.db.aql.execute(aql)
        return [Question.from_db(doc) for doc in cursor]

    def create_answer(self, answer: Answer) -> Answer:
        """Create a new answer."""
        collection = self.db_client.db.collection('answers')
        result = collection.insert(answer.dict())
        return Answer.from_db({'_key': result['_key'], **answer.dict()})

    def get_answers_for_business(self, business_id: UUID) -> List[Answer]:
        """Get all answers for a specific business."""
        collection = self.db_client.db.collection('answers')
        cursor = collection.find({'business_id': str(business_id)})
        return [Answer.from_db(doc) for doc in cursor]

    def seed_questions(self):
        """Seed the database with initial questions."""
        # TOGAF questions
        togaf_questions = [
            Question(category="Business Architecture", framework="TOGAF", text="What are the key business goals and objectives?"),
            Question(category="Data Architecture", framework="TOGAF", text="What are the main data entities in your organization?"),
            Question(category="Application Architecture", framework="TOGAF", text="What are the core business applications used in your organization?"),
            Question(category="Technology Architecture", framework="TOGAF", text="What is the current technology infrastructure?"),
        ]

        # CMMI questions
        cmmi_questions = [
            Question(category="Process Management", framework="CMMI", text="How do you define and improve your organizational processes?"),
            Question(category="Project Management", framework="CMMI", text="How do you plan and monitor projects?"),
            Question(category="Engineering", framework="CMMI", text="How do you manage requirements and technical solutions?"),
            Question(category="Support", framework="CMMI", text="How do you measure and analyze process performance?"),
        ]

        # BMC questions
        bmc_questions = [
            Question(category="Value Propositions", framework="BMC", text="What value do you deliver to the customer?"),
            Question(category="Customer Segments", framework="BMC", text="Who are your most important customers?"),
            Question(category="Channels", framework="BMC", text="Through which channels do your customer segments want to be reached?"),
            Question(category="Revenue Streams", framework="BMC", text="For what value are your customers willing to pay?"),
        ]

        all_questions = togaf_questions + cmmi_questions + bmc_questions
        for question in all_questions:
            self.create_question(question)
