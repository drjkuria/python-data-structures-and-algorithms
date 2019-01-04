from binary_tree import BinaryTree, Node

# Set up BinaryTree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
print(tree.search(4)) # True
print(tree.search(6)) # False

# Test print_tree
print(tree.print_tree()) # 1-2-4-5-3
