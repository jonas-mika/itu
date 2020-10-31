import networkx as nx
import sys

## from lecture notes
# fh=open(sys.argv[1], "rb")
# G=nx.read_adjlist(fh, create_using=nx.DiGraph())
# fh.close()

def read_adjlist(filename : str):
     with open(filename, 'rb') as infile: # create a filehandler to open the sample data
         return nx.read_adjlist(infile, create_using=nx.DiGraph()) # read it into a nx directed graph object

def random_walk(G):
    pass

def page_rank(G):
    pass

# testing environment and main function
def main():
    G = read_adjlist('PageRankExampleData/tiny.txt')
    # print(type(G))

def testenv():
    pass

if __name__ == "__main__":
    testenv()
