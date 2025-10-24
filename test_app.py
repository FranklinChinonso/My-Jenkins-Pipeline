from app import reverse_and_upper
import pytest

def test_reverse_and_upper_normal():
    assert reverse_and_upper("abc") == "CBA"

def test_reverse_and_upper_empty():
    assert reverse_and_upper("") == ""

def test_reverse_and_upper_non_string():
    with pytest.raises(TypeError):
        reverse_and_upper(123)
