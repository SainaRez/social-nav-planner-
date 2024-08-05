import os
import socket
import pathlib
from typing import Callable

WORKING_DIR = pathlib.Path(__file__).parent.parent.parent.resolve()
DATA_DIR = WORKING_DIR
CACHE_DIR = WORKING_DIR / ".experiment_cache"
LLM_DIR = WORKING_DIR / "llms"


def allow_abs(fun: Callable[[str], str]) -> Callable[[str], str]:
    # wrapper to return no add anything if user give a abs path
    def _wrapper(path):
        if path[0] == '/':
            return path
        else:
            return fun(path)

    return _wrapper


def working_dir_path(relative_path: str) -> str:
    """ "
    given a path relative to working dir (llm_experiment)
    return absolute path
    """
    return str((WORKING_DIR / relative_path).resolve())
