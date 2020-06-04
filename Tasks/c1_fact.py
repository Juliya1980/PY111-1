def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    f_1 = 1
    if n >= 0:
        if n == 0:
            return f_1
        if n != 0:
            for i in range(1, n+1):
                f_1 = f_1 * i
            return  f_1
    else:
        return 0


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    print(n)
    return 0
