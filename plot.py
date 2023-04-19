import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('data.txt', delimiter=',')
plt.scatter(data[:, 0], data[:, 1])
plt.show()

