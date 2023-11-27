import re
from helper.fetchInput import get_input


input_string = open("day8/day22_test.txt").read()
input_string = get_input(22)


def parse_input(input_string):

    vector_input = input_string.strip().split("\n")

    vector_input = [re.split(r"[\s]*[(,)]*[xyz]*=", x) for x in vector_input]
    operations = []
    cells = []
    for x in vector_input:
        if x[0] == "on":
            operations.append(1)
        elif x[0] == "off":
            operations.append(-1)
        else:
            Exception


        cells_x = []
        skip = False
        for y in range(3):
            lower, upper = re.findall(r"[-]*\d+", x[y+1])
            cells_x.append([int(lower), int(upper)])

            #skip = True if (abs(int(lower)) > 50) or (abs(int(upper)) > 50) or skip else False

        if not skip:
            cells.append(cells_x)

    return zip(operations, cells)





def create_cube(status, min_x, max_x, min_y, max_y, min_z, max_z):
    range_x = [min_x, max_x]
    range_y = [min_y, max_y]
    range_z = [min_z, max_z]

    return (status, [range_x, range_y, range_z])


def find_intersection(cube_1, cube_2):

    if (max(cube_1[1][0]) < min(cube_2[1][0])) or (max(cube_2[1][0]) < min(cube_1[1][0])):
        return None
    if (max(cube_1[1][1]) < min(cube_2[1][1])) or (max(cube_2[1][1]) < min(cube_1[1][1])):
        return None
    if (max(cube_1[1][2]) < min(cube_2[1][2])) or (max(cube_2[1][2]) < min(cube_1[1][2])):
        return None

    if cube_1[0] == cube_2[0]:
        # if current_entry and already_present both ON then status needs to be off
        # if current_entry OFF And already_present 2 OFF then ON
        status = - cube_1[0]
    elif cube_1[0] == 1:
        # if current_entry ON and already_present OFF then OFF
        status = 1
    else:
        # if current_entry OFF and already_present ON then ON
        status = -1

    # define the intersecting cube
    min_x = max(min(cube_1[1][0]), min(cube_2[1][0]))
    max_x = min(max(cube_1[1][0]), max(cube_2[1][0]))

    min_y = max(min(cube_1[1][1]), min(cube_2[1][1]))
    max_y = min(max(cube_1[1][1]), max(cube_2[1][1]))

    min_z = max(min(cube_1[1][2]), min(cube_2[1][2]))
    max_z = min(max(cube_1[1][2]), max(cube_2[1][2]))

    return create_cube(status, min_x, max_x, min_y, max_y, min_z, max_z)


def get_volume(cube):
    return (cube[1][0][1] - cube[1][0][0] + 1) * (cube[1][1][1] - cube[1][1][0] + 1) * (cube[1][2][1] - cube[1][2][0] + 1)


instructions = list(parse_input(input_string))

# test
# min_example=[
#     create_cube(1,5,9,5,9,0,0),
#     create_cube(-1,4,6,4,6,0,0),
#     create_cube(1,1,4,9,12,0,0),
#     create_cube(1,4,4,4,4,0,0),
#     create_cube(1,8,11,8,11,0,0),
#      create_cube(-1,1,5,6,6,0,0)]


output_cubes = []
i = 0
for instruction in instructions:
    print("Doing step", i)
    i += 1
    intersections = []
    for cube in output_cubes:
        intersection = find_intersection(instruction, cube)
        if intersection is not None:
            intersections.append(intersection)

    for intersection in intersections:
        output_cubes.append(intersection)

    if instruction[0] == 1:
        output_cubes.append(instruction)



result = 0
for cube in output_cubes:
    result += cube[0] * get_volume(cube)

print(result)










