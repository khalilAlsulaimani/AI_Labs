import sys


class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def __init__(self):
        self.num_of_vertices = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            self.num_of_vertices += 1
            return True
        else:
            return False

    def add_edge(self, u, v, weight):

        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            # print(u , v , " cost is " ,weight)
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

    def stateLineDistance(self, row):
        count = 0
        for t in range(len(self.edges)):
            if isinstance(row, int):
                count += self.edges[row][t]

        return count

    def minDistance(self, dist, sptSet):
        global min_index
        min = sys.maxsize
        for v in range(self.num_of_vertices):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.num_of_vertices
        dist[src] = 0
        sptSet = [False] * self.num_of_vertices
        count = 0

        for cout in range(self.num_of_vertices):
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.num_of_vertices):
                if self.edges[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.edges[u][v]:
                    dist[v] = dist[u] + self.edges[u][v]

        return dist

    def A_Star(self, start, goal):
        open_list = []
        closed_list = []
        dijkster = self.dijkstra(start)

        open_list.append(start)
        while len(open_list) > 0:
            current_vertex = open_list.pop(0)
            if current_vertex == goal:
                closed_list.append(current_vertex)
                return closed_list
            else:
                if current_vertex not in closed_list:
                    closed_list.append(current_vertex)

                temp = {}
                for i in range(len(self.edges)):
                    for j in range(len(self.edges)):
                        edge = self.edges[i][j]

                        if edge != 0 and edge not in closed_list:
                            fN = dijkster[j] + self.stateLineDistance(j)
                            temp[i] = fN
                            open_list.append(j)
                smallest = min(temp, key=temp.get)

                open_list.append(temp[smallest])


g = Graph()

a = Vertex(0)
g.add_vertex(a)

for i in range(1, 21):
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

path = g.A_Star(1, 10)
print("goal found and its path is : ", path)
