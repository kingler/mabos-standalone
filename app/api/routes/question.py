# app/routers/question_router.py
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.core.dependencies import get_question_service
from app.core.models.knowledge.question_models import Answer, Question
from app.core.services.question_service import QuestionService

router = APIRouter()

@router.post("/questions", response_model=Question)
async def create_question(question: Question, service: QuestionService = Depends(get_question_service)):
    return await service.create_question(question)

@router.get("/questions/{question_id}", response_model=Question)
async def get_question(question_id: UUID, service: QuestionService = Depends(get_question_service)):
    question = await service.get_question(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.put("/questions/{question_id}", response_model=Question)
async def update_question(question_id: UUID, question: Question, service: QuestionService = Depends(get_question_service)):
    updated_question = await service.update_question(question)
    if not updated_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return updated_question

@router.delete("/questions/{question_id}")
async def delete_question(question_id: UUID, service: QuestionService = Depends(get_question_service)):
    success = await service.delete_question(question_id)
    if not success:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}

@router.get("/questions", response_model=List[Question])
async def list_questions(framework: Optional[str] = None, category: Optional[str] = None, service: QuestionService = Depends(get_question_service)):
    return await service.list_questions(framework, category)

@router.post("/answers", response_model=Answer)
async def create_answer(answer: Answer, service: QuestionService = Depends(get_question_service)):
    return await service.create_answer(answer)

@router.get("/answers/{business_id}", response_model=List[Answer])
async def get_answers_for_business(business_id: UUID, service: QuestionService = Depends(get_question_service)):
    return await service.get_answers_for_business(business_id)

@router.post("/seed-questions")
async def seed_questions(service: QuestionService = Depends(get_question_service)):
    await service.seed_questions()
    return {"message": "Questions seeded successfully"}