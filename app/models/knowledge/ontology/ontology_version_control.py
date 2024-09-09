import json
from typing import Any, Dict, List

import git
import os
from pydantic import BaseModel

from app.models.knowledge.ontology.ontology import Ontology


class OntologyCommitInfo(BaseModel):
    id: str
    message: str
    ontology_state: Dict[str, Any]

class OntologyVersionControl:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
        try:
            self.repo = git.Repo(repo_path)
        except git.exc.InvalidGitRepositoryError:
            self.repo = git.Repo.init(repo_path)
        self.current_ontology = Ontology()
    
    def commit_changes(self, message: str):
        
        self.repo.git.add(A=True)
        commit = self.repo.index.commit(message)
        return OntologyCommitInfo(
            id=str(commit),
            message=message,
            ontology_state=self.current_ontology.to_dict()
        )

    def create_branch(self, branch_name: str):
        self.repo.git.checkout('-b', branch_name)

    def switch_branch(self, branch_name: str):
        self.repo.git.checkout(branch_name)
        self.current_ontology = self._load_ontology_state()

    def _serialize_ontology_state(self, ontology: Ontology) -> str:
        return json.dumps(ontology.dict(), indent=2)

    def _deserialize_ontology_state(self, state: str) -> Ontology:
        return Ontology(**json.loads(state))

    def _save_ontology_state(self):
        ontology_file = os.path.join(self.repo_path, 'ontology_state.json')
        with open(ontology_file, 'w') as f:
            f.write(self._serialize_ontology_state(self.current_ontology))

    def _load_ontology_state(self) -> Ontology:
        ontology_file = os.path.join(self.repo_path, 'ontology_state.json')
        if os.path.exists(ontology_file):
            with open(ontology_file, 'r') as f:
                return self._deserialize_ontology_state(f.read())
        return Ontology()  # Return an empty ontology if file doesn't exist

    def merge_branch(self, branch_name: str):
        self.repo.git.merge(branch_name)
        # Resolve conflicts if any
        if self.repo.index.unmerged_blobs():
            # Implement conflict resolution logic here
            pass
        # Update the current ontology state after merge
        self.current_ontology = self._merge_ontology_states(branch_name)

    def list_branches(self) -> List[str]:
        return [branch.name for branch in self.repo.branches]

    def get_commit_history(self) -> List[OntologyCommitInfo]:
        return [
            OntologyCommitInfo(
                id=str(commit),
                message=commit.message.strip(),
                ontology_state=self._get_ontology_state_at_commit(commit)
            )
            for commit in self.repo.iter_commits()
        ]
    def _load_ontology_state(self) -> Ontology:
        # Load the ontology state from a file in the current branch
        ontology_file = os.path.join(self.repo_path, 'ontology_state.json')
        if os.path.exists(ontology_file):
            with open(ontology_file, 'r') as f:
                ontology_data = json.load(f)
            return Ontology(**ontology_data)
        return Ontology()  # Return an empty ontology if file doesn't exist

    def _merge_ontology_states(self, branch_name: str) -> Ontology:
        # Save current ontology state
        current_state = self.current_ontology

        # Switch to the branch to merge
        self.repo.git.checkout(branch_name)
        branch_state = self._load_ontology_state()

        # Switch back to the original branch
        self.repo.git.checkout('-')

        # Merge ontology states
        merged_ontology = Ontology()
        merged_ontology.concepts = list(set(current_state.concepts + branch_state.concepts))
        merged_ontology.relationships = list(set(current_state.relationships + branch_state.relationships))

        return merged_ontology

    def _get_ontology_state_at_commit(self, commit) -> Dict[str, Any]:
        # Checkout the specific commit
        self.repo.git.checkout(commit.hexsha)

        # Load the ontology state at this commit
        ontology_at_commit = self._load_ontology_state()

        # Return to the previous state
        self.repo.git.checkout('-')

        return ontology_at_commit.to_dict()

# Example of correct usage
repo_path = "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/app/repositories/ontologies"
ontology_vc = OntologyVersionControl(repo_path)
