# Common recursive problems solved

##########################
# INTEGERS
##########################

# sum of first n integers
def sum_of_first_n_integers(n):
    assert type(n) == int and n >= 0
    if n==1:
        return 1
    return n + sum_of_first_n_integers(n-1)

# print(sum_of_first_n_integers(10))

####################

# power function 
def power(a,b):
    if b==1:
        return a
    return a * power(a,b-1)

# print(power(5,3))

####################

# sum of 1/n for all integers n>=1
def harmonic_sum(n):
    if n==1:
        return 1
    return 1/n + harmonic_sum(n-1)

print(harmonic_sum(10))


####################

def number_of_digits(n):
    if n<10:
        return 1
    return 1 + number_of_digits(int(n/10))

#print(number_of_digits(108234))

####################

def sum_of_digits(n):
    if n<10:
        return n
    return int(str(n)[0]) + sum_of_digits(int(str(n)[1:]))
    
#print(sum_of_digits(888))


##########################
# STRINGS AND LISTS
##########################

# length of list 
def length_rec(S):
    if S == '':
        return 0
    if S[0] not in ["a", "e", "i", "o", "u"]:
        print(S[0], end=" ")
    return 1 + length_rec(S[1:])
#print(length_rec("ksedjfksadfja"))

################

# given a list of numbers calculate the number of even numbers in the list
def count_even(L):
    if len(L) == 0:
        return 0
    if L[0]%2==0:
        return 1 + count_even(L[1:])
    else: return 0 + count_even(L[1:])

# print(count_even([1,2,3,4]))

################

#  find max in list
def max_rec(L):
    if len(L) <= 1:
        return L[0]
    else:
        m = max_rec(L[1:])
        return m if m > L[0] else L[0]  
#print(max_rec([2,4,6]))

##############

# find max recursively
def findMax(A):
	if(len(A) == 1):
		return A[0]
	return max(A[0], findMax(A[1:]))	

###############

# Reverse list recursively
def rev(L):
	if (len(L) <= 1):
		return L
	else:
		return rev(L[1:]) + [L[0]]

###############

# palindrome
def is_palindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return is_palindrome(word[1:-1])

# print(is_palindrome("racecar"))




##########################
# SEQUENCES
##########################

##################
# n! (N-factorial)
def factorial(n):
    assert type(n) == int and n>=0, "Please enter a valid number to calculate the factorial"
    if n <= 0:
        return 1
    return n * factorial(n-1)

##################
# find nth fibonacci number
def fibonacci(n):
    assert type(n) == int and n>0
    if n<=1:
        return n
    return (fibonacci(n-1) + fibonacci(n-2))

#print(fibonacci(30))



###################################
# OTHERS
###################################

def bubble_sort(L, order="ascending"):
    assert order in ["ascending", "descending"], "I don't know this order type."
    if order=="ascending":
        for _ in range(len(L)):
            for i in range(len(L)-1):
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
    elif order=="descending":
       for _ in range(len(L)):
            for i in range(len(L)-1):
                if L[i] < L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
    return L

#print(bubble_sort([3,2,1,4,2.5], "descending"))