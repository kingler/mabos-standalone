from plantuml import PlantUML

class UMLDiagramGenerator:
    def __init__(self, server_url='http://www.plantuml.com/plantuml/img/'):
        self.plantuml = PlantUML(url=server_url)

    def generate_agent_diagram(self, agent):
        uml_code = self._generate_agent_uml_code(agent)
        return self.plantuml.processes(uml_code)

    def generate_mas_diagram(self, mas):
        uml_code = self._generate_mas_uml_code(mas)
        return self.plantuml.processes(uml_code)

    def _generate_agent_uml_code(self, agent):
        # Generate PlantUML code for agent components
        uml_code = "@startuml\n"
        uml_code += f"class {agent.__class__.__name__} {{\n"
        for attr, value in agent.__dict__.items():
            uml_code += f"  {attr} : {type(value).__name__}\n"
        uml_code += "}\n@enduml"
        return uml_code

    def _generate_mas_uml_code(self, mas):
        # Generate PlantUML code for entire MAS
        uml_code = "@startuml\n"
        for agent in mas.agents:
            uml_code += f"class {agent.__class__.__name__} {{\n"
            for attr, value in agent.__dict__.items():
                uml_code += f"  {attr} : {type(value).__name__}\n"
            uml_code += "}\n"
        uml_code += "@enduml"
        return uml_code
