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

    while ind_r != ind_l + 1:
        ind_m = (ind_l + ind_r) // 2
        if elem > arr[ind_m]:
            ind_l = ind_m
        else:
            ind_r = ind_m

    if elem == arr[ind_l]:
        return ind_l
    elif elem == arr[ind_r]:
        return ind_r
    else:
        return None

if __name__ == '__main__':
    print(binary_search(23, [1, 2, 3, 4, 5, 9, 23]))
