from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AgentDB(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    # Add other fields

class ActionDB(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    # Add other fields

# Add other models as needed