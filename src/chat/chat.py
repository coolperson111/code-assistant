"""
Chat module to start a chat session with the selected model
"""
import json

from langchain_community.tools import DuckDuckGoSearchResults
# from google import genai
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama.chat_models import ChatOllama
from rich.align import Align
from rich.markdown import Markdown
from rich.panel import Panel

from src.chat.input import take_multiline_input
from src.console import console
from src.tools.inspect_code_file import inspect_code_file
from src.tools.inspect_code_file_structure import inspect_code_file_structure


def get_panel_width(markdown_text: str) -> int:
    """
    Get the width of the panel based on the terminal width
    """

    terminal_width = console.width 
    max_width = int(terminal_width * 0.75)
    content_width = len(max(markdown_text.split("\n"), key=len))  # Longest line length
    return min(content_width, max_width)


def start_chat_session(model: str, src: str) -> None:
    """
    Start chat session with the selected model
    - Pretty prints the messages and responses
    - Left aligns the model responses and right aligns the user messages
    - Logs the chat session to a file
    """

    console.print(f"Starting chat session with model: [bold green]{model}[/bold green]")
    console.print(f"Source code directory: [bold cyan]{src}[/bold cyan]")

    sys_instruction = f"You are an AI assistant for code. You can analyse the codebase located at '{src}' and answer questions regarding it."

    if model == "gemini":
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    else:
        llm = ChatOllama(model=model)

    search = DuckDuckGoSearchResults(output_format="list")
    tools = [
        inspect_code_file_structure,
        inspect_code_file,
        search,

        # Commenting out file modification tools because i prefer mostly a suggestive tool
        # save_file,
        # edit_file,
    ]
    tools_dict = {
        "inspect_code_file_structure": inspect_code_file_structure,
        "inspect_code_file": inspect_code_file,
        "duckduckgo_search_results": search,

        # Commenting out file modification tools because i prefer mostly a suggestive tool
        # "save_file": save_file,
        # "edit_file": edit_file,
    }

    llm_tools = llm.bind_tools(tools)

    messages = [SystemMessage(sys_instruction)]

    while True:
        try:
            # take response from human
            message = take_multiline_input()
            messages.append(HumanMessage(message))

            console.print(Align(Panel.fit(message, title="you", border_style="green"), "right"))

            # get response from model
            response1 = llm_tools.invoke(messages)
            messages.append(response1)

            for tool_call in response1.tool_calls:
                selected_tool = tools_dict[tool_call["name"].lower()]
                tool_msg = selected_tool.invoke(tool_call)
                messages.append(tool_msg)

            tools_width = get_panel_width(str(response1.tool_calls))
            content1_width = get_panel_width(response1.content)
            if response1.tool_calls:
                console.print(Align(Panel.fit(Markdown(json.dumps(response1.tool_calls)), title="bot", border_style="blue", width=tools_width), "left"))
            if response1.content:
                console.print(Align(Panel.fit(Markdown(response1.content), title="bot", border_style="green", width=content1_width), "left"))


            response2 = llm_tools.invoke(messages)

            content_width = get_panel_width(response2.content)
            console.print(Align(Panel.fit(Markdown(response2.content), title="bot", border_style="green", width=content_width), "left"))

        except KeyboardInterrupt:
            console.print("[bold red]Chat session ended.[/bold red]")
            break

