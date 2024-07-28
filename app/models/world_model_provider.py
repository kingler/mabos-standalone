from functools import lru_cache
from .world_model import WorldModel

@lru_cache(maxsize=None)
def get_world_model() -> WorldModel:
    """
    Returns a singleton instance of WorldModel.
    
    The @lru_cache decorator with maxsize=None ensures that this function
    is only called once, and the same WorldModel instance is returned
    for subsequent calls.
    """
    return WorldModel(
        ontology_path="/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/core/ontologies/mabos.owl",
        num_agents=1,  # Ensure this is a positive integer
        num_states=10,  # Ensure this is a positive integer
        state_size=10,  # Adjust based on your specific use case
        action_size=5   # Adjust based on your specific use case
    )