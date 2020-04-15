import sys
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    unique_node = []
    My_Graph = Graph()

    # Get Unique Values from ancestors
    for i in range(0, len(ancestors)):
        for x in range(0, len(ancestors[i])):
            if ancestors[i][x] not in unique_node:
                unique_node.append(ancestors[i][x])

    # Create Graph
    for i in range(0, len(unique_node)):
        My_Graph.add_vertex(unique_node[i])

    # Connect vertices together
    for i in range(0, len(ancestors)):
        My_Graph.add_edge(ancestors[i][1], ancestors[i][0])

    print(My_Graph.vertices)
    # Id of individual - Node/vertices
    # Earliest known ancestor - longest chain depth
    # If more than 1 earliest, put both nodes in array and find least value node
    # Result - length of array. Do I keep 2 sets of array?


earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 2)
