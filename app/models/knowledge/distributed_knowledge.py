from typing import Any, Dict, List
from pydantic import BaseModel, Field
from openai import OpenAI
from app.db.db_integration import DatabaseIntegration

class KnowledgeItem(BaseModel):
    key: str
    value: Any
    metadata: Dict[str, Any] = Field(default_factory=dict)

class QueryResult(BaseModel):
    items: List[KnowledgeItem]
    total_count: int

class ProcessingResult(BaseModel):
    result: Any
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DistributedKnowledge:
    def __init__(self, db_integration: DatabaseIntegration):
        self.db_integration = db_integration
        self.client = OpenAI()

    async def store_distributed(self, data: Dict[str, Any]):
        knowledge_item = KnowledgeItem(key=data['key'], value=data['value'], metadata=data.get('metadata', {}))
        await self.db_integration.insert_one('distributed_knowledge', knowledge_item.dict())

    async def retrieve_distributed(self, query: str) -> List[Dict[str, Any]]:
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a distributed knowledge retrieval system. Parse the query and return relevant items."},
                {"role": "user", "content": query}
            ],
            response_format=QueryResult
        )

        if hasattr(completion.choices[0].message, 'refusal'):
            print(completion.choices[0].message.refusal)
            return []
        
        result = completion.choices[0].message.parsed
        retrieved_items = await self.db_integration.find('distributed_knowledge', 
                                                         {'key': {'$in': [item.key for item in result.items]}})
        return retrieved_items

    async def process_distributed(self, operation: str, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        completion = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": f"You are a distributed knowledge processing system. Perform the {operation} operation on the given data."},
                {"role": "user", "content": str(data)}
            ],
            response_format=ProcessingResult
        )

        if hasattr(completion.choices[0].message, 'refusal'):
            print(completion.choices[0].message.refusal)
            return {}
        
        result = completion.choices[0].message.parsed
        return result.dict()