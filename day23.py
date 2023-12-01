from functools import cache


# three moves
# from a room to hallway
# from a hallway to room
# from a room to destination room

# test input
test_input = open("inputs/day23_test.txt"). read().strip().split("\n")

input_state = [[x for x in y if x.isalpha()] for y in test_input[2:6]]

hallway = ((None, ) * 11)
rooms = ((a, b, c, d) for a, b, c, d in zip(*input_state))
formatted_input_state = (hallway, *rooms)


# define the target state

target_state = ((None, ) * 11, ('A', 'A', 'A', 'A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'))

# define which amphipod wnats to get to which room. Room is numeric
target_rooms = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# room_to_hall, i.e. leaving room 1 takes you to hallway position 2
room_to_hall = {1: 2, 2: 4, 3: 6, 4: 8}

# energy costs
energy_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def get_room_moves(state):
    # possible moves for amphipods in rooms
    for i in range(1, 5):
        current_state = list(map(list, state))
        # iterate each room, check if a boi exists
        if current_state[i][0] is not None:
            # top spot occupied
            top_loc = 0
        elif current_state[i][1] is not None:
            # 1 spot occupied
            top_loc = 1
        elif current_state[i][2] is not None:
            # bottom spot occupied
            top_loc = 2
        elif current_state[i][3] is not None:
        # bottom spot occupied
            top_loc = 3
        else:
            # room empty
            continue

        amphipod_type = current_state[i][top_loc]

        # check if the amphipod in the right room AND the one below it is
        if target_rooms[amphipod_type] == i and all(amphipod_type == x for x in current_state[i][top_loc:]):
            #no action required as boiz are in position
            continue

        # Amphipods not inposition so we need to start some movements
        # the original position is now empty
        current_state[i][top_loc] = None

        # Find the spaces it can move to
        possible_locs = []

        for j in range(room_to_hall[i]):
            # start by adding rooms from the left
            if j not in [2, 4, 6, 8]:
                possible_locs.append(j)
            if state[0][j] is not None:
                # if any square is blocked the remove all previous entries
                possible_locs.clear()

        for j in range(room_to_hall[i], 11):
            if current_state[0][j] is not None:
                # if any room is filled then cannot move. Break
                break
            if j not in [2, 4, 6, 8]:
                possible_locs.append(j)

        for loc in possible_locs:
        # sort data structure for new states
            new_state = list(map(list, current_state))
            # update where j has moved to
            new_state[0][loc] = amphipod_type

            # top_loc adds a step if in the bottom room, 1 is the step out of the room, the rest is steps down the hall
            steps = 1 + abs(room_to_hall[i] - loc) + top_loc

            energy = energy_costs[amphipod_type] * steps
            yield tuple(map(tuple, new_state)), energy


def get_hall_moves(state):
    # for a hall move, it can only move to its room. and only if its empty or contains its mate

    current_state = list(map(list, state))

    for i in range(len(current_state[0])):
        # if state empty then skip
        if current_state[0][i] is None:
            continue

        new_state = list(map(list, state))

        # get current type
        amphipod_type = current_state[0][i]

        # find target room
        target_room = target_rooms[amphipod_type]

        # check if the pathway blocked
        if i < room_to_hall[target_room]:
            hall_locations = slice(i+1, room_to_hall[target_room]+1)
        else:
            hall_locations = slice(room_to_hall[target_room], i)

        blocked = False
        for loc in state[0][hall_locations]:
            if loc is not None:
                blocked = True

        if blocked:
            continue
        # can move if target room is empty
        elif all(y is None for y in current_state[target_room]):
            top_loc = 3
        # can move if the bottom space is a mate and the rest empty
        elif all(current_state[target_room][n] == amphipod_type for n in range(3, 4)) & \
                all(current_state[target_room][n] is None for n in range(0, 3)):
            top_loc = 2

        elif all(current_state[target_room][n] == amphipod_type for n in range(2, 4)) & \
                all(current_state[target_room][n] is None for n in range(0, 2)):
            top_loc = 1

        # or can move if the target room contains its buddy
        elif all(current_state[target_room][n] == amphipod_type for n in range(1, 4)):
            top_loc = 0

        else:
            continue

        # empty the current position
        new_state[0][i] = None
            # fill the new positions
        new_state[target_room][top_loc] = amphipod_type

        # 2 is the step into the room plus the step to the bottom position
        steps = 1 + top_loc + abs(room_to_hall[target_room] - i)
        energy = energy_costs[amphipod_type] * steps

        yield tuple(map(tuple, new_state)), energy


def get_possible_moves(state):
    for poss_state, energy in get_room_moves(state):
        yield poss_state, energy
    for poss_state_2, energy in get_hall_moves(state):
        yield poss_state_2, energy


@cache
def solve(starting_state):
    if starting_state == target_state:
        return 0

    possible_costs = []

    for new_state, new_energy in get_possible_moves(starting_state):
        possible_costs.append(new_energy + solve(new_state))

    return min(possible_costs, default=float('inf'))


print(solve(formatted_input_state))


# # test a state one move from completion
# target_state = ((None, ) * 11, ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))
# starting_state = list(map(list, target_state))
# starting_state[0][0] = 'A'
# starting_state[0][1] = 'B'
# starting_state[1][0] = None
# starting_state[2][0] = None
# starting_state = tuple(map(tuple, starting_state))
# z = get_possible_moves(formatted_input_state)
#
# test_state = (('B', None, None, 'D', None, 'B', None, 'D', None, 'A', None), (None, 'A'), (None, None), ('C', 'C'), (None, None))
# j = get_possible_moves(test_state)