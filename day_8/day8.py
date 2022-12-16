import numpy as np
import time

from utils import *

def main():

    # import data
    tree_data = read_data("day_8/data/test_data.txt")
    no_rows = len(tree_data)
    no_columns = len(tree_data[0])

    # convert each row of data to a numpy array
    ncombined = np.array(list(tree_data[0]),dtype=int)
    for row_no in range(1, no_rows):
        nparray = np.array(list(tree_data[row_no]),dtype=int)
        ncombined = np.concatenate((ncombined, nparray), axis=0)
    
    ncombined=ncombined.reshape(no_rows,no_columns)

    print(ncombined)
    print(ncombined.shape)

    print(f"Getting the 4th element of the 5th row...: {ncombined[4][3]}")

    start_time = time.time()

    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    main()