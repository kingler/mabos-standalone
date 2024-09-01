import os
from typing import Dict, Optional

import git
from pydantic import BaseModel, Field


class RepositoryConfig(BaseModel):
    """
    Pydantic model for repository configuration.
    """
    ontology_path: str = Field(default="ontologies", description="Path to ontology files")
    repo_path: str = Field(default="repositories", description="Base path for the repository")
    rules_path: str = Field(default="rules", description="Path to rules files")
    business_goals_path: str = Field(default="business_goals", description="Path to business goals files")
    topic_map_path: str = Field(default="topic_maps", description="Path to topic map files")
    archimate_path: str = Field(default="archimate", description="Path to ArchiMate files")
    bpmn_path: str = Field(default="bpmn", description="Path to BPMN files")
    tropos_path: str = Field(default="tropos", description="Path to Tropos files")
    uml_path: str = Field(default="uml", description="Path to UML files")
    auth_credentials: Dict[str, str] = Field(
        default={"username": "default_user", "password": "default_password"},
        description="Authentication credentials"
    )
    ontology_repo_path: str = Field(
        default="/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/repositories/ontologies",
        description="Path to ontology repository"
    )

class Repository:
    """
    Manages repository configuration and provides methods to access and update paths and credentials.
    """
    def __init__(self, config: Optional[Dict[str, str]] = None):
        """
        Initialize the Repository with optional configuration.

        Args:
            config (Optional[Dict[str, str]]): Configuration dictionary. If None, default configuration is used.
        """
        self.config = RepositoryConfig(**(config or {}))
        self.ensure_repo_path()

    def ensure_repo_path(self):
        """
        Ensure the repo_path is a valid Git repository.
        """
        repo_path = self.get_path('repo_path')
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
        try:
            git.Repo(repo_path)
        except git.exc.InvalidGitRepositoryError:
            git.Repo.init(repo_path)

    def get_path(self, key: str) -> str:
        """
        Get the path for a specific key from the configuration.

        Args:
            key (str): The configuration key.

        Returns:
            str: The path associated with the key.
        """
        return getattr(self.config, key, "")

    def set_path(self, key: str, path: str):
        """
        Set the path for a specific key in the configuration.

        Args:
            key (str): The configuration key.
            path (str): The path to set.
        """
        setattr(self.config, key, path)

    def get_auth_credentials(self) -> Dict[str, str]:
        """
        Get the authentication credentials.

        Returns:
            Dict[str, str]: The authentication credentials.
        """
        return self.config.auth_credentials

    def set_auth_credentials(self, username: str, password: str):
        """
        Set the authentication credentials.

        Args:
            username (str): The username to set.
            password (str): The password to set.
        """
        self.config.auth_credentials = {"username": username, "password": password}

    def update_based_on_mas_activities(self, activity_data: Dict[str, str]):
        """
        Update the configuration based on MAS activities.

        Args:
            activity_data (Dict[str, str]): Activity data to update the configuration.
        """
        for key, value in activity_data.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)