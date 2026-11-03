# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Completed Program

I created a network equipment inventory example using a Python list. I implemented `insert_at()` with `list.insert()`, `delete_at()` with index validation and `list.pop()`, and `search_value()` with a sequential linear search.

I tested inserting and deleting equipment at the beginning, middle, and end of the list. I searched for equipment that was present and equipment that was missing. I also tested an invalid deletion index, insertion into an empty list, and deletion from an empty list.

I observed that inserting or deleting near the beginning of a Python list required shifting other elements, while adding at the end generally required less work. Searching through the list checked items one by one. I used a communications equipment inventory because units need to track devices as they are added, issued, returned, or replaced.

## How I Ran the Program

I ran `python unit3_discussion.py` and checked the printed results for the insertion, deletion, search, and edge-case tests.
