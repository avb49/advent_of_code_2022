# read data from a given text file and return a list with each item being a line in the text file
def read_data(data_path: str, encoding_type='utf-8-sig') -> list:
    
    with open(data_path, encoding=encoding_type, mode='r') as file:
        data = file.read().splitlines()
        file.close()
    
    return data

# given two strings, finds the character(s) present in both and return them
def get_intersection_of_two_items(item1, item2):
    return set(item1).intersection(set(item2))

# given three strings, finds the character(s) present in all of them and return them
def get_intersection_of_three_items(item1, item2, item3):
    intersection_1 = set(item1).intersection(set(item2))
    return intersection_1.intersection(set(item3))