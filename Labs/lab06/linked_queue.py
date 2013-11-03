# Author: Abrar Hussain


class EmptyQueueError(Exception):

    '''Error raised if a Queue is empty.'''

    def __init__(self: 'EmptyQueueError'):
        Exception.__init__(self, "Queue is empty.")


class Node():

    """ Node to be used in a linked list."""

    def __init__(self: 'Node', value: object=None,
                 nxt: 'Node'=None) -> None:
        """ Create a new Node. """
        self.value, self.nxt = value, nxt

    def __repr__(self: 'Node') -> str:
        """ String representation of this Node. """

        return 'Node(' + str(self.value) + ', ' + str(self.nxt) + ')'


class Queue():

    """ Queue ADT. A first in, first out (FIFO) structure of items
    which uses a LinkedList for internal representation.

    operations:
            - enqueue(item): Add an item to the back of the queue
            - dequeue(): Remove and return the front item. Raise
            EmptyQueueError if queue is empty.
            - front(): Return the front item without removing it. Raise
            EmptyQueueError if the queue is empty.
            - is_empty(): Return True if the queue is empty.

    attributes:
            - self.first: Reference to the first Node in the linked list.
            - self.last: Reference to the last Node in the linked list.

    """

    def __init__(self: 'Queue') -> None:
        ''' Creates a new Queue. '''
        self.first = None

    def enqueue(self: 'Queue', item: object) -> None:
        ''' Add an item to the Queue. '''
        if self.is_empty():
            self.first = Node(item, Node())
            self.last = self.first
        else:
            self.last.nxt = Node(item)
            self.last = self.last.nxt

    def dequeue(self: 'Queue') -> str:
        ''' Remove and return the front item from the Queue. '''
        if self.is_empty():
            raise EmptyQueueError()

        first = self.first.value
        self.first = self.first.nxt

        # make the last value None after making the Queue empty
        if self.first is None and self.last is not None:
            self.last = None

        return first

    def front(self: 'Queue') -> str:
        ''' Return the first item of the Queue without removing it. '''
        if self.is_empty():
            raise EmptyQueueError()
        return self.first.value

    def is_empty(self: 'Queue') -> bool:
        ''' Return True if the Queue is empty, False  otherwise. '''
        if self.first is None:
            return True
        if self.first.value is None:
            return True
        return False
