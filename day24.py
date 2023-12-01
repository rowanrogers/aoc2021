
from helper.fetchInput import get_input
lines = get_input(24).strip()
lines = lines.split("\n")

def parse_operation(line, sub_id, current_inputs={}):
    split_line = line.strip().split(" ")

    if split_line[0] == "inp":
        current_inputs[split_line[1]] = int(next(sub_id))
        return current_inputs

    input_1 = current_inputs[split_line[1]]

    try:
        input_2 = int(split_line[2])
    except ValueError:
        input_2 = current_inputs[split_line[2]]

    if split_line[0] == "add":
        current_inputs[split_line[1]] = input_1 + input_2
    elif split_line[0] == "mul":
        current_inputs[split_line[1]] = input_1 * input_2
    elif split_line[0] == "div":
        current_inputs[split_line[1]] = input_1 // input_2
    elif split_line[0] == "mod":
        current_inputs[split_line[1]] = input_1 % input_2
    elif split_line[0] == "eql":
        current_inputs[split_line[1]] = 1 if input_1 == input_2 else 0
    return current_inputs

def solve(lines):
    current_inputs = {"w":0, "x":0, "y":0, "z":0}
    sub_id_num = 99999999999999
    # find largest number with success
    completed = False
    while not completed:
        sub_id = iter(x for x in str(sub_id_num))

        # skip if any zeros
        if any(x == "0" for x in str(sub_id_num)):
            continue

        # otherwise solve
        for line in lines:
            current_inputs = parse_operation(line, sub_id, current_inputs=current_inputs)

        # if z is 0 then we win
        if current_inputs["z"] == 0:
            break

        sub_id_num -= 1

    return sub_id_num

print(solve(lines))


