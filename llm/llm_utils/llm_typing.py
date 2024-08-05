from typing import List, Optional
from typing_extensions import TypedDict, Literal


class ChatMessage(TypedDict, total=False):
    role: Literal["system", "user", "assistant"]
    content: str
    images: List[str]


ChatHistory = List[ChatMessage]
