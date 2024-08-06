# Social Nav Planner

## Setup

### Conda environment

Setup environment with `conda env create -f environment.yml`

### Ollama server

LLM is set up with ollama which is a local web server built on top of llama cpp. It automatically takes care of templates, model download, image loading and etc. 

Mac download with home brew is available. Can also download from https://ollama.com/library. 

Documents for ollama is [here](https://github.com/ollama/ollama/tree/main/docs). We are using [ollama python api](https://github.com/ollama/ollama-python), with usage examples [here](https://github.com/ollama/ollama-python/tree/main/examples)