Implement these features to enhance the [[reasoner]].

```python
import openai
from owlready2 import *
import re
from typing import List, Tuple

class Reasoner:
    def __init__(self, ontology_path, openai_api_key):
        self.onto = get_ontology(ontology_path).load()
        openai.api_key = openai_api_key

    def query_llm(self, prompt, max_tokens=150):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

    def extract_relevant_concepts(self, query):
        return [concept for concept in self.onto.classes() 
                if concept.name.lower() in query.lower()]

    def generate_ontology_context(self, concepts):
        context = ""
        for concept in concepts:
            context += f"Concept: {concept.name}\n"
            for prop in concept.get_properties():
                context += f"  Property: {prop.name}\n"
            for parent in concept.is_a:
                if isinstance(parent, ThingClass):
                    context += f"  Parent: {parent.name}\n"
        return context

    def extract_relationships(self, concepts: List[ThingClass]) -> List[str]:
        """Extract relationships between concepts from the ontology."""
        relationships = []
        for concept in concepts:
            for prop in concept.get_properties():
                domain = prop.domain
                range = prop.range
                if domain and range:
                    relationships.append(f"{domain[0].name} {prop.name} {range[0].name}")
        return relationships

    def decompose_query(self, query: str) -> List[str]:
        """Decompose a complex query into sub-queries based on ontology structure."""
        relevant_concepts = self.extract_relevant_concepts(query)
        context = self.generate_ontology_context(relevant_concepts)
        relationships = self.extract_relationships(relevant_concepts)

        prompt = f"""
        Given the following ontology context and relationships:
        {context}
        Relationships:
        {'; '.join(relationships)}

        Decompose the following complex query into simpler sub-queries that align with the ontology structure:
        Query: {query}

        Sub-queries:
        1.
        """

        response = self.query_llm(prompt, max_tokens=200)
        sub_queries = [sq.strip() for sq in response.split('\n') if sq.strip()]
        return sub_queries

    def star_reasoning(self, query: str, max_iterations: int = 3) -> Tuple[str, str, float]:
        relevant_concepts = self.extract_relevant_concepts(query)
        ontology_context = self.generate_ontology_context(relevant_concepts)
        relationships = self.extract_relationships(relevant_concepts)
        sub_queries = self.decompose_query(query)

        best_rationale = ""
        best_answer = ""
        best_score = -1

        for iteration in range(max_iterations):
            prompt = f"""
            Given the following ontology context and relationships:
            {ontology_context}
            Relationships:
            {'; '.join(relationships)}

            And the main query decomposed into sub-queries:
            Main Query: {query}
            Sub-queries:
            {' '.join(f'{i+1}. {sq}' for i, sq in enumerate(sub_queries))}

            Provide a step-by-step rationale for answering the main query by addressing each sub-query, 
            and then synthesize a final answer. Use the ontology relationships to guide your reasoning:

            Rationale:
            """

            rationale = self.query_llm(prompt, max_tokens=500)

            # Extract the answer from the rationale
            answer_match = re.search(r"(?:Final answer|Therefore|In conclusion):\s*(.*)", rationale, re.IGNORECASE | re.DOTALL)
            answer = answer_match.group(1).strip() if answer_match else ""

            # Self-evaluation prompt
            eval_prompt = f"""
            Rate the quality and correctness of the following rationale and answer on a scale of 0 to 10,
            considering how well it uses the ontology relationships and addresses all sub-queries:

            Query: {query}
            Sub-queries: {', '.join(sub_queries)}
            Ontology Relationships: {'; '.join(relationships)}

            Rationale and Answer:
            {rationale}

            Rating (0-10):
            """

            score = float(self.query_llm(eval_prompt, max_tokens=10))

            if score > best_score:
                best_score = score
                best_rationale = rationale
                best_answer = answer

            if score >= 8:
                break

        return best_rationale, best_answer, best_score

    def infer_new_knowledge(self, statement: str) -> str:
        relevant_concepts = self.extract_relevant_concepts(statement)
        ontology_context = self.generate_ontology_context(relevant_concepts)
        relationships = self.extract_relationships(relevant_concepts)

        prompt = f"""
        Given the following ontology context and relationships:
        {ontology_context}
        Relationships:
        {'; '.join(relationships)}

        And the new statement:
        {statement}

        Infer new knowledge or relationships that can be added to the ontology, 
        ensuring they align with the existing structure and relationships:
        1.
        """

        inferred_knowledge = self.query_llm(prompt, max_tokens=200)
        return inferred_knowledge

# Usage example
if __name__ == "__main__":
    reasoner = Reasoner("path/to/your/ontology.owl", "api-key")
    
    query = "How do customer satisfaction, product quality, and marketing strategies jointly impact our sales performance?"
    rationale, answer, score = reasoner.star_reasoning(query)
    print("Rationale:", rationale)
    print("Answer:", answer)
    print("Confidence Score:", score)
    
    statement = "Our new loyalty program has increased customer retention by 15% over the last quarter."
    new_knowledge = reasoner.infer_new_knowledge(statement)
    print("Inferred knowledge:", new_knowledge)
```

Key enhancements:

1. Relationship Exploitation:
   - Added the `extract_relationships` method to explicitly extract relationships between concepts from the ontology.
   - These relationships are now included in the reasoning prompts, guiding the LLM to consider important connections between concepts.

   ```python
   def extract_relationships(self, concepts: List[ThingClass]) -> List[str]:
       relationships = []
       for concept in concepts:
           for prop in concept.get_properties():
               domain = prop.domain
               range = prop.range
               if domain and range:
                   relationships.append(f"{domain[0].name} {prop.name} {range[0].name}")
       return relationships
   ```

2. Ontology-guided Question Decomposition:
   - Implemented the `decompose_query` method to break down complex queries into sub-queries based on the ontology structure.
   - This decomposition is used in the `star_reasoning` method to guide the reasoning process.

   ```python
   def decompose_query(self, query: str) -> List[str]:
       relevant_concepts = self.extract_relevant_concepts(query)
       context = self.generate_ontology_context(relevant_concepts)
       relationships = self.extract_relationships(relevant_concepts)

       prompt = f"""
       Given the following ontology context and relationships:
       {context}
       Relationships:
       {'; '.join(relationships)}

       Decompose the following complex query into simpler sub-queries that align with the ontology structure:
       Query: {query}

       Sub-queries:
       1.
       """

       response = self.query_llm(prompt, max_tokens=200)
       sub_queries = [sq.strip() for sq in response.split('\n') if sq.strip()]
       return sub_queries
   ```

3. Enhanced STaR Reasoning:
   - The `star_reasoning` method now incorporates both the relationships and the decomposed sub-queries in its prompts.
   - This encourages the LLM to structure its reasoning around the ontology's concepts and relationships, and to address each aspect of the complex query systematically.

4. Improved Knowledge Inference:
   - The `infer_new_knowledge` method now also considers ontology relationships when generating new insights, ensuring better alignment with the existing knowledge structure.

These enhancements allow the MABOS reasoner to:
1. More effectively leverage the structural relationships in the ontology during reasoning.
2. Break down complex queries into manageable sub-components that align with the ontology's structure.
3. Generate more coherent and ontology-aligned rationales for its answers.
4. Infer new knowledge that's more likely to be consistent with the existing ontological structure.

This improved reasoner provides MABOS agents with even more sophisticated knowledge-based decision-making capabilities, tightly integrating the structured knowledge from the ontology with the flexible reasoning of the LLM.