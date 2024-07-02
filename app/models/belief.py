from pydantic import BaseModel, Field

class Belief(BaseModel):
    description: str = Field(..., description="Description of the belief")
    certainty: float = Field(..., ge=0, le=1, description="Certainty level of the belief (0-1)")
    
    def update_certainty(self, new_certainty: float):
        self.certainty = max(0, min(new_certainty, 1))  # Ensure certainty stays between 0 and 1