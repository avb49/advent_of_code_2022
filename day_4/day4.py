from utils import *

def convert_shorthand_to_list_of_sections(sections_shorthand: str) -> list:

    dash_index = sections_shorthand.index('-')
    first_number, second_number = sections_shorthand[:dash_index], sections_shorthand[dash_index+1:]
    numbers_to_add = int(second_number) - int(first_number)
    
    numbers_list = [int(first_number), int(second_number)]

    to_add = int(first_number) + 1
    for _ in range(0, numbers_to_add - 1):
        numbers_list.append(to_add)
        to_add += 1
    
    return numbers_list

def main():
    # import data
    cleaning_sections_data = read_data("day_4/data/data.txt")
    overlaps = 0

    for pair_section_assignment in cleaning_sections_data:

        # 1. split string into 2 using split(,) using comma as delimiter
        elf_1_sections, elf_2_sections = pair_section_assignment.split(',')
        
        # 2. convert each assignment (e.g., 2-4) into a number (234)
        elf_1_sections, elf_2_sections = convert_shorthand_to_list_of_sections(elf_1_sections), convert_shorthand_to_list_of_sections(elf_2_sections)
        
        # 3. identify overlap of two numbers, e.g., 234 and 678 (using intersection method)
        intersection = get_intersection_of_two_items(elf_1_sections, elf_2_sections)
        
        # 4. check for overlaps
        
        # part 1 - uncomment below for part 1 
        #if intersection == set(elf_1_sections) or intersection == set(elf_2_sections):
        #    overlaps += 1
        
        # part 2 - comment out below for part 2
        if len(intersection) != 0:
            overlaps +=1

    print(overlaps)

if __name__ == "__main__":
    main()