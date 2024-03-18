import numpy.random as rand
import matplotlib.pyplot as plt
import numpy as np

N = 2000000
x = rand.uniform(0,1,N)
n = rand.normal(0,1,N)

y = 3*x + n

hist, xedges, yedges = np.histogram2d(x, y, bins=(50,50))

X, Y = np.meshgrid(xedges[:-1], yedges[:-1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, hist.T)
plt.show()