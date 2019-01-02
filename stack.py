"""Uses a linked list to implement a Stack.
insert_first, delete_first have been added
to the LinkedList while push and pop are
functionalities built into the Stack."""

from linked_list import LinkedList

class Stack:
    """Stack representation with push and pop."""
    def __init__(self, top=None):
        self.linked_list = LinkedList(top)
