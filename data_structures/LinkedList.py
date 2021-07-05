"""
This python file provides Linked List data structure.
This structure is realized with LinkedList class.
More details in the class itself.
"""


class LinkedList:
    """
    This class implements linked list data structure.
    :: methods
    1) __init__ - standard python method of initialization
    2) __str__ - standard high level python method of output representation
    3) __repr__ - standard low level python method of output representation
    4) __len__ - implements interface for the len function
    5) __getitem__ - allow the user to index elements such as arrays
    6) __setitem__ - allow the user to assign elements via index
    7) __contains__ - implements interface for in/not in keywords
    8) reverse - allow the user to reverse list
    9) add_to_end - allow the user to add element to the end
    10) remove_element_by_index - allow user to delete element by its index
    11) remove_element_by_value - allow user to delete element by its value
    12) remove_last - allow user to delete the last element
    13) remove_first - allow user to delete the first element
    14) add_to_index - allow user to add item by index
    """
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        lst = []
        instance = self

        while instance is not None:
            lst.append(instance.val)
            instance = instance.next

        return f"LinkedList: {lst}"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        instance = self
        counter = 0

        while instance is not None:
            counter += 1
            instance = instance.next

        return counter

    def __getitem__(self, item):
        if item < 0:
            item = len(self) - item

        instance = self
        counter = 0

        while instance is not None:
            if counter == item:
                return instance.val

            counter += 1
            instance = instance.next

        raise IndexError('Index does not exists')

    def __setitem__(self, key, value):
        if value is None:
            raise ValueError("Invalid value")
        if key < 0:
            key = len(self) - key

        instance = self
        counter = 0

        while instance is not None:
            if counter == key:
                instance.val = value
                return

            counter += 1
            instance = instance.next

        raise IndexError('Index does not exists')

    def __contains__(self, item):

        instance = self
        while instance is not None:
            if item == instance.val:
                return True

            instance = instance.next

        return False

    def reverse(self):
        if self is None:
            raise ValueError("Object does not exists")

        previous = None
        current = self
        nxt = current.next

        while current is not None:
            current.next = previous
            previous = current
            current = nxt

            if nxt:
                nxt = nxt.next

        return previous

    def add_to_end(self, value) -> None:
        instance = self

        while instance.next is not None:
            instance = instance.next

        instance.next = LinkedList(value)

    def remove_element_by_index(self, index: int) -> None:
        if self is None:
            raise IndexError("Index does not exists")

        instance = self
        counter = 1

        while instance.next is not None:
            if counter == index:
                instance.next = instance.next.next
                return
            counter += 1
            instance = instance.next

        raise IndexError("Index does not exists")

    def remove_element_by_value(self, value) -> None:
        if self is None:
            raise IndexError("Index does not exists")

        instance = self

        while instance.next is not None:
            if instance.next.val == value:
                instance.next = instance.next.next
                return
            instance = instance.next

        raise IndexError("Index does not exists")

    def remove_last(self):
        if self is None:
            return

        instance = self

        if len(instance) == 1:
            return instance.next

        while instance.next.next is not None:
            instance = instance.next
        instance.next = None

    def remove_first(self):
        if self is None:
            return

        instance = self
        instance = instance.next

        return instance

    def add_to_index(self, index, value):
        if self is None:
            raise IndexError("Index does not exists")

        instance = self
        counter = 0

        while instance is not None:
            if counter == index:
                tmp = instance.next
                instance.next = LinkedList(value, tmp)
                return

            instance = instance.next
            counter += 1

        raise IndexError("Index does not exists")

    def reverseBetween(self, head, m, n):

        if (m == n):
            return head

        # revs and revend is start and end respectively
        # of the portion of the linked list which
        # need to be reversed. revs_prev is previous
        # of starting position and revend_next is next
        # of end of list to be reversed.
        revs = None
        revs_prev = None
        revend = None
        revend_next = None

        # Find values of above pointers.
        i = 1
        curr = head

        while (curr and i <= n):
            if (i < m):
                revs_prev = curr

            if (i == m):
                revs = curr

            if (i == n):
                revend = curr
                revend_next = curr.next

            curr = curr.next
            i += 1

        revend.next = None

        # Reverse linked list starting with
        # revs.
        revend = LinkedList.reverse(revs)

        # If starting position was not head
        if (revs_prev):
            revs_prev.next = revend

        # If starting position was head
        else:
            head = revend

        revs.next = revend_next
        return head


def create_linked_list(lst):
    if len(lst) == 0:
        raise ValueError("Can't create LinkedList without any values")
    if len(lst) > 1:
        return LinkedList(val=lst[0], nxt=create_linked_list(lst[1:]))
    return LinkedList(val=lst[0])