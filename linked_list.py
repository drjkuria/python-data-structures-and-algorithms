class Node:
    """A single unit in a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Linked List representation."""
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        """Add new element to the end of the linked list."""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element