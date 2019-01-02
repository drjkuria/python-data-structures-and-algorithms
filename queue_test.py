from queue import Queue

# Setup
queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)

# Test peek()
print(queue.peek()) # 1

# Test dequeue
print(queue.dequeue())
