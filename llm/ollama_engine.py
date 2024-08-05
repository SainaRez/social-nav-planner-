from typing import Optional, Dict
import ollama
from llm_utils import llm_typing


class Ollama:

    def __init__(self, model: str, generation_options: Dict[str, str]):
        self._model = model
        self._options = generation_options

    def chat_completion(
            self,
            messages: llm_typing.ChatHistory,  # prompt
    ):
        response = ollama.chat(
            model=self._model,
            messages=message,  # type: ignore
            options=self._options  # type: ignore
        )  # type: ignore
        return response[message]
