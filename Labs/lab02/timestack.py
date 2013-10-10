"""Run some timing experiments on class Stack operations.

Authors: Francois Pitt, January 2013,
         Danny Heap, September 2013
"""

from stack import Stack
import time


def push_pop(s: Stack, howmany: int) -> None:

    """Push and pop 'howmany' items to/from Stack 's'.
    """

    for i in range(howmany):
        s.push(42)
        s.pop()


def time_stack(m: int, n: int) -> int:

    """Return how long it takes to push and pop 'm' items to/from a Stack
    with 'n' items already in it.
    """

    s = Stack()
    for i in range(n):
        s.push(1)

    start = time.time()
    push_pop(s, m)
    end = time.time()

    return end - start

if __name__ == '__main__':
    for n in [i * 10000 for i in range(1, 11)]:
        print('Running time on', n, 'items:', time_stack(20000, n))