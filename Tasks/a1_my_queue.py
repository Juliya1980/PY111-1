"""
My little Queue
"""
from typing import Any

spis_1 = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue
    :param elem: element to be added
    :return: Nothing
    """
    global spis_1
    if elem != None:
        spis_1.append(elem)
        return spis_1
    else:
        raise ValueError('Введите элемент')
        return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.
    :return: dequeued element
    """
    global spis_1
    if len(spis_1) > 0:
        el_p = spis_1[0]
        del spis_1[0]
        return el_p
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global spis_1
    if type(ind) == int:
        if ind < 0:
            raise ValueError('Введите целое положительное число')
        elif ind > len(spis_1):
            return None
        else:
            if len(spis_1) == 0:
                raise ValueError('No elements there')
            else:
                a = spis_1[ind]
                print(a)
                return a
    else:
        return None


def clear() -> None:
    """
    Clear my queue
    :return: None
    """
    global spis_1
    spis_1.clear()
    return None
