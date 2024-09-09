import logging
from typing import Dict, Any
from app.agents.core_agents.agent_types import EnvironmentalAgent as BaseEnvironmentalAgent
from app.models.agent.belief import Belief

logger = logging.getLogger(__name__)

class EnvironmentalAgent(BaseEnvironmentalAgent):
    async def perceive(self) -> None:
        """
        Update the agent's perception of the environment and beliefs.
        """
        try:
            new_perceptions = self._simulate_environment_perception()
            self.environment_state.update(new_perceptions)
            
            for key, value in new_perceptions.items():
                new_belief = Belief(id=f"env_{key}", content={"key": key, "value": value}, description=f"Environmental state: {key}", certainty=1.0)
                self.update_beliefs([new_belief])
            
            logger.info(f"Updated environment state: {self.environment_state}")
        except Exception as e:
            logger.error(f"Error during perception: {str(e)}")

    def _simulate_environment_perception(self) -> Dict[str, Any]:
        """
        Simulate perceiving the environment. Replace this with actual sensor data in a real implementation.
        """
        # This is a placeholder. In a real system, this would interface with actual sensors or data sources.
        return {
            "temperature": 22.5,
            "humidity": 45,
            "light_level": 800,
        }

    async def act(self) -> None:
        """
        Perform the agent's main action cycle: perceive and reason.
        """
        await self.perceive()
        context = self.get_current_state()
        await self.reason(context)

    def get_current_state(self) -> Dict[str, Any]:
        """
        Get the current state of the agent, including environment state.
        """
        state = super().get_current_state()
        state["environment_state"] = self.environment_state
        return state
