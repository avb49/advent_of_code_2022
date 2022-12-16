import numpy as np

def read_data(data_path: str, encoding_type='utf-8-sig') -> list:
    """Reads data from a given text file and returns a list with each item being a line in the text file"""
    
    with open(data_path, encoding=encoding_type, mode='r') as file:
        data = file.read().splitlines()
    
    return data

def read_matrix_as_2d_np_array(data_path: str) -> np.ndarray:
    """Reads a data file as a 2d numpy array and returns it"""

    matrix_data = read_data(data_path)
    no_rows = len(matrix_data)
    no_columns = len(matrix_data[0])

    # convert each row of matrix to a numpy array
    ncombined = np.array(list(matrix_data[0]),dtype=int)
    for row_no in range(1, no_rows):
        nparray = np.array(list(matrix_data[row_no]),dtype=int)
        ncombined = np.concatenate((ncombined, nparray), axis=0)
    
    # reshape data as a 2d np array
    return ncombined.reshape(no_rows,no_columns)

def get_intersection_of_two_items(item1, item2):
    """Given two iterables, finds the item(s) present in both and returns them"""
    return set(item1).intersection(set(item2))

def get_intersection_of_three_items(item1, item2, item3):
    """Given three iterables, finds the item(s) present in both and returns them"""
    intersection_1 = set(item1).intersection(set(item2))
    return intersection_1.intersection(set(item3))