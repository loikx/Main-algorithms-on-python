"""
This file provides queue data structure.
It's implemented with python list.
"""


class Queue:
    """
    This class provides queue data structure.
    This data structure is FIFO.
    """
    def __init__(self, queue=[]):
        self.queue = queue

    def push(self, item) -> None:
        """
        This function add new element into queue.

        : item: any python type
        """
        self.queue.append(item)

    def pop(self):
        """
        This function delete element from queue.
        """
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return self.queue.__str__()
