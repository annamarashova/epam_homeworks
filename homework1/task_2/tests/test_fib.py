import pytest

from task_2.fib_sequence import check_sequence


def test_zero_sequence():
    """Testing that sequence of zero is not fib_seq"""
    seq = [0, 0, 0, 0, 0, 0, 0]
    result = check_sequence(seq)
    assert not result  # not = is False


def test_arbitary_sequence():
    """Testing that arbitary sequence is not fib_seq"""
    assert not check_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_fib_sequence():
    """Testing that fib sequence is fib_seq"""
    assert check_sequence([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
