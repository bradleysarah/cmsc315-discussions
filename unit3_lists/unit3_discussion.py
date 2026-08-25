#AUTHOR:      Bradley, Sarah
#UNIT 3:      CMSC315 Data Structures and Analysis
#PURPOSE:     fundamental lists
#DATE:        21Aug2026
#LAST UPDATED:21Aug2026


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
    # insert places the new value at the chosen index
    lst.insert(index, value)

    # items after the insertion point shift right



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
    # check the index first so the program does not crash
    if index < 0 or index >= len(lst):
        return None

    # pop removes and returns the value at the given index
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
    # linear search checks each item one at a time from the beginning
    for i in range(len(lst)):
        if lst[i] == value:
            return i

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
    print("TODO: Create a list and demonstrate insertions.")

    race_list = ["5K", "10K", "42K"]
    print("Original list:", race_list)

    # insert at beginning
    insert_at(race_list, 0, "1 Mile")
    print("After beginning insertion:", race_list)

    # insert in middle
    insert_at(race_list, 2, "21K")
    print("After middle insertion:", race_list)

    # insert at end
    insert_at(race_list, len(race_list), "50K")
    print("After end insertion:", race_list)

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
    print("TODO: Demonstrate deletions from multiple positions.")

    # remove the first item
    removed = delete_at(race_list, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", race_list)

    # remove from the middle
    removed = delete_at(race_list, 2)
    print("Removed from middle:", removed)
    print("Updated list:", race_list)

    # remove the last item
    removed = delete_at(race_list, len(race_list) - 1)
    print("Removed from end:", removed)
    print("Updated list:", race_list)

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
    print("TODO: Demonstrate searching for values.")

    # search for a value that exists
    result = search_value(race_list, "21K")
    print("Index of 21K:", result)

    # search for a value that does not exist
    result = search_value(race_list, "100K")
    print("Index of 100K:", result)

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
    print("TODO: Demonstrate at least two edge cases.")

    #edge case 1: invalid index returns None instead of crashing
    print("Delete invalid index:", delete_at(race_list, 20))

    # edge case 2: insert into an empty list
    empty_list = []
    insert_at(empty_list, 0, "5K")
    print("Insert into empty list:", empty_list)



if __name__ == "__main__":
    main()