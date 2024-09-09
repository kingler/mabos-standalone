import json
from uuid import UUID

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        return str(obj) if isinstance(obj, UUID) else super().default(obj)
