# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
## Implementation Summary

I created an equipment inventory using a Python dictionary with five fictional serial numbers as keys and equipment descriptions as values. I retrieved two existing records, updated a radio record without creating a duplicate, and removed a tool kit record. I displayed the inventory before and after changes.

## Edge Cases and Results

I tested missing lookups, missing deletions, an empty dictionary, and repeated updates to an existing key. I used default values with get() and pop() to avoid errors. I added assertions to verify that updates did not create duplicate keys and that deleted records were removed.

## Hashing and Real-World Application

I used a simple modulo example to illustrate how two different serial numbers could map to the same bucket. I distinguished this simulation from Python's actual dictionary implementation, which resolves collisions through probing. I explained that dictionary lookups typically took constant time on average, while heavy collisions could lead to linear worst-case lookup time. I connected these operations to Army equipment inventories, where retrieving records by serial number could reduce the time spent searching through lists.

## Verification

I ran the completed program and verified that all assertions passed. The output demonstrated insertion, lookup, update, deletion, edge cases, and the simulated collision.
