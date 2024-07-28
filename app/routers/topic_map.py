# app/routers/topic_map.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict
from app.core.topic_map.topic_map import TopicMap, Topic, Association
from app.services.topic_map_service import TopicMapService

router = APIRouter()

def get_topic_map_service():
    return TopicMapService()

@router.post("/topic_maps", response_model=TopicMap)
async def create_topic_map(topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    return topic_map_service.create_topic_map()

@router.get("/topic_maps/{topic_map_id}", response_model=TopicMap)
async def get_topic_map(topic_map_id: str, topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    topic_map = topic_map_service.get_topic_map(topic_map_id)
    if not topic_map:
        raise HTTPException(status_code=404, detail="Topic map not found")
    return topic_map

@router.post("/topic_maps/{topic_map_id}/topics", response_model=TopicMap)
async def add_topic(topic_map_id: str, topic: Topic, topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    topic_map = topic_map_service.add_topic(topic_map_id, topic)
    if not topic_map:
        raise HTTPException(status_code=404, detail="Topic map not found")
    return topic_map

@router.post("/topic_maps/{topic_map_id}/associations", response_model=TopicMap)
async def add_association(topic_map_id: str, association: Association, topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    topic_map = topic_map_service.add_association(topic_map_id, association)
    if not topic_map:
        raise HTTPException(status_code=404, detail="Topic map not found")
    return topic_map

@router.get("/topic_maps/{topic_map_id}/topics/{topic_id}", response_model=Topic)
async def get_topic(topic_map_id: str, topic_id: str, topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    topic = topic_map_service.get_topic(topic_map_id, topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic

@router.get("/topic_maps/{topic_map_id}/associations/{association_id}", response_model=Association)
async def get_association(topic_map_id: str, association_id: str, topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    association = topic_map_service.get_association(topic_map_id, association_id)
    if not association:
        raise HTTPException(status_code=404, detail="Association not found")
    return association

@router.get("/topic_maps/{topic_map_id}/centrality/{centrality_type}", response_model=Dict[str, float])
async def get_topic_centrality(topic_map_id: str, centrality_type: str, topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    centrality = topic_map_service.get_topic_centrality(topic_map_id, centrality_type)
    if not centrality:
        raise HTTPException(status_code=404, detail="Topic map not found or invalid centrality type")
    return centrality

@router.get("/topic_maps/{topic_map_id}/communities/{method}", response_model=List[List[str]])
async def get_communities(topic_map_id: str, method: str, topic_map_service: TopicMapService = Depends(get_topic_map_service)):
    communities = topic_map_service.get_communities(topic_map_id, method)
    if communities is None:
        raise HTTPException(status_code=404, detail="Topic map not found or invalid community detection method")
    return communities