from typing import List, Optional
from uuid import UUID, uuid4

from app.core.models.agent.intention import (Intention, IntentionCreate,
                                             IntentionUpdate)
from app.core.services.goal_service import GoalService
from app.core.services.plan_service import PlanService


class IntentionService:
    def __init__(self, goal_service: GoalService, plan_service: PlanService):
        self.intentions: dict[UUID, Intention] = {}
        self.goal_service = goal_service
        self.plan_service = plan_service

    def create_intention(self, intention_create: IntentionCreate) -> Intention:
        goal = self.goal_service.get_goal(intention_create.goal_id)
        if not goal:
            raise ValueError("Goal not found")
        
        plan = None
        if intention_create.plan_id:
            plan = self.plan_service.get_plan(intention_create.plan_id)
            if not plan:
                raise ValueError("Plan not found")
        
        intention_id = uuid4()
        intention = Intention(id=intention_id, goal=goal, plan=plan)
        self.intentions[intention_id] = intention
        return intention

    def get_intentions(self) -> List[Intention]:
        return list(self.intentions.values())

    def get_intention(self, intention_id: UUID) -> Optional[Intention]:
        return self.intentions.get(intention_id)

    def update_intention(self, intention_id: UUID, intention_update: IntentionUpdate) -> Optional[Intention]:
        intention = self.intentions.get(intention_id)
        if not intention:
            return None

        if intention_update.status:
            intention.update_status(intention_update.status)

        if intention_update.goal_id:
            new_goal = self.goal_service.get_goal(intention_update.goal_id)
            if new_goal:
                intention.revise_intention(new_goal)

        if intention_update.plan_id:
            new_plan = self.plan_service.get_plan(intention_update.plan_id)
            if new_plan:
                intention.revise_intention(intention.goal, new_plan)

        return intention

    def delete_intention(self, intention_id: UUID) -> bool:
        if intention_id in self.intentions:
            del self.intentions[intention_id]
            return True
        return False

    def activate_intention(self, intention_id: UUID) -> Optional[Intention]:
        intention = self.intentions.get(intention_id)
        if intention:
            intention.activate_intention()
        return intention

    def suspend_intention(self, intention_id: UUID) -> Optional[Intention]:
        intention = self.intentions.get(intention_id)
        if intention:
            intention.suspend_intention()
        return intention

    def complete_intention(self, intention_id: UUID) -> Optional[Intention]:
        intention = self.intentions.get(intention_id)
        if intention:
            intention.complete_intention()
        return intention

    def is_intention_achievable(self, intention_id: UUID, current_beliefs: List) -> bool:
        intention = self.intentions.get(intention_id)
        if intention:
            return intention.is_achievable(current_beliefs)
        return False

    def execute_intention(self, intention_id: UUID, execute_action) -> bool:
        intention = self.intentions.get(intention_id)
        if intention:
            return intention.execute_intention(execute_action)
        return False
