# read data from a given text file and return a list with each item being a line in the text file
def read_data(data_path: str, encoding_type='utf-8-sig') -> list:
    
    with open(data_path, encoding=encoding_type, mode='r') as file:
        data = file.read().splitlines()
        file.close()
    
    return data

# given two strings, finds the character(s) present in both and return them
def get_intersection_of_two_strings(string1: str, string2: str) -> str:
    return set(string1).intersection(set(string2))

# given three strings, finds the character(s) present in all of them and return them
def get_intersection_of_three_strings(string1: str, string2: str, string3: str) -> str:
    intersection_1 = set(string1).intersection(set(string2))
    return intersection_1.intersection(set(string3))