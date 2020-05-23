"""
My little Stack
"""

from typing import Any
#test tamp help git.
spis_1 = [1, 2, 3, 4, 5]

def push(elem: Any) -> None:
    """
    Operation that add element to stack
    :param elem: element to be pushed
    :return: Nothing
    """
    global spis_1
    spis_1.append(elem)
    print(spis_1)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.
    :return: popped element
    """
    global spis_1
    if len(spis_1) >= 1:
        el_0 = (spis_1[0])
        del spis_1[0]
        return el_0
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
    print(spis_1)
    return None

if __name__ == '__main__':
    push(6)
    pop()
    peek(2)