#AUTHOR:      Bradley, Sarah
#UNIT 1:      CMSC315 Data Structures and Analysis
#PURPOSE:     fundamental linear data structures
#DATE:        21Aug2026
#LAST UPDATED:21Aug2026

"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        #new values added top, last item added is removed first
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "stack is empty"
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        #peek returns the top item without removing it from the stack
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        #new values go to back, first item added is removed first
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "queue is empty"
        return self.items.popleft()

    def front(self):
    # TODO (Student): Return the front value without removing it.
    # Add a comment explaining what front returns.
    # front returns first item without removing it from the queue
         if self.is_empty():
            return "queue is empty"
         return self.items[0]

    def is_empty(self):
    # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

stack = Stack()

stack.push("5k")
stack.push("10k")
stack.push("21k")
stack.push("42k")

# LIFO removes the most recently added distance first
print("Top item:", stack.peek())
print("Removed first:", stack.pop())
print("Removed second:", stack.pop())

#test pop and peek on empty stack
empty_stack = Stack()
print("Pop from empty stack:", empty_stack.pop())
print("Peek at empty stack:", empty_stack.peek())

# test a stack containing only 1 item
single_stack = Stack()
single_stack.push("5K")
single_stack.pop()
print("Single-item stack empty:", single_stack.is_empty())


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

queue = Queue()

queue.enqueue("5K")
queue.enqueue("10K")
queue.enqueue("21K")
queue.enqueue("42K")

# FIFO removes the first distance added to the queue first
print("Front item:", queue.front())
print("Removed first:", queue.dequeue())
print("Removed second:", queue.dequeue())

# test dequeue and front on an empty queue
empty_queue = Queue()
print("Dequeue from empty queue:", empty_queue.dequeue())
print("Front of empty queue:", empty_queue.front())

# test a queue containing only one item
single_queue = Queue()
single_queue.enqueue("5K")
single_queue.dequeue()
print("Single-item queue empty:", single_queue.is_empty())

if __name__ == "__main__":
    main()
