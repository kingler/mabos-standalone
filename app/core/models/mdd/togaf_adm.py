from typing import List
from app.core.models.mdd.mdd_mas_model import OnboardingProcess
from app.core.models.repository import Repository
from app.core.services.version_control_service import VersionControlService

class TOGAFADM:
    def __init__(self):
        self.phases = [
            "Preliminary",
            "Vision",
            "Business Architecture",
            "Information Systems Architecture",
            "Technology Architecture",
            "Opportunities and Solutions",
            "Migration Planning",
            "Implementation Governance",
            "Architecture Change Management"
        ]
        self.enterprise_continuum = EnterpriseContinuum()
        self.repository = Repository()
        self.vc_service = VersionControlService(self.repository)

    def execute_phase(self, phase, onboarding_process: OnboardingProcess):
        if phase not in self.phases:
            raise ValueError(f"Invalid phase: {phase}")
        # Implement the logic for each phase
        if phase == "Preliminary":
            self._preliminary_phase(onboarding_process)
        elif phase == "Vision":
            self._vision_phase(onboarding_process)
        # Add more phases as needed

    def _preliminary_phase(self, onboarding_process: OnboardingProcess):
        # Implement preliminary phase logic for onboarding
        pass

    def _vision_phase(self, onboarding_process: OnboardingProcess):
        # Implement vision phase logic for onboarding
        pass

    def save_artifact(self, artifact_type: str, content: str, filename: str):
        file_location = f"app/repositories/{artifact_type}/{filename}"
        with open(file_location, "w") as file_object:
            file_object.write(content)
        self.vc_service.commit_changes(f"Saved {artifact_type}: {filename}")

class EnterpriseContinuum:
    def __init__(self):
        self.current_state = None
        self.target_state = None
        self.transition_states = []

    def set_current_state(self, state):
        self.current_state = state

    def set_target_state(self, state):
        self.target_state = state

    def add_transition_state(self, state):
        self.transition_states.append(state)

    def get_current_state(self):
        return self.current_state

    def get_target_state(self):
        return self.target_state

    def get_transition_states(self):
        return self.transition_states