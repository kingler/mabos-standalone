from typing import List, Callable
from core.models.agent.agent import Agent
from core.models.agent.belief import Belief
from core.models.agent.desire import Desire
from core.models.agent.intention import Intention
from core.models.agent.goal import Goal
from rules import Rules, Rule

class DesireToIntentionRule:
    def condition(self, agent: Agent) -> bool:
        return len(agent.desires) > 0 and len(agent.intentions) < 3

    def action(self, agent: Agent):
        highest_priority_desire = max(agent.desires, key=lambda d: d.priority)
        plan = self.generate_plan(highest_priority_desire)
        goal = Goal(id=f"goal_{highest_priority_desire.desire_id}", description=highest_priority_desire.description, priority=highest_priority_desire.priority, status="active")
        intention = Intention(goal=goal, plan=plan)
        agent.intentions.append(intention)
        agent.desires.remove(highest_priority_desire)

    def generate_plan(self, desire: Desire) -> List[str]:
        # This would be more complex in a real system
        return [f"Step 1 for {desire.description}", f"Step 2 for {desire.description}"]

class ExecuteIntentionRule:
    def condition(self, agent: Agent) -> bool:
        return len(agent.intentions) > 0

    def action(self, agent: Agent):
        intention = agent.intentions[0]
        if not intention.plan.is_completed():
            print(f"Agent {agent.name} executing: {intention.plan.current_step()}")
            intention.plan.execute_next_step()
        else:
            print(f"Agent {agent.name} completed intention: {intention.goal.description}")
            intention.complete_intention()
            agent.intentions.remove(intention)

class RulesEngine:
    def __init__(self):
        self.rules = Rules()

    def add_rule(self, rule: Rule):
        self.rules.add_rule(rule.condition, rule.action)

    def run(self, agents: List[Agent]):
        for agent in agents:
            self.rules.evaluate(agent)

# Example usage
if __name__ == "__main__":
    # Create agents
    developer = Agent(name="Developer")
    manager = Agent(name="Manager")

    # Add beliefs
    developer.update_belief("coding_skill", Belief(description="Coding skill level", certainty=0.9, value="high"))
    manager.update_belief("project_status", Belief(description="Current project status", certainty=0.8, value="on_track"))

    # Add desires
    developer.add_desire(Desire(desire_id="complete_feature", description="Complete feature", priority=5))
    manager.add_desire(Desire(desire_id="deliver_project", description="Deliver project", priority=8))

    # Create rules engine
    engine = RulesEngine()
    engine.add_rule(DesireToIntentionRule())
    engine.add_rule(ExecuteIntentionRule())

    # Run the engine for a few cycles
    for _ in range(5):
        engine.run([developer, manager])