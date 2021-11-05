import pytest
from calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_zero_case():
    """Testing that zero give False"""
    assert not check_power_of_2(0)


def test_negative_power_two():
    """Testing that negative power of 2 give False"""
    assert not check_power_of_2(-8)


def test_negative_power():
    """Testing that negative power of any other numbers give False"""
    assert not check_power_of_2(-3)
