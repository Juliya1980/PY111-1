"""
This module implements some functions based on linear search algo
"""
from typing import Sequence, Any
import numpy as np

def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array
    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_el = arr[0]
    ind_el = 0
    for i, elem in enumerate(arr):
        if elem < min_el:
            ind_el = i
            min_el = elem
    return ind_el
