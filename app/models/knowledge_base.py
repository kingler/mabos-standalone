from pydantic import BaseModel, Field
from typing import Dict, Any, Union, List, Optional
from rdflib import Graph, Literal, URIRef
from ..core.sentence_transformer import SentenceTransformerWrapper

class KnowledgeItem(BaseModel):
    id: str
    content: Union[str, int, float, dict, list]
    embedding: Optional[List[float]] = None
    metadata: Dict[str, Any] = {}

class KnowledgeBase(BaseModel):
    id: str
    symbolic_kb: Dict[str, KnowledgeItem] = Field(default_factory=dict)
    neural_kb: Dict[str, KnowledgeItem] = Field(default_factory=dict)
    graph: Graph = Field(default_factory=Graph, exclude=True)
    sentence_transformer: SentenceTransformerWrapper = Field(default_factory=lambda: SentenceTransformerWrapper('all-MiniLM-L6-v2'), exclude=True)
    
    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {
            Graph: lambda v: "<Graph object>"
        }
    }

    def add_symbolic_knowledge(self, item: KnowledgeItem):
        self.symbolic_kb[item.id] = item
        self._add_to_graph(item)

    def add_neural_knowledge(self, item: KnowledgeItem):
        if isinstance(item.content, str):
            item.embedding = self.sentence_transformer.encode(item.content).tolist()
        self.neural_kb[item.id] = item

    def get_symbolic_knowledge(self, item_id: str) -> KnowledgeItem:
        return self.symbolic_kb.get(item_id)

    def get_neural_knowledge(self, item_id: str) -> KnowledgeItem:
        return self.neural_kb.get(item_id)

    def remove_symbolic_knowledge(self, item_id: str):
        if item_id in self.symbolic_kb:
            del self.symbolic_kb[item_id]
            self._remove_from_graph(item_id)

    def remove_neural_knowledge(self, item_id: str):
        if item_id in self.neural_kb:
            del self.neural_kb[item_id]

    def query(self, query: str) -> Dict[str, Any]:
        symbolic_results = self._query_symbolic(query)
        neural_results = self._query_neural(query)
        return self._integrate_results(symbolic_results, neural_results)

    def _query_symbolic(self, query: str) -> Dict[str, Any]:
        results = {}
        for triple in self.graph.triples((None, None, Literal(query))):
            subject, predicate, _ = triple
            results[str(subject)] = {
                'predicate': str(predicate),
                'value': query
            }
        return results

    def _query_neural(self, query: str) -> Dict[str, Any]:
        query_embedding = self.sentence_transformer.encode(query)
        results = {}
        for key, item in self.neural_kb.items():
            if item.embedding:
                similarity = self.sentence_transformer.cosine_similarity(query_embedding, item.embedding)
                if similarity > 0.5:  # Adjust threshold as needed
                    results[key] = {
                        'value': item.content,
                        'similarity': float(similarity)
                    }
        return results

    def _integrate_results(self, symbolic_results: Dict[str, Any], neural_results: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'symbolic': symbolic_results,
            'neural': neural_results,
            'combined': symbolic_results | neural_results
        }

    def _add_to_graph(self, item: KnowledgeItem):
        subject = URIRef(item.id)
        if isinstance(item.content, dict):
            for key, value in item.content.items():
                predicate = URIRef(key)
                obj = Literal(value)
                self.graph.add((subject, predicate, obj))
        else:
            self.graph.add((subject, URIRef('hasContent'), Literal(item.content)))

    def _remove_from_graph(self, item_id: str):
        subject = URIRef(item_id)
        self.graph.remove((subject, None, None))

    def find_most_similar(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        query_embedding = self.sentence_transformer.encode(query)
        similarities = []
        for key, item in self.neural_kb.items():
            if item.embedding:
                similarity = self.sentence_transformer.cosine_similarity(query_embedding, item.embedding)
                similarities.append((key, similarity, item))
        
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [
            {'id': key, 'similarity': similarity, 'content': item.content}
            for key, similarity, item in similarities[:top_k]
        ]