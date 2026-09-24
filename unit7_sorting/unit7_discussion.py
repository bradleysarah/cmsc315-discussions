# AUTHOR:      Bradley, Sarah
# UNIT 7:      CMSC315 Data Structures and Analysis
# PURPOSE:     Sorting Algorithms
# DATE:        23Sep2026
# LAST UPDATED:23Sep2026

"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""

import time


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # Make a copy so the original list does not change
    sorted_list = lst.copy()

    # Go through the list to compare neighboring values
    for i in range(len(sorted_list) - 1):

        # Track whether any values were swapped
        swapped = False

        for j in range(len(sorted_list) - 1 - i):

            # Swap the values if the left value is larger
            if sorted_list[j] > sorted_list[j + 1]:

                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp

                swapped = True

        # Stop early if the list is already sorted
        if not swapped:
            break

    # Return the sorted copy
    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # A list with zero or one value is already sorted
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list
    mid = len(lst) // 2

    # Divide the list into two halves
    left = lst[:mid]
    right = lst[mid:]

    # Sort each half using recursion
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    # Create a new list to hold the sorted values
    result = []

    # Start at the first value in each list
    i = 0
    j = 0

    # Compare values from both lists
    while i < len(left) and j < len(right):

        # Add the smaller value to the result
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any values remaining in the left list
    result.extend(left[i:])

    # Add any values remaining in the right list
    result.extend(right[j:])

    # Return the completed sorted list
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    # Product prices from an online store
    prices = [42, 19, 88, 7, 31, 65, 24, 53]

    print("Original prices:", prices)
    print("Bubble Sort:", bubble_sort(prices))
    print("Merge Sort:", merge_sort(prices))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    # Student grades in a gradebook
    grades = [91, 73, 85, 62, 100, 78, 94, 81]

    print("Original grades:", grades)

    bubble_result = bubble_sort(grades)
    merge_result = merge_sort(grades)

    print("Bubble Sort:", bubble_result)
    print("Merge Sort:", merge_result)

    # Check whether both algorithms return the same results
    print("Both sorting results match:", bubble_result == merge_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: An empty list should stay empty
    empty_list = []

    print("\nEmpty List:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Explanation: Both algorithms return an empty list without errors.")

    # Edge case 2: An already sorted list should stay in the same order
    sorted_list = [5, 10, 15, 20, 25]

    print("\nAlready Sorted List:")
    print("Original:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))
    print("Explanation: The values are already sorted, so the order does not change.")

    # Edge case 3: A reverse-sorted list needs to be reordered
    reverse_list = [50, 40, 30, 20, 10]

    print("\nReverse-Sorted List:")
    print("Original:", reverse_list)
    print("Bubble Sort:", bubble_sort(reverse_list))
    print("Merge Sort:", merge_sort(reverse_list))
    print("Explanation: Both algorithms reorder the values from lowest to highest.")

    # Edge case 4: Duplicate values should remain in the sorted list
    duplicate_list = [12, 5, 12, 8, 5, 20]

    print("\nList With Duplicate Values:")
    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))
    print("Explanation: Both algorithms sort the list while keeping duplicate values.")

    # ===============================
    # PERFORMANCE COMPARISON
    # ===============================

    print("\n=== PERFORMANCE COMPARISON ===")

    # Create a larger dataset to compare sorting times
    large_list = list(range(1000, 0, -1))

    # Measure how long Bubble Sort takes
    start = time.perf_counter()
    bubble_sort(large_list)
    bubble_time = time.perf_counter() - start

    # Measure how long Merge Sort takes
    start = time.perf_counter()
    merge_sort(large_list)
    merge_time = time.perf_counter() - start

    print("Dataset size:", len(large_list))
    print(f"Bubble Sort time: {bubble_time:.6f} seconds")
    print(f"Merge Sort time: {merge_time:.6f} seconds")

    print("\nBubble Sort has O(n^2) worst-case time complexity.")
    print("Merge Sort has O(n log n) time complexity.")
    print("Merge Sort generally performs better with larger datasets.")
    print("Bubble Sort is simpler but can be slower with large datasets.")


if __name__ == "__main__":
    main()