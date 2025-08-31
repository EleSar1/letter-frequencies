import pytest 

from src.processing import count_letters


def test_count_letters_success():

    assert count_letters("hello, world") == {"h": 1, "e": 1, "l": 3, "o": 2, "d": 1, ",": 1, "w": 1, "r": 1, " ": 1}


def test_no_space():

    assert count_letters("hello,world") == {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1, ",": 1}


def test_no_puntuaction():

    assert count_letters("helloworld") == {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}


def test_uppercase():

    assert count_letters("HELLOWORLD") == {"H": 1, "E": 1, "L": 3, "O": 2, "W": 1, "R": 1, "D": 1}