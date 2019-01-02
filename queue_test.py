from queue import Queue

# Setup
queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)

# Test peek()
print(queue.peek()) # 1

# Test dequeue
print(queue.dequeue())

# Test enqueue
queue.enqueue(4)
print(queue.dequeue()) # 2
print(queue.dequeue()) # 3
print(queue.dequeue()) # 4
queue.enqueue(5)
print(queue.dequeue()) # 5
print(queue.peek) # prints bound method of Queue.peek, no value.
