import pathlib
from argparse import ArgumentParser


class CLI(ArgumentParser):
    def __init__(self):
        """Initialize the CLI with the specified arguments."""
        super().__init__()
        self.add_argument("path", help="Path to the input file", type=pathlib.Path)
        self.add_argument(
            "--model",
            help="Model to use for analysis",
            type=str,
            default="qwen2.5-coder",
        )
        self.add_argument(
            "--host",
            help="Host of the Ollama API",
            type=str,
            default="http://localhost:11434",
        )
        self.add_argument(
            "--lang", help="Language you speak", type=str, default="german"
        )
