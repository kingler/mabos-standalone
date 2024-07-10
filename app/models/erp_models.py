from pydantic import BaseModel
from typing import Dict, Any, List
from uuid import UUID

class ERPModule(BaseModel):
    id: UUID
    name: str
    description: str
    config: Dict[str, Any]

class FinancialModule(ERPModule):
    accounting_method: str
    reporting_frequency: str

class HRModule(ERPModule):
    employee_count: int
    payroll_frequency: str

class CRMModule(ERPModule):
    customer_segments: List[str]
    sales_channels: List[str]

class SupplyChainModule(ERPModule):
    suppliers: List[str]
    logistics_partners: List[str]

class InventoryModule(ERPModule):
    warehouses: List[str]
    inventory_method: str

class ProjectManagementModule(ERPModule):
    project_types: List[str]
    resource_types: List[str]

class ManufacturingModule(ERPModule):
    production_lines: List[str]
    quality_control_processes: List[str]

class ERPSystem(BaseModel):
    id: UUID
    name: str
    modules: List[ERPModule]