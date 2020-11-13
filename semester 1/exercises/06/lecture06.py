#lecture06

######################
# showing (p and q) == (q and p)
######################
for p in [True, False]:
	for q in [True, False]:
		(p and q) == (q and p)

######################
# no solutions to p == (p == False) , liar paradox
######################	
for p in [True, False]:
	p == (p == False)

##############
# find max recursively
##############
def findMax(A):
	if(len(A) == 1):
		return A[0]
	return max(A[0], findMax(A[1:]))	
###############
# Reverse list recursively
###############
def rev(A):
	if (len(A) <= 1):
		return A
	else:
		return rev(A[1:]) + [A[0]]
		

# def my_findMax(L): 
# 	if len(L) == 1:
# 		return L[0]

# 	if  < L[0]:
# 		curr_max = L[0]
# 	return my_findMax(L[1:])
