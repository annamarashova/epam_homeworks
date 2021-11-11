import os

import pytest
from task_3.find_maximum_and_minimum import find_maximum_and_minimum

path = os.path.dirname(__file__)  # возвращает путь к директории


def test_identical_number_seq():
    """Testing that that the code works for the sequence from the identical numbers"""
    assert find_maximum_and_minimum(path + "/identical_numbers") == (5, 5)


def test_arbitrary_number_seq():
    """Testing that that the code works for the sequence from the arbitrary numbers"""
    assert find_maximum_and_minimum(path + "/arbitrary_numbers") == (3, 854434)


def test_negative_number_seq():
    """Testing that that the code works for the sequence with the negative numbers"""
    assert find_maximum_and_minimum(path + "/negative_numbers") == (-7, 21)


def test_not_enough_numbers():
    """Testing that that the code works for the sequence with not enough numbers"""
    with pytest.raises(ValueError):
        find_maximum_and_minimum(path + "/not_enough_numbers")
