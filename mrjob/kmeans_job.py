from mrjob.job import MRJob
import math

__authors__ = "Emmanouil Dellatolas and Panagiotis Alexios Spanakis"

class KMeans(MRJob):

    def configure_args(self):
        super(KMeans, self).configure_args()
        self.add_passthru_arg("--centers", type=str)

    def load_centers(self):
        self.centers = []
        for center in self.options.centers.split('|'):
            x, y = center.split(',')
            self.centers.append((float(x), float(y)))

        # with open(self.options.centers, 'r') as f:
        #    for line in f:
        #        x, y = line.strip().split(',')
        #        self.centers.append((float(x), float(y)))

    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def mapper_init(self):
        # Load the centers if they haven't been loaded yet
        if not hasattr(self, 'centers'):
            self.load_centers()

    def mapper(self, _, line):
        # Parse the data point from the input line
        x, y = map(float, line.strip().split(','))

        # Find the closest center to the data point
        closest_center = None
        closest_distance = float('inf')
        for center in self.centers:
            distance = self.euclidean_distance((x, y), center)
            if distance < closest_distance:
                closest_center = center
                closest_distance = distance

        # Output the closest center and the data point
        yield closest_center, (x, y)

    def reducer(self, center, points):
        # Compute the new center for the list of data points
        num_points = 0
        sum_x = 0
        sum_y = 0
        for point in points:
            num_points += 1
            sum_x += point[0]
            sum_y += point[1]
        new_center = (sum_x / num_points, sum_y / num_points)

        # Output the new center
        yield center, new_center
