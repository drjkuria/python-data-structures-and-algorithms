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

    