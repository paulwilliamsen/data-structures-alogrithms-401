"""
NEW GRAPH AND VERTEX CLASS

"""

class Vertex:
    def __init__(self, data):
        self.data = data

class Graph:
    """
    Class to create graph instances
    """
    def __init__(self):
        self.new_table = {}

    def add_vertex(self, data):
        new_vertex = Vertex(data)
        self.new_table[data] = {}

    def add_edge(self, vertices_one, vertices_two, weight=0):
        if vertices_one in self.new_table and vertices_two in self.new_table:
            self.new_table[vertices_one][vertices_two] = weight
            self.new_table[vertices_two][vertices_one] = weight

    def get_vertices(self):
        output = []
        for key in self.new_table:
            output.append(key)
        if output == []:
            return None
        return output

    def get_neighbors(self, vertex):
        if vertex in self.new_table:
            return self.new_table[vertex]

    def size(self):
        return len(self.new_table)
