# imports for search_pascal_multiples_fast
from collections import Counter

# imports for search_pascal_multiples_readable
import numpy as np
from scipy.linalg import pascal


# fastest function (the results vary, the maximum i could get was 972x times faster)
def search_pascal_multiples_fast(row_limit):
     # create pascal using another algoritm and list data type
    ptriangle = [] # a container to collect each row
    for _ in range(250): 
        row = [1] # a starter 1 in the row
        if ptriangle:
            last_row = ptriangle[-1] # reference the previous row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # append the final 1 to the outside
            row.append(1)
        ptriangle.append(row) # add row to ptriangle list

    # create a generator objects of all numbers exlcluding outer two rows
    number_list = (item for row in ptriangle for item in row[2:-2])

    # initialize counter object on generator objects
    counter = Counter(number_list)
    
    return sorted(list(set([element for element in counter.elements() if counter[element] > 3]))) # return sorted list of unique numbers in the counter, where the counter is greater > 3


# most pleasant to read and understand (using numpy and scipy)
def search_pascal_multiples_readable(row_limit):
    # create pascal array with library pascal from scipy.linalg subpackage
    pascal_array = np.array(pascal(row_limit))

    # filter out the outer two rows 
    pascal_array = np.delete(pascal_array, [0,1], axis=0)
    pascal_array = np.delete(pascal_array, [0,1], axis=1)

    # store the unique numbers from the sliced array and their counts
    unique_num, counts = np.unique(pascal_array, return_counts=True)

    # create a mask, where the number of counts is greater than 3
    mask = np.where(counts > 3, True, False)

    return list(unique_num[mask]) # return the array of unique numbers, whose count is greater than 3 as a list
    

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
	print(search_pascal_multiples_fast(row_limit))
	end = timer()
	runtime_fast = end-start

	print(round(runtime_slow / runtime_fast, 2))

if __name__ == "__main__":
	main()