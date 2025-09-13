"""
Calculator module providing basic arithmetic operations.
Includes functions for addition, subtraction, multiplication, and division.
"""


def sumar(a, b):
    """
    Add two numbers.

    Args:
        a (float or int): First number.
        b (float or int): Second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def restar(a, b):
    """
    Subtract the second number from the first number.

    Args:
        a (float or int): First number.
        b (float or int): Second number.

    Returns:
        float: The result of subtracting b from a.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiply two numbers.

    Args:
        a (float or int): First number.
        b (float or int): Second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


def dividir(a, b):
    """
    Divide the first number by the second number.

    Args:
        a (float or int): Numerator.
        b (float or int): Denominator.

    Raises:
        ZeroDivisionError: If the denominator (b) is zero.

    Returns:
        float: The result of dividing a by b.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
