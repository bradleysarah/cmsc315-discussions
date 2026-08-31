#AUTHOR:      Bradley, Sarah
#UNIT 4:      CMSC315 Data Structures and Analysis
#PURPOSE:     binary search tree (BST)
#DATE:        31Aug2026
#LAST UPDATED:31Aug2026



"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # smaller values to the left and larger values to the right
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        #if an empty position is found create a new node
        if node is None:
            return Node(value)

        # smaller values inserted into the left subtree
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # larger values inserted to the right subtree
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # return the node after the new value has been inserted
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        #BST can reduce the search area at each step by choosing the left or right subtree instead of checking every value
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # no more nodes to search the value was not found
        if node is None:
            return False

        #current node matches the value the search is complete
        if value == node.value:
            return True

        # smaller values are searched for in the left subtree
        if value < node.value:
            return self._search_recursive(node.left, value)

        # larger values are searched for in the right subtree
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # create a list to store the values from the traversal
        values = []

        # start the in order traversal at the root
        self._inorder_recursive(self.root, values)

        # return the completed list
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # visit the left subtree first
            self._inorder_recursive(node.left, values)

            # add the current node value to the list
            values.append(node.value)

            #visit the right subtree last
            self._inorder_recursive(node.right, values)

            #smaller values are on the left and larger values are on the right, in order traversal produces sorted output


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # create a new BST
    tree = BST()

    # values create both left and right subtrees.
    values = [50, 30, 70, 20, 40, 60, 80]

    # insert each value into the tree
    # BST compares each value and reduces the search space by moving left for smaller and right for larger
    for value in values:
        tree.insert(value)

    # Display the values that were inserted.
    print("Values inserted:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # in order traversal visits the left subtree, current node, and then the right subtree. produces sorted values in a BST.
    traversal = tree.inorder()

    print("In-order traversal:", traversal)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # search for two values that exist in the tree
    print("Search for 30:", tree.search(30))
    print("Search for 70:", tree.search(70))

    # search for two values that do not exist in the tree
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # create an empty BST to test searching when no nodes exist
    empty_tree = BST()

    # searching an empty tree returns False because there are no values to search
    print("Search empty tree for 50:", empty_tree.search(50))



if __name__ == "__main__":
    main()