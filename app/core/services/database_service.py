from typing import TYPE_CHECKING, List, Optional

from sqlalchemy.orm import Session

from app.core.models.agent.action import Action, ActionDB
from app.core.models.agent.agent import Agent
from app.db.database import get_db

if TYPE_CHECKING:
    from app.core.agents.meta_agents.database_agent import AgentDB

class DatabaseService:
    def __init__(self):
        self.db: Session = next(get_db())

    def create_action(self, action: Action) -> Action:
        db_action = ActionDB(**action.dict())
        self.db.add(db_action)
        self.db.commit()
        self.db.refresh(db_action)
        return Action.from_orm(db_action)

    def get_all_actions(self) -> List[Action]:
        return [Action.from_orm(action) for action in self.db.query(ActionDB).all()]

    def get_action(self, action_id: str) -> Optional[Action]:
        db_action = self.db.query(ActionDB).filter(ActionDB.id == action_id).first()
        return Action.from_orm(db_action) if db_action else None

    def update_action(self, action: Action) -> Action:
        db_action = self.db.query(ActionDB).filter(ActionDB.id == action.id).first()
        if db_action:
            for key, value in action.dict().items():
                setattr(db_action, key, value)
            self.db.commit()
            self.db.refresh(db_action)
        return Action.from_orm(db_action)

    def delete_action(self, action_id: str) -> bool:
        db_action = self.db.query(ActionDB).filter(ActionDB.id == action_id).first()
        if db_action:
            self.db.delete(db_action)
            self.db.commit()
            return True
        return False

    def create_agent(self, agent: Agent) -> Agent:
        db_agent = AgentDB(**agent.dict())
        self.db.add(db_agent)
        self.db.commit()
        self.db.refresh(db_agent)
        return Agent.from_orm(db_agent)

    def get_all_agents(self) -> List[Agent]:
        return [Agent.from_orm(agent) for agent in self.db.query(AgentDB).all()]

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        db_agent = self.db.query(AgentDB).filter(AgentDB.id == agent_id).first()
        return Agent.from_orm(db_agent) if db_agent else None

    def update_agent(self, agent: Agent) -> Agent:
        db_agent = self.db.query(AgentDB).filter(AgentDB.id == agent.id).first()
        if db_agent:
            for key, value in agent.dict().items():
                setattr(db_agent, key, value)
            self.db.commit()
            self.db.refresh(db_agent)
        return Agent.from_orm(db_agent)

    def delete_agent(self, agent_id: str) -> bool:
        db_agent = self.db.query(AgentDB).filter(AgentDB.id == agent_id).first()
        if db_agent:
            self.db.delete(db_agent)
            self.db.commit()
            return True
        return False