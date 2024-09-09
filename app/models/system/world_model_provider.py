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
        # You can add any initial configuration here
        # For example:
        # initial_state={'time': 0},
        # ontology_path='path/to/your/ontology.owl'
    )