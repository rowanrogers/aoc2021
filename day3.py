# Day three code
import operator

from helper.fetchInput import get_input
from collections import Counter


day_input = get_input(3)

#print(day_input)

day_input_split = day_input.split("\n")

day_input_array = [x for x in day_input_split if len(x) > 0]

nchar = len(day_input_array[0])

outputCounter = [0 for x in day_input_array[0]]
oneVector = []
zeroVector = []

for char in range(len(day_input_array[0])):
    nextStepVector = day_input_array
    for x in nextStepVector:
        if x[char] == "1":
            outputCounter[char] += 1
        else:
            outputCounter[char] -= 1

gamma = int("".join([str(int(x > 0)) for x in outputCounter]), base=2)
epsilon = int("".join([str(int(x < 0)) for x in outputCounter]), base=2)

print(gamma * epsilon)

# Part 1 using zip and collections
zip_list = zip(*day_input_array)
"".join(Counter(column).most_common(1)[0][0] for column in zip_list)


# Part two



def checkVector(op):
    nextStepVector = day_input_array
    outputCounter = [0 for x in day_input_array[0]]

    for char in range(len(day_input_array[0])):

        zeroVector = []
        oneVector = []

        for x in nextStepVector:

            if x[char] == "1":
                outputCounter[char] += 1
                oneVector.append(x)
            else:
                outputCounter[char] -= 1
                zeroVector.append(x)

            if op(outputCounter[char], 0):
                nextStepVector = oneVector
            else:
                nextStepVector = zeroVector

        if len(nextStepVector) == 1:
            break
        print("For character ", char,
              " there are ", outputCounter[char],
              " more instances of 1s than 0s, and there are ",
              len(nextStepVector), " elements remaining.")
    return nextStepVector

oxGen = str(checkVector(operator.ge)[0])
print(oxGen)
co2Scrub = str(checkVector(operator.lt)[0])
print(co2Scrub)

print(int(oxGen, base=2) * int(co2Scrub, base=2))