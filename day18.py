import re
import math
import functools
from helper.fetchInput import get_input


EXPLODE = re.compile(r"\[(\d+),(\d+)\]")
SPLIT = re.compile(r"\d{2}")


def apply_reduction(x):

    while True:
        for match in re.finditer(EXPLODE, x):

            before = x[:match.start()]
            depth = sum((c == "[") - (c == "]") for c in before)
            after = x[match.end():]

            if depth > 3:
                # after the match we explode that pair
                exploding_numbers = re.findall(r"\d+", match.group())

                # find the last number before the match
                number_matches_lhs = [m for m in re.finditer(r'\d+', before)]
                if len(number_matches_lhs) > 0:
                    new_number_lhs = int(before[number_matches_lhs[-1].start():number_matches_lhs[-1].end()]) + int(exploding_numbers[0])
                    before = before[:number_matches_lhs[-1].start()] + str(new_number_lhs) + before[
                                                                                             number_matches_lhs[-1].end():]

                # find the first number after the match
                number_matches_rhs = [m for m in re.finditer(r'\d+', after)]
                if len(number_matches_rhs) > 0:
                    new_number_rhs = int(after[number_matches_rhs[0].start():number_matches_rhs[0].end()]) + int(exploding_numbers[1])

                    after = after[:number_matches_rhs[0].start()] + str(new_number_rhs) + after[number_matches_rhs[0].end():]

                # add the components together
                x = before + str(0) + after
                break

        else:
            if not (match := re.search(SPLIT, x)):
                break

            number_to_split = int(x[match.start():match.end()])
            replacement = "[" + str(math.floor(number_to_split / 2)) + "," + str(math.ceil(number_to_split / 2)) + "]"

            x = x[:match.start()] + replacement + x[match.end():]

    return x


def apply_addition(x, y):

    new_string = "[" + x + "," + y + "]"

    return apply_reduction(new_string)


def calc_mag_i(i, x):
    if x[i + 1].isdigit():
        lhs = int(x[i+1])
        i += 2
    else:
        i, lhs = calc_mag_i(i + 1, x)

    if x[i + 1].isdigit():
        rhs = int(x[i+1])
        i += 2
    else:
        i, rhs = calc_mag_i(i + 1, x)

    return i + 1, 3 * lhs + 2 * rhs


def calculate_magnitude(x):
    i, magnitude = calc_mag_i(0, x)

    return magnitude

day_input = get_input(18).strip().split("\n")

x = functools.reduce(lambda x,y: apply_addition(x,y), day_input)

print(calculate_magnitude(x))

max(calculate_magnitude(apply_addition(x, y))
    for i, x in enumerate(day_input)
    for j, y in enumerate(day_input)
    if i != j)




