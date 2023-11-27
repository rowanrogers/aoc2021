import re
import numpy as np
from helper.fetchInput import get_input
from matplotlib import pyplot as plt


day_input = open("day13test.txt").read()

day_input = get_input(13)
# separate points and folds
points, folds = day_input.strip().split("\n\n")

# format the points
points_formatted = [point.split(",") for point in points.split("\n")]
points_formatted = [[int(x), int(y)] for x, y in points_formatted]

# format the folds
folds_formatted = [[re.search("[x,y]", fold).group(), int(re.search("[0-9]+", fold).group())] for fold in folds.split("\n")]

for fold in folds_formatted:
    unique_points = []
    # 'i' is index of the points that will be affected
    i = 0 if fold[0] == "x" else 1
    axis = fold[1]

    for point in points_formatted:

        if point[i] > axis:
            point[i] = 2*axis - point[i]

        if point not in unique_points:
            unique_points.append(point)

    points_formatted = unique_points


plot_data = np.array(unique_points)

x, y = plot_data.T
plt.scatter(x, -y)
plt.show()


