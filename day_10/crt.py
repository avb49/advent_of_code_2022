import numpy as np

# for part 1 - cycles to check for signal strength
CYCLES_TO_CHECK = [20, 60, 100, 140, 180, 220]

class CRT:

    def __init__(self):

        # size of CRT screen
        self.screen_size = (6, 40)
        # screen is a numpy array (later it is reshaped to be 2d)
        self.screen = np.asarray((["."] * (self.screen_size[0] * self.screen_size[1])))
        # starting sprite position (indeces on CRT screen)
        self.sprite_position = [0,1,2]
        # register starts at 1 as per instructions
        self.register_value = 1
        # cycle starts at 0
        self.current_cycle = 0
        # list used for Part 1 - to collect signals strengths
        self.signal_strength_list = []

    def cycle(self):
        """Completes 1 cycle. Completes signal strength check if required
        and draws on the CRT."""

        self.current_cycle += 1

        """Part 1 - Checks if current cycle is a signal strength test.
        If yes, appends the signal strength to the list"""

        if self.current_cycle in CYCLES_TO_CHECK:
            signal_strength = self.current_cycle * self.register_value
            self.signal_strength_list.append(signal_strength)

        """Part 2 - Draw pixel on CRT if sprite is in overlapping position"""
        
        # move sprite position down a row if at end of row on crt screen
        if (self.current_cycle % self.screen_size[1]) == 1 and self.current_cycle != 1:
            self.sprite_position = [x + self.screen_size[1] for x in self.sprite_position]
        
        # draw on CRT
        if (self.current_cycle - 1) in self.sprite_position:
            self.screen[self.current_cycle - 1] = "#"

    def update_register(self, to_add: int) -> None:
        """Updates value of register and the sprite position"""
        
        self.register_value += to_add
        # update sprite position
        self.sprite_position = [x + to_add for x in self.sprite_position]