"""Unit 2 discussion: stack and queue examples from IT operations."""
from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.items.append(value)  # Newest change goes on top (LIFO).

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None  # Avoid an error when no changes remain.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        return None if self.is_empty() else self.items[-1]  # Look without undoing.

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
        self.items.append(value)  # New tickets wait behind older tickets (FIFO).

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None  # No ticket is available to process.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        return None if self.is_empty() else self.items[0]  # Next ticket in line.

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print('=== UNIT 2: STACKS AND QUEUES ===')

    # TODO (Student): STACK DEMO
    # Requirements: add at least 4 values, show LIFO and empty pop/peek.
    # Edge Cases: verify a single-item stack becomes empty after removal.
    print('\n=== STACK DEMO: Undo network changes (LIFO) ===')
    changes = Stack()
    for change in ['Set IP address', 'Update subnet mask', 'Set gateway', 'Change DNS']:
        changes.push(change)
        print('Saved change:', change)
    print('Most recent change:', changes.peek())
    while not changes.is_empty():
        print('Undoing:', changes.pop())
    print('Pop on empty stack:', changes.pop())
    print('Peek on empty stack:', changes.peek())
    single_change = Stack()
    single_change.push('Restart switch')
    print('Removed only change:', single_change.pop())
    print('Single-item stack is now empty:', single_change.is_empty())

    # TODO (Student): QUEUE DEMO
    # Requirements: add at least 4 values, show FIFO and empty dequeue/front.
    # Edge Cases: verify a single-item queue becomes empty after removal.
    print('\n=== QUEUE DEMO: IT support tickets (FIFO) ===')
    tickets = Queue()
    for ticket in ['Printer offline', 'Password reset', 'Wi-Fi issue', 'Computer update']:
        tickets.enqueue(ticket)
        print('Ticket received:', ticket)
    print('Next ticket:', tickets.front())
    while not tickets.is_empty():
        print('Processing:', tickets.dequeue())
    print('Dequeue on empty queue:', tickets.dequeue())
    print('Front on empty queue:', tickets.front())
    single_ticket = Queue()
    single_ticket.enqueue('Replace cable')
    print('Processed only ticket:', single_ticket.dequeue())
    print('Single-item queue is now empty:', single_ticket.is_empty())


if __name__ == '__main__':
    main()
