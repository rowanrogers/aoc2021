import numpy as np
import networkx as nx
from helper.fetchInput import get_input

day_input = get_input(15).strip().split("\n")

#day_input = ["1163751742","1381373672","2136511328","3694931569","7463417111", "1319128137","1359912421","3125421639","1293138521","2311944581"]
day_input = [list(map(int,x)) for x in day_input]
day_input = np.array(day_input)

#part 2 repeat by 5 in both directions adding each time
expanded_input = day_input

def add_one(input_array):
    new_input = input_array + 1

    with np.nditer(new_input, op_flags=['readwrite']) as it:
        for x in it:
            x[...] = x if x <= 9 else 1
    return new_input

def create_large_array(input_array):
    expanded_input = [input_array]
    for _ in range(4):
        input_array = add_one(input_array)
        expanded_input.append(input_array)

    wide_input = np.column_stack((expanded_input))

    expanded_input = [wide_input]

    for _ in range(4):
        wide_input = add_one(wide_input)
        expanded_input.append(wide_input)

    final_input = np.row_stack((expanded_input))

    return(final_input)


new_input = create_large_array(day_input)

day_input = new_input

my_graph = nx.DiGraph()
for i in range(day_input.shape[0]):
    for j in range(day_input.shape[1]):

        to_node = "r" + str(i) + "_c" + str(j)

        if i < day_input.shape[0]-1:
            my_graph.add_edge("r" + str(i+1) + "_c" + str(j), to_node, weight=day_input[(i, j)])
        if j < day_input.shape[1]-1:
            my_graph.add_edge("r" + str(i) + "_c" + str(j+1), to_node, weight=day_input[(i, j)])
        if j > 0:
            my_graph.add_edge("r" + str(i) + "_c" + str(j-1), to_node, weight=day_input[(i, j)])
        if i > 0:
            my_graph.add_edge("r" + str(i-1) + "_c" + str(j), to_node, weight=day_input[(i, j)])

x, y = day_input.shape

target = "r"+str(x-1)+"_c"+str(y-1)
print(nx.shortest_path_length(my_graph, source="r0_c0", target=target, weight="weight"))


