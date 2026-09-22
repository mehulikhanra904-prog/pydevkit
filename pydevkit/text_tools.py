def analyze_text(text: str) -> dict:
    words = text.split()
    characters = len(text)
    lines = len(text.splitlines())

    return {
        "words": len(words),
        "characters": characters,
        "lines": lines,
    }