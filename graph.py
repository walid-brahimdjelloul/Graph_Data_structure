class Graph:
    def __init__(self, directed = False):
        self.directed =  directed
        self.graph_dic = {}
    
    def add_vertex(self, vertex):
        self.graph_dic[vertex.value] = vertex
    
    def add_edges(self, from_vertex, to_vertex, weight=0):
        self.graph_dic[from_vertex.value].add_edges(to_vertex.value, weight)
        if not self.directed:
            self.graph_dic[to_vertex.value].add_edges(from_vertex.value, weight)
    
    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print('Visiting :' + current_vertex)
            if current_vertex == end_vertex:
                return True
            
            vertex = self.graph_dic[current_vertex]
            next_vertex = vertex.get_egdes()

            next_vertex = [vertex for vertex in next_vertex if vertex not in seen]
            start.extend(next_vertex)
        return False