def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n > 0:
        if n in (1, 2):
            return 1
        else:
            return fib_recursive(n-1) + fib_recursive(n-2)
    else:
        return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    print(n)
    return 0
