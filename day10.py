from helper.fetchInput import get_input
import functools


day_input = get_input(10).strip().split("\n")


pairs = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

error_chars = []
incomplete_input = []
positions_not_closed = []
for string in day_input:

    positions_not_closed.append([])
    incomplete_input.append(string)
    for x in string:

        # if character is opening char then move to next
        if x in pairs.keys():
            positions_not_closed[-1].append(x)

            next
        elif x == pairs.get(positions_not_closed[-1][-1]):
            # character closes previous bracket so remove that from positions_not_closed
            positions_not_closed[-1].pop()

            next

        else:
            # the next character is an error so we just return
            error_chars.append(x)
            incomplete_input.pop()
            positions_not_closed.pop()
            break

scoring = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

sum([scoring.get(error) for error in error_chars])

# part 2

pairs_2 = {
    "{": 3,
    "(": 1,
    "[": 2,
    "<": 4
}

scores_2 = []
for unclosed_brackets in positions_not_closed:

    closing_brackets = list(reversed([pairs_2.get(x) for x in unclosed_brackets]))
    closing_brackets.insert(0,0)

    scores_2.append(functools.reduce(lambda a, b: a * 5 + b, closing_brackets))

len(scores_2)

scores_2.sort()

scores_2[22]