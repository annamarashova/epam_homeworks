import string

import pytest
from task5.range_func import custom_range


def test_stop_equals_start():
    assert custom_range(string.ascii_lowercase, "a") == []


def test_stop_equals_start_explicitely():
    assert custom_range(string.ascii_lowercase, "a", "a") == []


def test_start_less_than_stop():
    assert custom_range(string.ascii_lowercase, "z", "a") == []


def test_reversed():
    assert custom_range(string.ascii_lowercase, "z", "a", -1) == [
        "z",
        "y",
        "x",
        "w",
        "v",
        "u",
        "t",
        "s",
        "r",
        "q",
        "p",
        "o",
        "n",
        "m",
        "l",
        "k",
        "j",
        "i",
        "h",
        "g",
        "f",
        "e",
        "d",
        "c",
        "b",
    ]


def test_only_stop():
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_start_and_stop():
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_reversed_step_2():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
