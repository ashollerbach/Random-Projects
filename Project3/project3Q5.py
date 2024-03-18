import numpy.random as rand
import matplotlib.pyplot as plt
import numpy as np

N = 2000000
x = rand.uniform(0,1,N)
n = rand.normal(0,1,N)

y = 3*x + n

hist_x, bin_xedges = np.histogram(x, bins=50)
hist_y, bin_yedges = np.histogram(y, bins=50)

X, Y = np.meshgrid(bin_xedges[:-1], bin_yedges[:-1])

joint = hist_x[:, np.newaxis] * hist_y[np.newaxis, :]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, joint)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
