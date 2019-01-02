"""Uses a linked list to implement a Stack.
insert_first, delete_first have been added
to the LinkedList while push and pop are
functionalities built into the Stack."""

from linked_list import LinkedList

class Stack:
    """Stack representation with push and pop."""
    def __init__(self, top=None):
        self.linked_list = LinkedList(top)
    
    def push(self, new_element):
        """Add a new element at the top of the stack."""
        self.linked_list.insert_first(new_element)
    
    def pop(self):
        """Remove the first element off the top of the stack and return it."""
        return self.linked_list.delete_first()

