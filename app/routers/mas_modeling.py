from fastapi import APIRouter
from app.core.openai_client import openai_client
import json
from uuid import uuid

router = APIRouter()

@router.post("/generate-model")
async def generate_mas_model(prompt: str):
    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Generate a Multi-Agent System (MAS) model based on the given prompt. Output should be in JSON format with 'nodes' and 'edges' fields."},
            {"role": "user", "content": prompt}
        ]
    )
    model_data = json.loads(response.choices[0].message.content)
    return {"id": str(uuid.uuid4()), "type": "MAS", "nodes": model_data["nodes"], "edges": model_data["edges"]}
