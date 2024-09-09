from typing import List, Optional

from pydantic import BaseModel


class BaseArchiMateElement(BaseModel):
    id: int
    name: str
    description: str

class BusinessProcess(BaseArchiMateElement):
    pass

class BusinessFunction(BaseArchiMateElement):
    pass

class ApplicationComponent(BaseArchiMateElement):
    pass

class ApplicationService(BaseArchiMateElement):
    pass

class TechnologyService(BaseArchiMateElement):
    pass

class Node(BaseArchiMateElement):
    pass

class Relationship(BaseModel):
    id: int
    source_id: int
    target_id: int
    type: str

class ArchiMateModel(BaseModel):
    business_processes: List[BusinessProcess] = []
    business_functions: List[BusinessFunction] = []
    application_components: List[ApplicationComponent] = []
    application_services: List[ApplicationService] = []
    technology_services: List[TechnologyService] = []
    nodes: List[Node] = []
    relationships: List[Relationship] = []

    def add_element(self, element: BaseArchiMateElement):
        element_type = type(element).__name__.lower() + 's'
        getattr(self, element_type).append(element)

    def add_relationship(self, relationship: Relationship):
        self.relationships.append(relationship)

    def get_element_by_id(self, element_id: int) -> Optional[BaseArchiMateElement]:
        for element_list in [self.business_processes, self.business_functions,
                             self.application_components, self.application_services,
                             self.technology_services, self.nodes]:
            for element in element_list:
                if element.id == element_id:
                    return element
        return None
