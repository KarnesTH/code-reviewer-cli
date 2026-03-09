import pathlib


class TemplateManager:
    """Class for managing Templates."""

    def __init__(self, template_path: str):
        """
        Initialize the TemplateManager with the specified template path

        Parameters:
        template_path (str): The path to the directory containing templates
        """
        self.template_path = template_path

    def get_template(self, template_name: str) -> pathlib.Path:
        """
        Get the template by name.

        Parameters:
        template_name (str): The name of the template

        Returns:
        pathlib.Path: The path to the template file
        """
        basepath = pathlib.Path(self.template_path)
        template_path = basepath / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template {template_name} not found.")
        return template_path

    @staticmethod
    def parse_template(template: pathlib.Path, values: dict) -> str:
        """
        Parse the template with the given values and return the rendered content.

        Parameters:
        template (pathlib.Path): The path to the template file
        values (dict): The values to be replaced in the template

        Returns:
        str: The rendered content with values replaced
        """
        if not template.exists():
            raise FileNotFoundError(f"Template {template} not found.")
        
        with open(template, "r", encoding="utf-8") as file:
            content = file.read()

        for key, value in values.items():
            if type(value) == list:
                items = ""
                for item in value:
                    if len(value) > 0:
                        items += f"- {item}\n"
                    else:
                        items += "No issues found."

                content = content.replace("{{ " + key + " }}", items)
            else:
                content = content.replace("{{ " + key + " }}", str(value))

        return content
