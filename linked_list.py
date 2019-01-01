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
    
    def get_element(self, new_element):
        """Get an element from a given position."""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None




        