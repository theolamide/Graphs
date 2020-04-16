"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vrtes not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def dfs_recursive_length(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []

        visited.add(starting_vertex)
        new_path = list(path)
        new_path.append(starting_vertex)
        # print("new_path", new_path)
        # Do the thing!
        if starting_vertex == destination_vertex:
            return new_path

        for neighbour in self.vertices[starting_vertex]:
            if neighbour not in visited:
                neighbour_path = self.dfs_recursive_length(
                    neighbour, destination_vertex, visited, new_path)
                if neighbour_path:
                    # print(neighbour_path)
                    return neighbour_path
