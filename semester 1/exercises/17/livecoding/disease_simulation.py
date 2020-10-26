
# import 
import random
import matplotlib.pyplot as plt


# classes
class Network:

    def __init__(self, n, p, c, h, s):
        self.n = n  # number of nodes in network
        self.p = p  # probability of contact in network
        self.c = c  # probability of getting sick
        self.h = h  # probability of getting healthy
        self.s = s  # probability of spreading the infection along an edge
        self.N = {i: Node(i) for i in range(n)}
        self.E = []
        self.S = 0  # number of infected people

    def __str__(self):
        return f"\nNodes: {self.n}\nEdges: {len(self.E)}\nHealthy People: {self.n - self.S}\nInfected People: {self.S}"

    # construct the edges in the netwr
    def genesis(self):
        """
        Construct the edges in the network with a given probablity of contact
        """
        for i in range(self.n):
            for j in range(i+1, self.n):
                if random.random() < self.p:
                    self.E.append([self.N[i], self.N[j]]) # we could rewrite all of this in a list comprehension
    
    def outbreak(self):
        """
        Simulates an outbreak within the given Network, such that a node gets sick with a given probability of infection
        """
        for node in self.N.values():
            if random.random() < self.c:
                node.state = -1
                self.S += 1 

    def progress(self):
        """

        """

        for node in self.N.values():
            # update immunity 
            if node.state == -1 and random.random() < self.h:
                node.state = 1
                self.S -= 1

            # spread infection along the edges
            for edge in self.E:
                if edge[0].state == -1 and edge[1].state == 0 and random.random() < self.s:
                    edge[1].state = -1
                    self.S += 1

                elif edge[1].state == -1 and edge[0].state == 0 and random.random() < self.s:
                    edge[0].state = -1
                    self.S += 1

    def plotter(self):
        pass

class Node:
    
    def __init__(self, id):
        self.id = id
        self.deg = 0
        self.state = 0

    def __repr__(self):
        pass

# functions
N = Network (1000, 0.01, 0.1, 0.1, 0.3)
print(N)
N.genesis()
print(N)

N.outbreak()
y = [N.S]; x = [i for i in range(111)]
print(N)

for _ in range(110):
    N.progress()
    y.append(N.S)

plt.plot(x,y)
plt.show()



