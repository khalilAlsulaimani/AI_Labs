class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight):

        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            #print(u , v , " cost is " ,weight)
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for i in range(len(self.edges)):
            print(i, " ", end="")
        print("")
        for v in range(len(self.edges)):
            print(v, "", end=" ")
            for j in range(len(self.edges)):
                print(" ", self.edges[v][j], end="")
            print("")

    def oneRowDicretion(self, row):
        count = 0
        for i in range(len(self.edges)):
            count += self.edges[row][i]

        return count


g = Graph()

a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(1, 20):
    g.add_vertex(Vertex(i))

edges = [
    # edge one , edge two , cost between them
    [20, 1, 3],
    [20, 16, 2],
    [1, 17, 0.5],
    [1, 9, 3],
    [1, 2, 2],
    [16, 17, 0.3],
    [10, 8, 1],
    [17, 8, 0.5],
    [2, 18, 0.5],
    [2, 3, 1.5],
    [3, 9, 2],
    [3, 10, 2],
    [3, 4, 0.3],
    [4, 11, 1],
    [4, 5, 0.5],
    [5, 11, 2],
    [5, 12, 0.5],
    [5, 6, 0.2],
    [6, 7, 0.3],
    [6, 13, 0.4],
    [7, 13, 0.2],
    [7, 14, 0.3],
    [14, 13, 0.1],
    [14, 12, 0.1],
    [12, 15, 0.5]
]

for edge in edges:
    g.add_edge(edge[0], edge[1], edge[2])

print(g.oneRowDicretion(2))
g.print_graph()
