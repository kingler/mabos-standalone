from openai import OpenAI
from pydantic import BaseModel

class QueryModel(BaseModel):
    query: str

class NLPService:
    def __init__(self):
        self.client = OpenAI()

    def translate_query(self, query: str) -> str:
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "Translate the following natural language query to AQL."},
                {"role": "user", "content": query}
            ],
            response_format=QueryModel
        )
        if hasattr(response.choices[0].message, 'refusal'):
            raise ValueError(response.choices[0].message.refusal)
        return response.choices[0].message.parsed.query