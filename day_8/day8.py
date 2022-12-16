import numpy as np
import time

from utils import *
from day_8.forest import *

def main():

    start_time = time.time()
    
    # 1. create Forest object containing forest as 2d array
    forest = Forest("day_8/data/data.txt")

    # 2. count edge trees - they are all visible
    edge_trees_count = 2 * (forest.width + forest.height) - 4
    forest.trees_visible_counter += edge_trees_count

    # 3. iterate through each inner (non-edge) tree and check if it is visible
    for tree in forest.inner_trees:
        
        # 4. count number of visible trees
        if tree.is_visible_from_north():
            forest.trees_visible_counter += 1
            continue
        if tree.is_visible_from_east():
            forest.trees_visible_counter += 1
            continue
        if tree.is_visible_from_south():
            forest.trees_visible_counter += 1
            continue
        if tree.is_visible_from_west():
            forest.trees_visible_counter += 1
            continue

    # 4. iterate through each inner (non-edge) tree and find the most scenic tree
    forest.most_scenic_tree = max(forest.inner_trees, key=lambda tree: tree.scenic_score)

    print(f"Part 1: A total of {forest.trees_visible_counter} trees are visible")
    print(f"""Part 2: The most scenic tree has a scenic score of: {forest.most_scenic_tree.scenic_score}
    It is located at {forest.most_scenic_tree.row}, {forest.most_scenic_tree.column} 
    It has a height of {forest.most_scenic_tree.height}""")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()