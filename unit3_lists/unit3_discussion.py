"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Inserting near the front shifts existing items to the right.
    # Inserting at the end usually takes less work than inserting at the front.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check the index first so an invalid position does not crash the program.
    # Negative indexes are treated as invalid for this inventory example.
    if index < 0 or index >= len(lst):
        return None
    # pop removes the equipment and returns its name.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search: check each item in order until it matches.
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Example equipment that might be tracked in a communications section.
    equipment = ["Router", "Switch", "Laptop"]
    print("Original equipment:", equipment)
    insert_at(equipment, 0, "Radio")  # Beginning: shifts the other items.
    print("After beginning insertion:", equipment)
    insert_at(equipment, 2, "KVM")  # Middle: shifts later items.
    print("After middle insertion:", equipment)
    insert_at(equipment, len(equipment), "Server")  # End: append position.
    print("After end insertion:", equipment)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Show what was removed and the remaining inventory each time.
    print("Removed from beginning:", delete_at(equipment, 0))
    print("Updated equipment:", equipment)
    print("Removed from middle:", delete_at(equipment, 1))
    print("Updated equipment:", equipment)
    print("Removed from end:", delete_at(equipment, len(equipment) - 1))
    print("Updated equipment:", equipment)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Search for one device we have and another that is not listed.
    for device in ["Router", "Firewall"]:
        position = search_value(equipment, device)
        if position == -1:
            print(f"{device} was not found in the inventory.")
        else:
            print(f"{device} was found at index {position}.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Edge case 1: Invalid indexes return None instead of causing an error.
    print("Invalid index deletion:", delete_at(equipment, 99))
    # Edge case 2: Inserting into an empty list is allowed.
    empty_inventory = []
    insert_at(empty_inventory, 0, "Access Point")
    print("After inserting into an empty list:", empty_inventory)
    # Edge case 3: Deleting from an empty list safely returns None.
    print("Delete from empty list:", delete_at([], 0))



if __name__ == "__main__":
    main()