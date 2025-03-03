"""
Main file for the Code Assistant CLI Tool

This file contains the main logic for the CLI tool.
Takes in multiline input from the user and starts the chat session with the selected model.
"""

import argparse
import os

from dotenv import load_dotenv

from src.chat.chat import start_chat_session
# from src.models.base import verify_models


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(
        prog="code-assistant",
        description="Code Assistant CLI Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # source code directory, default is current directory
    parser.add_argument(
        "--src", "-s",
        type=str,
        default=os.getcwd(),
        help='Set the source code directory'
    )
    parser.add_argument(
        "--model", "-m",
        type=str,
        default="gemini",
        help='Select the model (e.g. "gemini", "deepseek-coder-v2")'
    )
    args = parser.parse_args()

    # if verify_models(args.model):
    start_chat_session(args.model, args.src)


if __name__ == "__main__":
    main()
