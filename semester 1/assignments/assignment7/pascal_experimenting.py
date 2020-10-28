import numpy as np
from scipy.linalg import pascal

# firs
def search_pascal_multiples_fast(row_limit):
    # create pascal array with library
    ptriangle = np.array(pascal(row_limit))

    # filter out the outer two rows 
    ptriangle = np.delete(ptriangle, [0,1], axis=0)
    ptriangle = np.delete(ptriangle, [0,1], axis=1)

    # uniques that occur more than once
    unique_num, counts = np.unique(ptriangle, return_counts=True)

    mask = np.where(counts > 3, True, False)

    return list(unique_num[mask])

def search_pascal_multiples_np(row_limit):
     # create the pascal triangle within a numpy array
    # ptriangle = np.empty(shape=(row_limit, row_limit), dtype=int)

    # ptriangle[0][0] = 1
    # ptriangle[1][0:2] = 1

    # for i in range(2, row_limit):
    #     len_row = i + 1 # 3, ..., 250
    #     for j in range(len_row):
    #         if j == 0:
    #             ptriangle[i][0] = 1
    #         if j == 0:
    #           ptriangle[i][i] = 1
    #         if j == 
    pass

