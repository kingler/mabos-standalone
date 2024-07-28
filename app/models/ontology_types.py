from typing import Dict, Any, List, Union

OntologyStructure = Dict[str, Any]
QueryResult = List[Dict[str, Any]]
ConceptType = Union[str, Dict[str, Any]]
RelationshipType = Dict[str, Any]

def validate_ontology_structure(structure: OntologyStructure) -> bool:
    """
    Validate the structure of an ontology.

    Args:
        structure (OntologyStructure): The ontology structure to validate.

    Returns:
        bool: True if the structure is valid, False otherwise.
    """
    required_keys = {'concepts', 'relationships'}
    return all(key in structure for key in required_keys)

def validate_query_result(result: QueryResult) -> bool:
    """
    Validate the structure of a query result.

    Args:
        result (QueryResult): The query result to validate.

    Returns:
        bool: True if the result is valid, False otherwise.
    """
    return all(isinstance(item, dict) for item in result)

def create_concept(name: str, description: str = None) -> ConceptType:
    """
    Create a concept structure.

    Args:
        name (str): The name of the concept.
        description (str, optional): The description of the concept. Defaults to None.

    Returns:
        ConceptType: A concept structure.
    """
    concept: ConceptType = {"name": name}
    if description:
        concept["description"] = description
    return concept

def create_relationship(name: str, domain: str, range: str, description: str = None) -> RelationshipType:
    """
    Create a relationship structure.

    Args:
        name (str): The name of the relationship.
        domain (str): The domain of the relationship.
        range (str): The range of the relationship.
        description (str, optional): The description of the relationship. Defaults to None.

    Returns:
        RelationshipType: A relationship structure.
    """
    relationship: RelationshipType = {"name": name, "domain": domain, "range": range}
    if description:
        relationship["description"] = description
    return relationship