class VocabularyManager:
    def __init__(self):
        self.terms = {}
        self.names = {}
        self.verb_concepts = {}

    def add_term(self, term: str, definition: str):
        self.terms[term] = definition

    def add_name(self, name: str, individual: str):
        self.names[name] = individual

    def add_verb_concept(self, verb_concept: str, definition: str):
        self.verb_concepts[verb_concept] = definition

    def get_definition(self, concept: str) -> str:
        return self.terms.get(concept) or self.names.get(concept) or self.verb_concepts.get(concept)