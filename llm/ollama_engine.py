from typing import Optional, Dict
import ollama
from llm_utils import llm_typing, path


class OllamaEngine:

    def __init__(self, model: str, generation_options: Dict[str, str]):
        self._model = model
        self._options = generation_options

    def chat_completion(
            self,
            messages: llm_typing.ChatHistory,  # prompt
    ):
        response = ollama.chat(
            model=self._model,
            messages=messages,  # type: ignore
            options=self._options  # type: ignore
        )  # type: ignore
        return response["message"]


if __name__ == "__main__":
    engine = OllamaEngine("moondream", {})
    res = engine.chat_completion([{
        "role":
        "user",
        "content":
        "what is in this image?",
        "images":
        [path.working_dir_path("llm/prompts/img/bobs_burgers_promo.png")]
    }])
    print(res)
