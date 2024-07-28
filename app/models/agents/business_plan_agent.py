from app.models.business_plan import BusinessPlan, BusinessGoal, BusinessAction
from app.models.reasoner import Reasoner

class BusinessPlanAgent:
    def __init__(self, business_plan: BusinessPlan, reasoner: Reasoner):
        self.business_plan = business_plan
        self.reasoner = reasoner

    def update_plan(self):
        # Update beliefs based on the current state
        beliefs = [{"content": f"{k}: {v}"} for k, v in self.business_plan.current_state.items()]
        updated_beliefs = self.reasoner.update_beliefs(beliefs)

        # Generate new desires (goals) based on updated beliefs
        updated_desires = self.reasoner.generate_desires(updated_beliefs)

        # Select intentions (actions) based on updated desires and available resources
        updated_intentions = self.reasoner.select_intentions(updated_desires, updated_beliefs, self.business_plan.resources)

        # Update the business plan with new goals and actions
        self.business_plan.goals = [BusinessGoal(id=d.id, description=d.description, priority=d.priority) for d in updated_desires]
        self.business_plan.actions = [BusinessAction(id=i.id, description=i.desire_id, impact={}) for i in updated_intentions]

    def execute_action(self, action_id: str):
        # Find the action to execute
        action = next((a for a in self.business_plan.actions if a.id == action_id), None)
        if not action:
            raise ValueError(f"Action with id {action_id} not found")

        # Simulate the action and update the current state
        updated_state = self.reasoner.simulate_action(action.description, self.business_plan.current_state)
        self.business_plan.current_state = updated_state