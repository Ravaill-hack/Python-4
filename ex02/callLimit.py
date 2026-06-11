def callLimit(limit: int):
    """A function that allows to define how many times at maximum
    a given function can be called
    """
    count = 0

    def callLimiter(function):
        """A function that returns the wrapped function that limits
        the number of times a function can be called
        """

        def limit_function(*args: any, **kwds: any):
            """The inner function that counts how many times a function
            can be called and returns either the function's result
            or print an error message
            """
            nonlocal count
            count += 1
            if (count <= limit):
                return (function(*args, **kwds))
            else:
                print(f"Error: {function} call too many times")

        return (limit_function)
    return (callLimiter)
