from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.core.models.knowledge.knowledge_base import KnowledgeBase, KnowledgeItem
from app.core.services.knowledge_base_service import KnowledgeBaseService

router = APIRouter()
knowledge_service = KnowledgeBaseService()

@router.post("/knowledge_bases/", response_model=KnowledgeBase)
async def create_knowledge_base():
    return knowledge_service.create_knowledge_base()

@router.get("/knowledge_bases/{kb_id}", response_model=KnowledgeBase)
async def get_knowledge_base(kb_id: str):
    if not (kb := knowledge_service.get_knowledge_base(kb_id)):
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return kb

@router.get("/knowledge_bases/", response_model=List[KnowledgeBase])
async def list_knowledge_bases():
    return knowledge_service.list_knowledge_bases()

@router.post("/knowledge_bases/{kb_id}/symbolic", response_model=KnowledgeBase)
async def add_symbolic_knowledge(kb_id: str, item: KnowledgeItem):
    kb = knowledge_service.add_symbolic_knowledge(kb_id, item)
    if not kb:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return kb

@router.post("/knowledge_bases/{kb_id}/neural", response_model=KnowledgeBase)
async def add_neural_knowledge(kb_id: str, item: KnowledgeItem):
    kb = knowledge_service.add_neural_knowledge(kb_id, item)
    if not kb:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return kb

@router.post("/knowledge_bases/{kb_id}/query")
async def query_knowledge_base(kb_id: str, query: str):
    result = knowledge_service.query_knowledge_base(kb_id, query)
    if result is None:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return result

@router.post("/knowledge_bases/{kb_id}/reason")
async def reason(kb_id: str, context: Dict[str, Any]):
    result = knowledge_service.reason(kb_id, context)
    if result is None:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return result

@router.post("/knowledge_bases/{kb_id}/simulate")
async def simulate_action(kb_id: str, action: str, state: Dict[str, Any]):
    result = knowledge_service.simulate_action(kb_id, action, state)
    if result is None:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return result

@router.post("/knowledge_bases/{kb_id}/plan")
async def generate_plan(kb_id: str, goal: str, initial_state: Dict[str, Any]):
    result = knowledge_service.generate_plan(kb_id, goal, initial_state)
    if result is None:
        raise HTTPException(status_code=404, detail="Knowledge base not found")
    return result