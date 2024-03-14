import numpy as np
import matplotlib.pyplot as plt

trials = 2000000

dist = np.random.random(trials)

plt.hist(dist, bins=10, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(True)
plt.show()
