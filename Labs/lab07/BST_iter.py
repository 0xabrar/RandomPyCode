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

    def __str__(self: 'BST'):
        """
        Return a "sideways" representation of the values in this BST, with
        right subtrees above nodes above left subtrees and each value preceded
        by a number of TAB characters equal to its depth.
        """
        # Tricky to do iteratively so we cheat,
        # You could take up the challenge...
        return BST._str("", self.root)

    # Recursive helper for __str__.
    def _str(indent: str, root: '_BSTNode') -> str:
        """
        Return a "sideways" representation of the values in the BST rooted at
        root, with right subtrees above nodes above left subtrees and each
        value preceded by a number of TAB characters equal to its depth, plus
        indent.
        """
        if root:
            return (BST._str(indent + "\t", root.right) +
                    indent + str(root.item) + "\n" +
                    BST._str(indent + "\t", root.left))
        else:
            return ""

    def insert(self: 'BST', item: object) -> None:
        """
        Insert item into this BST.
        """
        # Find the point of insertion.
        parent, current = None, self.root
        while current:
            if item < current.item:
                parent, current = current, current.left
            else:  # item > current.item
                parent, current = current, current.right
        # Create a new node and link it in appropriately.
        new_node = _BSTNode(item)
        if parent:
            if item < parent.item:
                parent.left = new_node
            else:  # item > parent.item
                parent.right = new_node
        else:
            self.root = new_node

    def count_less(self: 'BST', item: object) -> int:
        """
        Return the number of items in this BST that are strictly less tham
        item.
        """
        stack = []
        count = 0

        if self.root is None:
            return 0

        stack.append(self.root)
        while len(stack) != 0:
            root = stack.pop()

            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

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
        self.item, self.left, self.right = item, left, right
