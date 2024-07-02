from pydantic import BaseModel
from typing import Optional

class Desire(BaseModel):
    desire_id: str
    description: str
    priority: float
    status: Optional[str] = "active"

    class Config:
        from_attributes = True

    def activate_desire(self):
        self.status = "active"

    def suspend_desire(self):
        self.status = "suspended"

    def complete_desire(self):
        self.status = "completed"

    def update_status(self, new_status: str):
        self.status = new_status