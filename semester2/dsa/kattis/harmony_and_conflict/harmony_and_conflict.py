# solution to harmony and conflict
import sys

lines = sys.stdin.readlines()

# number of vertices and edges
V, E = [int(i) for i in lines[0].strip().split()]
edges = [[int(i) for i in line.strip().split()] for line in lines[1:]]


def opposite(i):  # helper to get complement coloring
    if i == 0:
        return 1
    elif i == 1:
        return 0


def solve():
    # built necessary data structure
    # array with coloring 0/1 for each vertex at array index, -1 if not colored
    coloring = [-1] * V

    for edge in edges:
        # print(f"Edge: {edge}")
        v, w, t = edge

        # check for violation (only appears when it checks two already colored vertices)
        if coloring[v] != -1 and coloring[w] != -1:
            # print("checked edge")
            if t == 0:  # harmony edge conflict
                if coloring[v] != coloring[w]:
                    # print("Harmony Edge Conflict")
                    return 0
            elif t == 1:  # conflict edge conflict
                if coloring[v] == coloring[w]:
                    # print("Conflict Edge Conflict")
                    return 0

        # both uncolored yet
        elif coloring[v] == -1 and coloring[w] == -1:
            if t == 1:  # conflict edge
                coloring[v] = 1
                coloring[w] = 0
            elif t == 0:  # harmony edge
                coloring[v] = 1
                coloring[w] = 1

        # start node not colored yet
        elif coloring[v] == -1 and coloring[w] != -1:
            if t == 1:  # conflict edge
                coloring[v] = opposite(coloring[w])
            if t == 0:  # harmony edge
                coloring[v] = coloring[w]

        # end node not colored yet
        elif coloring[v] != -1 and coloring[w] == -1:
            if t == 1:  # conflict edge
                coloring[w] = opposite(coloring[v])
            if t == 0:  # harmony edge
                coloring[w] = coloring[v]
        # print(f"Coloring: {coloring}")
        # print("-"*5)

    return 1


print(solve())
