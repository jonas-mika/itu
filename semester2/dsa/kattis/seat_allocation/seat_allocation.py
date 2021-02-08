import sys

lines = sys.stdin.readlines()

n, m = [int(i) for i in lines[0].strip().split()]
V = [float(i) for i in lines[1:]]

def solve(m, V):
    seats = {i: 0 for i in range(len(V))}
    copy_V = [i for i in V]

    while m>0:
        max_index = [i for i,_ in enumerate(V) if _ == max(V)][0]
        V[max_index] = copy_V[max_index]/(seats[max_index]+2)
        seats[max_index] += 1
        m -= 1
    # print seat distribution
    for seat_counts in seats.values():
        print(seat_counts)

if __name__ == '__main__':
    solve(m, V)
