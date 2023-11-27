from day8.helper import create_number_dictionary
from helper.fetchInput import get_input

day_input = open("day8/test8.txt").read()
day_input = get_input(8)

formatted_input = []

for y in [x.split("|") for x in day_input.strip().split("\n")]:
    formatted_input.append([z.strip().split(" ") for z in y])

for i in range(len(formatted_input)):
    formatted_input[i][0] = ["".join(sorted(y)) for y in formatted_input[i][0]]
    formatted_input[i][1] = ["".join(sorted(y)) for y in formatted_input[i][1]]

# part 1
count_1478 = 0

for entry in formatted_input:
    count_1478 += sum([1 for x in entry[1] if len(x) in [2, 3, 4, 7]])

print(count_1478)

# part 2
running_total = 0

for coded_input in formatted_input:
    input_list = coded_input[0]

    output_mapping = create_number_dictionary(input_list)

    output_number = "".join([list(output_mapping.keys())[list(output_mapping.values()).index(x)] for x in coded_input[1]])

    running_total += int(output_number)

print(running_total)

