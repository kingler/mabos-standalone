import json
import uuid

from app.models.business.business_model import BusinessModel
from app.models.openai_client import openai_client


class BusinessModelService:
    async def generate_model(self, model_type: str, description: str) -> BusinessModel:
        response = await openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Generate a {model_type} based on the given business description. Output should be in JSON format with 'nodes' and 'edges' fields."},
                {"role": "user", "content": description}
            ]
        )
        model_data = json.loads(response.choices[0].message.content)
        return BusinessModel(id=str(uuid.uuid4()), type=model_type, **model_data)

    def get_model(self, model_id: str) -> BusinessModel:
        if model_data := self.db.get_business_model(model_id):
            return BusinessModel(**model_data)
        return None

    def update_model(self, model_id: str, model: BusinessModel) -> BusinessModel:
        if existing_model := self.db.get_business_model(model_id):
            updated_model_data = {**existing_model, **model.dict(exclude_unset=True)}
            self.db.update_business_model(model_id, updated_model_data)
            return BusinessModel(**updated_model_data)
        return None
