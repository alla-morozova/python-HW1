import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive_test()
def utils():
    return StringUtils()
# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# Позитивные сценарии:
@pytest.mark.positive()
@pytest.mark.parametrize("input_str, expected",  [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
    ("a", "A"),
    ("погода", "Погода"),
    ("hi", "Hi"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Негативные сценарии:
@pytest.mark.negative()
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("   ", "   "),
    ("None", "None"),
    ("11111", "11111"),
    ("1234567890", "1234567890"),
    ("skypro", "skypro"),
    ("python", "python"),
    ("hello", "HELLO"),
    (" Word", " word")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

#Принимает на вход текст и удаляет пробелы в начале, если они есть
#Позитивные сценарии:
@pytest.mark.positive()
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" hello world ", "hello world "),
    (" python", "python"),
    (" тест", "тест"),
    (" а", "а"),
    (" python", "python"),
])

def test_trim_positive(input_str, expected):
     assert string_utils.trim(input_str) == expected

# Негативные сценарии:
@pytest.mark.negative()
@pytest.mark.parametrize("input_str, expected", [
    (" 123abc", " 123abc"),
    (" ", " "),
    ("  Hi", "  Hi"),
    (" None"," None"),
    (" 11111", " 11111"),
    (" 1234567890", " 1234567890"),
    (" skypro", " skypro"),
    (" python", " python"),
    (" hello"," hello"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
# Позитивные сценарии:
@pytest.mark.positive()
@pytest.mark.parametrize(
    "string, symbol, expected", [
    ("SkyPro", "S", True),
    ("hello world", "h", True),
    ("тест", "т", True),
    ("а", "A", False),
    ("hi", "i", True),
    ("123", "4", False),
])
def test_contains_positive(string, symbol, expected):
     assert string_utils.contains(string, symbol) ==expected

# Негативные сценарии:
@pytest.mark.negative()
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "u", False),
    ("hello world", "1", False ),
    ("тест", "C", False),
    ("а", "A", False),
    ("погода", "k", False),
    ("hi", "D", False),
    ("123", "4", False),
])
def test_contains_negative(string, symbol, expected):
     assert string_utils.contains(string, symbol) == expected

#Удаляет все подстроки из переданной строки
#Позитивные сценарии:
@pytest.mark.positive()
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("hello world", "hello", " world"),
    ("python", "ython", "p"),
    ("тест", "е", "тст"),
    ("a", "a", ""),
    ("погода", "да", "пого"),
    ("hi", "h", "i"),
])

def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

#Негативные сценарии:

@pytest.mark.negative()
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "", ""),
    ("   ", "   ", "   "),
    ("11111", "A", "11111"),
    ("skypro", "x", "skypro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
