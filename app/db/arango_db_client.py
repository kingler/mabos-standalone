from typing import List, Dict, Any, Optional
from arango import ArangoClient
from click import UUID
from app.core.models.knowledge.question_models import Question, Answer

class ArangoDBClient:
    def __init__(self, host: str, port: int, username: str, password: str, database: str):
        self.client = ArangoClient(hosts=f"http://{host}:{port}")
        self.db = self.client.db(database, username=username, password=password)

    async def execute_query(self, query: str, bind_vars: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        cursor = await self.db.aql.execute(query, bind_vars=bind_vars)
        return [doc async for doc in cursor]
    
    async def create_question(self, question: Question) -> Question:
        question_dict = question.dict()
        result = await self.db.collection('questions').insert(question_dict)
        question_dict['_key'] = result['_key']
        return Question(**question_dict)

async def get_question(self, question_id: UUID) -> Optional[Question]:
    result = await self.db.collection('questions').get(str(question_id))
    return Question(**result) if result else None

async def update_question(self, question: Question) -> Question:
    question_dict = question.dict()
    await self.db.collection('questions').update(str(question.id), question_dict)
    return question

async def delete_question(self, question_id: UUID) -> bool:
    try:
        await self.db.collection('questions').delete(str(question_id))
        return True
    except:
        return False

async def list_questions(self, framework: Optional[str] = None, category: Optional[str] = None) -> List[Question]:
    query = "FOR q IN questions"
    if framework or category:
        query += " FILTER "
        conditions = []
        if framework:
            conditions.append(f"q.framework == '{framework}'")
        if category:
            conditions.append(f"q.category == '{category}'")
        query += " AND ".join(conditions)
    query += " RETURN q"
    cursor = await self.db.aql.execute(query)
    return [Question(**doc) for doc in await cursor.all()]

async def create_answer(self, answer: Answer) -> Answer:
    answer_dict = answer.dict()
    result = await self.db.collection('answers').insert(answer_dict)
    answer_dict['_key'] = result['_key']
    return Answer(**answer_dict)

async def get_answers_for_business(self, business_id: UUID) -> List[Answer]:
    query = f"FOR a IN answers FILTER a.business_id == '{business_id}' RETURN a"
    cursor = await self.db.aql.execute(query)
    return [Answer(**doc) for doc in await cursor.all()]