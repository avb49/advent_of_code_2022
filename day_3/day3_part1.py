from utils import *

ASCII_OFFSET_UPPERCASE = -38
ASCII_OFFSET_LOWERCASE = -96

def get_item_priority(item: str):
    if item.islower():
        return ord(item) + ASCII_OFFSET_LOWERCASE
    else:
        return ord(item) + ASCII_OFFSET_UPPERCASE

def main():
    # import data
    rucksacks_data = read_data("day_3/data/data.txt")

    priority_sum = 0
    for rucksack in rucksacks_data:
        # 1. split string into 2 parts (the two rucksack compartments)
        compartment_1, compartment_2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        # 2. check for intersection to find the single character in both (write method)
        item_in_both_compartments = get_intersection_of_two_strings(compartment_1, compartment_2)
        # 3. translate character into a value using a list with indeces representing value
        value = get_item_priority(item_in_both_compartments.pop())

        priority_sum += value
    
    print(priority_sum)

if __name__ == "__main__":
    main()