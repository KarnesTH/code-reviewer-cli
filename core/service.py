import json

from ollama import Client
from tqdm import tqdm

from core.template_manager import TemplateManager


class OllamaService:
    def __init__(self, model: str, host: str, language: str, programming_language: str):
        """
        Initialize the OllamaService with the specified model, host, and language.

        Parameters:
        model (str): The Ollama model to be used for analysis.
        host (str): The host URL for the Ollama service.
        language (str): The programming language of the code to be analyzed.
        programming_language (str): The specific programming language for code analysis.
        """
        self.client = Client(host)
        self.model = model
        self.language = language
        self.programming_language = programming_language

    def analyze_code(self, code: str) -> dict:
        """
        Analyze the given code using the Ollama model and return the analysis result.

        Parameters:
        code (str): The code to be analyzed.

        Returns:
        dict: The analysis result containing security issues, style issues, etc.
        """
        context_prompt = (
            "Analyze the following code and identify:\n"
            "1. The purpose and type of this application\n"
            "2. Intentional design decisions and WHY they were made\n"
            "3. UX-relevant elements and their intent\n\n"
            f"Code:\n{code}"
        )
        context = self.client.generate(model=self.model, prompt=context_prompt)

        print(context.response)

        options = {"temperature": 0.0}
        tm = TemplateManager("templates")
        rules_template = tm.get_template("RULES.md")
        rules = tm.parse_template(rules_template, {
            "programming_language": self.programming_language,
            "output_language": self.language,
            "context": context
        })
        prompt = (
            f"{rules}\n\n"
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
