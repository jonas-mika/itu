# implementation of finding the shortest path for any pair of vertices in a line graph
#
# Example: 3 - 2 - 1 - 4 - 5

V = list(range(6))[1:]
edge_list = [(1, 2), (1, 3), (1, 4), (4, 5)]
E = len(edge_list)

print(V, edge_list, E)
