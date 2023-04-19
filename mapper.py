#!/usr/bin/env python
"""mapper.py"""

__authors__ = "Emmanouil Dellatolas and Panagiotis Alexios Spanakis"

import sys
import math

# Define the three cluster centers
with open("centers.txt", "r") as f:
    centers = [tuple(map(float, line.strip().split(","))) for line in f]
# Map each data point to the closest center
for line in sys.stdin:
    x, y = map(float, line.strip().split(","))
    min_dist = math.inf
    closest_center = None
    for center in centers:
        dist = math.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
        if dist < min_dist:
            min_dist = dist
            closest_center = center

    # Emit the closest center and the point
    print(f"{closest_center[0]}\t{closest_center[1]}\t{x}\t{y}")
