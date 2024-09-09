from typing import Any, Dict, List

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.models.knowledge.ontology.ontology import Ontology
from app.db.database import Base

class DatabaseSchemaGenerator:
    def __init__(self):
        self.Base = Base

    def generate_schema(self, ontology: Ontology) -> Dict[str, Any]:
        schema = {}
        
        for concept in ontology.concepts.values():
            class_name = concept.name.capitalize()
            class_attrs = {
                '__tablename__': f"{concept.name.lower()}s",
                'id': Column(Integer, primary_key=True)
            }
            
            prop_type_mapping = {
                'string': String,
                'integer': Integer,
                'float': Float
            }
            
            for prop in ontology.get_properties_for_concept(concept.name):
                if prop.range in prop_type_mapping:
                    class_attrs[prop.name] = Column(prop_type_mapping[prop.range])
            
            for rel in ontology.get_relationships_for_concept(concept.name):
                if rel.type == 'many_to_one':
                    class_attrs[f"{rel.name}_id"] = Column(Integer, ForeignKey(f"{rel.target.lower()}s.id"))
                    class_attrs[rel.name] = relationship(rel.target.capitalize())
            
            schema[class_name] = type(class_name, (self.Base,), class_attrs)

        return schema

    def create_tables(self, schema: Dict[str, Any]):
        for table_name, columns in schema.items():
            Table(table_name, self.Base.metadata, *columns.values())

    def generate_orm_classes(self, schema: Dict[str, Any]) -> List[Any]:
        orm_classes = []
        for table_name, columns in schema.items():
            class_name = table_name[:-1].replace('_', ' ').title().replace(' ', '')
            orm_class = type(class_name, (self.Base,), {
                '__tablename__': table_name,
                **dict(columns.items()),
            })
            orm_classes.append(orm_class)
        return orm_classes

    def generate_and_create_schema(self, ontology: Ontology):
        schema = self.generate_schema(ontology)
        self.create_tables(schema)
        return self.generate_orm_classes(schema)