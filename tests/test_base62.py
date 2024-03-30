import pytest

from src.base62 import encode, decode


@pytest.mark.parametrize(
    "num,encoded",
    [(0, "0"), (61, "Z"), (62, "10"), (123, "1Z"), (124, "20"), (3844, "100")],
)
def test_encode(num: int, encoded: str):
    assert encode(num) == encoded


@pytest.mark.parametrize(
    "num,decoded",
    [("0", 0), ("Z", 61), ("10", 62), ("1Z", 123), ("20", 124), ("100", 3844)],
)
def test_decode(num, decoded):
    assert decode(num) == decoded
