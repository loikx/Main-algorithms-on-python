"""
This file provides stack data structure.
It's  implemented with python list.
"""


class Stack:
    """
    This class provides stack data structure.
    This data structure is LIFO.
    """
    def __init__(self, stack=[]):
        self.stack = stack

    def push(self, value) -> None:
        """
        This function add new element into stack.
        """
        self.stack.append(value)

    def pop(self):
        """
        This function delete element from stack.
        """
        return self.stack.pop()

    def __str__(self):
        return f"{self.stack[::-1]}"

    def __len__(self):
        return len(self.stack)
