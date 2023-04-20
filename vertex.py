class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def get_egdes(self):
        return list(self.edges.keys())
    
    def add_edges(self, vertex, weight):
        self.edges[vertex] = weight
    
    # def __str__(self):
    #     return str(self.value)