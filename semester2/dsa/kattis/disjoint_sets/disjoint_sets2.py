import sys

class myUnionFind:
    def __init__(self, n):
        self.data = [{i} for i in range(n)]
        self.count = len(self.data)

    def find(self,p):
        for x, s in enumerate(self.data):
            if p in s:
                return x

    def union(self, p, q):
        p_index = self.find(p)
        q_index = self.find(q)

        if p != q:
            self.data[p_index].update(self.data[q_index])
            del self.data[q_index]

        self.count = len(self.data)

    def connected(self, p, q):
        p_index, q_index = self.find(p), self.find(q)

        if p_index == q_index:
            return True
        else: return False

    def move(self, p, q): # from p to q
        p_index, q_index = self.find(p), self.find(q)
        
        self.data[p_index].remove(p)
        self.data[q_index].add(p)

        self.count = len(self.data)

# read input 
lines = sys.stdin.readlines()
n, _ = [int(i) for i in lines[0].split()]
operations = [[int(i) for i in operation.split()] for operation in lines[1:]]

def main():
    UF = myUnionFind(n)

    for operation in operations:
        o, s, t = operation

        if o == 0: # query
            if UF.connected(s,t) == True:
                print("1")
            else: print("0")

        elif o == 1: # union
            UF.union(s,t)

        elif o == 2: # move
            UF.move(s,t)

if __name__ == '__main__':
    main()