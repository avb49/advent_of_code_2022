from utils import *
from day3_part1 import get_item_priority

ASCII_OFFSET_UPPERCASE = -38
ASCII_OFFSET_LOWERCASE = -96

def main():
    # import data
    rucksacks_data = read_data("day_3/data/data.txt")

    priority_sum = 0
    # step through rucksacks in steps of three
    for rucksack_index in range(0, len(rucksacks_data), 3):
        # 1. identify the three rucksacks
        rucksack_1, rucksack_2, rucksack_3 = rucksacks_data[rucksack_index], rucksacks_data[rucksack_index + 1], rucksacks_data[rucksack_index + 2]
        # 2. get intersection of the three rucksacks
        badge_in_rucksacks = get_intersection_of_three_items(rucksack_1, rucksack_2, rucksack_3)
        # 3. translate character into a value using ASCII values with an offset applied
        value = get_item_priority(badge_in_rucksacks.pop())

        priority_sum += value
    
    print(priority_sum)

if __name__ == "__main__":
    main()