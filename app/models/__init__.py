"""
Models package for MABOS.
Provides backward compatibility layer for the new core models structure.
"""
import warnings
from typing import Any, Dict, Type

from .core import (AgentFactory, AgentType, BaseAction, BaseAgent, BaseGoal,
                  BaseModel, BasePlan, BusinessAgent, BusinessModel,
                  BusinessModelFactory, BusinessOnboarding, BusinessPlan,
                  BusinessProcess, BusinessProfile, BusinessStrategy,
                  BusinessWorkflow, Communication, DeliberativeAgent,
                  EnvironmentalAgent, HybridAgent, InferenceEngine, KnowledgeBase,
                  KnowledgeFactory, KnowledgeGraph, KnowledgeItem, MetaAgent,
                  ModelRepository, ModelType, OnboardingProcess,
                  PerformanceMetrics, ReactiveAgent, ReasoningRule,
                  ReusableComponent, SystemIntegration, UIAgent)

# Backward compatibility mappings
_compatibility_mappings: Dict[str, Type[Any]] = {
    # Agent models
    'agent.Agent': BaseAgent,
    'agent.BusinessAgent': BusinessAgent,
    'agent.ReactiveAgent': ReactiveAgent,
    'agent.DeliberativeAgent': DeliberativeAgent,
    'agent.HybridAgent': HybridAgent,
    'agent.EnvironmentalAgent': EnvironmentalAgent,
    'agent.MetaAgent': MetaAgent,
    'agent.UIAgent': UIAgent,
    
    # Business models
    'business.BusinessModel': BusinessModel,
    'business.BusinessPlan': BusinessPlan,
    'business.BusinessStrategy': BusinessStrategy,
    'business.BusinessWorkflow': BusinessWorkflow,
    'business.BusinessProfile': BusinessProfile,
    'business.BusinessOnboarding': BusinessOnboarding,
    
    # Knowledge models
    'knowledge.KnowledgeItem': KnowledgeItem,
    'knowledge.KnowledgeBase': KnowledgeBase,
    'knowledge.ReasoningRule': ReasoningRule,
    'knowledge.InferenceEngine': InferenceEngine,
    'knowledge.KnowledgeGraph': KnowledgeGraph,
    
    # System models
    'system.BusinessProcess': BusinessProcess,
    'system.Communication': Communication,
    'system.PerformanceMetrics': PerformanceMetrics,
    'system.ModelRepository': ModelRepository,
    'system.SystemIntegration': SystemIntegration,
    'system.ReusableComponent': ReusableComponent,
    
    # MDD models
    'mdd.Model': BaseModel,
    'mdd.OnboardingProcess': OnboardingProcess
}

def __getattr__(name: str) -> Type[Any]:
    """
    Provides backward compatibility for old import paths.
    
    Example:
        from app.models.agent import Agent  # Old style
        # Will now return app.models.core.base_models.BaseAgent
    """
    if name in _compatibility_mappings:
        warnings.warn(
            f"Importing from {name} is deprecated. "
            f"Use 'from app.models.core import {_compatibility_mappings[name].__name__}' instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return _compatibility_mappings[name]
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

# Re-export all core models
__all__ = [
    # Base Models
    'BaseModel',
    'BaseAgent',
    'BaseGoal',
    'BasePlan',
    'BaseAction',
    'ModelType',
    'BusinessProcess',
    'Communication',
    'PerformanceMetrics',
    'ModelRepository',
    'SystemIntegration',
    'ReusableComponent',
    'OnboardingProcess',
    
    # Agent Models
    'AgentType',
    'ReactiveAgent',
    'DeliberativeAgent',
    'HybridAgent',
    'BusinessAgent',
    'EnvironmentalAgent',
    'MetaAgent',
    'UIAgent',
    'AgentFactory',
    
    # Business Models
    'BusinessModel',
    'BusinessPlan',
    'BusinessStrategy',
    'BusinessWorkflow',
    'BusinessProfile',
    'BusinessOnboarding',
    'BusinessModelFactory',
    
    # Knowledge Models
    'KnowledgeItem',
    'KnowledgeBase',
    'ReasoningRule',
    'InferenceEngine',
    'KnowledgeGraph',
    'KnowledgeFactory'
]

# Version information
__version__ = '1.0.0'
__author__ = 'MABOS Development Team'
__description__ = 'Models for the Multi-Agent Business Operating System'
