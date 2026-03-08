from core.cli import CLI
from core.review_manager import ReviewManager
from core.service import OllamaService


def main():
    """The main function for running the code review tool."""

    # Parse command-line arguments
    cli = CLI()
    args = cli.parse_args()

    # Initialize the OllamaService
    service = OllamaService(args.model, args.host, args.lang)

    # Initialize the ReviewManager
    rm = ReviewManager()
    # Extract filename and programming language from the file path
    # TODO: add _programming_language to the model prompt. (For better code understanding. I hope so. =))
    (filename, _programming_language) = rm.parse_filename(args.path)
    print("Starting review...")

    # Get the code from the file
    code = rm.get_code_from_file(args.path)

    # Analyze the code using the OllamaService
    result = service.analyze_code(code)

    # Parse the review result and write it to a file
    review_result = rm.parse_review_result(result)
    rm.write_review_result(review_result, f"{filename}_{args.model}_review.md")

    print("Review completed successfully.")


if __name__ == "__main__":
    main()
