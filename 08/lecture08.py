#lecture08
#####################
#edgelist
######################
[['a', 'b'], ['a', 'c'], ['a', 'e'], ['c', 'a'], ['c', 'd'],
['c', 'e'], ['d', 'c'], ['d', 'e'], ['e', 'a'], ['e', 'c'], ['e', 'd']]

#####################
#adjacency list
######################
vertices = ['a','b','c','d','e']
adjacencies=[
['b','c','e'],
['a'],
['a','d','e'],
['c','e'],
['a','c','d']
] 

adjacencies[vertices.index('a')]

#####################
#adjacency matrix
######################
vertices = ['a','b','c','d','e']
matrix = [
[0,1,1,1,1], 
[0,1,0,1,0], 
[1,0,1,0,1], 
[0,0,0,0], 
[0,1,1,1,0]]
matrix[vertices.index('a')][vertices.index('b')]

#################
# depth first
#################
# Using a Python list of lists to act as an adjacency list
vertices = ['A','B','C','D','E','F']
graph = [
    ['B','C'],
    ['D', 'E'],
    ['F'],
    [],
    ['F'],
    []
]



def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[vertices.index(node)]:
            dfs(visited, graph, neighbour)

# Driver Code
def do_dfs():
  visited = set() # Set to keep track of visited nodes.
  dfs(visited, graph, 'A')

###############
#stack
###############
stack = [1,2,3]
stack.append(4) #push to stack
stack.pop() #pop LIFO

###############
#queue
###############
queue = [5,6,7]
queue.append(8) #enqueue
queue.pop(0) #dequeue FIFO


#################
# breadth first
#################
vertices = ['A','B','C','D','E','F']
graph = [
  ['B','C'],
  ['D', 'E'],
  ['F'],
  [],
  ['F'],
  []
]

queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[vertices.index(s)]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
def do_bfs():
  visited = [] # List to keep track of visited nodes.
  bfs(visited, graph, 'A')

