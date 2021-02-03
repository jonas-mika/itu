# testing own implementation of union find

class UF:
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


    

UF = UF(10)
print(UF.data)
UF.union(1,2)
print(UF.data)
UF.union(3,4)
print(UF.data)
UF.union(2,3)
print(UF.data)
UF.union(5,6)
print(UF.data)
UF.move(3,5)
print(UF.data)
print(UF.count)
print(UF.connected(0,1))
print(UF.connected(3,5))
