import numpy as np
import matplotlib.pyplot as plt

trials = 2000000

dist = np.random.rand(trials)

newdist = np.sqrt(-2*np.log(1-dist))

#swap the distrbution whether you want to use the regular dist. or the adjusted dist.
plt.hist(newdist, bins=100, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(True)
plt.show()
