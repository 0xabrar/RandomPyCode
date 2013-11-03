"""Incomplete Binary Search Tree implementation.
Author: Francois Pitt, March 2013,
        Danny Heap, October 2013.
"""


class BST:

    """A Binary Search Tree."""

    def __init__(self: 'BST', container: list=[]) -> None:
        """
        Initialize this BST by inserting the items from container (default [])
        one by one, in the order given.
        """
        # Initialize empty tree.
        self.root = None
        # Insert every item from container.
        for item in container:
            self.insert(item)

    def __str__(self: 'BST') -> str:
        """
        Return a "sideways" representation of the values in this BST, with
        right subtrees above nodes above left subtrees and each value preceded
        by a number of TAB characters equal to its depth.
        """
        return self.root._str("") if self.root else ""

    def insert(self: 'BST', item: object) -> None:
        """
        Insert item into this BST.
        """
        if self.root:
            self.root.insert(item)
        else:
            self.root = _BSTNode(item)

    def count_less(self: 'BST', item: object) -> int:
        """
        Return the number of items in this BST that are strictly less tham
        item.
        """
        if self.root is None:
            return 0
        return self.root.counter(item)


class _BSTNode:

    """A node in a BST."""

    def __init__(self: '_BSTNode', item: object,
                 left: '_BSTNode'=None, right: '_BSTNode'=None) -> None:
        """
        Initialize this node to store item and have children left and right.
        """
        self.item, self.left, self.right = item, left, right

    def _str(self: '_BSTNode', indent: str) -> str:
        """
        Return a "sideways" representation of the values in the BST rooted at
        this node, with right subtrees above nodes above left subtrees and each
        value preceded by a number of TAB characters equal to its depth, plus
        indent.
        """
        return ((self.right._str(indent + '\t') if self.right else '') +
                indent + str(self.item) + '\n' +
                (self.left._str(indent + '\t') if self.left else ''))

    def insert(self: '_BSTNode', item: object) -> None:
        """
        Insert item into the BST rooted at this node.
        """
        if item < self.item:
            if self.left:
                self.left.insert(item)
            else:
                self.left = _BSTNode(item)
        elif item > self.item:
            if self.right:
                self.right.insert(item)
            else:
                self.right = _BSTNode(item)
        # else:  # item == self.item
        # pass  # nothing to do: item is already in the tree

    def counter(self: '_BSTNode', item: object):
        ''' Count the number of items less than the given item
        that are children or the root of this _BSTNode.
        '''
        count = 0
        if self.item is None:
            return 0

        if self.left is not None:
            count += self.left.counter(item)
        if self.right is not None:
            count += self.right.counter(item)

        if self.item < item:
            count += 1
        return count
