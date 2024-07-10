# app/services/question_service.py
from typing import List, Optional
from uuid import UUID
from app.models.question_models import Question, Answer
from app.db.arango_db_client import ArangoDBClient

class QuestionService:
    def __init__(self, db_client: ArangoDBClient):
        self.db_client = db_client

    async def create_question(self, question: Question) -> Question:
        return await self.db_client.create_question(question)

    async def get_question(self, question_id: UUID) -> Optional[Question]:
        return await self.db_client.get_question(question_id)

    async def update_question(self, question: Question) -> Question:
        return await self.db_client.update_question(question)

    async def delete_question(self, question_id: UUID) -> bool:
        return await self.db_client.delete_question(question_id)

    async def list_questions(self, framework: Optional[str] = None, category: Optional[str] = None) -> List[Question]:
        return await self.db_client.list_questions(framework, category)

    async def create_answer(self, answer: Answer) -> Answer:
        return await self.db_client.create_answer(answer)

    async def get_answers_for_business(self, business_id: UUID) -> List[Answer]:
        return await self.db_client.get_answers_for_business(business_id)

    async def seed_questions(self):
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
            await self.create_question(question)