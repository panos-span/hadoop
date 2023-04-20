import sys

from kmeans_job import KMeans

if __name__ == '__main__':

    centers = "-5,-5|-5,5|8,8"
    mr_job = KMeans(args=[sys.argv[1], "--centers=" + centers])

    # Run the job once to get the initial centers
    with mr_job.make_runner() as runner:
        runner.run()

    # Load the initial centers
    # with open('centers.txt', 'r') as f:
    #    centers = [tuple(map(float, line.strip().split(','))) for line in f]

    # Iterate until the centers have converged
    converged = False
    while not converged:
        # Write the current centers to a file
        # with open('current_centers', 'w') as f:
        #    for center in centers:
        #        f.write('{},{}\n'.format(center[0], center[1]))

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
            # print(centers)
            # print(new_centers)
            centers = new_centers

            # print(centers)

    # Write the final centers to a single file
    # with open('final_centers.txt', 'w') as f:
    #    for center in centers:
    #        f.write('{},{}\n'.format(center[0], center[1]))
