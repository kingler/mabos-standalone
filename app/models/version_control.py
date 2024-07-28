import git
import os
from pydantic import BaseModel
from typing import List
from app.models.repository import Repository

class CommitInfo(BaseModel):
    """
    Represents information about a commit.

    Attributes:
        id (str): The unique identifier of the commit.
        message (str): The commit message.
    """
    id: str
    message: str

class BranchInfo(BaseModel):
    """
    Represents information about a branch.

    Attributes:
        name (str): The name of the branch.
    """
    name: str

class MASVersionControl:
    """
    Manages version control for a Multi-Agent System (MAS) using Git.
    """
    def __init__(self, repository: Repository):
        """
        Initializes the MASVersionControl instance.

        Args:
            repository (Repository): The repository object containing the path to the Git repository.
        """
        self.repo_path = repository.get_path("repo_path")
        if not os.path.exists(self.repo_path):
            raise git.exc.NoSuchPathError(self.repo_path)
        self.repo = git.Repo(self.repo_path)
        self.branches = self.repo.branches

    def commit_changes(self, message: str):
        """
        Commits changes to the repository.

        Args:
            message (str): The commit message.
        """
        self.repo.git.add(A=True)
        self.repo.index.commit(message)

    def create_branch(self, branch_name: str):
        """
        Creates a new branch.

        Args:
            branch_name (str): The name of the branch to create.
        """
        self.repo.git.checkout('-b', branch_name)

    def switch_branch(self, branch_name: str):
        """
        Switches to a different branch.

        Args:
            branch_name (str): The name of the branch to switch to.
        """
        self.repo.git.checkout(branch_name)

    def merge_branch(self, branch_name: str):
        """
        Merges a branch into the current branch.

        Args:
            branch_name (str): The name of the branch to merge.
        """
        self.repo.git.merge(branch_name)

    def list_branches(self) -> List[str]:
        """
        Lists all branches in the repository.

        Returns:
            List[str]: A list of branch names.
        """
        return [branch.name for branch in self.repo.branches]

    def get_commit_history(self) -> List[CommitInfo]:
        """
        Retrieves the commit history of the repository.

        Returns:
            List[CommitInfo]: A list of CommitInfo objects representing the commit history.
        """
        return [CommitInfo(id=str(commit), message=commit.message.strip()) for commit in self.repo.iter_commits()]

    def get_branch(self, branch_name):
        """
        Gets a branch by name.

        Args:
            branch_name (str): The name of the branch to get.

        Returns:
            BranchInfo: The BranchInfo object for the specified branch, or None if not found.
        """
        return next((branch for branch in self.branches if branch.name == branch_name), None)