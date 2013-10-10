''' Author: Abrar Hussain '''


class EmptyQueueError(Exception):

    '''Error raised if a Queue is empty.'''

    def __init__(self: 'EmptyQueueError'):
        Exception.__init__(self, "Queue is empty.")


class Queue():

    '''A small class which resembles a Queue data structure of ints.

    operations:
            - enqueue(item): Add an item to the back of the queue.
            - dequeue(): Remove and return the front item. Raise EmptyQueueError
                    queue is empty.
            - front(): Return the front item without removing it. Raise
                    EmptyQueueError if the queue is empty.
            - is_empty(): Return True iff the queue is empty.

    attributes:
        -self.info: maintains the Queue information in a data structure
    '''

    def __init__(self: 'Queue') -> None:
        '''Creates a new Queue'''
        self.info = []

    def enqueue(self: 'Queue', item: int) -> None:
        ''' Add an iem to the Queue'''
        self.info.append(item)

    def dequeue(self: 'Queue') -> str:
        '''Remove and return the front of the Queue'''
        if self.is_empty():
            raise EmptyQueueError()
        return self.info.pop(0)

    def front(self: 'Queue') -> None:
        '''Return the first item of Queue without removing it.'''
        if self.is_empty():
            raise EmptyQueueError()
        return self.info[0]

    def is_empty(self: 'Queue') -> bool:
        '''Return True if the Queue is empty, False otherwise.'''
        return self.info == []
