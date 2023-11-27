import math
import numpy as np
from itertools import combinations
from copy import deepcopy
from helper.fetchInput import get_input


def rotations():
    """Generate all possible rotation functions"""
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(np.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = np.cross(vi, vj)
                yield lambda x: np.matmul(x, np.array([vi, vj, vk]))


def parse_input(string):
    test_input_chr = [x.split("\n") for x in string.strip().split("\n\n")]

    scanners = [np.array([list(map(int, y.split(","))) for y in x if y[1] != "-"]) for x in test_input_chr]

    return scanners


# set first beacon of first scanner to be the origin
# calculate positions of all other scanners relative to that scanner

# for each scanner, we can calculate the distance between every pair of beacons it detects. I.e. if it detects 10 beacons
# Then we can detect 55 pairs of distances.
# Therefore, if we have another scanner that detects the same 10 beacons then it will share 55 distance lengths
# For every element in parsed input we need to calcualte the distances between every set of points.


def fit(scanners, hashes, i, j, v):
    """Function to calculate the correct orientation of scanner j relative to scanner i"""
    s1, s2 = scanners[i], scanners[j]
    p = hashes[i][v][0]  # this is the distance between the current pair of beacons that we are looking at for scanner i.
    for rot in rotations():
        # calculate the translated s2
        s2t = rot(s2)
        for q in hashes[j][v]:  # this contains 2 points which we loop over which is just the 2 beacons whose distances match what we're looking for
            diff = s1[p, :] - s2t[q, :]
            if len((b := set(map(tuple, s2t + diff))) & set(map(tuple,s1))) >= 12:
                return diff, b, rot




def map_hash(scanner):
    """
    Generate a hashset of sorted absolute coordinate differences
    between pairs of beacons of a scanner
    """
    s = {
        tuple(sorted(map(abs, scanner[i, :] - scanner[j, :]))): (i, j)
        for i, j in combinations(range(len(scanner)), 2)
    }
    return s


def match(hashes):
    """
    Function to match scanners to the hash maps of distances
    """
    for i, j in combinations(range(len(hashes)), 2):
        overlaps = len(m := set(hashes[i]) & set(hashes[j]))
        if overlaps >= math.comb(12, 2):
            yield i, j, next(iter(m))



def solve(scanners):
    new_scanners = deepcopy(scanners)
    hashes = list(map(map_hash, new_scanners))
    # initial set of beacons are all the beacons scanned by the first scanner
    beacons = set(map(tuple, new_scanners[0]))
    positions = {0: (0, 0, 0)}  # this is the initial scanner (scanner 0) and its position relative to itself.. i.e. 0,0,0
    # all other scanners in 'positions' are added relative to scanner 0
    while len(positions) < len(new_scanners):
        for i, j, v in match(hashes):
            # if we make it here then i and j share at least 12 beacons

            if not (i in positions) ^ (j in positions):
                # if both i and j are in positions or neither, then skip.
                # Neither is because we don't know their positions relative to scanner 0
                # both is because they've already been done
                continue
            elif j in positions:
                # if j is already in then swap i and j as we need know js position relative to scanner 0
                i, j = j, i

            # we then return position j relative to scanner 0, along with the rotation that gets us there.
            # We also return the new_beacons
            positions[j], new_beacons, rot = fit(new_scanners, hashes, i, j, v)
            # replace scanner j with its beacon positions relative to 0
            new_scanners[j] = rot(new_scanners[j]) + positions[j]
            # add the new beacons to our set
            beacons |= new_beacons

    return [positions[i] for i in range(len(new_scanners))], beacons



test_input = open("day8/day19_test.txt").read()
day_input = get_input(19)
parsed_input = parse_input(day_input)
positions, beacons = solve(parsed_input)

part1 = len(beacons)
part2 = max(sum(abs(positions[i] - positions[j])) for i, j in combinations(range(len(positions)), 2))

print(part1)
print(part2)
