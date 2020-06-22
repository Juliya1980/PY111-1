"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

spis_1 = []

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue
    :param elem: element to be added
    :return: Nothing
    """
    global spis_1
    if type(priority) == int:
        if priority >= len(spis_1):
            while len(spis_1) <= priority:
                spis_1.append([])
            else:
                spis_1[priority].append(elem)
        else:
            spis_1[priority].append(elem)
    else:
        return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.
    :return: dequeued element
    """
    global spis_1
    if len(spis_1) > 0:
        for i in range(len(spis_1)):
            if len(spis_1[i]) > 0:
                a = spis_1[i][0]
                del spis_1[i][0]
                return a
                break
            else:
                continue
    else:
        return None

def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global spis_1
    if type(ind) == int and type(priority) == int:
        if priority > len(spis_1):
            raise ValueError('Введите целое положительное число')
        if ind > len(spis_1[priority]):
            raise ValueError('No elements there')
        else:
            return spis_1[priority][ind]
    else:
        raise ValueError('Введите целое положительное число')


def clear() -> None:
    """
    Clear my queue
    :return: None
    """
    global spis_1
    for i in range(len(spis_1)):
        spis_1[i].clear()
    return None

if __name__ == '__main__':
    enqueue(5, 3)
    enqueue(6, 5)
    enqueue(4, 3)
    enqueue(2, 0)
    print(spis_1)
    dequeue()
    print(spis_1)
    clear()
    print(spis_1)