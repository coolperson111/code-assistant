from langchain.tools import tool

@tool(parse_docstring=True)
def save_file(filepath: str, content: str):
    """
    Saves raw text in the content string to a file specified by filename string

    Args:
        filepath (str): The path to the file to save
        content (str): The content to save to the file

    Returns:
        None
    """
    with open(filepath, 'w') as f:
        f.write(content)
