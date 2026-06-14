import re


def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def truncate(text: str, max_length: int = 100) -> str:
    if len(text) <= max_length:
        return text

    return text[: max_length - 3] + "..."


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)

    return text.strip("-")


def extract_code_blocks(text: str) -> list[str]:
    pattern = r"```(?:\w+)?\n(.*?)```"
    return re.findall(pattern, text, re.DOTALL)
