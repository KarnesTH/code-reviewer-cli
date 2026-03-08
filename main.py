from core.cli import CLI
from core.review_manager import ReviewManager
from core.service import OllamaService

def main():
    """The main function for running the code review tool."""
    cli = CLI()
    args = cli.parse_args()

    service = OllamaService(args.model, args.host, args.lang)

    rm = ReviewManager()
    path = rm.parse_filename(args.path)
    code = rm.get_code_from_file(args.path)
    result = service.analyze_code(code)

    review_result = rm.parse_review_result(result)
    rm.write_review_result(review_result, f"{path}_review.md")

    print(f"Review completed for {path}")
    print(f"Review saved to {path}_review.md")

if __name__ == "__main__":
    main()