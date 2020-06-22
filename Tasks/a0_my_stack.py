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
    spis_1.append(elem)
    return spis_1


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.
    :return: popped element
    """
    global spis_1
    if len(spis_1) > 0:
        el_p = spis_1[-1]
        del spis_1[-1]
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
    if type(ind) == int:
        if len(spis_1) == 0:
            return None
        if ind >= len(spis_1):
            return None
        else:
            a = spis_1[::-1]
            return a[ind]
    else:
        raise ValueError('Введите целое положительное число')


def clear() -> None:
    """
    Clear my stack
    :return: None
    """
    global spis_1
    if len(spis_1) > 0:
        spis_1.clear()
    return None

if __name__ == '__main__':
    push(1)
    push(2)
    push(3)
    push(4)
    pop()
    print(peek(1))
    print(spis_1)
