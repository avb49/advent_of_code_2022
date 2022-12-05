import time
from utils import *

def convert_shorthand_to_list_of_sections(sections_shorthand: str) -> list:
    
    dash_index = sections_shorthand.index('-')
    first_number, second_number = int(sections_shorthand[:dash_index]), int(sections_shorthand[dash_index+1:])

    return list(range(first_number, second_number + 1))

def main():
    # import data
    cleaning_sections_data = read_data("day_4/data/data.txt")

    start_time = time.time()
    
    overlaps = 0
    for pair_section_assignment in cleaning_sections_data:

        # 1. split string into 2 using split(,) using comma as delimiter
        elf_1_sections, elf_2_sections = pair_section_assignment.split(',')
        
        # 2. convert each assignment (e.g., 2-4) into a list of numbers, [2,3,4]
        elf_1_sections, elf_2_sections = convert_shorthand_to_list_of_sections(elf_1_sections), convert_shorthand_to_list_of_sections(elf_2_sections)

        # 3. identify overlap of two lists, e.g., [2,3,4] and [6,7,8] (using intersection method)
        intersection = get_intersection_of_two_items(elf_1_sections, elf_2_sections)
        
        # 4. check for overlaps
        
        # part 1 - uncomment below for part 1 
        #if intersection == set(elf_1_sections) or intersection == set(elf_2_sections):
        #    overlaps += 1
        
        # part 2 - comment out below for part 2
        if len(intersection) != 0:
            overlaps +=1

    print(overlaps)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()