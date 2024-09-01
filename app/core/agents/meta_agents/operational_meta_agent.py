from typing import Any, Dict, List

from app.core.models.agent.agent import Agent
from app.core.models.agent.goal import Goal
from app.core.models.agent.plan import Plan
from app.core.services.agent_service import AgentService
from app.core.services.goal_service import GoalService
from app.core.services.plan_service import PlanService


class OperationalMetaAgent(Agent):
    def __init__(self, agent_service: AgentService, goal_service: GoalService, plan_service: PlanService):
        super().__init__()
        self.agent_service = agent_service
        self.goal_service = goal_service
        self.plan_service = plan_service

    def interpret_tactical_plans(self, tactical_plans: List[Plan]) -> List[Dict[str, Any]]:
        operational_tasks = []
        for plan in tactical_plans:
            for step in plan.steps:
                task = {
                    "description": step.description,
                    "plan_id": plan.id,
                    "status": "pending"
                }
                operational_tasks.append(task)
        return operational_tasks

    def assign_tasks(self, operational_tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        task_assignments = {}
        available_agents = self.agent_service.get_available_agents()
        
        for task in operational_tasks:
            suitable_agent = self.agent_service.find_suitable_agent(task, available_agents)
            if suitable_agent:
                if suitable_agent.id not in task_assignments:
                    task_assignments[suitable_agent.id] = []
                task_assignments[suitable_agent.id].append(task)
                available_agents.remove(suitable_agent)
            else:
                # Handle case when no suitable agent is found
                task_assignments["unassigned"] = task_assignments.get("unassigned", []) + [task]
        
        return task_assignments

    def monitor_task_execution(self, task_assignments: Dict[str, Any]) -> Dict[str, Any]:
        execution_status = {}
        for agent_id, tasks in task_assignments.items():
            if agent_id != "unassigned":
                agent_status = self.agent_service.get_agent_status(agent_id)
                for task in tasks:
                    task_status = self.agent_service.get_task_status(agent_id, task)
                    execution_status[task["description"]] = {
                        "agent_id": agent_id,
                        "agent_status": agent_status,
                        "task_status": task_status
                    }
        return execution_status

    def handle_exceptions(self, execution_status: Dict[str, Any]) -> Dict[str, Any]:
        exception_handling = {}
        for task, status in execution_status.items():
            if status["task_status"] == "failed":
                # Implement exception handling logic
                exception_handling[task] = {
                    "original_agent": status["agent_id"],
                    "action": "reassign",
                    "new_agent": self.agent_service.find_alternative_agent(status["agent_id"])
                }
            elif status["agent_status"] == "offline":
                exception_handling[task] = {
                    "original_agent": status["agent_id"],
                    "action": "reassign",
                    "new_agent": self.agent_service.find_alternative_agent(status["agent_id"])
                }
        return exception_handling

    def report_operational_status(self) -> Dict[str, Any]:
        operational_status = {
            "total_tasks": self.plan_service.get_total_tasks(),
            "completed_tasks": self.plan_service.get_completed_tasks(),
            "in_progress_tasks": self.plan_service.get_in_progress_tasks(),
            "failed_tasks": self.plan_service.get_failed_tasks(),
            "agent_utilization": self.agent_service.get_agent_utilization(),
            "overall_progress": self.plan_service.get_overall_progress(),
            "estimated_completion_time": self.plan_service.get_estimated_completion_time()
        }
        return operational_status
