import re

from helper.fetchInput import get_input

# Read in txt file
day_input = get_input(2)

day_input_array = day_input.split("\n")
day_input_array = [x for x in day_input_array if len(x) > 0]

f = 0
aim = 0
depth = 0

for x in day_input_array:
    magnitude = int(re.findall("[0-9]+$", x)[0])
    direction = x[0]

    if direction == "f":
        f += magnitude
        depth += magnitude * aim
    elif direction == "d":
        aim += magnitude
    elif direction == "u":
        aim -= magnitude

print(f)
print(depth)
print(f*depth)



