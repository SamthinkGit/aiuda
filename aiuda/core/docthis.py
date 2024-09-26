import os
import sys
from pathlib import Path

from colorama import Fore
from colorama import Style
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from aiuda.prompts.autodoc import AUTODOC_PROMPT


class DocThis:

    def __init__(self, model: str = "gpt-4o-mini") -> None:

        if os.environ["OPENAI_API_KEY"] == "":
            raise SystemError(
                "Please ensure to settle the 'OPENAI_API_KEY' in your enviroment before useing aiuda"
            )

        llm = ChatOpenAI(model=model)
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", AUTODOC_PROMPT),
                ("system", "{additional_input}"),
                ("user", "{input}"),
            ]
        )
        self.chain = prompt | llm

    def __call__(self, additional_prompt: str = "") -> None:
        path = Path(sys.argv[0])
        with open(path, encoding="utf-8") as f:
            file_content = f.read()

        print(f"{Fore.YELLOW + Style.BRIGHT}[docthis] Loading...{Fore.RESET}")
        response = self.chain.invoke(
            {"additional_input": additional_prompt, "input": file_content}
        )
        new_path = path.parent / ("docthis." + path.name)

        with open(f"{new_path}", mode="w") as f:
            f.write(response.content)

        print(f"{Fore.GREEN + Style.BRIGHT}-> Document Generated at `{new_path}`{Fore.RESET}")
