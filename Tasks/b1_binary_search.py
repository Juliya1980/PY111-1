from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    ind_l = 0
    ind_r = len(arr)
    ind_m = round((ind_l + ind_r) / 2)
    n = 0
    while n < 100:
        while elem != arr[ind_m]:
            if elem > arr[ind_m]:
                ind_l = (ind_l + ind_r) / 2
                n += 1
                ind_m = round((ind_l + ind_r) / 2)
            else:
                ind_r = (ind_l + ind_r) / 2
                n += 1
                ind_m = round((ind_l + ind_r) / 2)
        else:
            return ind_m
    return None

