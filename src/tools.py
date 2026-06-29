from langchain_community.tools import WikipediaQueryRun
from langchain_community.tools import ArxivQueryRun

from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import ArxivAPIWrapper

wiki=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
arxiv_tool=ArxivQueryRun(api_wrapper=ArxivAPIWrapper(top_k_results=3,doc_content_chars_max=2000))

from langchain.tools import tool
@tool
def calculator(expression: str) -> str:
    """
    Perform mathematical calculations on a given expression.
    """
    return str(eval(expression))