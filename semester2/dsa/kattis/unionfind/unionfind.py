# union find kattis exercise
import sys
from itu.algs4.fundamentals.uf import WeightedQuickUnionUF 

# start by reading in input globally
lines = sys.stdin.readlines()
N, Q = [int(i) for i in lines[0].split()]
operations = [i.split() for i in lines[1:]]

def solve():
    UF = WeightedQuickUnionUF(N)

    for operation in operations:
        o, p, q = operation[0], int(operation[1]), int(operation[2])

        if o == '?':
            if UF.connected(p, q):
                print("yes")
            else: print("no") 
        elif o == '=':
            UF.union(p, q) 

solve()
