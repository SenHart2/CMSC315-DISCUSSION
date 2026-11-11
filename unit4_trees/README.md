[README_unit4_completed.md](https://github.com/user-attachments/files/34666465/README_unit4_completed.md)
# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Completed Implementation

I created a binary search tree to organize military equipment IDs. I used a `Node` class to store each ID and its left and right child references. I implemented recursive insertion so smaller IDs were placed on the left and larger IDs on the right. Duplicate IDs were ignored.

I inserted seven equipment IDs: 500, 300, 700, 200, 400, 600, and 800. I performed an in-order traversal, which returned the IDs in ascending order. I also tested searches for existing IDs (200 and 700) and missing IDs (250 and 900).

I tested edge cases by searching and traversing an empty tree, inserting a duplicate ID, and traversing a single-node tree. All of these cases were handled without errors.

## Running the Program

I ran the program with `python unit4_discussion.py`. The output showed the inserted IDs, sorted traversal, search results, and edge-case results.

## Performance Reflection

I learned that a BST can narrow the search to one subtree at each comparison. Searching and inserting typically took O(log n) time when the tree was balanced, but could take O(n) time when the tree became skewed, such as when values were inserted in sorted order.
