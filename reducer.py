#!/usr/bin/env python
"""reducer.py"""

__authors__ = "Emmanouil Dellatolas and Panagiotis Alexios Spanakis"

import sys
import math

THRESHOLD = 0.0001


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Define the three cluster centers
with open("centers.txt", "r") as f:
    centers = [tuple(map(float, line.strip().split(","))) for line in f]

center_sums = {}
center_counts = {}
for line in sys.stdin:
    # Parse the input line into the closest center and the point
    center_x, center_y, x, y = map(float, line.strip().split("\t"))
    # Add the point to the sum and count for its center
    if (center_x, center_y) in center_sums:
        center_sums[(center_x, center_y)][0] += x
        center_sums[(center_x, center_y)][1] += y
        center_counts[(center_x, center_y)] += 1
    else:
        center_sums[(center_x, center_y)] = [x, y]
        center_counts[(center_x, center_y)] = 1

new_centers = []
# Compute the new centers by taking the average of the points for each cluster
for center, sum_xy in center_sums.items():
    count = center_counts[center]
    new_center_x = sum_xy[0] / count
    new_center_y = sum_xy[1] / count
    print(f"{new_center_x},{new_center_y}")
    new_centers.append((new_center_x, new_center_y))

# Check if the new centers are the same as the old ones

converged = True
for center1, center2 in zip(centers, new_centers):
    if euclidean_distance(center1, center2) > THRESHOLD:
        converged = False

if converged:
    print("Converged")  # Converged
else:
    print("Not")  # Not converged
