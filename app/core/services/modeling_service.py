from typing import Any, Dict, List
from uuid import uuid4

from app.core.models.mas.mas_modeling_tool import (TOGAFADM,
                                                   EnterpriseContinuum,
                                                   MASModelingTool)
from app.core.models.mdd.mdd_mas_model import (Agent, BusinessProcess,
                                               BusinessSystemIntegration,
                                               Communication,
                                               DomainSpecificLanguage, Goal,
                                               Model, ModelRepository,
                                               ModelType, OnboardingProcess,
                                               PerformanceMetrics,
                                               ReusableComponent)
from app.core.models.repository import Repository


class ModelingService:
    def __init__(self, repository_service: Repository):
        self.ontology_path = repository_service.get_path("ontology_path")
        self.repo_path = repository_service.get_path("repo_path")
        self.rules_path = repository_service.get_path("rules_path")
        self.mas_modeling_tool = MASModelingTool(self.ontology_path, self.repo_path)
        self.togaf_adm = TOGAFADM()
        self.enterprise_continuum = EnterpriseContinuum()
        self.model_repository = ModelRepository(id=uuid4(), name="Main Repository")

    def create_agent(self, agent_data: Dict[str, Any]) -> Agent:
        return self.mas_modeling_tool.create_agent(agent_data)

    def update_agent(self, agent_id: str, updated_data: Dict[str, Any]) -> Agent:
        return self.mas_modeling_tool.update_agent(agent_id, updated_data)

    def delete_agent(self, agent_id: str):
        self.mas_modeling_tool.delete_agent(agent_id)

    def generate_diagrams(self) -> Dict[str, Any]:
        return self.mas_modeling_tool.generate_diagrams()

    def commit_changes(self, message: str):
        self.mas_modeling_tool.commit_changes(message)

    def initiate_onboarding(self, onboarding_data: Dict[str, Any]) -> OnboardingProcess:
        return self.mas_modeling_tool.initiate_onboarding(onboarding_data)

    def execute_togaf_phase(self, phase: str, mas: Any):
        self.togaf_adm.execute_phase(phase, mas)

    def set_current_state(self, state: Any):
        self.enterprise_continuum.set_current_state(state)

    def set_target_state(self, state: Any):
        self.enterprise_continuum.set_target_state(state)

    def add_transition_state(self, state: Any):
        self.enterprise_continuum.add_transition_state(state)

    def create_model(self, name: str, model_type: ModelType, content: Dict[str, Any]) -> Model:
        model = Model(name=name, type=model_type, content=content)
        self.model_repository.models.append(model)
        return model

    def update_model(self, model_id: uuid4, updates: Dict[str, Any]) -> Model:
        for model in self.model_repository.models:
            if model.id == model_id:
                for key, value in updates.items():
                    setattr(model, key, value)
                model.version += 1
                return model
        raise ValueError(f"Model with ID {model_id} not found")

    def delete_model(self, model_id: uuid4):
        self.model_repository.models = [model for model in self.model_repository.models if model.id != model_id]

    def create_goal(self, name: str, description: str, subgoals: List[uuid4] = None) -> Goal:
        return Goal(name=name, description=description, subgoals=subgoals or [])

    def create_business_process(self, name: str, bpmn_xml: str) -> BusinessProcess:
        return BusinessProcess(name=name, bpmn_xml=bpmn_xml)

    def create_communication(self, sender: uuid4, receiver: uuid4, content: str) -> Communication:
        return Communication(sender=sender, receiver=receiver, content=content)

    def create_performance_metrics(self, agent_count: int, average_response_time: float, goals_achieved: int) -> PerformanceMetrics:
        return PerformanceMetrics(agent_count=agent_count, average_response_time=average_response_time, goals_achieved=goals_achieved)

    def create_domain_specific_language(self, name: str, grammar: str, version: str) -> DomainSpecificLanguage:
        return DomainSpecificLanguage(name=name, grammar=grammar, version=version)

    def create_business_system_integration(self, system_name: str, integration_type: str, connection_details: Dict[str, Any]) -> BusinessSystemIntegration:
        return BusinessSystemIntegration(system_name=system_name, integration_type=integration_type, connection_details=connection_details)

    def create_reusable_component(self, name: str, component_type: str, content: Dict[str, Any]) -> ReusableComponent:
        return ReusableComponent(name=name, type=component_type, content=content)