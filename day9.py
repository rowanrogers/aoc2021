from helper.fetchInput import get_input
import numpy as np


day_input = get_input(9)

z = np.array([list(map(int, x)) for x in day_input.strip().split("\n")])

def get_adj(z, i, j):
    adjacents = []
    if i < 99:
        adjacents.append(z[i+1, j])
    if j < 99:
        adjacents.append(z[i, j+1])
    if j > 0:
        adjacents.append(z[i, j-1])
    if i > 0:
        adjacents.append(z[i-1, j])

    return adjacents

low_points_sum = 0
basins = []
for i in range(100):
    for j in range(100):

        base = z[i, j]

        adjacent_nums = get_adj(z, i, j)

        if all(base < adjacent_nums):
            basins.append([i,j])
            low_points_sum += base + 1

print(low_points_sum)


def valid_square(i,j):
    return all([i >= 0, j >= 0, i <= 99, j <= 99])


# part two, find the basins.
# We will start with our lowest points and move out from there
def find_next_square(z, i, j, searched_squares=[], search_counter=0):

    options = {
        "u": [i - 1, j],
        "r": [i, j + 1],
        "d": [i + 1, j],
        "l": [i, j - 1]
    }

    for direction in ["u", "r", "d", "l"]:
        next_cell = options[direction]
        if not valid_square(next_cell[0], next_cell[1]):
            next

        elif (z[next_cell[0], next_cell[1]] < 9) & (next_cell not in searched_squares):
            searched_squares.append(next_cell)
            return find_next_square(z, next_cell[0], next_cell[1], searched_squares, 0)

        else:
            next

    if search_counter < len(searched_squares):
        search_counter += 1

        next_square = searched_squares[-search_counter]

        return find_next_square(z, next_square[0], next_square[1], searched_squares, search_counter)
    else:
        return searched_squares

        # return searched_squares

    print("You shouldn't be here")


full_basins = []

for basin in basins:
    i = basin[0]
    j = basin[1]

    full_basins.append(find_next_square(z, i, j, searched_squares=[[i,j]], search_counter=0))


ordered_sizes = list(reversed(sorted([len(basin) for basin in full_basins])))

print(ordered_sizes[:3])


