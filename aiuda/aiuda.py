from aiuda.core.agents import MinimalLangChainAgent
from aiuda.core.types import SupportsStr


class Aiuda:

    def __init__(self) -> None:
        self.agent = MinimalLangChainAgent()

    def tree(self, obj: SupportsStr) -> None:
        prompt = (
            "You are an AI assistant, your goal is to return the given object of the user as a tree representation. "
            "Use the symbols such as ['├'. '─'. '│', '└'] to draw a pretty tree. "
            "Each tag should be encapsulated as [num](tag) or .tag depending on how to access that item in python"
        )
        input = str(obj)
        result = self.agent.invoke(prompt, input)
        print(result.content)
