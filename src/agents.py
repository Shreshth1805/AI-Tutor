from src.tools import wiki, arxiv_tool, calculator
from src.llm import get_llm

llm = get_llm()

def ask_agent(question):

    q = question.lower()

    try:

        if any(word in q for word in [
            "research",
            "paper",
            "arxiv",
            "publication"
        ]):

            return arxiv_tool.run(question)

        elif any(word in q for word in [
            "wikipedia",
            "who is",
            "what is",
            "history"
        ]):

            return wiki.run(question)

        elif any(op in q for op in [
            "+",
            "-",
            "*",
            "/"
        ]):

            return calculator.invoke(question)

        else:

            response = llm.invoke(question)

            if hasattr(response, "content"):
                return response.content

            return str(response)

    except Exception as e:

        return f"Error: {str(e)}"