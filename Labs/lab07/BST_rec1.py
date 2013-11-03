"""Incomplete Binary Search Tree implementation.
Author: Francois Pitt, March 2013,
        Danny Heap, October 2013
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
        return BST._str("", self.root)

    def _str(indent: str, root: '_BSTNode') -> str:
        """
        Return a "sideways" representation of the values in the BST rooted at
        root, with right subtrees above nodes above left subtrees and each
        value preceded by a number of TAB characters equal to its depth, plus
        indent.
        """
        return ((BST._str(indent + '\t', root.right) +
                 indent + str(root.item) + '\n' +
                 BST._str(indent + '\t', root.left))
                if root else "")

    def insert(self: 'BST', item: object) -> None:
        """
        Insert item into this BST.
        """
        self.root = BST._insert(self.root, item)

    def _insert(root: '_BSTNode', item: object) -> '_BSTNode':
        """
        Insert item into the BST rooted at this node, and return the root of
        the resulting tree.
        """
        if root:
            if item < root.item:
                root.left = BST._insert(root.left, item)
            elif item > root.item:
                root.right = BST._insert(root.right, item)
        else:
            root = _BSTNode(item)
        return root

    def count_less(self: 'BST', item: object) -> int:
        """
        Return the number of items in this BST that are strictly less than
        item.
        """
        return self.count_less_helper(item, self.root)

    def count_less_helper(self: 'BST', item: object, root: '_BSTNode'):
        ''' Recursively return the number of items in BST that are 
        strictly less than item.
        '''

        count = 0
        if root is None:
            return 0
        if root.left is not None:
            count += self.count_less_helper(item, root.left)
        if root.right is not None:
            count += self.count_less_helper(item, root.right)

        if root.item < item:
            count += 1
        return count


class _BSTNode:

    """A node in a BST."""

    def __init__(self: '_BSTNode', item: object,
                 left: '_BSTNode'=None, right: '_BSTNode'=None) -> None:
        """
        Initialize this node to store item and have children left and right.
        """
        self.item = item
        self.left = left
        self.right = right
