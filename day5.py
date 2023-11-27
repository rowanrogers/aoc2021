import re

from collections import Counter
from helper.fetchInput import get_input


# read in txt file
day_input = get_input(5)

#day_input = open("day5.txt").read()

day_input = list(filter(None, day_input.split("\n")))

def parse_input(string_input):

    split_input = [re.split("->", x) for x in day_input]
    formatted_input = [[[int(y) for y in re.split(",", x)] for x in z] for z in split_input]

    return formatted_input

def create_range(x, y):
    op = -1 if x > y else 1

    return range(x, y + op, op)

def part_one(formatted_input):
    total_counter = Counter()

    for x in formatted_input:
        start_point = x[0]
        end_point = x[1]

        x_range = create_range(start_point[0], end_point[0])
        y_range = create_range(start_point[1], end_point[1])

        if start_point[0] == end_point[0] or start_point[1] == end_point[1]:

            total_counter = total_counter + Counter([(a, b) for a in x_range for b in y_range])

        else:
            total_counter = total_counter + Counter(zip(x_range, y_range))

    x = [1 for k, v in total_counter.items() if v >= 2]

    return x.count(1)


formatted_input = parse_input(day_input)
output = part_one(formatted_input)

print(output)


