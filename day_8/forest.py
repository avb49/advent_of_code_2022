from utils import *

class Forest:

    def __init__(self, data_path: str):
        
        # stores the forest as a 2d numpy array
        self.forest = read_matrix_as_2d_np_array(data_path)
        
        # keeps track of how many trees are visible in the map
        self.trees_visible_counter = 0

        # keeps track of most scenic tree in forest
        self.most_scenic_tree = None

        self.height = self.forest.shape[0]
        self.width = self.forest.shape[1]

        # create list of Tree objects
        self.inner_trees = []
        for column_index in range(1, self.width - 1):
            for row_index in range(1, self.height - 1):
                self.inner_trees.append(Tree(row_index, column_index, self))

class Tree:

    def __init__(self, row: int, column: int, forest: Forest):
        self.row = row
        self.column = column
        self.height = forest.forest[row][column]
        self.forest = forest
        self.scenic_score = self.get_total_scenic_score()

    def __repr__(self):
        return str(self.height)

    
    """Methods which calculate viewing distance"""

    def get_total_scenic_score(self) -> int:
        return (self.viewing_distance_north() * self.viewing_distance_east() *
            self.viewing_distance_south() * self.viewing_distance_west())

    def viewing_distance_north(self) -> int:
        """Calculates viewing distance looking North of the tree"""
        viewing_distance = 1
        for north_index in range(self.row - 1, 0, -1):
            if self.forest.forest[north_index][self.column] < self.height:
                viewing_distance += 1
            else:
                break
        return viewing_distance

    def viewing_distance_south(self) -> int:
        """Calculates viewing distance looking South of the tree"""
        viewing_distance = 1
        for south_index in range(self.row + 1, self.forest.height - 1):
            if self.forest.forest[south_index][self.column] < self.height:
                viewing_distance += 1
            else:
                break
        return viewing_distance

    def viewing_distance_east(self) -> int:
        """Calculates viewing distance looking East of the tree"""
        viewing_distance = 1
        for east_index in range(self.column + 1, self.forest.width - 1):
            if self.forest.forest[self.row][east_index] < self.height:
                viewing_distance += 1
            else:
                break
        return viewing_distance

    def viewing_distance_west(self) -> int:
        """Calculates viewing distance looking West of the tree"""
        viewing_distance = 1
        for west_index in range(self.column - 1, 0, -1):
            if self.forest.forest[self.row][west_index] < self.height:
                viewing_distance += 1
            else:
                break
        return viewing_distance

    
    """ Methods which check visibility of tree"""

    def is_visible_from_north(self) -> bool:
        """Checks if given tree is visible from North (top)
        Returns True if visible, False if not visible"""
        for north_index in range(0, self.row):
            if self.forest.forest[north_index][self.column] >= self.height:
                return False
        return True

    def is_visible_from_south(self) -> bool:
        """Checks if given tree is visible from South (bottom)
        Returns True if visible, False if not visible"""
        for south_index in range(self.row + 1, self.forest.height):
            if self.forest.forest[south_index][self.column] >= self.height:
                return False
        return True

    def is_visible_from_east(self) -> bool:
        """Checks if given tree is visible from East (right)
        Returns True if visible, False if not visible"""
        for east_index in range(self.column + 1, self.forest.width):
            if self.forest.forest[self.row][east_index] >= self.height:
                return False
        return True

    def is_visible_from_west(self) -> bool:
        """Checks if given tree is visible from West (left)
        Returns True if visible, False if not visible"""
        for west_index in range(0, self.column):
            if self.forest.forest[self.row][west_index] >= self.height:
                return False
        return True