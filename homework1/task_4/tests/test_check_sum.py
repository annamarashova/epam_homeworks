import pytest

from task_4.check_sum_of_four import check_sum_of_four


def test_only_zero_list():
    """Testing that zero-list return 81"""
    assert check_sum_of_four([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) == 81


def test_empty_list():
    """Testing that empty-list return 0"""
    assert check_sum_of_four([], [], [], []) == 0


def test_arbitrary_list():
    """Testing that arbitrary list return 0. For ex, list with negative numbers"""
    assert (
        check_sum_of_four([-1, -2, -3], [-1, -2, -3], [-4, -5, -6], [-12, -12, -12])
        == 0
    )
