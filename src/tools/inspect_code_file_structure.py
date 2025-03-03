"""
This file contains a tool to get the file structure of a code file.
"""
import subprocess

from langchain.tools import tool


@tool(parse_docstring=True)
def inspect_code_file_structure(src: str) -> str:
    """ Get the file structure of a code file

    Args:
        src: str: The source code directory path

    Returns:
        str: The file structure returned by running "tree" command on the code file
    """

    # Run the "tree" command on the code file
    process = subprocess.Popen(["tree", src], stdout=subprocess.PIPE)

    # TODO: Add error handling
    output, _ =  process.communicate()

    return output.decode("utf-8")

