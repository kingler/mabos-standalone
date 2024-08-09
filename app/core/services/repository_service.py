from typing import Dict, Optional
from app.core.models.repository import RepositoryConfig
from cachetools import TTLCache
import logging
import os

class Repository:
    def __init__(self, config: Optional[RepositoryConfig] = None):
        self.config = config or RepositoryConfig()
        self.cache = TTLCache(maxsize=100, ttl=300)  # Cache with TTL of 5 minutes
        self.base_path = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/repositories"
        self.config = {
            "ontology_path": os.path.join(self.base_path, "ontologies", "business_ontology.owl")
        }

    def get_path(self, key: str) -> str:
        logging.debug(f"get_path called with key: {key} (type: {type(key)})")
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        return self.config.get(key, "")

    def set_path(self, key: str, path: str):
        self.config[key] = path
        self.cache[key] = path

    def get_auth_credentials(self) -> Dict[str, str]:
        if "auth_credentials" in self.cache:
            return self.cache["auth_credentials"]
        credentials = self.config.auth_credentials
        self.cache["auth_credentials"] = credentials
        return credentials

    def set_auth_credentials(self, username: str, password: str):
        self.config.auth_credentials = {"username": username, "password": password}
        self.cache["auth_credentials"] = self.config.auth_credentials

    def update_based_on_mas_activities(self, activity_data: Dict[str, str]):
        for key, value in activity_data.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)