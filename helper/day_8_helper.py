from collections import Counter


# function to find numbers directly based on lambda expression
def find_number_direct(input_list, condition):
    y = next(x for x in input_list if condition(x))
    return y

# function to find lights directly based on occurence counts
def find_light_direct(input_list, count):
    full_string = "".join(input_list)
    letter_count = Counter(full_string)
    return list(letter_count.keys())[list(letter_count.values()).index(count)]


def create_number_dictionary(input_list):

    # define how to find initial numbers
    number_find_dict = {
        "1": (lambda i: len(i) == 2),
        "4": (lambda i: len(i) == 4),
        "7": (lambda i: len(i) == 3),
        "8": (lambda i: len(i) == 7)
    }

    # define how many occurences of each light occur
    light_dict = {
        "b": 6,
        "e": 4,
        "f": 9
    }

    # create initial number mapping from known lengths
    number_dict = {}
    for (number, lambdas) in number_find_dict.items():
        number_dict[number] = find_number_direct(input_list, lambdas)

    # create initial dictionary from known counts
    letter_dict = {}
    for (base_letter, count) in light_dict.items():
        letter_dict[base_letter] = find_light_direct(input_list, count)

    # add the mapping of light c
    letter_dict["c"] = next(x for x in number_dict["1"] if x not in letter_dict.values())

    # find number 2
    number_dict["2"] = next(x for x in input_list if letter_dict["f"] not in x)

    # find number 3
    number_dict["3"] = next(x for x in input_list if (len(x) == 5) & all(letter_dict[y] not in x for y in ["b", "e"]))

    # find number 0
    number_dict["0"] = next(
        x for x in input_list if (len(x) == 6) & all(letter_dict[y] in x for y in ["b", "c", "e", "f"]))

    number_dict["5"] = next(x for x in input_list if (len(x) == 5) & (x not in number_dict.values()))

    number_dict["6"] = next(
        x for x in input_list if all(letter_dict[y] in x for y in ["b", "e", "f"]) & (x not in number_dict.values()))

    number_dict["9"] = next(x for x in input_list if x not in number_dict.values())

    return number_dict

