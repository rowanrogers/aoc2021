
# three moves
# from a room to hallway
# from a hallway to room
# from a room to destination room

# test input
test_input = open("day8/day23_test.txt"). read().strip().split("\n")

input_state = [[x for x in y if x.isalpha()] for y in test_input[2:4]]

formatted_input_state = [[None, ] * 11]
formatted_input_state.extend(list(a) for a in zip(*input_state))

# define the target state

target_state = [[None, ] * 11, ['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]

# define which amphipod wnats to get to which room. Room is numeric
target_rooms = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# room_to_hall, i.e. leaving room 1 takes you to hallway position 2
room_to_hall = {1: 2, 2: 4, 3: 6, 4: 8}

# energy costs
energy_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def get_possible_moves(state):

    # possible moves for amphipods in rooms
    for i in range(1, 5):
        # iterate each room, check if a boi exists
        if state[i][0] is not None:
            # top spot occupied
            top_loc = 0
        elif state[i][1] is not None:
            # bottom spot occupied
            top_loc = 1
        else:
            # room empty
            continue

        amphipod_type = state[i][top_loc]

        # check if the amphipod in the right room AND the one below it is
        if target_rooms[amphipod_type] == i and all(amphipod_type == x for x in state[i][top_loc:]):
            #no action required as boiz are in position
            continue

        # Amphipods not inposition so we need to start some movements
        # the original position is now empty
        state[i][top_loc] = []

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
            if state[0][j] is not None:
                # if any room is filled then cannot move. Break
                break
            if j not in [2, 4, 6, 8]:
                possible_locs.append(j)

        for loc in possible_locs:
# sort data structure for new states
            new_state = list(map(tuple, state))

            # update where j has moved to
            new_state[0][loc] = j

            # top_loc adds a step if in the bottom room, 1 is the step out of the room, the rest is steps down the hall
            steps = 1 + abs(room_to_hall[i] - loc) + top_loc

            energy = energy_costs[amphipod_type] * steps
            yield tuple(new_state), energy


y = get_possible_moves(formatted_input_state)
for move in y:
    print(move)
