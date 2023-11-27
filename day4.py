
import numpy as np

from helper.fetchInput import get_input


day_input = get_input(4)

#day_input = open("test4.txt", "r").read()

new_input = day_input.split("\n\n")

def parse_draw(string_input):
    nums = string_input[0]

    nums = list(map(int, nums.split(",")))
    return nums


def parse_boards(string_input):
    boards = string_input[1:]

    split_board = [[y for y in x.split("\n") if y] for x in boards]

    double_split = np.array([[list(map(int, y.split())) for y in x if len(x) > 0] for x in split_board])

    return double_split

def play_bingo(draws, boards, find_winner=True):
    completion_boards = [np.ones((5,5)) for board in boards]
    list_of_winners = []
    already_won = []
    for current_draw in draws:

        locations = [np.where(board == current_draw) for board in boards]

        # take the turn
        for i in range(len(completion_boards)):
            completion_boards[i][locations[i][0], locations[i][1]] = 0

            # check success
            sum_totals = \
                np.sum(completion_boards[i], axis=0).tolist() +\
                np.sum(completion_boards[i], axis=1).tolist() #+\

            if any(x == 0 for x in sum_totals) & (i not in already_won):
                #game finished, so return the sum of un-crossed numbers
                if find_winner:
                    unmarked = np.multiply(completion_boards[i], boards[i])
                    total_sum = np.sum(unmarked)

                    return total_sum, current_draw
                else:
                    # for finding the loser we add that winning board to a longer list
                    list_of_winners.append(completion_boards[i])
                    already_won.append(i)

                    if len(list_of_winners) == len(completion_boards):
                        unmarked = np.multiply(list_of_winners[len(list_of_winners)-1], boards[i])
                        total_sum = np.sum(unmarked)

                        return total_sum, current_draw
    print("Shouldn't get here")


draws = parse_draw(new_input)
boards = parse_boards(new_input)

x = play_bingo(draws, boards)
print(x[0], x[1])
print(x[0] * x[1])

x = play_bingo(draws, boards, find_winner=False)
print(x[0], x[1])
print(x[0] * x[1])


