from helper.fetchInput import get_input
from collections import defaultdict, Counter

day_input = get_input(14)

starting_code, pair_insertions = day_input.strip().split("\n\n")

pair_insertions = [pair.split(" -> ") for pair in pair_insertions.split("\n")]

insert_dict = defaultdict(list)
for pair in pair_insertions:
    insert_dict[pair[0]] = pair[1]

total_counter = Counter(starting_code)

pair_counter = Counter()

for i in range(len(starting_code)-1):
    pair_counter[starting_code[i]+starting_code[i+1]] += 1

for _ in range(40):
    step_counter = Counter()
    for pair, count in pair_counter.items():
        # work out the new character to be added
        new_char = insert_dict.get(pair[0]+pair[1])
        #add the two new pairs of characters
        step_counter[pair[0]+new_char] += count
        step_counter[new_char + pair[1]] += count
        # add the new letter to the total counters
        total_counter[new_char] += count
    # replace the pair counter with the step counter (as all pairs get replaced every timestep
    pair_counter = step_counter


char_count = total_counter.most_common()

print(char_count[0][1] - char_count[-1][1])
