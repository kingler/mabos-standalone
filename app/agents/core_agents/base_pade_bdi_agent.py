from pade.core.agent import Agent
from pade.behaviours.protocols import FipaRequestProtocol
from typing import Dict, List, Any, Optional
import asyncio
import logging
import re
from enum import Enum

from app.tools.reasoning_engine import ReasoningEngine
from app.models.knowledge.knowledge_base import KnowledgeBase

class GoalType(Enum):
    ACHIEVEMENT = "achievement"
    MAINTENANCE = "maintenance"
    PERFORMANCE = "performance"

class Goal:
    def __init__(self, name: str, type: GoalType, preconditions: List[str], effects: List[str]):
        self.name = name
        self.type = type
        self.preconditions = preconditions
        self.effects = effects
        self.subgoals: List[Goal] = []

    def __eq__(self, other):
        if not isinstance(other, Goal):
            return False
        return (self.name == other.name and
                self.type == other.type and
                self.preconditions == other.preconditions and
                self.effects == other.effects)

    def __hash__(self):
        return hash((self.name, self.type, tuple(self.preconditions), tuple(self.effects)))

class DSLParser:
    @staticmethod
    def parse_goal(goal_string: str) -> Goal:
        pattern = r"(\w+)\s*:\s*(\w+)\s*\(\s*pre:\s*\[(.*?)\]\s*,\s*eff:\s*\[(.*?)\]\s*\)"
        match = re.match(pattern, goal_string)
        if not match:
            raise ValueError(f"Invalid goal string format: {goal_string}")
        
        name, type_str, pre_str, eff_str = match.groups()
        goal_type = GoalType(type_str.lower())
        preconditions = [p.strip() for p in pre_str.split(",") if p.strip()]
        effects = [e.strip() for e in eff_str.split(",") if e.strip()]
        
        return Goal(name, goal_type, preconditions, effects)

class BasePadeBDIAgent(Agent):
    def __init__(self, aid, api_key: str):
        super().__init__(aid=aid)
        self.beliefs: Dict[str, Any] = {}
        self.desires: List[Goal] = []
        self.intentions: List[Goal] = []
        self.knowledge_base = KnowledgeBase()
        self.reasoning_engine = ReasoningEngine(self.knowledge_base, api_key)
        self.logger = logging.getLogger(f"Agent_{aid}")
        self.dsl_parser = DSLParser()
    
    async def add_belief(self, belief: str, value: Any):
        try:
            self.beliefs[belief] = value
            await self.update_desires()
        except Exception as e:
            self.logger.error(f"Error adding belief: {str(e)}")
    
    async def remove_belief(self, belief: str):
        try:
            if belief in self.beliefs:
                del self.beliefs[belief]
                await self.update_desires()
        except Exception as e:
            self.logger.error(f"Error removing belief: {str(e)}")
    
    async def add_desire(self, desire_string: str):
        try:
            goal = self.dsl_parser.parse_goal(desire_string)
            if goal not in self.desires:
                self.desires.append(goal)
                await self.update_intentions()
        except Exception as e:
            self.logger.error(f"Error adding desire: {str(e)}")
    
    async def add_intention(self, goal: Goal):
        try:
            if goal not in self.intentions:
                self.intentions.append(goal)
                await self.execute_intentions()
        except Exception as e:
            self.logger.error(f"Error adding intention: {str(e)}")
    
    async def reason(self, problem_type: str, data: Dict[str, Any]) -> Any:
        try:
            return await self.reasoning_engine.reason(data)
        except Exception as e:
            self.logger.error(f"Error during reasoning: {str(e)}")
            return None

    async def update_desires(self):
        start_time = asyncio.get_event_loop().time()
        beliefs_list = [{"content": f"{k}: {v}"} for k, v in self.beliefs.items()]
        new_desires = await self.reasoning_engine.generate_desires(beliefs_list)
        self.desires = [self.dsl_parser.parse_goal(d['description']) for d in new_desires]
        for desire in self.desires:
            if all(pre in self.beliefs for pre in desire.preconditions):
                if desire not in self.intentions:
                    await self.add_intention(desire)
        end_time = asyncio.get_event_loop().time()
        self.logger.info(f"Desire update took {end_time - start_time:.4f} seconds")

    async def update_intentions(self):
        start_time = asyncio.get_event_loop().time()
        self.intentions = [intention for intention in self.intentions 
                           if all(pre in self.beliefs for pre in intention.preconditions) 
                           and intention in self.desires]
        end_time = asyncio.get_event_loop().time()
        self.logger.info(f"Intention update took {end_time - start_time:.4f} seconds")

    async def execute_intentions(self):
        start_time = asyncio.get_event_loop().time()
        tasks = [self.execute_goal(intention) for intention in self.intentions]
        await asyncio.gather(*tasks)
        end_time = asyncio.get_event_loop().time()
        self.logger.info(f"Intention execution took {end_time - start_time:.4f} seconds")

    async def execute_goal(self, goal: Goal):
        if goal.subgoals:
            tasks = [self.execute_goal(subgoal) for subgoal in goal.subgoals]
            await asyncio.gather(*tasks)
        else:
            # Execute atomic goal
            self.logger.info(f"Executing atomic goal: {goal.name}")
            plan = await self.reasoning_engine.reason_and_plan(goal.name, self.beliefs)
            for step in plan.get('steps', []):
                new_state = await self.reasoning_engine.simulate_action(step, self.beliefs)
                self.beliefs.update(new_state)
            for effect in goal.effects:
                await self.add_belief(effect, True)

    async def decompose_goal(self, goal: Goal) -> List[Goal]:
        subgoals = await self.reasoning_engine.reason_about_goals([goal.name])
        return [self.dsl_parser.parse_goal(sg) for sg in subgoals]

    async def handle_message(self, message: Dict[str, Any]):
        try:
            content = message['content']
            sender = message['sender']
            await self.add_belief(f"received_message_from_{sender}", content)
            
            # Parse the message content as a goal
            try:
                goal = self.dsl_parser.parse_goal(content)
                await self.add_desire(content)
            except ValueError:
                self.logger.warning(f"Received message is not a valid goal: {content}")
            
            # Process the message and update agent state
            await self.reason('message_processing', {'message': message})
        except Exception as e:
            self.logger.error(f"Error handling message: {str(e)}")

class RealTimeCommunicationBehavior(FipaRequestProtocol):
    def __init__(self, agent):
        super().__init__(agent=agent)
    
    async def handle_request(self, message):
        await self.agent.handle_message(message)