"""A Queue class that uses Python list."""

class Queue:
    """Queue class from a list."""
    def __init__(self, head=None):
        self.storage = [head]
    
    def enqueue(self, new_element):
        """Add new element to the tail."""
        self.storage.append(new_element)
    
    