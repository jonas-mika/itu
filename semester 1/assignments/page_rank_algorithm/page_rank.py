import networkx as nx
import sys
import random
import matplotlib.pyplot as plt
import numpy as np

## from lecture notes
# fh=open(sys.argv[1], "rb")
# G=nx.read_adjlist(fh, create_using=nx.DiGraph())
# fh.close()

# helper functions
def read_adjlist(filename : str):
    """
    Takes in .txt file containing the adjacencies and returns a directed nx.Graph object, that contains the unique nodes and directed linjs as edges.
    """

    with open(filename, 'rb') as infile: # create a filehandler to open the sample data
        return nx.read_adjlist(infile, create_using=nx.DiGraph()) # read it into a nx directed graph object

def show_graph(G):
    """
    Displays the nodes and edges of a nx.Graph object 
    """
    nx.draw(G, with_labels=True, node_color='green') #draw the network graph 
    plt.show() #to show the graph by plotting it

def neighbours(G, node):
    """
    Takes a node as input and returns all possible nodes, that have a directed link          
    """
    return [edge[1] for edge in G.edges() if edge[0] == node]

# setup function for page rank algorithm
def branching(G):
    branching = dict()

    for node in G.nodes():
        branching[node] = 0
        
        for edge in G.edges():
            if edge[0] == node:
                branching[node] += 1 # increment the count of outgoing links
    
    return branching
    
def importance(G):
    """
    Initializes the starting vector x0, holding 1/n for each node
    """
    return {node: 1/G.size() for node in G.nodes()}

def find_dangling_nodes(G):
    nondangling_nodes = set()
    for edge in G.edges():
        nondangling_nodes.add(edge[0])
    
    return [node for node in G.nodes() if node not in nondangling_nodes]

        
# functions
def random_surfer(G, n, m):
    """
    Random Sufer Function, to simulate a random walk.

    Parameters:
    - G: nx.Graph Object 
    - n: Number of Walks that should be performed
    - m: dumping factor (= probability, to move to a random node)
    """
    visited = {}
    # random_node = random.choice([i for i in G.nodes()])
    
    current_node = random.choice([i for i in G.nodes()])
    for i in range(n):
        print(f'Number of Walks: {i+1}')
        print(f'Current Node: {current_node}')
        
        if current_node not in visited:
            print('I havent seen this node so far')
            visited[current_node] = 1
        else:
            visited[current_node] += 1

        # accountant for dangling nodes
        if neighbours(G, current_node) == []:
            print('This note doesnt have any neighbours, we have to randomly choose')
            current_node = random.choice([i for i in G.nodes()])

        else:
            if random.random() < m:
                print('Damping Factor: Choose Random Node')
                current_node = random.choice([i for i in G.nodes()])
            
            else: 
                print('Walk to Neighbour')
                print(f'It must be one of those: {neighbours(G, current_node)}')
                current_node = random.choice(neighbours(G, current_node))

    return sorted(visited.items(), key=lambda x: x[1], reverse=True)


def page_rank(G, m, n):
    # setup
    size = G.size()
    G_reverse = nx.reverse(G)
    branches = branching(G)
    dangling_nodes = find_dangling_nodes(G)

    pagerank_vector = importance(G)

    for i in range(n):
        for node, rank in pagerank_vector.items():
            S = m * 1/size * rank # initialize next vector with mSkx
            if node in dangling_nodes:
                D = (1-m) * 1/size * node # add dangling nodes
                rank = D + S
            else: 
                pass # needs to add the computation if node is not dangling
                #rank += (1-m) * 
                A = (1-m) 
                rank = D + A
            


    return pagerank_vector

# testing environment and main function
def main():
    # read in the adj list using the read_adjlist() helper function
    G = read_adjlist('PageRankExampleData/tiny.txt')

    print(f'Nodes: {G.nodes()}\nNumber of Nodes: {len(G)}\n')
    print(f'Edges: {G.edges()}\nNumber of Edges/ Size: {G.size()}\n')

    #random_walk = random_surfer(G, 10000, 0.15)
    #print(random_walk)
    #print(sum([i[1] for i in random_walk]))

    page_rank(G, 100)
    
    show_graph(G)

def testenv():
    pass

if __name__ == "__main__":
    main()