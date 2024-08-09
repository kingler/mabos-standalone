from typing import Dict, Any, List
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.core.models.knowledge.ontology.ontology import Ontology

class DatabaseSchemaGenerator:
    def __init__(self):
        self.Base = Base

    def generate_schema(self, ontology: Ontology) -> Dict[str, Any]:
        schema = {}
        
        for concept in ontology.concepts.values():
            class_name = concept.name.capitalize()
            class_attrs = {
                '__tablename__': concept.name.lower() + 's',
                'id': Column(Integer, primary_key=True)
            }
            
            for prop in ontology.get_properties_for_concept(concept.name):
                if prop.range == 'string':
                    class_attrs[prop.name] = Column(String)
                elif prop.range == 'integer':
                    class_attrs[prop.name] = Column(Integer)
                elif prop.range == 'float':
                    class_attrs[prop.name] = Column(Float)
            
            for rel in ontology.get_relationships_for_concept(concept.name):
                if rel.type == 'many_to_one':
                    class_attrs[rel.name + '_id'] = Column(Integer, ForeignKey(rel.target.lower() + 's.id'))
                    class_attrs[rel.name] = relationship(rel.target.capitalize())
            
            schema[class_name] = type(class_name, (self.Base,), class_attrs)

        return schema

    def create_tables(self, schema: Dict[str, Any]):
        for table_name, columns in schema.items():
            Table(table_name, self.Base.metadata, *columns.values())

    def generate_orm_classes(self, schema: Dict[str, Any]) -> List[Any]:
        orm_classes = []
        for table_name, columns in schema.items():
            class_name = ''.join(word.capitalize() for word in table_name[:-1].split('_'))
            orm_class = type(class_name, (self.Base,), {
                '__tablename__': table_name,
                **{col_name: col for col_name, col in columns.items()},
            })
            orm_classes.append(orm_class)
        return orm_classes

    def generate_and_create_schema(self, ontology: Ontology):
        schema = self.generate_schema(ontology)
        self.create_tables(schema)
        orm_classes = self.generate_orm_classes(schema)
        return orm_classes