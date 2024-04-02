import pytest

from src.utils import clean_encoded_string


def test_encoded_number_with_invalid_string_raises_exception():
    data = "1234ABCDabcd$ABCD"
    with pytest.raises(ValueError):
        data = clean_encoded_string(data)


def test_encoded_number_gets_leading_zeros_removed():
    data = "001"
    assert clean_encoded_string(data) == "1"


def test_zero_with_leading_zeros_gets_cleaned():
    data = "000"
    assert clean_encoded_string(data) == "0"
