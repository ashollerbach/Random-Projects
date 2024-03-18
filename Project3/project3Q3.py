import numpy.random as rand
import matplotlib.pyplot as plt
import numpy as np

N = 2000000
x = rand.uniform(0,1,N)
n = rand.normal(0,1,N)

y = 3*x + n

fig, ax = plt.subplots()

plt.hist2d(x, y, bins=(50,50))
plt.show()