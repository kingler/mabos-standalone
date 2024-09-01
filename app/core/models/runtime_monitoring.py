from typing import Any, Dict, List

from pydantic import BaseModel


class TraceEvent(BaseModel):
    timestamp: float
    agent_id: str
    event_type: str
    details: Dict[str, Any]

class TraceModel:
    events: List[TraceEvent] = []

    def add_event(self, event: TraceEvent):
        self.events.append(event)

    def get_agent_trace(self, agent_id: str) -> List[TraceEvent]:
        return [event for event in self.events if event.agent_id == agent_id]