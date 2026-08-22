#
# Title: llm.py
# Description: wrapper around a local ollama server running llama3.2
# Development Environment: Ubuntu 22.04.5 LTS/python 3.10.12
#

import logging

import ollama

logger = logging.getLogger("mcp")


class LlamaClient:
    def __init__(self, args: dict[str, any]):
        self.host = args["host"]
        self.model = args["model"]
        self.client = ollama.Client(host=self.host)

    def generate(self, system: str, prompt: str) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
        )
        return response["message"]["content"].strip()

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
