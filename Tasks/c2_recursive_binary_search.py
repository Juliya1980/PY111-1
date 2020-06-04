from typing import Sequence, Optional

def rec_search(elem, arr):
    l = 0
    r = len(arr) - 1
    x = 0
    if elem > arr[(l + r) // 2]:
        l = (l + r) // 2
    elif elem < arr[(l + r) // 2]:
        r = (l + r) // 2
    else:
        x = (l + r) // 2
        return x
    return l, r

def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if elem in arr:
        rec_search(elem, arr)
    else:
        return None
