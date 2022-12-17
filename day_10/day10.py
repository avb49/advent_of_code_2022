import time
import re

from utils import *
from day_10.crt import CRT

ADDITION_COMMAND_PATTERN = r"addx (\D*\d*)"

def main():

    start_time = time.time()

    # 1. import data
    command_data = read_data("day_10/data/data.txt")

    # 2. create CRT (cathode ray tube) object
    crt_device = CRT()

    # loop through each command in the data
    for command in command_data:

        # use regex to get command
        command_found = re.search(ADDITION_COMMAND_PATTERN, command)

        # if command not found, it is a no-operation (noop)
        if command_found is None:
            crt_device.cycle()

        # else it is a 'addx' operation
        else:
            crt_device.cycle()
            crt_device.cycle()
            to_add_to_register = int(command_found.group(1))
            crt_device.update_register(to_add_to_register)

    # answer to part 1
    print(sum([x for x in crt_device.signal_strength_list]))

    # answer to part 2 (saved to txt file in data folder)
    final_crt_screen = crt_device.screen.reshape(crt_device.screen_size) # re-shape as 2d array
    np.savetxt('day_10/data/output.txt', final_crt_screen, delimiter='  ', fmt='%s')

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()