class Node:
    """Basic element of a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Binary tree representation."""
    def __init__(self, root):
        self.root = Node(root)
    
    def search(self, find_val):
        """Return true if find_val is in the tree,
        otherwise return false."""
        return self.preorder_search(tree.root, find_val)
    
    def print_tree(self):
        """Print all tree nodes in pre-order traversal."""
        return preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or \
                    self.preorder_search(start.right, find_val)
        return False
    
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    