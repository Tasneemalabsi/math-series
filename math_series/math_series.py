def fibonacci(n):
    """
    this functions takes a value(n) and returns the lucas sequence of it which is the sum of the previous to numbers, mathematically,fibonacci(n)=fibonacci(n-1)+fibonacci(n-2)

    """
    # the base case:
    if n <= 1:
	    return n
    else:
	    return (fibonacci(n-1) + fibonacci(n-2))
def lucas(n):
    """
    this functions takes a value(n) and returns the lucas sequence of it which is the sum of the previous to numbers, mathematically,lucas(n)=lucas(n-1)+lucas(n-2)but it starts with 2 and 1 instead of 0 and 1

    """
    # the base cases:
    if (n == 0):
        return 2
    if (n == 1):
        return 1
    else:
	    return (lucas(n-1) + lucas(n-2))                