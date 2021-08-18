"""
This file provides you TreeNode data structure.
This structure is realized with TreeNode class that has __init__, __str__, max_depth, min_depth and sum methods.
More details in the class itself.
"""


class TreeNode:
    """
    This class implements binary tree data structure.
    :: methods
    1) __init__ - standard python method of initialization
    2) __str__ - standard high level python method of output representation
    3) min_depth - returns min depth of binary tree
    4) max_depth - returns max depth of binary tree
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # create list where we will save the information
        lst = []

        # create function that will fill lst
        def _print(tree):
            # if tree is not exists
            if not tree:
                return
            # add value to lst
            lst.append(tree.val)
            # and go to the left branch
            _print(tree.left)
            # go to the right branch
            _print(tree.right)
        # call this function
        _print(self)
        # return the result
        return f"TreeNode: {lst}"

    def min_depth(self) -> int:
        """
        This method provides an algorithm that find min depth of binary tree

        :return int min depth value
        """
        # if tree is not exists that it can't have depth
        if self is None:
            return 0

        # count the left branch min depth
        min_left = 1 + TreeNode.min_depth(self.left)
        # count the right branch min depth
        min_right = 1 + TreeNode.min_depth(self.right)
        # if left branch is not exists
        if min_right == 1:
            # that we need to return the right branch
            return min_left
        # if right branch is not exists
        if min_left == 1:
            # that we need to return the right branch
            return min_right
        # in other way we need to return min from two values
        return min(min_left, min_right)

    def max_depth(self) -> int:
        """
        This method provides an algorithm that find the max depth of binary tree

        :return int max depth value
        """
        # if tree is not exists that it can't have depth
        if self is None:
            return 0
        # count the left branch max depth
        max_left = 1 + TreeNode.max_depth(self.left)
        # count the right branch max depth
        max_right = 1 + TreeNode.max_depth(self.right)
        # in other way we need to return max from two values
        return max(max_left, max_right)

