import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

def sum_of_RVs (n, num_samples, type):
  
  sum = 0
  if(type == "uniform"):
    for i in range(n):
      x = rand.uniform(0,1,num_samples)
      sum += x
  elif(type == "exponential"):
    for i in range(n):
      x = rand.exponential(1, num_samples)
      sum += x
  plt.hist(sum, bins=100, density=True)
  plt.show()

sum_of_RVs(2, 10000, "uniform")
sum_of_RVs(5, 10000, "uniform")
sum_of_RVs(50, 10000, "uniform")
sum_of_RVs(2, 10000, "exponential")
sum_of_RVs(5, 10000, "exponential")
sum_of_RVs(50, 10000, "exponential")