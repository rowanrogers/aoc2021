from helper.fetchInput import get_input
import numpy as np
from itertools import product

day_input = get_input(11).strip().split("\n")

mini_input = np.array([list(map(int, list(x))) for x in day_input])

# test_input = ["5483143223","2745854711","5264556173","6141336146","6357385478","4167524645","2176841721","6882881134","4846848554","5283751526"]
# #
# mini_input = np.array([list(map(int, list(x))) for x in test_input])


def find_adjacent(*args):

    adjacent_cells = []

    for arg in args:
        x, y = arg
        x_pos = [x-1, x, x+1]
        valid_x_pos = [x for x in x_pos if x >= 0 and x <= 9]
        y_pos = [y-1, y, y+1]
        valid_y_pos = [y for y in y_pos if y >= 0 and y <= 9]

        adjacent_cells.extend(list(product(valid_x_pos, valid_y_pos)))

    return adjacent_cells


flash_count = 0
for i in range(400):
    # first add one
    mini_input += 1
    already_flashed = np.zeros([10,10])
    step_wise_count = 0
# do until no more flashes:
    while True:

        # if all cells greater than 10 have flashed then we quit
        if not np.any((mini_input >= 10) * np.logical_not(already_flashed)):
            break

        # firstly we work out which cells are flashing on this turn by looking at cells greater than 9 that haven't yet flashed
        flash_array = (mini_input >= 10) * np.logical_not(already_flashed)

        # next we count those flashes
        flash_count = flash_count + np.count_nonzero(flash_array)
        step_wise_count += np.count_nonzero(flash_array)
        # then we list those flashing cells
        rows, columns = np.where(flash_array == 1)
        flashing_cells = list(zip(rows, columns))

        # update our already flashed counter
        for location in flashing_cells:
            row, column = location
            already_flashed[row, column] = True

        # calculate all adjacent cells (including diagonals)
        affected_cells = find_adjacent(*flashing_cells)

        # for each adjacent cell, we add one.
        for location in affected_cells:
            row, column = location
            mini_input[row, column] += 1

    for location in list(zip(*np.where(mini_input > 9))):
        row, column = location
        mini_input[row, column] = 0

    if step_wise_count == 100:
        print(i + 1)
        break
    #repeat

print(flash_count)
# anything that flashed goes to zero

