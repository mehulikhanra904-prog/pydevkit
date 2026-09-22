import secrets
import string


def generate_password(length: int = 12) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )