import json
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.models.openai_client import openai_client
from app.models.system.multi_model_view import (
    ArchitecturalView, BusinessDevelopmentView, CommunicationView,
    EnvironmentalView, IntentionalView, OperationsView,
    PerformanceMeasurementView)
from app.models.system.multiagent_system import MultiAgentSystem

router = APIRouter()
mas = MultiAgentSystem()

@router.post("/generate-model")
async def generate_mas_model(prompt: str):
    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Generate a Multi-Agent System (MAS) model based on the given prompt. Output should be in JSON format with 'nodes' and 'edges' fields."},
            {"role": "user", "content": prompt}
        ]
    )
    model_data = json.loads(response.choices[0].message.content)
    mas.id = str(uuid4())
    mas.type = "MAS"
    mas.nodes = model_data["nodes"]
    mas.edges = model_data["edges"]
    return {"id": mas.id, "type": mas.type, "nodes": mas.nodes, "edges": mas.edges}

@router.get("/architectural_view")
def render_architectural_view():
    view = ArchitecturalView()
    view_model = view.render(mas)
    return view_model.to_dict()

@router.get("/communication_view")
def render_communication_view():
    view = CommunicationView()
    view_model = view.render(mas)
    return view_model.to_dict()

@router.get("/environmental_view")
def render_environmental_view():
    view = EnvironmentalView()
    view_model = view.render(mas)
    return view_model.to_dict()

@router.get("/intentional_view")
def render_intentional_view():
    view = IntentionalView()
    view_model = view.render(mas)
    return view_model.to_dict()

@router.get("/business_development_view")
def render_business_development_view():
    view = BusinessDevelopmentView()
    view_model = view.render(mas)
    return view_model.to_dict()

@router.get("/operations_view")
def render_operations_view():
    view = OperationsView()
    view_model = view.render(mas)
    return view_model.to_dict()

@router.get("/performance_measurement_view")
def render_performance_measurement_view():
    view = PerformanceMeasurementView()
    view_model = view.render(mas)
    return view_model.to_dict()