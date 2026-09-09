# AUTHOR:      Bradley, Sarah
# UNIT 5:      CMSC315 Data Structures and Analysis
# PURPOSE:     linear search and binary search
# DATE:        09Sep2026
# LAST UPDATED:09Sep2026


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

    # go through the list one item at a time starting at the beginning
    for i in range(len(lst)):

        # check if the current item matches the target
        if lst[i] == target:

            # return the index where the target was found
            return i

    # linear search has O(n) time complexity because in the worst case it may have to check every item in the list
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

    # set the beginning and end positions of the search
    low = 0
    high = len(lst) - 1

    # keep searching while there are still values left to check
    while low <= high:

        # find the middle index of the current search area
        mid = (low + high) // 2

        # if the middle value matches the target, return its index
        if lst[mid] == target:
            return mid

        # if the target is larger, search the right half
        elif lst[mid] < target:
            low = mid + 1

        # if the target is smaller, search the left half
        else:
            high = mid - 1

        # each loop removes half of the remaining values from the search

    # return -1 if the target was not found
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
    print("Race distances completed by a runner:")

    # small sorted list of race distances in miles
    race_distances = [1, 3, 5, 10, 13, 26]

    # search for 10 miles, which exists in the list
    print("Linear search for 10 miles:",
          linear_search(race_distances, 10))
    print("Binary search for 10 miles:",
          binary_search(race_distances, 10))

    # search for 15 miles, which does not exist in the list
    print("Linear search for 15 miles:",
          linear_search(race_distances, 15))
    print("Binary search for 15 miles:",
          binary_search(race_distances, 15))

    # both searches find 10 miles at the same index.
    # both return -1 when 15 miles is not found.

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
    print("Searching a larger list of race results:")

    # create a sorted list of 1,000 race result numbers
    race_results = list(range(1, 1001))

    # search for a result near the end of the list
    print("Linear search for result 999:",
          linear_search(race_results, 999))
    print("Binary search for result 999:",
          binary_search(race_results, 999))

    # both searches return the same index.
    # binary search is more efficient with large sorted lists because it removes half of the remaining values after each comparison.

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

    # edge case 1: Search an empty list of race results
    empty_results = []
    print("Binary search empty race list:",
          binary_search(empty_results, 10))

    # empty list has no values to search, so the result is -1.

    # edge case 2: Search for the last distance in the list
    distance_list = [1, 3, 5, 10, 13, 26]

    print("Linear search for last distance:",
          linear_search(distance_list, 26))
    print("Binary search for last distance:",
          binary_search(distance_list, 26))

    # both searches find 26 miles at index 5, which is the last position in the list.


if __name__ == "__main__":
    main()