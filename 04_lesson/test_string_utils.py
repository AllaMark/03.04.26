import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    (" Hello world", "Hello world"),
    (" Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("skypro", "o", True),
    ("skypro", "f", False),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.parametrize("input_str, input_symbol, expected", 
    [
    ("skypro", "s", "kypro"),
    ("Hello world", "l", "Heo word"),
    ("Pothon", "o", "Pthn"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol,) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("skypro", "w", False),
])
def test_contains_negative(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.parametrize("input_str, input_symbol, expected", 
    [
    ("skypro", "h", "skypro"),
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol,) == expected

    