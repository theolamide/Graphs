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

    def dft_length(self, starting_vertex):
        """
        Print each vertex visited until it gets to the end and there's no neighbor anymore
        """
        # Create a stack
        st = Stack()
        st.push([starting_vertex])
        # Create a set for travesed vertices.
        visited = set()
        while st.size() > 0:
            path = st.pop()
            # Check visits
            if path[-1] not in visited:
                print(path[-1])
                # Add to visited
                visited.add(path[-1])
                # Stack all neighbours
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    st.push(new_path)
                    # if self.get_neighbors(path[-1]) is None:
                    #     print("Last Element", self.vertices[path[-1]])

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of travesed vertices
        visited = set()
        # While queue is not empty
        while qq.size() > 0:
            # dequeue/pop  the first vertex
            path = qq.dequeue()
            # If not visited
            if path[-1] not in visited:
                # Do the thing!
                print(path[-1])
                # Mark as visited
                visited.add(path[-1])
                # Enqueue all neighbours
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        st = Stack()
        st.push([starting_vertex])
        # Create a set for travesed vertices.
        visited = set()
        while st.size() > 0:
            path = st.pop()
            # Check visits
            if path[-1] not in visited:
                print(path[-1])
                # Add to visited
                visited.add(path[-1])
                # Stack all neighbours
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    st.push(new_path)

    def dft_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Initial case
        if visited is None:
            visited = set()
        # Track visited Nodes
        visited.add(starting_vertex)
        print(starting_vertex)
        # call the function recursively.
        for neighbour in self.vertices[starting_vertex]:
            if neighbour not in visited:
                self.dft_recursive(neighbour, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of travesed vertices
        visited = set()
        # While queue is not empty
        while qq.size() > 0:
            # dequeue/pop  the first vertex
            path = qq.dequeue()
            # If not visited
            if path[-1] not in visited:
                # Do the thing!
                # print("Queue -1", path[-1])
                if path[-1] == destination_vertex:
                    return path
                # Mark as visited
                visited.add(path[-1])
                # Enqueue all neighbours
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        st = Stack()
        st.push([starting_vertex])
        # Create a set for travesed vertices.
        visited = set()
        while st.size() > 0:
            path = st.pop()
            # Check visits
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                # Add to visited
                visited.add(path[-1])
                # Stack all neighbours
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    st.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
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
        new_path = path + [starting_vertex]

        # Do the thing!
        if starting_vertex == destination_vertex:
            return new_path

        for neighbour in self.vertices[starting_vertex]:
            if neighbour not in visited:
                neighbour_path = self.dfs_recursive(
                    neighbour, destination_vertex, visited, new_path)
                if neighbour_path:
                    return neighbour_path

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


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
