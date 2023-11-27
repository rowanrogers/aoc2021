import collections
import itertools


def play_turn(roll, player_pos, player_score):
    player_rolls = roll
    player_pos += player_rolls
    player_pos = (player_pos - 1) % 10 + 1

    player_score += player_pos

    return player_pos, player_score


possible_rolls = itertools.product((1,2,3), repeat=3)
roll_freq = collections.Counter(list(map(sum, list(possible_rolls))))


def play_quantum_round(p1_pos, p2_pos, p1_score=0, p2_score=0):

    if p2_score >= 21:
        return 0, 1

    total_1, total_2 = 0,0
    for r in roll_freq:
        p1_pos_new, p1_score_new = play_turn(r, p1_pos, p1_score)

        new_wins_2, new_wins_1 = play_quantum_round(p2_pos, p1_pos_new, p2_score, p1_score_new)

        total_1, total_2 = total_1 + new_wins_1 * roll_freq[r], total_2 + new_wins_2 * roll_freq[r]

    return total_1, total_2




player_1, player_2 = play_quantum_round(1, 2)

max(player_1,player_2)




