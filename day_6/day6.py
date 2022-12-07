import time

from utils import *

# part 1 - start of packet length is 4
#MARKER_LENGTH = 4
# part 2 - start of message length is 14
MARKER_LENGTH = 14

# function which tests if chars in string are all unique (True/False output)
def are_chars_unique(string: str) -> bool:
    return len(string) == len(set(string))

def main():

    # 1. import data
    stream_data = read_data("day_6/data/data.txt")
    datastream = stream_data[0]

    start_time = time.time()

    match_found = False
    for index in range(0, len(datastream) - MARKER_LENGTH):
        
        # 2. use string slicing to get 4-character blocks
        potential_marker = datastream[index:MARKER_LENGTH + index]

        # 3. check if 4-character block is unique, break out of for loop if it is
        if are_chars_unique(potential_marker):
            print(MARKER_LENGTH + index)
            match_found = True
            break

    if match_found == False:
        print("No match was found for the given input.")
    print()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()