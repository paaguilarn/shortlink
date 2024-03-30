import re

from . import ALPHABET


def _remove_leading_zeros(data: str) -> str:
    data = data.lstrip("0")
    return data if data else "0"


def _contains_only_allowed_characters(data: str) -> bool:
    exp = f"^[{ALPHABET}]*$"
    match = re.search(exp, data)
    return match is not None


def clean_encoded_string(data: str) -> str:
    if not _contains_only_allowed_characters(data):
        raise ValueError(f"Invalid characters in {data}")
    data = _remove_leading_zeros(data)
    return data
