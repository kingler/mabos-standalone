from pade.misc.utility import start_loop
from pade.acl.aid import AID
from core.agents.business_agent import BusinessAgent

if __name__ == "__main__":
    agents = []
    agent_name = "business_agent_1@localhost:5000"
    agent_1 = BusinessAgent(AID(name=agent_name))
    agents.append(agent_1)

    start_loop(agents)