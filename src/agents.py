from langchain.agents import initialize_agent
from langchain.agents import AgentType

from src.tools import (wiki,arxiv_tool,calculator)
from src.llm import llm 

def agent():
    llm=llm()
    tools=[wiki,arxiv_tool,calculator]
    return initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
