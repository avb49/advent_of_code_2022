import time
import re

from utils import *

class Directory:

    def __init__(self, name, size, parent_dir):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir

# finds name of directory (1 group)
COMMAND_SEARCH_PATTERN = r"cd (.*)"

# finds size and name of file (two groups)
FILE_SEARCH_PATTERN = r"([0-9]*) (.*)"

# finds name of a directory
DIR_SEARCH_PATTERN = r"dir (.*)"

MAX_DIRECTORY_SIZE = 100000
TOTAL_DISK_SPACE = 70000000
DISK_SPACE_NEEDED_FOR_UPDATE = 30000000

# Part 1 - returns the total size of directories smaller than max. directory size
def get_sum_of_directories_within_requirements(directories: list) -> int:

    directories_within_requirements = []
    for dir in directories:

        if dir.size <= MAX_DIRECTORY_SIZE:
            directories_within_requirements.append(dir)
        
    total_size = 0
    for dir in directories_within_requirements:
        total_size += dir.size
    
    return total_size

# Part 2 - returns the smallest directory size, which, upon deletion allows for installing the update
def get_best_directory_to_delete(directories: list, root_directory: Directory) -> int:

    unused_space = TOTAL_DISK_SPACE - root_directory.size
    to_be_deleted = DISK_SPACE_NEEDED_FOR_UPDATE - unused_space
    directory_size = DISK_SPACE_NEEDED_FOR_UPDATE

    for dir in directories:
        if (dir.size < directory_size) & (dir.size >= to_be_deleted):
            directory_size = dir.size
    
    return directory_size

def main():

    # import data
    filesystem_data = read_data("day_7/data/data.txt")

    start_time = time.time()
    root_directory = Directory("/", 0, None)
    current_dir = root_directory 

    directories = []

    for line_index in range(0, len(filesystem_data)):

        if "$ cd .." == filesystem_data[line_index]:
            current_dir = current_dir.parent_dir

        elif "$ cd" in filesystem_data[line_index]:
            # create new Directory object and add to list of directories
            directory_name = re.search(COMMAND_SEARCH_PATTERN, filesystem_data[line_index]).group(1)
            directory = Directory(directory_name, 0, current_dir)
            directories.append(directory)
            current_dir = directory

        elif filesystem_data[line_index][0] != "$":

            # match line to file regex search pattern
            file_match_object = re.search(FILE_SEARCH_PATTERN, filesystem_data[line_index])

            # if there is a match, then it is a file
            if file_match_object.group(1) != '':
                # get file size
                file_size = file_match_object.group(1)
                # add file size to current directory and all its parents
                to_update = current_dir
                while(to_update is not None):
                    to_update.size += int(file_size)
                    to_update = to_update.parent_dir

    # part 1 answer
    print(get_sum_of_directories_within_requirements(directories))
    # part 2 answer
    print(get_best_directory_to_delete(directories, root_directory))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()