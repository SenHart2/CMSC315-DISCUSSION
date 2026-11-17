"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

from time import perf_counter


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # In the worst case, every item is checked, so time complexity is O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        # Discard half of the remaining sorted values each iteration: O(log n).
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small = [10, 20, 30, 40, 50]
    # Both searches return index 3 for 40 and -1 for the missing value 35.
    for target in [40, 35]:
        print(f"Target {target}: Linear = {linear_search(small, target)}, "
              f"Binary = {binary_search(small, target)}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large = list(range(100000))
    target = 99999
    # Linear search checks every item for this target. Binary search halves
    # the remaining range, requiring far fewer comparisons as the list grows.
    for search in [linear_search, binary_search]:
        start = perf_counter()
        index = search(large, target)
        elapsed = perf_counter() - start
        print(f"{search.__name__}: Index = {index}, Time = {elapsed:.9f} seconds")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # An empty list returns -1; a matching single item returns index 0.
    # First and last positions test the boundaries of the search range.
    cases = [("Empty list", [], 10), ("Single item", [10], 10),
             ("First position", small, 10), ("Last position", small, 50),
             ("Missing value", small, 99)]
    for label, data, target in cases:
        print(f"{label}: Linear = {linear_search(data, target)}, "
              f"Binary = {binary_search(data, target)}")

    print("\n=== REAL-WORLD EQUIPMENT SEARCH ===")
    # Fictional equipment serial numbers in inventory order.
    serials = [1054, 1021, 1098, 1003, 1036]
    target = 1098
    print(f"Unsorted inventory: {serials}")
    print(f"Linear search for {target}: Index = {linear_search(serials, target)}")
    # Sorting makes binary search possible but changes the item indexes.
    sorted_serials = sorted(serials)
    print(f"Sorted inventory: {sorted_serials}")
    print(f"Binary search for {target}: Index = {binary_search(sorted_serials, target)}")


if __name__ == "__main__":
    main()
