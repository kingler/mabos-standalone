from typing import Dict, Any, List
from uuid import UUID, uuid4
from app.core.models.erp.erp_models import (
    ERPModule, FinancialModule, HRModule, CRMModule, SupplyChainModule,
    InventoryModule, ProjectManagementModule, ManufacturingModule, ERPSystem
)

class ERPService:
    def __init__(self):
        self.erp_systems: Dict[UUID, ERPSystem] = {}

    async def create_erp_system(self, name: str) -> ERPSystem:
        erp_id = uuid4()
        erp_system = ERPSystem(id=erp_id, name=name, modules=[])
        self.erp_systems[erp_id] = erp_system
        return erp_system

    async def add_module(self, erp_id: UUID, module: ERPModule) -> ERPModule:
        if erp_id not in self.erp_systems:
            raise ValueError("ERP system not found")
        self.erp_systems[erp_id].modules.append(module)
        return module

    async def get_erp_system(self, erp_id: UUID) -> ERPSystem:
        if erp_id not in self.erp_systems:
            raise ValueError("ERP system not found")
        return self.erp_systems[erp_id]

    async def update_module(self, erp_id: UUID, module_id: UUID, updates: Dict[str, Any]) -> ERPModule:
        erp_system = await self.get_erp_system(erp_id)
        for module in erp_system.modules:
            if module.id == module_id:
                for key, value in updates.items():
                    setattr(module, key, value)
                return module
        raise ValueError("Module not found")

    async def delete_module(self, erp_id: UUID, module_id: UUID) -> None:
        erp_system = await self.get_erp_system(erp_id)
        erp_system.modules = [m for m in erp_system.modules if m.id != module_id]

    async def list_erp_systems(self) -> List[ERPSystem]:
        return list(self.erp_systems.values())

    async def update_erp_system(self, erp_id: UUID, name: str) -> ERPSystem:
        if erp_id not in self.erp_systems:
            raise ValueError("ERP system not found")
        self.erp_systems[erp_id].name = name
        return self.erp_systems[erp_id]

    async def delete_erp_system(self, erp_id: UUID) -> None:
        if erp_id not in self.erp_systems:
            raise ValueError("ERP system not found")
        del self.erp_systems[erp_id]

    async def list_modules(self, erp_id: UUID) -> List[ERPModule]:
        erp_system = await self.get_erp_system(erp_id)
        return erp_system.modules

    async def get_module(self, erp_id: UUID, module_id: UUID) -> ERPModule:
        erp_system = await self.get_erp_system(erp_id)
        for module in erp_system.modules:
            if module.id == module_id:
                return module
        raise ValueError("Module not found")

    async def generate_module(self, module_type: str, requirements: Dict[str, Any]) -> ERPModule:
        module_id = uuid4()
        if module_type == "financial":
            return FinancialModule(id=module_id, name="Financial Management", **requirements)
        elif module_type == "hr":
            return HRModule(id=module_id, name="Human Resources", **requirements)
        elif module_type == "crm":
            return CRMModule(id=module_id, name="Customer Relationship Management", **requirements)
        elif module_type == "supply_chain":
            return SupplyChainModule(id=module_id, name="Supply Chain Management", **requirements)
        elif module_type == "inventory":
            return InventoryModule(id=module_id, name="Inventory Management", **requirements)
        elif module_type == "project":
            return ProjectManagementModule(id=module_id, name="Project Management", **requirements)
        elif module_type == "manufacturing":
            return ManufacturingModule(id=module_id, name="Manufacturing Management", **requirements)
        else:
            raise ValueError(f"Unknown module type: {module_type}")