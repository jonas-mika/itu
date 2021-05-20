# solution to island infection
import sys
from itu.algs4.fundamentals.queue import Queue

R, C = [int(i) for i in sys.stdin.readline().split()]
world = [[int(i) for i in line.strip()] for line in sys.stdin.readlines()]

# world = [[1, 1, 1, 0, 0, 1],
#         [1, 1, 2, 0, 0, 0],
#         [0, 1, 1, 1, 0, 3],
#         [1, 0, 1, 1, 1, 1]]


def adjacents(L, i, j):
    # function to return a list of adjacents indices
    R, C = len(L), len(L[0])
    if i < 0 or i > R-1 or j < 0 or j > C-1:
        return
    adjacents = []
    if i-1 >= 0:
        adjacents.append((i-1, j))  # top
    if i+1 <= R-1:
        adjacents.append((i+1, j))  # bottom
    if j-1 >= 0:
        adjacents.append((i, j-1))  # left
    if j+1 <= C-1:
        adjacents.append((i, j+1))  # right
    return adjacents


def solve(R, C, world):
    # find virus and make it source
    s = None
    for i in range(R):
        for j in range(C):
            if world[i][j] == 2:
                s = (i, j)

    # start bfs from infection
    q = Queue()
    q.enqueue(s)

    while q.is_empty() == False:
        v = q.dequeue()
        # for row in world:
        #    print(row)
        # print('\n')
        for adj in adjacents(world, v[0], v[1]):
            if world[adj[0]][adj[1]] == 1:
                world[adj[0]][adj[1]] = 2
                q.enqueue(adj)
            elif world[adj[0]][adj[1]] == 3:
                return 1
    return 0


print(solve(R, C, world))
