import logging

from core.cli import CLI
from core.review_manager import ReviewManager
from core.service import OllamaService

logger = logging.getLogger(__name__)


def main():
    """The main function for running the code review tool."""

    # Set up logging
    logging.basicConfig(filename='code-reviewer.log', level=logging.INFO)

    try:
        # Parse command-line arguments
        cli = CLI()
        args = cli.parse_args()

        # Initialize the ReviewManager
        rm = ReviewManager()
        # Extract filename and programming language from the file path
        (filename, programming_language) = rm.parse_filename(args.path)

        # Initialize the OllamaService
        service = OllamaService(args.model, args.host, args.lang, programming_language)

        logger.info(f"Starting review for {filename} with {args.model} model...")

        # Get the code from the file
        code = rm.get_code_from_file(args.path)

        # Analyze the code using the OllamaService
        result = service.analyze_code(code)

        # Parse the review result and write it to a file
        review_result = rm.parse_review_result(result)
        rm.write_review_result(review_result, f"{filename}_{args.model}_review.md")

        logger.info("Review completed successfully.")
    except (FileNotFoundError, ValueError) as e:
        logger.error(e)
        print(f"Error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
