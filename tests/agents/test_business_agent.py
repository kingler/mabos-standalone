import pytest
from app.agents.core_agents.business_agent import BusinessAgent
from app.models.agent.belief import Belief
from app.models.agent.desire import Desire
from app.models.agent.intention import Intention
from app.models.agent.goal import Goal

@pytest.fixture
def business_agent():
    return BusinessAgent(
        agent_id="test_agent",
        name="Test Business Agent",
        business_id="B001",
        business_type="Retail"
    )

def test_init_business_beliefs(business_agent):
    assert any(belief.id == "business_id" for belief in business_agent.beliefs)
    assert any(belief.id == "business_type" for belief in business_agent.beliefs)

def test_init_business_desires(business_agent):
    assert any(desire.id == "increase_profit" for desire in business_agent.desires)
    assert any(desire.id == "expand_market" for desire in business_agent.desires)

@pytest.mark.asyncio
async def test_reason(business_agent):
    context = {
        "financial_data": {
            "revenue": 1000000,
            "expenses": 800000,
            "profit_margin": 0.2
        }
    }
    result = await business_agent.reason(context)
    assert result is not None
    assert any(belief.id == "financial_revenue" for belief in business_agent.beliefs)

def test_deliberate(business_agent):
    business_agent.add_belief(Belief(id="profit_margin", content={"profit_margin": 0.1}, description="Current profit margin", certainty=1.0))
    business_agent.deliberate()
    assert any(intention.id == "implement_cost_cutting" for intention in business_agent.intentions)

@pytest.mark.asyncio
async def test_execute_business_actions(business_agent, caplog):
    business_agent.add_intention(Intention(id="implement_cost_cutting", goal=Goal(id="reduce_costs", description="Reduce operational costs"), plan=None))
    await business_agent._execute_business_actions()
    assert "Implementing cost-cutting measures" in caplog.text

@pytest.mark.asyncio
async def test_act(business_agent, mocker):
    mocker.patch.object(business_agent, 'reason')
    mocker.patch.object(business_agent, 'deliberate')
    mocker.patch.object(business_agent, '_execute_business_actions')
    
    await business_agent.act()
    
    business_agent.reason.assert_called_once()
    business_agent.deliberate.assert_called_once()
    business_agent._execute_business_actions.assert_called_once()