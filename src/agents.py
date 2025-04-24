import asyncio
from typing import List, Tuple

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

from config.agent_prompts import (
    DATA_INTEGRATION_SYSTEM_PROMPT,
    ENERGY_OPTIMIZATION_SYSTEM_PROMPT,
    PREDICTIVE_MAINTENANCE_SYSTEM_PROMPT,
    SAFETY_COMPLIANCE_SYSTEM_PROMPT
)
from config.settings import OPENAI_API_KEY, DEFAULT_MODEL

async def initialize_agents() -> Tuple[RoundRobinGroupChat, OpenAIChatCompletionClient]:
    """Initialize the multi-agent system"""
    # Initialize the model client
    model_client = OpenAIChatCompletionClient(
        model=DEFAULT_MODEL,
        api_key=OPENAI_API_KEY
    )
    
    # Create the specialized agents
    data_integration_agent = AssistantAgent(
        "data_integration_agent",
        model_client=model_client,
        system_message=DATA_INTEGRATION_SYSTEM_PROMPT
    )
    
    energy_optimization_agent = AssistantAgent(
        "energy_optimization_agent",
        model_client=model_client,
        system_message=ENERGY_OPTIMIZATION_SYSTEM_PROMPT
    )
    
    predictive_maintenance_agent = AssistantAgent(
        "predictive_maintenance_agent",
        model_client=model_client,
        system_message=PREDICTIVE_MAINTENANCE_SYSTEM_PROMPT
    )
    
    safety_compliance_agent = AssistantAgent(
        "safety_compliance_agent",
        model_client=model_client,
        system_message=SAFETY_COMPLIANCE_SYSTEM_PROMPT
    )
    
    # Create the group chat team
    team = RoundRobinGroupChat(
        [data_integration_agent, energy_optimization_agent, 
         predictive_maintenance_agent, safety_compliance_agent],
        # The data integration agent will always start and end the conversation
        speaker_selection_method="round_robin",
        starting_agent=data_integration_agent
    )
    
    return team, model_client

async def run_scenario(team: RoundRobinGroupChat, scenario_data) -> str:
    """Run a scenario through the multi-agent system"""
    # Convert the building data to a prompt
    prompt = scenario_data.to_prompt()
    
    # Add instructions for the agents
    task = f"""
    The following building data has been received:
    
    {prompt}
    
    Analyze this data, identify any issues or optimization opportunities, and provide recommendations.
    
    Data Integration Agent: First analyze the overall situation and identify which specialized agents need to be consulted.
    Each specialized agent: Analyze the data relevant to your domain and provide specific recommendations.
    Data Integration Agent: After all specialized agents have responded, synthesize their recommendations into a coherent action plan.
    """
    
    # Run the group chat
    result = await team.run(task=task)
    return result

