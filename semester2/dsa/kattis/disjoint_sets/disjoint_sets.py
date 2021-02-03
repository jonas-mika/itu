from itu.algs4.fundamentals.uf import WeightedQuickUnionUF
import sys

# read input 
lines = sys.stdin.readlines()
n, _ = [int(i) for i in lines[0].split()]
operations = [[int(i) for i in operation.split()] for operation in lines[1:]]

# print(n,m)
# print(operations)

# my_operations = [
#     [1,0,1],
#     [1,1,2],
#     [1,4,3],
#     [2,4,2],
#     [2,5,4],
#     [2,0,3]
# ]

def main():
    # initialising family of disjoints sets, as singelton {0}, {1}, ..., {n-1}
    UF = WeightedQuickUnionUF(n)

    for operation in operations:
        o, s, t = operation
        #print(UF._count) # number of disjoint sets
        #print(UF._size) # list of sizes of each tree

        if o == 0: # query
            if UF.connected(s,t) == True:
                print("1")
            else: print("0")

        elif o == 1: # union
            UF.union(s,t)

        elif o == 2: # move
            # find children and parent
            children = [index for index,elm in enumerate(UF._parent) if elm==s]
            root = UF.find(s)

            if s == UF._parent[s]: # moving node is root node
                children.remove(s)
                for child in children:
                    UF._parent[child] = children[0]
            else: # moving node is not a root node
                for child in children:
                    UF._parent[child] = root

            # move s into t
            UF._parent[s] = UF.find(t)

if __name__ == '__main__':
    main()