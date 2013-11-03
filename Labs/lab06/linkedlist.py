# Author: Abrar Hussain


class IndexError(Exception):

    '''Error raised if a Queue is empty.'''

    def __init__(self: 'IndexError'):
        Exception.__init__(self, "Index is out of bounds.")


class _Node():

    """ Node to be used in a linked list. """

    def __init__(self: '_Node', value: object=None,
                 ref: '_Node'=None) -> None:
        """ Create a new node."""
        self.value, self.ref = value, ref


class LinkedList():

    """ A linked list class.

    attributes:
        - self.first: Reference to the first _Node in the list.
        - self.size: Integer number of elements in the linked list.
    """

    def __init__(self: 'LinkedList') -> None:
        """ Create a new LinkedList. """
        self.first = _Node()
        self.size = 0

    def __len__(self: 'LinkedList') -> int:
        """ Retuns the number of elements in the LinkedList. """
        return self.size

    def __contains__(self: 'LinkedList', elem: 'object') -> bool:
        """ Return True iff this LinkedList contains elem. """
        current = self.first
        while current.ref is not None:
            if current.value == elem:
                return True
            current = current.ref
        return False

    def __getitem__(self: 'LinkedList', ind: 'int') -> object:
        """ Return the element stored at index ind in this linked list.
        Raises IndexError if ind < 0 or ind > size of the linked list.
        """
        if ind < 0 or ind >= self.size:
            raise IndexError()

        current = self.first
        current_ind = 0
        while current_ind != ind:
            current = current.ref
            current_ind += 1
        return current.value

    def insert(self: 'LinkedList', elem: object) -> None:
        """Insert elem at index 0 of this linked list.
        Does not overwrite any element previosly at element 0,
        though the index of that element (and all following) increases
        by one.
        """
        self.first = _Node(elem, self.first)
        self.size += 1
