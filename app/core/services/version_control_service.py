import os

from app.core.models.mas.mas_version_control import MASVersionControl


class VersionControlService:
    def __init__(self):
        repo_path = os.getenv('MAS_REPO_PATH', '/path/to/your/mas/project')
        self.vc = MASVersionControl(repo_path)

    def commit_changes(self, message: str):
        self.vc.commit_changes(message)

    def create_branch(self, branch_name: str):
        self.vc.create_branch(branch_name)

    def merge_branch(self, branch_name: str):
        self.vc.merge_branch(branch_name)

    def list_branches(self):
        return self.vc.list_branches()

    def get_commit_history(self):
        return self.vc.get_commit_history()