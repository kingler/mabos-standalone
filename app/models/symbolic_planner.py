class SymbolicPlanner:
    def __init__(self):
        # Initialize the symbolic planner
        self.domain = None
        self.problem = None
        self.plan = None

    def plan(self, goal):
        from app.services.planning_service import PlanningService
        from app.models.plan import Plan
        
        planning_service = PlanningService(domain_knowledge={})
        
        current_state = self.get_current_state()
        plan = planning_service.generate_plan(goal, current_state)
        
        if isinstance(plan, Plan):
            self.plan = plan
            return plan
        else:
            raise ValueError("Failed to generate a valid plan")
