import json

from ollama import Client
from tqdm import tqdm


class OllamaService:
    def __init__(self, model: str, host: str, language: str):
        """
        Initialize the OllamaService with the specified model, host, and language.

        Parameters:
        model (str): The Ollama model to be used for analysis.
        host (str): The host URL for the Ollama service.
        language (str): The programming language of the code to be analyzed.
        """
        self.client = Client(host)
        self.model = model
        self.language = language

    def analyze_code(self, code: str) -> dict:
        """
        Analyze the given code using the Ollama model and return the analysis result.

        Parameters:
        code (str): The code to be analyzed.

        Returns:
        dict: The analysis result containing security issues, style issues, etc.
        """
        options = {"temperature": 0.0}
        prompt = (
            "You are a senior software engineer performing a professional code review.\n"
            "Analyze the following code and provide a detailed review.\n"
            "IMPORTANT:\n"
            "1. LANGUAGE: Identify the language and use its specific idiomatic best practices.\n"
            "2. NO TRIVIA: Do not report issues in commented-out code. Do not report hardcoded 'localhost' as a security risk.\n"
            "3. IGNORE DEAD CODE: Do not comment on commented-out code or unused imports unless they are a security risk.\n"
            "4. HONESTY: If a category has no significant issues, return an empty list [].\n"
            "5. CLEAN CODE: Apply Clean Code principles. A method that does one thing well is not a style issue.\n"
            "Generator expressions consumed exactly once are idiomatic Python, not a style issue.\n"
            "Only report style issues that genuinely reduce readability or maintainability.\n\n"
            "Return your answer in the given language.\n"
            "language:\n"
            f"{self.language}\n\n"
            "Return your answer strictly in JSON with the following structure:\n"
            "{\n"
            '  "summary": "...",\n'
            '  "security_issues": ["..."],\n'
            '  "performance_issues": ["..."],\n'
            '  "style_issues": ["..."],\n'
            '  "suggestions": ["..."]\n'
            "}\n"
            "Code:\n"
            f"{code}\n"
        )

        response = self.client.generate(
            model=self.model, prompt=prompt, format="json", stream=True, options=options
        )

        pb = tqdm(total=None, desc="Reviewing code", unit=" chunks")

        full_text = ""
        for chunk in response:
            full_text += chunk.response
            pb.update(1)
            if chunk.done:
                break
        pb.close()

        result = json.loads(full_text)
        return result
