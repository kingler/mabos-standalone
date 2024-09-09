import asyncio
import logging
import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from app.api.dependencies import get_db_client
from app.utils.uuid_encoder import UUIDEncoder 
from concurrent.futures import ThreadPoolExecutor
import json

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return str(obj)
        return json.JSONEncoder.default(self, obj)

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
    is_current: bool = Field(default=True, description="Flag to indicate if this is the current business profile")
    
    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        d['id'] = str(d['id'])  # Convert UUID to string
        d['onboarding_date'] = d['onboarding_date'].isoformat()  # Convert datetime to ISO format string
        return d

    @classmethod
    async def create(cls, name: str, industry: str, employee_count: int, llm_agent) -> 'BusinessProfile':
        from app.tools.togaf_questions import generate_db_name
        
        profile = cls(
            name=name,
            industry=industry,
            employee_count=employee_count
        )
        profile.db_name = await generate_db_name(name, llm_agent)
        return profile

    @classmethod
    async def get_current(cls):
        db_client = get_db_client()
        thread_pool = ThreadPoolExecutor() 
        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                thread_pool,
                db_client.execute_query,
                "FOR doc IN business_profiles FILTER doc.is_current == true LIMIT 1 RETURN doc"
            )

            if result:
                return cls(**result[0])
            
            logging.info("No current business profile found. Creating a default one.")
            default_profile = cls(
                name="Default Business",
                industry="Technology",
                employee_count=1,
                is_current=True
            )
            # Insert the default profile in a separate thread
            await loop.run_in_executor(
                thread_pool,
                db_client.execute_query,
                "INSERT @profile INTO business_profiles",
                {"profile": default_profile.dict()}
            )
            return default_profile
        
        except Exception as e:
            logging.error(f"Error in get_current: {str(e)}")
            raise
        finally:
            db_client.close()  # Ensure we always close the connection

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class BusinessProfileDB(Base):
    __tablename__ = 'business_profiles'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    employee_count = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    website = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    onboarding_date = Column(DateTime, default=datetime.utcnow)
    db_name = Column(String, nullable=True)
    is_current = Column(Boolean, default=False)