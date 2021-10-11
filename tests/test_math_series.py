from math_series import __version__
from math_series.math_series import fibonacci


def test_version():
    assert __version__ == '0.1.0'

def test_one():
    """
    this function tests the fibonacci sequence function when n=1
    """
    #Arrange
    n=1
    expected = 1
    #Act
    actual = fibonacci(1)
    #Assert
    assert actual == expected

def test_two():
    """
    this function tests the fibonacci sequence function when n=2
    """
    #Arrange
    n=2
    expected = 1
    #Act
    actual = fibonacci(2)
    #Assert
    assert actual == expected


def test_three():
    """
    this function tests the fibonacci sequence function when n=3
    """
    #Arrange
    n=3
    expected = 2
    #Act
    actual = fibonacci(3)
    #Assert
    assert actual == expected    