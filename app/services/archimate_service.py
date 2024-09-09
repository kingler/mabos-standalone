from typing import List, Optional

from app.models.mdd.archimate_model import (ApplicationComponent,
                                                 ApplicationService,
                                                 ArchiMateModel,
                                                 BaseArchiMateElement,
                                                 BusinessFunction,
                                                 BusinessProcess, Node,
                                                 Relationship,
                                                 TechnologyService)


class ArchiMateService:
    def __init__(self):
        self.model = ArchiMateModel()

    def create_element(self, element_type: str, id: int, name: str, description: str) -> BaseArchiMateElement:
        element_classes = {
            'business_process': BusinessProcess,
            'business_function': BusinessFunction,
            'application_component': ApplicationComponent,
            'application_service': ApplicationService,
            'technology_service': TechnologyService,
            'node': Node
        }
        element_class = element_classes.get(element_type)
        if not element_class:
            raise ValueError(f"Invalid element type: {element_type}")
        
        element = element_class(id=id, name=name, description=description)
        self.model.add_element(element)
        return element

    def create_relationship(self, id: int, source_id: int, target_id: int, type: str) -> Relationship:
        relationship = Relationship(id=id, source_id=source_id, target_id=target_id, type=type)
        self.model.add_relationship(relationship)
        return relationship

    def get_element(self, element_id: int) -> Optional[BaseArchiMateElement]:
        return self.model.get_element_by_id(element_id)

    def get_all_elements(self) -> List[BaseArchiMateElement]:
        return (
            self.model.business_processes +
            self.model.business_functions +
            self.model.application_components +
            self.model.application_services +
            self.model.technology_services +
            self.model.nodes
        )

    def get_relationships(self) -> List[Relationship]:
        return self.model.relationships

    def update_element(self, element_id: int, name: str = None, description: str = None) -> Optional[BaseArchiMateElement]:
        element = self.get_element(element_id)
        if element:
            if name:
                element.name = name
            if description:
                element.description = description
        return element

    def delete_element(self, element_id: int) -> bool:
        for attr in dir(self.model):
            if attr.endswith('s') and isinstance(getattr(self.model, attr), list):
                elements = getattr(self.model, attr)
                for i, element in enumerate(elements):
                    if element.id == element_id:
                        elements.pop(i)
                        return True
        return False

    def delete_relationship(self, relationship_id: int) -> bool:
        for i, relationship in enumerate(self.model.relationships):
            if relationship.id == relationship_id:
                self.model.relationships.pop(i)
                return True
        return False
