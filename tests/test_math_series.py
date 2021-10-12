from math_series import __version__
from math_series.math_series import fibonacci, lucas


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_one():
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

def test_fibonacci_two():
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


def test_fibonacci_three():
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

def test_fibonacci_four():
    """
    this function tests the fibonacci sequence function when n=0
    """
    #Arrange
    n=0
    expected = 0
    #Act
    actual = fibonacci(0)
    #Assert
    assert actual == expected 

def test_lucas_one():
    """
    this function tests the lucas sequence function when n=0
    """
    #Arrange
    n=0
    expected = 2
    #Act
    actual = lucas(0)
    #Assert
    assert actual == expected 

def test_lucas_two():
    """
    this function tests the lucas sequence function when n=1
    """
    #Arrange
    n=1
    expected = 1
    #Act
    actual = lucas(1)
    #Assert
    assert actual == expected   

def test_lucas_three():
    """
    this function tests the lucas sequence function when n=2
    """
    #Arrange
    n= 2
    expected = 3
    #Act
    actual = lucas(2)
    #Assert
    assert actual == expected 

def test_lucas_four():
    """
    this function tests the lucas sequence function when n=3
    """
    #Arrange
    n= 3
    expected = 4
    #Act
    actual = lucas(3)
    #Assert
    assert actual == expected 
