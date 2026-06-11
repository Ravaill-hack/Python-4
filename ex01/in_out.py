def square(x: int | float) -> int | float:
    """Returns the square of the input
    """
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of the input by himself
    """
    return (x ** x)


def outer(x: int | float, function) -> object:
    """Returns a function that applies a function to an input
    """
    count = 0

    def inner() -> float:
        """Applies a function to a number and returns the result
        """
        nonlocal x
        nonlocal count
        result = function(x)
        x = result
        count += 1
        return result
    return inner
