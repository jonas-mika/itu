from random import random
def estimate_pi(n = 10000000):
    in_circle = 0
    total = n
    
    while n != 0:
        prec_x = random()
        prec_y = random()
        if pow(prec_x, 2) + pow(prec_y, 2) <= 1: # circle equation: x^2+y^2=r^2
            in_circle += 1 # inside the circle
        n -= 1
        
    return 4 * in_circle / total

estimate_pi()
