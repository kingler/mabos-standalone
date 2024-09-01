from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4

class BusinessProfile(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the business profile")
    name: str = Field(..., description="The name of the business")
    industry: str = Field(..., description="The industry the business operates in")
    employee_count: int = Field(..., description="The number of employees in the organization")
    description: Optional[str] = Field(None, description="A brief description of the business")
    website: Optional[str] = Field(None, description="The business website URL")
    contact_email: Optional[str] = Field(None, description="The primary contact email for the business")
    onboarding_date: datetime = Field(default_factory=datetime.now, description="Date when the business was onboarded")
    db_name: Optional[str] = Field(None, description="The name of the database associated with this business")

    @classmethod
    async def create(cls, name: str, industry: str, employee_count: int, llm_agent) -> 'BusinessProfile':
        from app.core.services.db.togaf_questions import generate_db_name
        
        profile = cls(
            name=name,
            industry=industry,
            employee_count=employee_count
        )
        profile.db_name = await generate_db_name(name, llm_agent)
        return profile

    @classmethod
    async def get_current(cls) -> 'BusinessProfile':
        from app.core.services.database_service import DatabaseService
        from app.config.config import get_settings

        settings = get_settings()
        db_service = DatabaseService(settings.database_url)

        # Retrieve the current business profile from the database
        profile_data = await db_service.get_current_business_profile()

        if profile_data:
            return cls(**profile_data)
        else:
            # If no profile is found, return a default profile
            return cls(name="Default Business", industry="Technology", employee_count=100)
