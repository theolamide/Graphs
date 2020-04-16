import sys
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    unique_node = []
    My_Graph = Graph()
    paths = []
    max_lengths = []

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

    # Check if Node is an end Node and return -1. There's no need to traverse graph in that case.
    if len(My_Graph.vertices[starting_node]) == 0:
        return -1
    else:  # Traverse the graph to get path
        for key in My_Graph.vertices:
            if len(My_Graph.vertices[key]) == 0:
                paths.append(My_Graph.dfs_recursive_length(starting_node, key))

        for i in range(0, len(paths)):  # Organize returned paths and eliminate Nones
            if paths[i] == None:
                pass
            else:
                max_lengths.append((paths[i][-1], len(paths[i])))

        # Compare lengths of the paths and get ancestor based on the given parameters in the README
        for i in range(0, len(max_lengths)):
            Base_Compare = max_lengths[0][1]
            Node_value = max_lengths[0][0]
            if len(max_lengths) == 1:
                print("Earliest known ancestor of",
                      starting_node, "is:", Node_value)
                return max_lengths[0][0]
            elif Base_Compare > max_lengths[i][1]:
                pass
            elif Base_Compare < max_lengths[i][1] and Node_value:
                Base_Compare = max_lengths[i][1]
                Node_value = max_lengths[i][0]
            elif Base_Compare == max_lengths[i][1] and Node_value > max_lengths[i][0]:
                Base_Compare = max_lengths[i][1]
                Node_value = max_lengths[i][0]
                print("Base_Compare 47:", Base_Compare)
        # print("Line 50:", Base_Compare, Node_value)

        print("Earliest known ancestor of",
              starting_node, "is:", Node_value)
        return Node_value

    # print("max_lengths", max_lengths)
    # print(My_Graph.vertices)
    # Id of individual - Node/vertices
    # Earliest known ancestor - longest chain depth
    # If more than 1 earliest, put both nodes in array and find least value node
    # Result - length of array. Do I keep 2 sets of array?


earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9)
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 7)
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6)
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 8)
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 2)
