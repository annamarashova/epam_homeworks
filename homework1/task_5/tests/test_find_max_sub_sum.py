import pytest

from task_5.find_maximal_subarray_sum import find_maximal_subarray_sum


def test_zero_list():
    """Testing that zero-sequense return 0"""
    assert find_maximal_subarray_sum([0, 0, 0, 0], 2) == 0


def test_negative_list():
    """Testing that list of negative numbers return minimal negative sum"""
    assert find_maximal_subarray_sum([-1, -15, -6, -1, -1, -1, -5, -4], 3) == -3


def test_common_list():
    """Testing of common list"""
    assert find_maximal_subarray_sum([5, 6, 7, 2, 3, 5, 4, 2], 5) == 23


def test_one_number_list():
    """Testing that one-number list return itself"""
    assert find_maximal_subarray_sum([-1], 1) == -1
