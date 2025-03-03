"""
trying out the rich library - framework for our chat

result: rich is what i want, it is a good choice for chat app
"""

import sys
from textwrap import dedent

from rich.align import Align
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def take_multiline_input(prompt: str) -> str:
    """
    Take multiline input from the user
    """

    console.print("Enter your message below. [green]Press Ctrl+D to send the message.[/green]")

    # console.print("Enter your message below. Press Ctrl+D to send the message.")
    console.print("[bold blue]> [/bold blue]", end="")

    lines = [] # store the lines of input
    n_lines = 0 # number of lines to clear after taking input

    while True:
        try:
            lines.append(input()) # Capture input without displaying the prompt
            n_lines += 1
        except EOFError:
            # remove lines in the end which are empty
            while lines and not lines[0]:
                lines.pop(0)
            while lines and not lines[-1]:
                lines.pop()

            # if lines is empty, continue the loop
            if not lines:
                console.print("Please enter a message.")
                n_lines += 1
                continue
            break

    # clear the lines, so chat is shown above clearly
    for _ in range(n_lines):
        sys.stdout.write("\033[F")  # Move cursor up
        sys.stdout.write("\033[K")  # Clear line

    message = "\n".join(lines)
    return message

def echo_chat():
    """
    Echo chat
    Take user input into a prompt and echo it back
    own messages right align into a panel
    echo messages left align into a panel
    """

    while True:
        message = take_multiline_input("") 

        # Clear the last typed input from the terminal
        sys.stdout.write("\033[F")  # Move cursor up
        sys.stdout.write("\033[K")  # Clear line

        MARKDOWN = dedent("""
        ### This is an h1

        Rich can do a pretty *decent* job of rendering markdown.

        1. This is a list item
        2. This is another list item
        """)

        console.print(Align(Panel.fit(message, title="you", border_style="green"), "right"))
        console.print(Align(Panel.fit(Align(Markdown(MARKDOWN), "left"), title="bot", border_style="green"), "left"))


if __name__ == "__main__":
    echo_chat()
