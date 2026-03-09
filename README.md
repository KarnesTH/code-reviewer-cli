# 🔍 Local Code Reviewer

A local, privacy-friendly code review tool powered by [Ollama](https://ollama.com). Analyzes your code and generates a
detailed Markdown review report – without sending your code to any external service.

---

## Features

- 🔒 **100% local** – runs entirely via Ollama, no cloud, no data leaves your machine
- 📝 **Structured review output** – security issues, performance issues, style issues and suggestions
- 🌍 **Multilingual** – review reports can be generated in your language
- 📄 **Markdown output** – results are saved as a readable `.md` file

---

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) running locally
- A supported Ollama model (e.g. `qwen3-coder`)

### Python Dependencies

```bash
pip install ollama tqdm
```

---

## Usage

```bash
python main.py  [--model MODEL] [--host HOST] [--lang LANGUAGE]
```

### Arguments

| Argument  | Description                    | Default                  |
|-----------|--------------------------------|--------------------------|
| `path`    | Path to the file to review     | *(required)*             |
| `--model` | Ollama model to use            | `qwen3-coder`            |
| `--host`  | Ollama API host                | `http://localhost:11434` |
| `--lang`  | Language for the review report | `german`                 |

### Examples

```bash
# Basic usage
python main.py my_script.py

# With a specific model and English output
python main.py my_script.py --model mistral --lang english

# Custom Ollama host
python main.py my_script.py --host http://192.168.1.100:11434
```

---

## Output

The review is saved as a Markdown file in the current directory:

```
<filename>_<model>_review.md
```

**Example:** reviewing `service.py` with `qwen2.5-coder` produces `service_qwen2.5-coder_review.md`

### Report Structure

```markdown
# Summary

...

## Security Issues

...

## Performance Issues

...

## Style Issues

...

## Suggestions

...
```

---

## License

[MIT](LICENSE)