import sys

from kmeans_job import KMeans

__authors__ = "Emmanouil Dellatolas and Panagiotis Alexios Spanakis"

if __name__ == '__main__':

    centers = "-5,-5|-5,5|8,8"
    mr_job = KMeans(args=[sys.argv[1], "--centers=" + centers])

    # Run the job once to get the initial centers
    with mr_job.make_runner() as runner:
        runner.run()

    # Iterate until the centers have converged
    converged = False
    while not converged:

        # Run the job with the current centers
        mr_job = KMeans(args=[sys.argv[1], '--centers=' + centers])
        with mr_job.make_runner() as runner:
            runner.run()

            # Load the new centers from the reducer output
            new_centers = []
            for key, value in mr_job.parse_output(runner.cat_output()):
                new_centers.append(value)

            print(centers)
            print(new_centers)
            new_centers = "|".join([",".join([str(x) for x in center]) for center in new_centers])
            print(new_centers)
            # Check for convergence
            if centers == new_centers:
                converged = True
            centers = new_centers

