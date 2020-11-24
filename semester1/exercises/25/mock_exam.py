def secret_operation(k):
    for i in range(1, len(k)):
        j=i
        temp = k[j]
        while j > 0 and temp < k[j-1]:
            k[j] = k[j-1]
            j -= 1
        k[j] = temp
    return k

# print(secret_operation([3, 2, 5, 4]))

def are_they_unique(some_list):
	sorted_list = sorted(some_list)
	for i in range(len(sorted_list)-1):
		if sorted_list[i] == sorted_list[i+1]:
			return False
	return True

# print(are_they_unique([1,2,3,3,4,5]))

def recur_fact(n):
	if n == 1: return 1
	return n * recur_fact(n-1)

# print(recur_fact(3))

def sum_list(L):
	if len(L) == 1:
		return L[0]
	return L[0] + sum_list(L[1:])

print(sum_list([1,2,4]))