import sys

lines = sys.stdin.readlines()
N, t = [int(i) for i in lines[0].split()]
A = [int(i) for i in lines[1].split()]

def sol(N, t, A):
    if t==1:
        print(7)
    elif t == 2:
        if A[0]>A[1]:
            print("Bigger")
        elif A[0] == A[1]:
            print("Equal")
        else:  print("Smaller")
    elif t == 3:
        print(sorted(A[:3])[1])
    elif t == 4:
        print(sum(A))
    elif t == 5:
        print(sum([i for i in A if i%2==0]))
    elif t == 6:
        modulus_list = [i%26 for i in A]
        map_dict = {num: character for num, character in zip(list(range(25)), list(map(chr, range(97, 123))))}
        for x, num in enumerate(modulus_list):
            if x == N-1:
                print(map_dict[num])
            else: print(map_dict[num], end="")
    elif t == 7:
        i = 0
        i = A[i]

        while i!=0:
            if i == N-1:
                exit("Done")
            elif i > N-1 or i < 0:
                exit("Out")
            i = A[i] 
        print("Cyclic")

sol(N,t,A)
