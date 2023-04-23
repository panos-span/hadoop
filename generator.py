import numpy as np

__authors__ = "Emmanouil Dellatolas and Panagiotis Alexios Spanakis"

# Define the three cluster centers
with open("centers.txt", "r") as f:
    centers = np.array([tuple(map(float, line.strip().split(","))) for line in f])
# Define the number of points per cluster
n_points = 350000

# Define the standard deviation of the distance from the centers
std = 1

# Define the degree of skewness
skew = 0.1

# Set the random seed for reproducibility
np.random.seed(42)

# Generate the points around the centers with skewness
points = []
for center in centers:
    cluster_points = np.random.normal(0, std, size=(n_points, 2))
    cluster_points[:, 0] += center[0] + skew * np.random.normal(size=n_points)
    cluster_points[:, 1] += center[1] + skew * np.random.normal(size=n_points)
    points.append(cluster_points)

points = np.concatenate(points)

# Save the points to a text file
np.savetxt('data.txt', points, delimiter=',')
