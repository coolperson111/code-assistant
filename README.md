# Code Assistant for WebDev in AI

LLM based Code assistant that uses LLMs with tool-calling ability to analyse large codebases, and search through latest docs to mainly try and resolve 2 issues
    1. LLMs fail to retain entire context of codebases, I want to emulate a Cursor Composer esque chatbot that can understand the context of the codebase and provide more accurate suggestions
    2. LLMs fail to provide accurate suggestions for the latest libraries, I want to use the tool-calling ability to search through the latest docs and provide accurate suggestions, and avoid all dependancy issues


## Features

- [x] LLM based code assistant
- [x] Tool-calling ability
- [x] Works with various LLMs from Ollama and Gemini
- [x] Context understanding (0.5 - needs improved understanding of the codebase)
- [ ] Latest docs search (0.2 - needs improved web search - currently only does web search)


## Usage

To run the App
```python
python3 main.py
```

```bash
python3 main.py --help

usage: code-assistant [-h] [--src SRC] [--model MODEL]

Code Assistant CLI Tool

options:
  -h, --help            show this help message and exit
  --src SRC, -s SRC     Set the source code directory (default: current directory)
  --model MODEL, -m MODEL
                        Select the model (e.g. "gemini", "deepseek-coder-v2") (default: gemini)
```

