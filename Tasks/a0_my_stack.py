"""
My little Stack
"""

from typing import Any

spis_1 = []

def push(elem: Any) -> None:
    """
    Operation that add element to stack
    :param elem: element to be pushed
    :return: Nothing
    """
    global spis_1
    spis_1 = [i for i in range(20)]
    for i in range(len(spis_1)):
        if i == len(spis_1) - 1:
            spis_1.append(elem)
            print(spis_1)
            return spis_1
        else:
            continue
            return None

def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.
    :return: popped element
    """
    global spis_1
    if len(spis_1) >= 1:
        el_p = (spis_1[len(spis_1)-1])
        del spis_1[len(spis_1)-1]
        print(spis_1)
        return el_p
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.
    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global spis_1
    if ind < len(spis_1):
        print(ind, spis_1[ind])
        return spis_1[ind]
    else:
        return None


def clear() -> None:
    """
    Clear my stack
    :return: None
    """
    global spis_1
    clear(spis_1)
    return None
