# imports
import networkx as nx
import random
from timeit import default_timer
from matplotlib import pyplot as plt
import os
import csv

# global variable storing the filenames of the example datasets
FILENAMES = ['tiny', 'three', 'wikipedia', 'medium', 'p2p-Gnutella08-mod', 'bigRandom']


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
    print('SUMMARY OF GRAPH\n-----------------------')
    print(f'Number of Nodes: {len(G)}\nNumber of Edges/ Size: {G.size()}')
    print(f'Nodes: {G.nodes()}\nEdges: {G.edges()}')


def summary(x : dict, type, n=10):
    """
    Prints out a nicely formatted output of the ten highest importance scores for both the random surfer and the pagerank algorithm.
    """

    if type == 'surfer':
        total_visits = sum(x.values())

        print(f'SUMMARY: Random Walk ({total_visits} iterations)')
        print('---------------------------')
        print('Ranked Nodes\t#Visits\t\tRelative Importance Score')
        for i, key in enumerate(x):
            if i == n: break
            print(f'{key}\t\t{x[key]}\t\t{round(x[key]/total_visits, 5)} ({round((x[key]/total_visits)*100, 3)}%)')

    elif type == 'pagerank':
        print('SUMMARY: Pagerank')
        print('---------------------------')
        print('Ranked Nodes\tImportance Score')
        for i, key in enumerate(x):
            if i == n: break
            print(f'{key}\t\t{x[key]} ({x[key]*100}%)')

    else: print('Please specify a valid type.')



def write_to_csv(x : dict, filename, type):
    try: os.mkdir('results')
    except: None
    
    if type == 'surfer':
        total_visits = sum(x.values())

        with open(f'results/surfer_results_{filename}.csv', 'w', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Node', 'Number of Visits', 'Relative Importance Score', '%'])
            for key in x:
                writer.writerow([key, x[key], x[key]/total_visits, (x[key]/total_visits)*100])

    elif type == 'pagerank':
        with open(f'results/pagerank_results_{filename}.csv', 'w', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Node', 'Importance Score', '%'])
            for key in x:
                writer.writerow([key, x[key], x[key]*100])

    else: print('Please specify a valid type.')
        


    
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
    # initialize a dictionary with a key for each node and initializing the value (number of visits) to 0
    visited = {node: 0 for node in G.nodes()}

    # choose start node randomly
    nc = len(G)-1 # maximum index
    node = random.randint(0, nc)


    for _ in range(n):
        # increment the visit counter for current node
        visited[node] += 1

        # walk to next next node according to random surfer algorithm
        if [neighbor for neighbor in G.neighbors(node)] == [] or random.random() < m:
            node = random.randint(0, nc)
            
        else: node = random.choice([neighbor for neighbor in G.neighbors(node)])

    return dict(sorted(visited.items(), key=lambda x: x[1], reverse=True))


def page_rank(G, n, m):
    """
    PageRank Algorithm Function, that computes the importance vector for each node in a network.

    Input Arguments:
    - G: nx.Graph Object 
    - n: Number of Iterations performed
    - m: damping factor (= probability, to move to a random node)
    """
    # setup
    size = len(G) # number of nodes
    G_reverse = nx.reverse(G) # directed graph object with reversed edges (later used to compute the backlinks of each node)
    dangling_nodes = find_dangling_nodes(G) # list of dangling nodes
    x = {node: 1/size for node in G.nodes()} # x_0 (starting vector with equal importance for each node)

    # initialize mSx_k
    S = m * 1/size

    for i in range(n):
        D = (1-m)*sum(x[node]/size for node in dangling_nodes)

        for node, score in x.items():
            backlinks = [i for i in G_reverse.neighbors(node)] 
            scores = [1/len([i for i in G.neighbors(backlink)]) for backlink in backlinks]
            
            A = 0
            for i, backlink in enumerate(backlinks):
                A += scores[i] * x[backlink]
            A = (1-m) * A
          
            x[node] = A + D + S

    return dict(sorted(x.items(), key=lambda x: x[1], reverse=True)) 


def main():
    # choosing file 
    current_file = FILENAMES[5]
    print(f'Performing Random Surfer and PageRank onto: {current_file}.txt\n')

    # load network into networkx object representation    
    st = default_timer()
    G = read_adjlist(f'PageRankExampleData/{current_file}.txt')
    print(f'Loading File: {default_timer() - st}s')
    
    # perform random walk and print summary
    st = default_timer()
    surf_results = random_surfer(G, 10_000_000, 0.15)
    print(f'\nSurf File: {default_timer() - st}s')
    summary(surf_results, type='surfer')
    write_to_csv(surf_results, current_file, type='surfer')

    # perform pagerank algorithm and print summary    
    st = default_timer()
    pagerank_results = page_rank(G, 1, 0.15)
    print(f'\nTime for PageRank Computation: {default_timer() - st}s')
    summary(pagerank_results, type='pagerank')
    write_to_csv(pagerank_results, current_file, type='pagerank')

    # perform pagerank algorithm and print summary
    # pagerank1 = nx.pagerank(G, alpha=0.15)
    # print(pagerank1)

if __name__ == "__main__":
    main()