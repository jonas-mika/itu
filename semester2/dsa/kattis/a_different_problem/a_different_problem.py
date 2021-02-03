import sys

for line in sys.stdin:
    ab =  line.split()
    a = int(ab[0])
    b = int(ab[1])
    
    if a>b:
        print(a-b)  
    else: print(b-a)
