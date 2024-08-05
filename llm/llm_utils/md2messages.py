'''
All message templates are written in markdown, this module turns each md file to a series of messages

Each document is a series of messages formatted like

# {role}

Here is the content of the message. A parameter is contand in a box bracket 
like [.this]

```image
if_including_an_image/put_image_path/at_the_end_here.jpg
```

'''
import re
from typing import List, Optional, Dict, Any
import path
from llm_typing import ChatHistory


def add_params_to_message(message: str, params: Dict[str, str]) -> str:
    out_message = message
    for k, v in params.items():
        out_message.replace(f"[.{k}]", v)
    return out_message


def md_to_chat_history(text: str, params: Dict[str, str]) -> ChatHistory:
    '''
    split markdown text by individual messages
    '''

    # breaking md in to messages
    roles = re.findall(
        r"# *(system *|user *|assistant *)",
        text,
        flags=re.M | re.I,
    )
    roles: List[str] = [r.strip().lower() for r in roles]
    contents: List[str] = re.split(
        r"# *(?:system *|user *|assistant *)",
        text,
        flags=re.I,
    )
    contents = [add_params_to_message(c, params).strip() for c in contents[1:]]

    # extrating image addresses if there is one
    images: List[Optional[str]] = []
    for i in range(len(contents)):
        img_addr = re.search(r"```image *\n(.+)\n```", contents[i])
        if img_addr is not None:
            images.append(img_addr.group(1))
            contents[i] = re.sub(r"```image *\n(.+)\n```", "", contents[i])
        else:
            images.append(None)

    out: List[Dict[str, Any]] = [{
        "role": r,
        "content": c
    } for r, c in zip(roles, contents)]

    for i, img in enumerate(images):
        if img is not None:
            out[i]['images'] = [img]
    return out  # type: ignore


if __name__ == "__main__":
    with open(path.working_dir_path("llm/prompts/test.md")) as i_file:
        chat = md_to_chat_history(i_file.read(), {"test": "123"})
    for c in chat:
        print(c, end="\n\n")
