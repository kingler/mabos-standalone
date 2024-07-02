import git
from pydantic import BaseModel
from typing import List

class CommitInfo(BaseModel):
    id: str
    message: str

class BranchInfo(BaseModel):
    name: str

class MASVersionControl:
    def __init__(self, repo_path: str):
        self.repo = git.Repo(repo_path)

    def commit_changes(self, message: str):
        self.repo.git.add(A=True)
        self.repo.index.commit(message)

    def create_branch(self, branch_name: str):
        self.repo.git.checkout('-b', branch_name)

    def merge_branch(self, branch_name: str):
        self.repo.git.merge(branch_name)

    def list_branches(self):
        return [branch.name for branch in self.repo.branches]

    def get_commit_history(self):
        return [git.Commit(self.repo, commit) for commit in self.repo.iter_commits()]