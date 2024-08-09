from pydantic import BaseModel
from typing import List


class AgentRole(BaseModel):
    name: str
    responsibilities: List[str]
    """
    Represents a role that an agent can occupy within a BDI multiagent system.
    Roles provide structure and organization to interactions, task allocation, and decision-making.
    """

    def allocate_task(self, task):
        """
        Allocate a task to the role based on its responsibilities.
        """
        for responsibility in self.responsibilities:
            if task.description.lower() in responsibility.lower():
                print(f"Task '{task.description}' allocated to role '{self.name}'")
                return True
        
        print(f"Task '{task.description}' does not match any responsibilities of role '{self.name}'")
        return False

    def reallocate_role(self, new_agent):
        """
        Reallocate the role to a new agent in case of failure or changing circumstances.
        """
        if new_agent.has_capabilities(self.responsibilities):
            print(f"Role '{self.name}' reallocated to agent '{new_agent.name}'")
            new_agent.add_role(self)
            return True
        else:
            print(f"Agent '{new_agent.name}' does not have the necessary capabilities for role '{self.name}'")
            return False

    def support_decision_making(self, context, team_objectives):
        """
        Provide a framework for decision-making based on the role's responsibilities and team objectives.
        """
        relevant_responsibilities = [resp for resp in self.responsibilities if resp.lower() in context.lower()]
        
        if relevant_responsibilities:
            print(f"Role '{self.name}' has relevant responsibilities for decision-making in the given context.")
            print(f"Relevant responsibilities: {', '.join(relevant_responsibilities)}")
            
            # Implement specific decision-making logic based on the relevant responsibilities and team objectives
            decision_scores = {}
            for objective in team_objectives:
                score = 0
                for resp in relevant_responsibilities:
                    if resp.lower() in objective.lower():
                        score += 1
                decision_scores[objective] = score
            
            # Select the decision with the highest score
            best_decision = max(decision_scores, key=decision_scores.get)
            
            print(f"Decision made by role '{self.name}': {best_decision}")
            return best_decision
        else:
            print(f"Role '{self.name}' does not have relevant responsibilities for decision-making in the given context.")
            return None
    
    def make_decision(self, context, relevant_responsibilities):
        """
        Make a decision based on the context and relevant responsibilities.
        """
        decision_scores = {}
        for responsibility in relevant_responsibilities:
            score = 0
            if responsibility.lower() in context.lower():
                score += 1
            decision_scores[responsibility] = score
        
        if decision_scores:
            best_decision = max(decision_scores, key=decision_scores.get)
            print(f"Decision made by role '{self.name}': {best_decision}")
            return best_decision
        else:
            print(f"No relevant responsibilities found for decision-making in the given context.")
            return None

    def facilitate_knowledge_exchange(self, knowledge):
        """
        Organize and facilitate the exchange of knowledge between agents.
        """
        # Identify agents with relevant knowledge
        relevant_agents = [agent for agent in self.agents if agent.has_knowledge(knowledge)]
        
        if relevant_agents:
            print(f"Role '{self.name}' facilitating knowledge exchange for: {knowledge}")
            
            # Create a knowledge sharing session
            session_id = self.create_knowledge_sharing_session(knowledge)
            
            # Invite relevant agents to the session
            for agent in relevant_agents:
                self.invite_agent_to_session(agent, session_id)
            
            # Facilitate knowledge exchange during the session
            self.facilitate_session(session_id)
            
            print(f"Knowledge exchange session '{session_id}' completed.")
        else:
            print(f"No agents found with relevant knowledge for: {knowledge}")

    def adapt_to_changes(self, environment):
        """
        Adapt the role's responsibilities and actions in response to environmental changes.
        """
        # Detect changes in the environment
        changes = self.detect_environmental_changes(environment)
        
        if changes:
            print(f"Role '{self.name}' detected changes in the environment: {changes}")
            
            # Assess the impact of the changes on the role's responsibilities
            impacted_responsibilities = self.assess_impact_on_responsibilities(changes)
            
            if impacted_responsibilities:
                print(f"Impacted responsibilities: {', '.join(impacted_responsibilities)}")
                
                # Adjust the role's responsibilities based on the changes
                self.adjust_responsibilities(impacted_responsibilities)
                
                # Modify the role's actions to align with the updated responsibilities
                self.modify_actions()
                
                print(f"Role '{self.name}' adapted to the environmental changes.")
            else:
                print(f"No significant impact on the role's responsibilities.")
        else:
            print(f"No significant changes detected in the environment.")
