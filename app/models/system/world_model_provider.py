"""
Compatibility module for world model provider.
Maintains singleton pattern for world model access.
"""
import warnings
from typing import Optional

from .world_model import WorldModel

_world_model_instance: Optional[WorldModel] = None


async def get_world_model() -> WorldModel:
    """
    Get or create the world model singleton instance.
    Maintains backward compatibility while using new core model structure.
    
    Returns:
        WorldModel: The singleton world model instance
    """
    warnings.warn(
        "Importing get_world_model from app.models.system.world_model_provider is deprecated. "
        "Use 'from app.models.core import get_world_model' instead.",
        DeprecationWarning,
        stacklevel=2
    )
    
    global _world_model_instance
    if _world_model_instance is None:
        _world_model_instance = await WorldModel.create()
    return _world_model_instance


async def reset_world_model() -> None:
    """
    Reset the world model instance.
    Useful for testing and initialization.
    """
    global _world_model_instance
    _world_model_instance = None
