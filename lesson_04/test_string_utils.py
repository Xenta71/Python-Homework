import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("this is a test example", "This is a test example"),
    ("it's a positive test", "It's a positive test"),
    ("other test is negative", "Other test is negative"),
])

def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("@", "@"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   this is a test example", "this is a test example"),
    ("   it's a positive test", "it's a positive test"),
    ("   123abc", "123abc"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("noname", "noname"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, bool", [
    ("Nizhny Novgorod", "N", True),
    ("Nizhny Novgorod", "v", True),
    ("study", "a", False),
])
def test_contains_positive(string, symbol, bool):
    assert string_utils.contains(string, symbol) == bool


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, bool", [
    ("Nizhny", "zh", False),
    ("Novgorod", "gor", False),
    ("hello", "H", True),
    ("1234", "55", True),
])
def test_contains_negative(string, symbol, bool):
    assert string_utils.contains(string, symbol) == bool


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Nizhny", "z", "Nihny"),
    ("Novgorod", "gorod", "Nov"),
    ("Nizhny Novgorod.", ".", "Nizhny Novgorod"),
    ("Nizhny Novgorod", "Novgorod", "Nizhny "),
    ("Nizhny Novgorod", "Nizhny ", "Novgorod")
])

def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Nizhny", "", "Nizhny"),
    ("", "", ""),
    ("Novgorod", "n", "Novgorod"),
    ("Nizhny Novgorod", "-", "Nizhny Novgorod"),
    ])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

