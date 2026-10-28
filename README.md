# Unit 2 Discussion: Stacks and Queues

## Overview
I implemented two linear data structures in Python: a stack using a list and a queue using `collections.deque`. I kept the TODO prompts and added comments explaining each operation.

## Design and real-world scenario
I modeled a stack as a history of network configuration changes. I used `push()` to save each change and `pop()` to undo the most recent change first (last-in, first-out). I used `peek()` to view the latest change without removing it.

I modeled a queue as incoming IT support tickets. I used `enqueue()` to add tickets at the back and `dequeue()` to process the oldest ticket first (first-in, first-out). I used `front()` to view the next ticket without removing it. I chose `deque` because removing from the front is efficient.

## Testing and edge cases
I added four items to each structure and printed the removal order to demonstrate LIFO and FIFO. I tested removal and inspection on empty structures; these operations returned `None` rather than causing an error. I also tested a single-item stack and queue and checked that each was empty after removing its item.

## Memory and performance
Both structures used O(n) memory for n stored items, so memory grew as more items were added. The stack's append/pop and the queue's append/popleft operations took O(1) amortized or constant time, respectively.

## How to run
I ran the program using `python unit2_discussion.py` from this folder.
