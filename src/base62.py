from typing import List


from . import ALPHABET, BASE


def _base_decode_alphabet(data: str, alphabet: str) -> List[int]:
    return [alphabet.index(character) for character in data]


def _base_decode(digits: List[int], base: int) -> int:
    total = 0
    for power, digit in enumerate(digits[::-1]):
        total += digit * (base**power)

    return total


def _base_encode(num: int, base: int) -> List[int]:
    if num == 0:
        return [0]
    digits = []
    while num:
        quotient, remainder = divmod(num, base)
        digits.append(remainder)
        num = quotient
    return digits[::-1]


def _base_encode_alphabet(digits: List[int], alphabet: str) -> str:
    return "".join(alphabet[digit] for digit in digits)


def encode(num: int) -> str:
    digits = _base_encode(num, BASE)
    return _base_encode_alphabet(digits, ALPHABET)


def decode(data: str) -> int:
    digits = _base_decode_alphabet(data, ALPHABET)
    return _base_decode(digits, BASE)
