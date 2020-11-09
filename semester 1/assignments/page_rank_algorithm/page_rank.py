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
    Takes in .txt file containing the adjacencies and returns a directed nx.Graph object, that contains the unique nodes and directed links as edges.
    """

    with open(filename, 'rb') as infile: # create a filehandler to open the sample data
        return nx.read_adjlist(infile, create_using=nx.DiGraph(), nodetype=int) # read it into a nx directed graph object

def show_graph(G):
    """
    Displays the nodes and edges of a nx.Graph object 
    """
    nx.draw(G, with_labels=True, node_color='green') #draw the network graph 
    plt.show() #to show the graph by plotting it

def summary_graph(G):
    """
    Prints a summary of the properties of an graph objected provided as an input argument.
    """
    print('SUMMARY OF GRAPH')
    print(f'Nodes: {G.nodes()}\nNumber of Nodes: {len(G)}\n')
    print(f'Edges: {G.edges()}\nNumber of Edges/ Size: {G.size()}\n')

def neighbours(G, node):
    """
    Takes a node as input and returns all possible nodes, that have a directed link          
    """
    return [edge[1] for edge in G.edges() if edge[0] == node]

def summary_random_sufer(visited : dict):
    total_visits = sum(visited.values())

    print('SUMMARY OF RANDOM WALK')
    print('---------------------------')
    print(f'Performed {total_visits} Iterations of Random Walks.\n')
    print('Ranked Nodes\t#Visits\t\tRelative Importance Score')
    for key in visited:
        print(f'{key}\t\t{visited[key]}\t\t{round(visited[key]/total_visits, 3)} ({round((visited[key]/total_visits)*100, 2)}%)')


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

    Input Arguments:
    - G: nx.Graph Object 
    - n: Number of Walks that should be performed
    - m: damping factor (= probability, to move to a random node)
    """
    visited = {}
    # random_node = random.choice([i for i in G.nodes()])
    
    current_node = random.choice([i for i in G.nodes()])
    for i in range(n):
        #print(f'Number of Walks: {i}')
        #print(f'Current Node: {current_node}')
        
        # count the visits
        if current_node not in visited:
            #print('I havent seen this node so far')
            visited[current_node] = 1
        else:
            visited[current_node] += 1

        # choose the next node
        # account for dangling nodes
        if neighbours(G, current_node) == []:
            #print('This note doesnt have any neighbours, we have to randomly choose')
            current_node = random.choice([i for i in G.nodes()])

        # damping factor 
        elif random.random() < m:
            #print('Damping Factor: Choose Random Node')
            current_node = random.choice([i for i in G.nodes()])
            
        else: 
            #print('Walk to Neighbour')
            #print(f'It must be one of those: {neighbours(G, current_node)}')
            current_node = random.choice(neighbours(G, current_node))

    # return dict(sorted(visited.items()))
    return dict(sorted(visited.items(), key=lambda x: x[1], reverse=True))


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

    # print small summary and graphical representation of network
    show_graph(G)
    summary_graph(G)
    
    # perform random walk and print summary
    surf_results = random_surfer(G, 10000, 0.15)
    summary_random_sufer(surf_results)

    # perform pagerank algorithm and print summary
    # pagerank_results = page_rank(G, 100)
    # summary_pagerank(pagerank_results)


if __name__ == "__main__":
    main()