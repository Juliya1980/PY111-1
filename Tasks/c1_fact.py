def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError ('Факториал отрицательного числа не существует')
    elif n in (0, 1):
        return 1
    else:
        return factorial_recursive(n-1) * n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way
    :param n: int > 0
    :return: factorial of n
    """
    f_1 = 1
    if n < 0:
        raise ValueError ('Факториал отрицательного числа не существует')
    elif n in (0, 1):
        return 1
    elif n > 1:
        while n >= 2:
            f_1 = f_1 * n
            n -= 1
        return f_1

