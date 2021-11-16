import pytest
from task3.combinations import combinations


def test_combination_of_three_list():
    assert combinations([1, 2, 3], [4, 5], [6, 7, 8, 9]) == [
        [1, 4, 6],
        [1, 4, 7],
        [1, 4, 8],
        [1, 4, 9],
        [1, 5, 6],
        [1, 5, 7],
        [1, 5, 8],
        [1, 5, 9],
        [2, 4, 6],
        [2, 4, 7],
        [2, 4, 8],
        [2, 4, 9],
        [2, 5, 6],
        [2, 5, 7],
        [2, 5, 8],
        [2, 5, 9],
        [3, 4, 6],
        [3, 4, 7],
        [3, 4, 8],
        [3, 4, 9],
        [3, 5, 6],
        [3, 5, 7],
        [3, 5, 8],
        [3, 5, 9],
    ]


def test_combination_of_two_same_length_list():
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]


def test_combination_from_one_list():
    assert combinations([1, 2, 3, 4]) == [[1], [2], [3], [4]]
