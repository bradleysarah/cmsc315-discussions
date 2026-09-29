# AUTHOR:      Bradley, Sarah
# UNIT 8:      CMSC315 Data Structures and Analysis
# PURPOSE:     Breadth-First Search (BFS)
# DATE:        29Sep2026
# LAST UPDATED:29Sep2026

"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Return an empty list if the starting node does not exist
    if start not in graph:
        return []

    # Keep track of the order nodes are visited
    visited_order = []

    # Keep track of nodes that have already been seen
    visited = set()

    # A queue is used because BFS visits nodes in first-in, first-out order
    queue = deque([start])

    # Mark the starting node as visited
    visited.add(start)

    # Continue until there are no more nodes waiting in the queue
    while queue:
        current = queue.popleft()

        # Add the current node to the traversal result
        visited_order.append(current)

        # Check each connected neighbor
        for neighbor in graph[current]:

            # Only visit neighbors that have not already been seen
            if neighbor not in visited:

                # Mark the neighbor as visited before adding it to the queue
                visited.add(neighbor)

                # Neighbors are added to the queue so BFS visits them level by level
                queue.append(neighbor)

    # BFS explores nearby nodes first, while DFS usually follows one path deeper first
    return visited_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # This graph represents locations on a campus
    # Each key is a building and each value lists the connected buildings
    campus_graph = {
        "Library": ["Science Hall", "Student Center"],
        "Science Hall": ["Library", "Gym"],
        "Student Center": ["Library", "Cafeteria"],
        "Gym": ["Science Hall", "Dorm"],
        "Cafeteria": ["Student Center", "Dorm"],
        "Dorm": ["Gym", "Cafeteria"]
    }

    # Display each building and its connections
    for building, neighbors in campus_graph.items():
        print(building, "->", neighbors)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    # Start the traversal at the Library
    start_node = "Library"

    # BFS visits all nearby buildings before moving farther away
    first_traversal = bfs(campus_graph, start_node)

    print("Starting node:", start_node)
    print("BFS traversal:", first_traversal)

    # Add a new building and connect it to the Cafeteria
    campus_graph["Bookstore"] = ["Cafeteria"]
    campus_graph["Cafeteria"].append("Bookstore")

    # Run BFS again after updating the graph
    updated_traversal = bfs(campus_graph, start_node)

    print("\nAdded Bookstore connected to Cafeteria.")
    print("Updated BFS traversal:", updated_traversal)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Start from a different node
    print("\nDifferent Starting Node:")
    print("Starting from Gym:", bfs(campus_graph, "Gym"))
    print("Explanation: BFS begins at Gym and visits connected buildings level by level.")

    # Edge case 2: Missing starting node
    print("\nMissing Starting Node:")
    print("Starting from Unknown:", bfs(campus_graph, "Unknown"))
    print("Explanation: The function safely returns an empty list because the node does not exist.")

    # Edge case 3: Graph with one node
    single_node_graph = {
        "Parking Garage": []
    }

    print("\nSingle Node Graph:")
    print("Traversal:", bfs(single_node_graph, "Parking Garage"))
    print("Explanation: BFS visits the only node and then stops.")

    # Edge case 4: Empty graph
    empty_graph = {}

    print("\nEmpty Graph:")
    print("Traversal:", bfs(empty_graph, "Library"))
    print("Explanation: The graph is empty, so BFS returns an empty list.")


if __name__ == "__main__":
    main()