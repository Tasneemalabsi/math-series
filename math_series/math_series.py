def fibonacci(n):
    """
    this functions takes a value(n) and returns the fibonacci sequence of it which is the sum of the previous to numbers, for example fibonacci(4) is: 0,1,1,2

    """
    # the base case:
    if n <= 1:
	    return n
    else:
	    return (fibonacci(n-1) + fibonacci(n-2))