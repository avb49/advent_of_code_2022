from utils import read_data

# Points I get for playing X (rock), Y (paper), or Z (scissors)
SHAPE_POINTS = {
    'X': 1, # points for playing rock
    'Y': 2, # points for playing paper
    'Z': 3  # points for playing scissors
}

# Part 1 of task - points I get for each of the 9 outcomes of the game
GAME_OUTCOMES = {
    # games lost
    'A Z': 0,
    'B X': 0,
    'C Y': 0,
    # games drawn
    'A X': 3,
    'B Y': 3,
    'C Z': 3,
    # games won
    'C X': 6,
    'A Y': 6,
    'B Z': 6
}

# moves to play to lose
LOSE_MOVE = {'A':'Z', 'B':'X','C':'Y'}
# moves to play to draw
DRAW_MOVE = {'A':'X','B':'Y','C':'Z'}
# moves to play to win
WIN_MOVE = { 'A':'Y','B':'Z','C':'X'}

ELF_MOVE_INDEX = 0
MY_MOVE_INDEX = 2

# Part 2 of challenge - translating win/draw/loss to a shape played for the given round
# Returns: round played with the second letter replaced by the shape required to be played
def translate_round_to_shapes_played(round: str) -> str:
    
    elf_move = round[ELF_MOVE_INDEX]
    # translate intended outcome of game to a move (X - loss, Y - draw, Z - win)
    if round[MY_MOVE_INDEX] == 'X':
        translated_round = elf_move + ' ' + LOSE_MOVE[elf_move]
    elif round[MY_MOVE_INDEX] == 'Y':
        translated_round = elf_move + ' ' + DRAW_MOVE[elf_move]
    elif round[MY_MOVE_INDEX] == 'Z':
        translated_round = elf_move + ' ' + WIN_MOVE[elf_move]
    
    return translated_round

def main():
    
    # 1. import data
    rounds_played = read_data("day_2/data/data.txt")

    # 2. for each round played, count points for the game
    total_points = 0
    for round in rounds_played:
        
        # COMMENT OUT BELOW FOR PART 1 - translate round to shapes played by both players
        round = translate_round_to_shapes_played(round)

        # points for shape played
        shape_points = SHAPE_POINTS[round[MY_MOVE_INDEX]]
        # points for outcome of game 
        outcome_points = GAME_OUTCOMES[round]
        # add both to running total
        total_points += shape_points + outcome_points

    print(total_points)

if __name__ == "__main__":
    main()