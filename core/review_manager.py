import pathlib
from typing import Any, Generator



class ReviewManager:
    """Class for managing code review operations."""

    @staticmethod
    def get_code_from_file(path: str) -> str:
        """
        Retrieve the code content from a file at the given path.

        Parameters:
        path (str): The path to the file.

        Returns:
        str: The content of the file.
        """
        if not pathlib.Path(path).exists():
            raise FileNotFoundError(f"The file {path} does not exist.")
        else:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()

    @classmethod
    def _extract_list(cls, txt_list: list) -> Generator[str, Any, None]:
        """
        Extract list items with bullet points.

        Parameters:
        txt_list (list): List of text items to format.

        Returns:
        Generator[str, Any, None]: Generator yielding formatted list items.
        """
        return (f"- {txt}" for txt in txt_list)

    @classmethod
    def parse_review_result(cls, result: dict) -> str:
        """
        Parse the review result dictionary and generate a formatted review report.

        Parameters:
        result (dict): The review result dictionary containing analysis details.

        Returns:
        str: The formatted review report.
        """
        return (
            f"# Summary\n{result['summary']}\n\n"
            f"## Security Issues\n{'\n'.join(cls._extract_list(result['security_issues']))}\n\n"
            f"## Performance Issues\n{'\n'.join(cls._extract_list(result['performance_issues']))}\n\n"
            f"## Style Issues\n{'\n'.join(cls._extract_list(result['style_issues']))}\n\n"
            f"## Suggestions\n{'\n'.join(cls._extract_list(result['suggestions']))}"
        )

    @staticmethod
    def write_review_result(result: str, path: str) -> None:
        """
        Write the review result to a file at the specified path.

        Parameters:
        result (str): The formatted review report.
        path (str): The path to the output file.
        """
        with open(path, "w", encoding="utf-8") as file:
            file.write(result)

    @staticmethod
    def parse_filename(path: str) -> str:
        """
        Extract the filename from a given file path.

        Parameters:
        path (str): The file path.

        Returns:
        str: The filename without the extension.
        """
        return pathlib.Path(path).stem