def sol(N,t,A):
    if t==7:
        i = 0
        i = A[i]

        while i!=0:
            if i == N-1:
                exit("Done")
            elif i > N-1 or i < 0:
                exit("Out")
            i = A[i]
        print("Cyclic")

sol(3,7,[1,2,2])