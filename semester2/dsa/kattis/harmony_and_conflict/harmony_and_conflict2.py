# bfs solution to harmony and conflict
# coded by jonas-mika senghaas and louis brandt
from itu.algs4.fundamentals.queue import Queue
from itu.algs4.fundamentals.bag import Bag
import sys

lines = sys.stdin.readlines()

# number of vertices and edges
V, E = [int(i) for i in lines[0].strip().split()]
edges = [[int(i) for i in line.strip().split()] for line in lines[1:]]


class Edge:
    def __init__(self, u, v, t):
        self._u = u
        self._v = v
        self._t = t

    def start(self):
        return self._u

    def end(self):
        return self._v

    def type(self):
        return self._t

    def __repr__(self):
        return f"Edge: {self._u}-{self._v} ({self._t})"


class Graph:
    def __init__(self, V, E):
        self._V = V
        self._E = E
        self._adj = []

        for _ in range(V):
            self._adj.append(Bag())

    def from_edge_list(self, edges):
        for edge in edges:
            u, v, t = edge
            self._adj[u].add(Edge(u, v, t))
            self._adj[v].add(Edge(u, v, t))

    def V(self):
        return self._V

    def E(self):
        return self._E

    def adj(self, u):
        return self._adj[u]

    def can_be_colored(self, src):
        coloring = [-1] * self._V

        for src in range(self._V):
            if coloring[src] == -1:
                coloring[src] = 1

                # Create a queue (FIFO) of vertex numbers and
                # enqueue source vertex for BFS traversal
                q = Queue()
                q.enqueue(src)

                # Run while there are vertices in queue
                # (Similar to BFS)
                while q.is_empty() == False:
                    u = q.dequeue()
                    for edge in self.adj(u):
                        start = u
                        for possibility in [edge.start(), edge.end()]:
                            if possibility != u:
                                end = possibility

                        # adjacent not visited yet
                        if coloring[end] == -1:
                            if edge.type() == 0:  # harmony
                                coloring[end] = coloring[start]

                            elif edge.type() == 1:  # conflict
                                if coloring[start] == 0:
                                    coloring[end] = 1
                                elif coloring[start] == 1:
                                    coloring[end] = 0
                            q.enqueue(end)
                            continue
                        if edge.type() == 0:  # harmony
                            # print(coloring[edge.start()], coloring[edge.end()])
                            if coloring[start] != coloring[end]:
                                return 0
                        elif edge.type() == 1:  # conflict
                            # print(coloring[edge.start()], coloring[edge.end()])
                            if coloring[start] == coloring[end]:
                                return 0
        return 1


G = Graph(V, E)
G.from_edge_list(edges)
print(G.can_be_colored(0))
