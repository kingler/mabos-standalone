"""
Core models package for MABOS.
Provides unified access to all core model implementations.
"""

from .agent_models import (AgentFactory, AgentType, BusinessAgent,
                         DeliberativeAgent, EnvironmentalAgent, HybridAgent,
                         MetaAgent, ReactiveAgent, UIAgent)
from .base_models import (BaseAction, BaseAgent, BaseGoal, BaseModel, BasePlan,
                        BusinessProcess, Communication, ModelRepository,
                        ModelType, OnboardingProcess, PerformanceMetrics,
                        ReusableComponent, SystemIntegration)
from .business_models import (BusinessModel, BusinessModelFactory, BusinessPlan,
                          BusinessProfile, BusinessStrategy,
                          BusinessWorkflow, BusinessOnboarding)
from .knowledge_models import (InferenceEngine, KnowledgeBase, KnowledgeFactory,
                           KnowledgeGraph, KnowledgeItem, Ontology,
                           ReasoningRule)

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
    'Ontology',
    'KnowledgeBase',
    'ReasoningRule',
    'InferenceEngine',
    'KnowledgeGraph',
    'KnowledgeFactory'
]

# Version information
__version__ = '1.0.0'
__author__ = 'MABOS Development Team'
__description__ = 'Core models for the Multi-Agent Business Operating System'
