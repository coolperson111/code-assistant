"""
Contains the input functions for the CLI tool.
"""

import sys

from src.console import console


def take_multiline_input() -> str:
    """
    Take multiline input from the user
    """

    console.print("Enter your message below. [bold green]Press Ctrl+D to send the message.[/bold green]")
    console.print("[bold blue]> [/bold blue]", end="")

    lines = [] # store the lines of input
    n_lines = 0 # number of lines to clear after taking input

    while True:
        try:
            lines.append(console.input()) # Capture input without displaying the prompt
            n_lines += 1
        except EOFError:
            # remove lines in the end which are empty
            while lines and not lines[0]:
                lines.pop(0)
            while lines and not lines[-1]:
                lines.pop()

            # if lines is empty, continue the loop
            if not lines:
                # sys.stdout.write("\033[F")  # Move cursor up
                sys.stdout.write("\033[2D")  # Clear line
                sys.stdout.write("\033[K")  # Clear line
                console.print("[bold red]Please enter a message.[/bold red]")
                console.print("[bold blue]> [/bold blue]", end="")
                n_lines += 1
                continue
            break

    # clear the lines, so chat is shown above clearly
    for _ in range(n_lines+1):
        sys.stdout.write("\033[F")  # Move cursor up
        sys.stdout.write("\033[K")  # Clear line

    message = "\n".join(lines)
    return message
