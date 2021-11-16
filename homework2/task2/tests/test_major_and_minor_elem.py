import pytest
from task2.major_and_minor_elem import major_and_minor_elem


def test_common_sequence():
    assert major_and_minor_elem(
        [-1, -1, -1, 97, 2, 2, -3, -3, -3, -3, -3, -3, -1, -1, -1, -1]
    ) == (-1, 97)


def test_sequence_with_negative_numbers():
    assert major_and_minor_elem([-1, -1, -1, 1, 2, 2, -3, -3, -3, -3, -3, -3]) == (
        -3,
        1,
    )
