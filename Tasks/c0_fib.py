def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm
    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError ('Факториал отрицательного числа не существует')
    elif n in (1, 2):
        return 1
    elif n > 2:
        return fib_recursive(n-1) + fib_recursive(n-2)
    else:
        return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm
    :param n: number of item
    :return: Fibonacci number
    """
    a = b = 1
    if n < 0:
        raise ValueError ('Факториал отрицательного числа не существует')
    elif n in (1, 2):
        return 1
    elif n > 2:
        for i in range(n-2):
            c = a + b
            a = b
            b = c
        return b
    else:
        return 0
