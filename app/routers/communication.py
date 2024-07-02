from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from app.models.message import Message
from app.services.agent_communication_service import AgentCommunicationService
from app.services.human_communication_service import HumanCommunicationService
from app.services.agent_service import AgentService
from app.services.knowledge_base_service import KnowledgeBaseService

router = APIRouter()

def get_agent_communication_service(
    agent_service: AgentService = Depends(),
    knowledge_base_service: KnowledgeBaseService = Depends()
) -> AgentCommunicationService:
    return AgentCommunicationService(agent_service, knowledge_base_service)

def get_human_communication_service(
    agent_service: AgentService = Depends()
) -> HumanCommunicationService:
    return HumanCommunicationService(agent_service)

@router.post("/agent/send")
async def send_agent_message(
    sender_id: UUID,
    recipient_id: UUID,
    content: str,
    performative: str,
    service: AgentCommunicationService = Depends(get_agent_communication_service)
):
    try:
        await service.send_message(sender_id, recipient_id, content, performative)
        return {"message": "Message sent successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

@router.post("/agent/broadcast")
async def broadcast_agent_message(
    sender_id: UUID,
    content: str,
    performative: str,
    service: AgentCommunicationService = Depends(get_agent_communication_service)
):
    try:
        await service.broadcast_message(sender_id, content, performative)
        return {"message": "Broadcast message sent successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/agent/publish")
async def publish_agent_message(
    sender_id: UUID,
    topic: str,
    content: str,
    performative: str,
    service: AgentCommunicationService = Depends(get_agent_communication_service)
):
    await service.publish_message(sender_id, topic, content, performative)
    return {"message": "Message published successfully"}

@router.post("/agent/subscribe")
async def subscribe_to_topic(
    agent_id: UUID,
    topic: str,
    service: AgentCommunicationService = Depends(get_agent_communication_service)
):
    service.subscribe_to_topic(agent_id, topic)
    return {"message": f"Agent {agent_id} subscribed to topic {topic}"}

@router.post("/agent/unsubscribe")
async def unsubscribe_from_topic(
    agent_id: UUID,
    topic: str,
    service: AgentCommunicationService = Depends(get_agent_communication_service)
):
    service.unsubscribe_from_topic(agent_id, topic)
    return {"message": f"Agent {agent_id} unsubscribed from topic {topic}"}

@router.post("/human/send")
async def send_human_message(
    human_id: UUID,
    agent_id: UUID,
    content: str,
    performative: str,
    service: HumanCommunicationService = Depends(get_human_communication_service)
):
    try:
        await service.send_message_to_agent(human_id, agent_id, content, performative)
        return {"message": "Message sent to agent successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/human/messages/{human_id}", response_model=List[Message])
async def get_human_messages(
    human_id: UUID,
    service: HumanCommunicationService = Depends(get_human_communication_service)
):
    return await service.get_messages_for_human(human_id)