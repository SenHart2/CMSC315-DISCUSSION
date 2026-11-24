"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    # A dictionary hashes each key to locate its associated value.
    inventory = {}
    inventory["SN1001"] = "Generator"
    inventory["SN1002"] = "Radio"
    inventory["SN1003"] = "Tool kit"
    inventory["SN1004"] = "Water pump"
    inventory["SN1005"] = "Air compressor"
    print("Equipment inventory:", inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # Hashing allows average O(1) lookup without scanning every entry.
    for serial in ("SN1002", "SN1004"):
        print(serial, "->", inventory[serial])
        assert serial in inventory

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before update:", inventory)
    # Assigning an existing key replaces its value without adding a duplicate.
    inventory["SN1002"] = "Radio - maintenance required"
    print("After update:", inventory)
    assert len(inventory) == 5

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before deletion:", inventory)
    # Removing a key also removes its associated value.
    del inventory["SN1003"]
    print("After deletion:", inventory)
    assert "SN1003" not in inventory

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # get() and pop() with defaults avoid KeyError for missing keys.
    print("Missing lookup:", inventory.get("SN9999", "Not found"))
    print("Missing deletion:", inventory.pop("SN9999", "Not found"))
    print("Empty inventory lookup:", {}.get("SN1001", "Not found"))
    # Additional test: repeated updates keep the number of keys unchanged.
    count = len(inventory)
    inventory["SN1001"] = "Generator - inspected"
    assert len(inventory) == count
    assert inventory["SN1001"] == "Generator - inspected"
    print("Repeated key update: no duplicate created.")

    print("\n=== SIMULATED HASH COLLISION ===")
    # These distinct keys map to the same bucket in a simple modulo model.
    # This illustrates collisions, not Python's actual dictionary layout.
    for serial in (1001, 1006):
        print(f"Serial {serial} maps to bucket {serial % 5}")
    # Collisions require extra work to distinguish keys. Python dictionaries
    # use probing; average lookup is O(1), but worst-case lookup is O(n).
    collision_example = {1001: "Generator", 1006: "Radio"}
    assert collision_example[1001] == "Generator"
    assert collision_example[1006] == "Radio"
    print("Both distinct keys remain retrievable:", collision_example)



if __name__ == "__main__":
    main()
