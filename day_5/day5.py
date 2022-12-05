import time
import re
from collections import deque
from utils import *

DISTANCE_BETWEEN_CRATES = 4
SEARCH_PATTERN = r"move ([0-9]*) from ([0-9]*) to ([0-9]*)"
# follows an arithmetic sequence
# e.g., converts 1, 5, 9 to 1, 2, 3
def stack_index_to_stack_number(stack_index: int) -> int:
    return (stack_index + 3) // DISTANCE_BETWEEN_CRATES

def main():

    # import data
    crate_data = read_data("day_5/data/data.txt")
    start_time = time.time()

    # 1. initiate variables and data structures
    blank_line_index = crate_data.index('')
    number_of_stacks = int(crate_data[blank_line_index - 1][-2])
    initial_height_of_stacks = blank_line_index - 1
    # initiate empty list of stacks
    stack_list = []
    # create empty stacks
    for _ in range(0, number_of_stacks):
        stack_list.append(deque())

    # 2. populate stacks with crates
    for row_index in range(0, initial_height_of_stacks, 1):
        
        for stack_index in range(1, len(crate_data[row_index]), DISTANCE_BETWEEN_CRATES):
            
            #print(f"Reading stack {stack_index_to_stack_number(stack_index)} at row {row_index}")
            crate = crate_data[row_index][stack_index]
            stack_to_add_crate_to = stack_index_to_stack_number(stack_index)-1

            if crate != ' ':
                # print(f"Appending '{crate}' to stack_list {stack_to_add_crate_to}")
                stack_list[stack_to_add_crate_to].appendleft(crate)
            #else:
            #    print(f"Not appending this: '{crate}'")
            #    pass

    #print(stack_list)

    # 3. carry out instructions / move crates
    for instruction in crate_data[blank_line_index+1:]:

        result = re.search(SEARCH_PATTERN, instruction)
        move_count = int(result.group(1))
        from_stack = int(result.group(2))
        to_stack = int(result.group(3))
        # pop x times and append x times
        
        temp_stack = deque()
        for _ in range(0, move_count):
            
            # for part 1:
            #stack_list[to_stack-1].append(stack_list[from_stack-1].pop())
            temp_stack.append(stack_list[from_stack-1].pop()) # for part 2
        
        # append temp stack - for part 2
        for _ in range(0, len(temp_stack)): # for part 2
            stack_list[to_stack-1].append(temp_stack.pop()) # for part 2
    #print("Final stacks:")
    print(stack_list)
    #print()

    # 4. pop from each list to get message
    message = ""
    for stack in stack_list:
        message = message + stack.pop()
    print(f"Message is: {message}")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()