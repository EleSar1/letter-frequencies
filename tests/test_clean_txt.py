import pytest

from src.processing import clean_txt


def test_clean_text_success():

    sentence = "hello world"
    cleaned = "helloworld"
    result = clean_txt(sentence)

    assert cleaned == result


def test_with_numbers_and_letters():

    sentence = "hello world 1234"
    cleaned = "helloworld"
    result = clean_txt(sentence)

    assert cleaned == result


def test_mixed():

    sentence = "Hello, World! 1234"
    cleaned = "helloworld"
    result = clean_txt(sentence)

    assert cleaned == result


def test_empty_str():

    sentence = ""
    cleaned = ""
    result = clean_txt(sentence)

    assert cleaned == result


def test_puntuaction_and_numbers():

    sentence = "!!!1234"
    cleaned = ""
    result = clean_txt(sentence)

    assert cleaned == result


def test_with_more_spaces():

    sentence = " A   AA  A   A"
    cleaned = "aaaaa"
    result = clean_txt(sentence)

    assert cleaned == result


def test_with_accented_letters():
    
    sentence = "città è"
    cleaned = "cittàè"
    result = clean_txt(sentence)

    assert cleaned == result


def test_uppercase_only():

    sentence = "HELLO"
    cleaned = "hello"
    result = clean_txt(sentence)

    assert cleaned == result


def test_camelcase_string():

    sentence = "HelloWorld"
    cleaned = "helloworld"
    result = clean_txt(sentence)

    assert cleaned == result


def test_with_whitespace_characters():

    sentence = "Hello\tworld\n"
    cleaned = "helloworld"
    result = clean_txt(sentence)

    assert cleaned == result


def test_long_string():

    sentence = "a1!" * 1000
    cleaned = "a" * 1000
    result = clean_txt(sentence)

    assert cleaned == result


def test_error_raises():

    with pytest.raises(TypeError):
        clean_txt(1234)

    with pytest.raises(TypeError):
        clean_txt(["not a string"])
