import numpy as np
from helper.fetchInput import get_input


day_input = get_input(7)

day_input = list(map(int, day_input.split(",")))

input_median = np.median(day_input)

fuel_vector = [abs(x - input_median) for x in day_input]

sum(fuel_vector)

# Part 2

# create distance calculation


def distance_calc(a, b):
    dist = sum(range(abs(a - b) + 1))
    return dist


# set median to int so we can iterate.
median_int = int(input_median)

# calculate initial position
fuel_vector = []

fuel_usage = sum([distance_calc(a, median_int) for a in day_input])

# start with test = median
test_val = median_int

#initial difference to start loop... bit lazy
diff = 1

while diff > 0:
    fuel_vector.append(fuel_usage)
    test_val = test_val + 1
    fuel_usage = sum([distance_calc(a, test_val) for a in day_input])
    diff = fuel_vector[-1] - fuel_usage

print(fuel_vector[-1])








