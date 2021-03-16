# building graph data types in python using adjacency list data structure
class Node:
    def __init__(self):
        self.item = None 
        self.next = None 

class Bag():
    def __init__(self):
        self.first = Node()
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def __len__(self):
        return self.size()

    def add(self, item):
        oldfirst = self.first
        self.first = Node()
        self.first.item = item
        self.first.next = oldfirst

        self.n += 1 

    def __iter__(self):
        current = self.first
        while current.item is not None:
            assert current.item is not None
            yield current.item
            current = current.next

    def __repr__(self) -> str:
        if self.size() == 0:
            return '{}'
        out = "{"
        for elem in self:
            out += f"{elem}, "
        return out[:-2] + "}"


class UndirectedGraph():
    # construct empty graph
    def __init__(self, V):
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
        self._V = V
        self._E = 0
        self._adj = []  # adjacency lists

        for _ in range(V):
            self._adj.append(Bag())  # Initialize all lists to empty bags.
     
    def V(self):
        return self._V

    def E(self):
        return self._E

    def size(self):
        return self._V

    def __len__(self):
        return self.size()

    def add_edge(self, v: int, w: int):
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._E += 1

    def adj(self, v: int):
        return self._adj[v]

    def degree(self, v: int):
        return len(self.adj(v)) 

    def max_degree(self):
        _max = 0

        for v in range(self._V):
            if _max < len(self._adj[v]):
                _max = len(self._adj[v])
        return _max

    def average_degree(self):
        return 2 * (self._E / self._V)

    def number_self_loops(self):
        count = 0
        for v in range(self._V):
            for w in self._adj[v]:
                if v==w: 
                    count += 1
        return int(count/2)


    def __repr__(self):
        s = ["{} vertices, {} edges\n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("%d : " % (v))
            for w in self._adj[v]:
                s.append("%d " % (w))
            s.append("\n")

        return "".join(s)

