# AUTHOR:      Bradley, Sarah
# UNIT 6:      CMSC315 Data Structures and Analysis
# PURPOSE:     Python Dictionaries as Hash Tables
# DATE:        14Sep2026
# LAST UPDATED:14Sep2026

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
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Create an empty dictionary to store inventory
    inventory = {}

    # Add SKUs as keys and quantities as values
    inventory["P100"] = 15
    inventory["P200"] = 8
    inventory["P300"] = 20
    inventory["P400"] = 12
    inventory["P500"] = 5

    # A dictionary works like a hash table by storing
    # information as key-value pairs for quick access

    # Display the inventory
    print("Inventory:", inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Look up the quantity for two existing SKUs
    print("P100 quantity:", inventory["P100"])
    print("P300 quantity:", inventory["P300"])

    # The SKU is used as the key to quickly find its stored quantity

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
    print("TODO: Demonstrate updating an existing key.")

    # Display the inventory before the update
    print("Before update:", inventory)

    # Update the quantity for P100
    inventory["P100"] = 25

    # Assigning a new value to an existing key replaces the old value
    print("After update:", inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Display the inventory before deleting an item
    print("Before deletion:", inventory)

    # Delete P200 from the inventory
    del inventory["P200"]

    # Removing a key also removes its stored value
    print("After deletion:", inventory)

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
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Look up a SKU that does not exist
    missing_item = inventory.get("P999")

    # get() safely returns None when the key is not found
    print("Lookup missing P999:", missing_item)

    # Edge case 2: Try to delete a SKU that does not exist
    removed_item = inventory.pop("P999", None)

    # Using pop with None prevents an error if the key does not exist
    print("Delete missing P999:", removed_item)
    print("Inventory after missing deletion:", inventory)



if __name__ == "__main__":
    main()