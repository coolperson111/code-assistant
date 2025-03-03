
from typing import Tuple

from langchain.tools import tool


@tool(parse_docstring=True)
def edit_file(filepath: str, line_numbers: Tuple[int, int], new_content: str) -> None:
    """
    Edits a file by replacing the content between the line numbers with new content

    Args:
        filepath (str): The path to the file to edit
        line_numbers (Tuple[int, int]): The line numbers to edit (start, end)
        new_content (str): The new content to replace the old content
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()

    start, end = line_numbers
    lines[start:end] = new_content.split("\n")

    with open(filepath, 'w') as f:
        f.write("".join(lines))
