from collections import Counter
from helper.fetchInput import get_input
from itertools import repeat
import numpy as np


day_input = get_input(6)

day_input = list(map(int, day_input.split(",")))

z = Counter(day_input)

t_mat = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.float64)


def calc_t_mat(n, t_mat):

    output = t_mat

    for i in range(n-1):
        output = np.matmul(output, t_mat)

    return output


def calc_start_vector(input_data):

    start_vector = list(repeat(0, 9))

    for key, value in Counter(input_data).items():
        start_vector[int(key)] = value

    return start_vector


t_mat_pow = calc_t_mat(256, t_mat)
print(t_mat_pow)
start_vector = np.array(calc_start_vector(day_input), dtype=np.float64)
print(start_vector)

print(np.sum(np.matmul(t_mat_pow, start_vector), dtype=np.float64))





