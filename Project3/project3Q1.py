import numpy.random as rand
import matplotlib.pyplot as plt
import numpy as np

N = 2000000
x = rand.uniform(0,1,N)
n = rand.normal(0,1,N)
y = 3*x + n

yshown = y[0:1000]
xshown = x[0:1000]
nshown = n[0:1000]

plt.scatter(xshown, yshown, color='r', label='y')
plt.show()
