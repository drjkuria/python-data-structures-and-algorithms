class Node:
    """A single unit in a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Linked List representation."""
    def __init__(self, head=None):
        self.head = head