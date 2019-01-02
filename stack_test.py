from linked_list import Node
from stack import Stack

## Stack Test Cases
## Set up seme Elements
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Start setting up a Stack
stack = Stack(node1)

# Test stack functionality
stack.push(node2)
stack.push(node3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(node4)
print(stack.pop().value)
