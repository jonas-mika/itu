##########
# Exercises 11 - Using Numpy Library 
##########

# Author		: 	Jonas-Mika Senghaas
# Date Created	:	28.09.2020

import numpy as np

A = np.zeros(10, dtype = int)
#print(A)

B = np.ones((3,5))
#print(B)

C  = np.full((3,5), 3.14)
#print(C)

D = np.identity(3)
#print(D)

###########
A = np.arange(1,10)
#print(A)

B = np.reshape(A, (3,3))
#print(B)

C = np.random.randint(10, size=(3, 3))
# print(C)

D = np.random.rand(4, 3, 3) 
# print(D)

#print(A[2:5])

#print(B[1,2])

#print(B[:, :2])

D = np.zeros(10)
D[(4,6), ] = 42
#print(D)

#print(np.nonzero(D))

#print(np.max(B))
#print(np.min(B))

# for i in range(3):
#     print("Max of Row " + str(i) + ":       " + str(np.max(B[i:i+1])))
#     print("Min of Row " + str(i) + ":       " + str(np.min(B[i:i+1])))
#     print("_________")

# coloumns
#print(np.amax(B, axis=0))
#print(np.amin(B, axis=0))

#print(np.amax(B, axis=1))
#print(np.amin(B, axis=1))

#print(np.mean(B))

#print(np.equal(B, C))

#print(np.where(A<6, A, -A))

###########
# Linear Algebra
###########

#print(np.dot(B, C))

#print(np.linalg.det(B))

assert np.linalg.det(C) != 0
print(np.linalg.inv(C))

#print(np.linalg.det(C))