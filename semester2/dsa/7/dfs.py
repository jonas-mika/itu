# implementation of depth first search in python

from graph import UndirectedGraph

class DFS:
    def __init__(self, G, s: int):
        self._G = G
        self._marked = [False] * G.V()
        self._id = [None] * G.V()
        self._count = 0
        self._cc = 1
        self._s = s

        self.dfs(G, s)
        for i in range(self._G.V()):
            if self._marked[i] == False:
                self._cc += 1
                self.dfs(G,i)
        

    def dfs(self, G, s):
        self._marked[s] = True
        self._id[s] = self._cc
        self._count += 1

        for a in G.adj(s):
            if self._marked[a] == False: 
                self.dfs(G, a)

    def has_path_to(self, v: int):
        return self._id[self._s] == self._id[v]

    def marked(self, v: int):
        return self._marked[v]

    def count(self):
        return self._count

    def connected(self):
        return self._cc == 1

class BFS:
    def __init__(self, G, s):
        self._G = G
        self._s = s


G1 = UndirectedGraph(6)
G1.add_edge(0,1)
G1.add_edge(0,2)
G1.add_edge(0,5)
G1.add_edge(1,2)
G1.add_edge(2,3)
G1.add_edge(2,4)
G1.add_edge(3,4)
G1.add_edge(3,5)
print(G1)
dfs = DFS(G1, 0)
print(dfs.connected())
print(dfs._cc)
print(dfs._id)
print(dfs.has_path_to(0))
