import time
import re

from utils import *

class File:

    def __init__(self, name, size, dir):
        self.name = name
        self.size = size
        self.dir = dir

class Directory:

    def __init__(self, name, size, parent_dir, children=[]):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir
        self.children = children

# finds name of directory (1 group)
COMMAND_SEARCH_PATTERN = r"cd (.*)"

# finds size and name of file (two groups)
FILE_SEARCH_PATTERN = r"([0-9]*) (.*)"

# finds name of a directory
DIR_SEARCH_PATTERN = r"dir (.*)"

def main():

    # 1. import data
    filesystem_data = read_data("day_7/data/test_data.txt")

    start_time = time.time()

    root_dir = Directory("/", None, None, None)
    current_dir = root_dir

    # 2. read line and determine if command or directory/file
    for line_index in range(0, len(filesystem_data)):

        #TODO: handle when '..' is used - update current directory
        if "$ cd .." == filesystem_data[line_index]:
            current_dir = current_dir.parent_dir
            print(f"Going up a directory... From {current_dir.name} to {current_dir.parent_dir.name}")

        elif "$ cd" in filesystem_data[line_index]:
            # create new Directory object
            directory_name = re.search(COMMAND_SEARCH_PATTERN, filesystem_data[line_index]).group(1)
            directory = Directory(directory_name, None, current_dir, None)
            current_dir = directory
            print(f"cd'ing into new directory... Current directory: {current_dir.name}. Parent dir is {current_dir.parent_dir.name}")

        elif filesystem_data[line_index][0] != "$":

            # for the current_dir, add children
            file_match_object = re.search(FILE_SEARCH_PATTERN, filesystem_data[line_index])
            if file_match_object.group(1) == '':
                dir_match_object = re.search(DIR_SEARCH_PATTERN, filesystem_data[line_index])
                print(f"Directory discovered: {dir_match_object.group(1)}")

            else:
                file_size, file_name = file_match_object.group(1), file_match_object.group(2)
                print(f"File discovered with filename: {file_name} and file size: {file_size}")


        elif "$ ls" in filesystem_data[line_index]:
            pass
                

    # 3. construct file tree using commands and info:
    # - cd: add a node if doesnt exit, otherwise keep track of current node
    # - ls: add children nodes to nodes 

    #file1 = File(1000, "/")
    #directory1 = Directory(None, "/", [file1])
    #for file in directory1.children:
    #    print(file)

    print()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()