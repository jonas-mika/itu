# solve seat_allocation with maxpq data structure that is implemented on party class
# coded by louis brandt and jonas-mika senghaas
from itu.algs4.sorting.max_pq import MaxPQ
import sys

# read in input 
lines = sys.stdin.readlines()

n, m = [int(i) for i in lines[0].strip().split()] # n (number of parties), m (number of seats)
V = [float(i) for i in lines[1:]] # number of votes for each party

class Party():
    def __init__(self, num, votes):
        self.num = num
        self.votes = votes
        self.quotient = votes 
        self.seats = 0

    def assign_seat(self): 
        self.quotient = self.votes/(self.seats+2)
        self.seats += 1

    def get_seats(self):
        return self.seats

    def get_quotient(self):
        return self.quotient

    def get_num(self):
        return self.num

    def __lt__(self, other):
        if self.quotient < other.quotient:
            return True 
        else: return False 

    def __repr__(self):
        return f"Vote Quotient: {self.quotient}"

    def __str__(self):
        return f"Number: {self.num}, Vote Quotient: {self.quotient}, Seats: {self.seats}"

def solve(m, n):
    # initialise priority queue as heap data structure with size == number of parties
    pq = MaxPQ(n)
    for i, votes in enumerate(V):
        pq.insert(Party(i, votes))

    seats = [0] * n

    while m>0:
        p = pq.del_max()
        p.assign_seat() # recalculating the quotient
        pq.insert(p)
        seats[p.get_num()] += 1
        m -= 1

    for seat in seats:
        print(seat)

solve(m, n)
