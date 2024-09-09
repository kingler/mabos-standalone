import logging
from typing import Any, Dict, List
from pydantic import Field

from app.agents.core_agents.agent_types import Agent
from app.models.agent.belief import Belief
from app.models.agent.desire import Desire
from app.models.agent.intention import Intention
from app.models.agent.goal import Goal
from app.tools.reasoning_engine import ReasoningEngine
from app.tools.reasoner import Reasoner
from app.tools.ontology_reasoner import OntologyReasoner

logger = logging.getLogger(__name__)

class CodeGenerationAgent(Agent):
    """
    Responsible for generating code for the domain-specific MAS based on the designs and models.
    """
    code_generation_capabilities: List[str] = Field(default_factory=list, description="List of code generation capabilities")
    reasoning_engine: ReasoningEngine = Field(default_factory=ReasoningEngine)
    reasoner: Reasoner = Field(default_factory=Reasoner)
    ontology_reasoner: OntologyReasoner = Field(default_factory=OntologyReasoner)

    def __init__(self, **data):
        super().__init__(**data)
        self._init_code_generation_beliefs()
        self._init_code_generation_desires()

    def _init_code_generation_beliefs(self):
        self.add_belief(Belief(id="code_generation_capability", content={"capabilities": self.code_generation_capabilities}, description="Code generation capabilities", certainty=1.0))

    def _init_code_generation_desires(self):
        self.add_desire(Desire(id="generate_high_quality_code", description="Generate high-quality, maintainable code", priority=0.9))
        self.add_desire(Desire(id="optimize_code_performance", description="Optimize code for better performance", priority=0.8))

    async def reason(self, context: Dict[str, Any]) -> Dict[str, Any]:
        reasoning_result = await super().reason(context)
        
        # Use reasoning engine for advanced decision-making
        reasoning_engine_result = await self.reasoning_engine.reason(context)
        
        # Use reasoner for logical inference
        reasoner_result = self.reasoner.infer(context)
        
        # Use ontology reasoner for knowledge inference
        ontology_result = await self.ontology_reasoner.infer_knowledge(context)
        
        # Combine results from different reasoning methods
        combined_result = {
            **reasoning_result,
            **reasoning_engine_result,
            **reasoner_result,
            **ontology_result
        }
        
        # Update beliefs based on combined reasoning
        if "code_requirements" in combined_result:
            self._update_code_generation_beliefs(combined_result["code_requirements"])
        
        return combined_result

    def _update_code_generation_beliefs(self, code_requirements: Dict[str, Any]):
        for key, value in code_requirements.items():
            self.add_belief(Belief(id=f"code_req_{key}", content={key: value}, description=f"Code requirement: {key}", certainty=0.9))

    async def act(self) -> None:
        """Perform the agent's main action cycle: reason, deliberate, and execute code generation actions."""
        try:
            context = self.get_current_state()
            await self.reason(context)
            self.deliberate()
            await self._execute_code_generation_actions()
        except Exception as e:
            logger.error(f"Error during code generation agent action cycle: {str(e)}")

    def deliberate(self) -> None:
        """Deliberate on current beliefs and desires to form code generation-related intentions."""
        for desire in self.desires:
            if desire.id == "generate_high_quality_code" and self._should_generate_code():
                self.add_intention(Intention(id="implement_code_structure", goal=Goal(id="create_code_structure", description="Create basic code structure"), plan=None))
            elif desire.id == "optimize_code_performance" and self._should_optimize_code():
                self.add_intention(Intention(id="optimize_code", goal=Goal(id="improve_performance", description="Improve code performance"), plan=None))

    def _should_generate_code(self) -> bool:
        return any(belief.content.get("code_structure_completed", False) == False for belief in self.beliefs if "code_structure_completed" in belief.content)

    def _should_optimize_code(self) -> bool:
        return any(belief.content.get("code_optimized", False) == False for belief in self.beliefs if "code_optimized" in belief.content)

    async def _execute_code_generation_actions(self):
        for intention in self.intentions:
            if intention.id == "implement_code_structure":
                await self._implement_code_structure()
            elif intention.id == "optimize_code":
                await self._optimize_code()

    async def _implement_code_structure(self):
        logger.info("Implementing code structure")
        # Implement code structure generation logic here

    async def _optimize_code(self):
        logger.info("Optimizing code")
        # Implement code optimization logic here

    def get_current_state(self) -> Dict[str, Any]:
        """Get the current state of the agent."""
        state = super().get_current_state()
        state["code_generation_capabilities"] = self.code_generation_capabilities
        return state
