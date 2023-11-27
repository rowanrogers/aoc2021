
from helper.fetchInput import get_input

# read in txt file
day_input = get_input(1)

day_input_vector = [int(x) for x in day_input.split("\n") if len(x) > 1]

print(day_input_vector)

def calcInc(input_array):
    x = [j-i for i, j in zip(input_array[:-1], input_array[1:])]

    return len([i for i in x if i > 0])

print(calcInc(day_input_vector))

# part 2
rollingSums = []

for i in range(len(day_input_vector) - 2):
    y = sum([day_input_vector[i], day_input_vector[i + 1], day_input_vector[i + 2]])
    rollingSums.append(y)

print(len(rollingSums))
print(calcInc(rollingSums))




