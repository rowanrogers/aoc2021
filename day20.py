import numpy as np
from itertools import product
from helper.fetchInput import get_input




def parse_input(raw_input):
    split_input = raw_input.split("\n\n")
    image_enhancement_algo = split_input[0]

    image_raw = split_input[1].strip().split("\n")
    image_np = [[0 if x == "." else 1 for x in y] for y in image_raw]
    image_np = np.array(image_np)

    return image_enhancement_algo, image_np


class Image:

    def __init__(self, initial_image):
        self.image = initial_image

    def pad(self, n, typo=0):
        nrow, ncol = self.image.shape

        if typo == 0:
            big_array = np.zeros((nrow + 2*n, ncol + 2*n))
        else:
            big_array = np.ones((nrow + 2 * n, ncol + 2 * n))

        big_array[n:n+nrow, n:n+ncol] = self.image

        self.image = big_array

    def enhance(self, algo):
        nrow, ncol = self.image.shape

        new_image = np.zeros((nrow,ncol))

        for i, j in product(range(1, nrow-1), repeat=2):
            sub_image = self.image[i-1:i+2, j-1:j+2]
            bin_lookup = "".join(sub_image.flatten().astype(int).astype(str))
            bin_lookup = int(bin_lookup, 2)
            new_image[i, j] = 0 if algo[bin_lookup] == "." else 1

        self.image = new_image[1:-1,1:-1]



day_input = open("day8/day20_test.txt").read()
day_input = get_input(20)
image_enhancement_algo, image_np = parse_input(day_input)

x = Image(image_np)
x.pad(2, typo=0)
x.enhance(algo=image_enhancement_algo)
x.pad(2, typo=1)
x.enhance(algo=image_enhancement_algo)

np.sum(x.image)

x = Image(image_np)
for i in range(50):
    x.pad(2, typo=i%2)
    x.enhance(algo=image_enhancement_algo)

np.sum(x.image)

