from langchain.tools import WikipediaQueryRun
from langchain.tools import ArxivQueryRun
from langchain.utilities import WikipediaAPIWrapper
from langchain.utilities import ArxivAPIWrapper

wiki=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
arxiv_tool=ArxivQueryRun(api_wrapper=ArxivAPIWrapper(top_k_results=3))

from langchain.tools import tool
@tool
def calculator(expression:str):
    return str(eval(expression))