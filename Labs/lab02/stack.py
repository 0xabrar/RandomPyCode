"""A simple implementation of the Stack ADT.

Author: Francois Pitt, January 2013,
        Danny Heap, September 2013
        Edited by: Abrar Hussain
"""


class StackEmptyError(Exception):

    """An exception raised when attempting to pop an empty stack."""
    pass


class Stack:

    """A collection of items stored in 'last-in, first-out' (LIFO) order.
    Items can have any type.

    Supports standard operations: push, pop, is_empty.
    """

    def __init__(self: 'Stack') -> None:
        """
        Initialize this stack.

        >>> isinstance(Stack(), Stack)
        True
        """

        self._items = []

    def push(self: 'Stack', item: object) -> None:

        """
        Add item to the top of this stack.

        item - object to add to the stack

        >>> s = Stack()
        >>> s.push(7)
        >>> s.push()
        7
        """

        self._items.append(item)

    def pop(self: 'Stack') -> object:
        """
        Remove and return the top item on this stack.

        >>> s = Stack()
        >>> s.push(7)
        >>> s.push()
        7
        """

        if self.is_empty():
            raise StackEmptyError()
        return self._items.pop()

    def is_empty(self: 'Stack') -> bool:

        """
        Return True iff this stack is empty.

        >>> Stack().is_empty
        True
        """

        return self._items == []