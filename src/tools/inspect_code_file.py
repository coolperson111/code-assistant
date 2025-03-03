"""
This file contains a tool for LLM to use to be able to inspect the code inside a specific file inside a complex codebase structure.
"""
import os

from langchain.tools import tool


@tool(parse_docstring=True)
def inspect_code_file(src_dir: str, file_path: str) -> str:
    """
    Inspect the code file by reading it and returning all lines of code

    Args:
        src_dir (str): The source code directory
        file_path (str): The path to the file to inspect

    Returns:
        list: The list of lines of code in the file
    """

    path = os.path.join(src_dir, file_path)
    with open(path, "r") as file:
        return "\n".join(file.readlines())
