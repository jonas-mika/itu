import numpy as np
from scipy.linalg import pascal
from collections import Counter
from collections import defaultdict

# first approach using external libraries
def search_pascal_multiples_fast1(row_limit):
    # create pascal array with library
    ptriangle = np.array(pascal(row_limit))

    # filter out the outer two rows 
    ptriangle = np.delete(ptriangle, [0,1], axis=0)
    ptriangle = np.delete(ptriangle, [0,1], axis=1)

    # uniques that occur more than once
    unique_num, counts = np.unique(ptriangle, return_counts=True)

    mask = np.where(counts > 3, True, False)

    return list(unique_num[mask])

# second approach with Counter Object
def search_pascal_multiples_fast2(row_limit):
    # Building up Pascal's triangle with a dict of lists
    ptriangle = {}
    ptriangle[0] = [1]
    ptriangle[1] = [1,1]
    ptriangle[2] = [1,2,1]
    for r in range(3, row_limit):
        ptriangle[r] = []
        for i in range(len(ptriangle[r-1])+1):
            if i == 0: # on left border, so we just add 1
                ptriangle[r].append(1)
            elif i == len(ptriangle[r-1]): # on right border, so we just add 1
                ptriangle[r].append(1)
            else: # not on border, so we sum up the two numbers above
                ptriangle[r].append(ptriangle[r-1][i-1] + ptriangle[r-1][i])


    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = (item for row in ptriangle.values() for item in row[2:-2])

    # initalize counter object
    counter = Counter(number_list)
    
    # result = []
    # for element in counter.elements():
    #    if counter[element] > 3:
    #        result.append(element)

    return sorted(list(set([element for element in counter.elements() if counter[element] > 3])))

# changed data type to list of lists
def search_pascal_multiples_fast3(row_limit):
    # Building up Pascal's triangle with a dict of lists
    ptriangle = [[1], [1,1], [1,2,1]]
    for r in range(3, 250):
        for i in range(len(ptriangle[-1])+1):
            if i == 0:
                ptriangle.append([1])
            elif i == len(ptriangle[-2]):
                ptriangle[-1].append(1)
            else:
                ptriangle[-1].append(ptriangle[-2][i-1] + ptriangle[-2][i])


    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = (item for row in ptriangle for item in row[2:-2])

    # initalize counter object
    counter = Counter(number_list)
    
    # result = []
    # for element in counter.elements():
    #    if counter[element] > 3:
    #        result.append(element)

    return sorted(list(set([element for element in counter.elements() if counter[element] > 3])))

def search_pascal_multiples_fast4(row_limit):
    
    # create pascal using another algorithm
    ptriangle = [] # a container to collect the rows
    for _ in range(250): 
        row = [1] # a starter 1 in the row
        if ptriangle: # then we're in the second row or beyond
            last_row = ptriangle[-1] # reference the previous row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        ptriangle.append(row) # add the row to the results.

    number_list = (item for row in ptriangle for item in row[2:-2])

    counter = Counter(number_list)
    
    return sorted(list(set([element for element in counter.elements() if counter[element] > 3])))

def search_pascal_multiples_fast5(row_limit):
    # create pascal using another algorithm
    ptriangle = [] # a container to collect the rows
    for _ in range(250): 
        row = [1] # a starter 1 in the row
        if ptriangle: # then we're in the second row or beyond
            last_row = ptriangle[-1] # reference the previous row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        ptriangle.append(row) # add the row to the results.

    number_list = (item for row in ptriangle for item in row[2:-2])

    d = defaultdict(int)
    for w in number_list: d[w] += 1 
        
    return sorted(list(set([element for element in d.keys() if d[element] > 3])))


#----------- DO NOT CHANGE ANYTHING BELOW THIS LINE


def search_pascal_multiples_slow(row_limit):

    # Building up Pascal's triangle with a dict of lists
    ptriangle = {}
    ptriangle[0] = [1]
    ptriangle[1] = [1,1]
    ptriangle[2] = [1,2,1]
    for r in range(3, row_limit):
        ptriangle[r] = []
        for i in range(len(ptriangle[r-1])+1):
            if i == 0: # on left border, so we just add 1
                ptriangle[r].append(1)
            elif i == len(ptriangle[r-1]): # on right border, so we just add 1
                ptriangle[r].append(1)
            else: # not on border, so we sum up the two numbers above
                ptriangle[r].append(ptriangle[r-1][i-1] + ptriangle[r-1][i])

    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = []
    for r in range(row_limit):
        row = ptriangle[r]
        for i, number in enumerate(row):
            if i > 1 and i < len(row)-1: # exclude the outermost 2 numbers in each row
                number_list.append(number)

    # Counting the numbers
    number_set = set(number_list) 
    pascal_multiples = []
    for unique_number in number_set:
        count = 0
        for number in number_list:
            if number == unique_number:
                count = count + 1
        if count > 3:
            pascal_multiples.append(unique_number)
    
    return sorted(pascal_multiples)


from timeit import default_timer as timer

def main():
	row_limit = 250

	start = timer()
	print(search_pascal_multiples_slow(row_limit))
	end = timer()
	runtime_slow = end-start

	start = timer()
	print(search_pascal_multiples_fast5(row_limit))
	end = timer()
	runtime_fast = end-start

	print(round(runtime_slow / runtime_fast, 2))

def test():
    # print(search_pascal_multiples_slow(250))
    print(search_pascal_multiples_fast5(250))

if __name__ == "__main__":
	main()