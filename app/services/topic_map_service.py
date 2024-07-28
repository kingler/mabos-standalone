# app/services/topic_map_service.py
from typing import List, Dict, Any
from app.core.topic_map.topic_map import TopicMap, Topic, Association
import uuid
import hypergraphx as hgx

class TopicMapService:
    def __init__(self):
        self.topic_maps: Dict[str, TopicMap] = {}

    def create_topic_map(self) -> TopicMap:
        topic_map_id = str(uuid.uuid4())
        new_topic_map = TopicMap(id=topic_map_id)
        self.topic_maps[topic_map_id] = new_topic_map
        return new_topic_map

    def get_topic_map(self, topic_map_id: str) -> TopicMap:
        return self.topic_maps.get(topic_map_id)

    def add_topic(self, topic_map_id: str, topic: Topic) -> TopicMap:
        topic_map = self.topic_maps.get(topic_map_id)
        if topic_map:
            topic_map.add_topic(topic)
        return topic_map

    def add_association(self, topic_map_id: str, association: Association) -> TopicMap:
        topic_map = self.topic_maps.get(topic_map_id)
        if topic_map:
            topic_map.add_association(association)
        return topic_map

    def get_topic(self, topic_map_id: str, topic_id: str) -> Topic:
        topic_map = self.topic_maps.get(topic_map_id)
        if topic_map:
            return topic_map.get_topic(topic_id)
        return None

    def get_association(self, topic_map_id: str, association_id: str) -> Association:
        topic_map = self.topic_maps.get(topic_map_id)
        if topic_map:
            return topic_map.get_association(association_id)
        return None

    def get_topic_centrality(self, topic_map_id: str, centrality_type: str) -> Dict[str, float]:
        topic_map = self.topic_maps.get(topic_map_id)
        if topic_map:
            if centrality_type == "degree":
                return hgx.centrality.degree_centrality(topic_map.hypergraph)
            elif centrality_type == "eigenvector":
                return hgx.centrality.eigenvector_centrality(topic_map.hypergraph)
            elif centrality_type == "betweenness":
                return hgx.centrality.betweenness_centrality(topic_map.hypergraph)
        return {}

    def get_communities(self, topic_map_id: str, method: str) -> List[List[str]]:
        topic_map = self.topic_maps.get(topic_map_id)
        if topic_map:
            if method == "spectral":
                return hgx.clustering.spectral_clustering(topic_map.hypergraph)
            elif method == "modularity":
                return hgx.clustering.modularity_clustering(topic_map.hypergraph)
        return []