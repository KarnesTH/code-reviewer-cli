import os


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
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file {path} does not exist.")
        else:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()

    @staticmethod
    def parse_review_result(result: dict) -> str:
        """
        Parse the review result dictionary and generate a formatted review report.

        Parameters:
        result (dict): The review result dictionary containing analysis details.

        Returns:
        str: The formatted review report.
        """
        summary = result["summary"]
        security_issues = (f"- {txt}" for txt in result["security_issues"])
        performance_issues = (f"- {txt}" for txt in result["performance_issues"])
        style_issues = (f"- {txt}" for txt in result["style_issues"])
        suggestions = (f"- {txt}" for txt in result["suggestions"])

        return (
            f"# Summary\n{summary}\n\n"
            f"## Security Issues\n{'\n'.join(security_issues)}\n\n"
            f"## Performance Issues\n{'\n'.join(performance_issues)}\n\n"
            f"## Style Issues\n{'\n'.join(style_issues)}\n\n"
            f"## Suggestions\n{'\n'.join(suggestions)}"
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
        return os.path.splitext(os.path.basename(path))[0]