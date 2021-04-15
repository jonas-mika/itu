# implementation of bfs in python

from graph import UndirectedGraph

class BFS:
    def __init__(self, G, s: int):
        self._G = G
        self._s = s
        self._marked = [False] * G.V()
        self._id = [None] * G.V()
        self._edgeto = [None] * G.V()
        self.queue = []

        self.bfs(G, s)

    def bfs(self, G, s):
        self._marked[s] = True
        self.queue.append(s)
        while len(self.queue)!=0:
            v = self.queue.pop(0)
            for a in G.adj(v):
                if self._marked[a] == False:
                    self._edgeto[a] = v
                    self._marked[a] = True
                    self.queue.append(a)

    def has_path_to(self, v: int):
        return self._marked[v] 

    def path_to(self, v: int):
        if self.has_path_to(v) == False: return None
        path = []
        x = v
        while x != self._s:
            path.append(x)
            x = self._edgeto[x]
        path.append(self._s)
        for i in reversed(path):
            print(f"{i}->", end='')

    def marked(self, v: int):
        return self._marked[v]

G1 = UndirectedGraph(5)
G1.add_edge(0,1)
G1.add_edge(1,2)
G1.add_edge(2,3)
print(G1)
bfs = BFS(G1, 0)
print(bfs.has_path_to(3))
print(bfs.path_to(4))
print(bfs.path_to(3))
