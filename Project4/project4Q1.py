import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


###################################
# n: number of distributions to sum
# num_samples: number of samples in each distribution
# type: type of each distribution
#
# generates a sum of n distributions of type "type" of sample size num_samples
###################################
def sum_of_RVs (n, num_samples, type):
  
  sum = 0
  match type: #match statement makes this easy to expand for more distributions
    
    #generate n uniform distributions and add them together
    case "uniform":
      for i in range(n):
        x = rand.uniform(0,100,num_samples)
        sum += x
        
    #generate n exponenetial distributions and add them
    case "exponential":
      for i in range(n):
        x = rand.exponential(7,num_samples)
        sum += x
  
  #plot the distributions
  plt.hist(sum, bins=100, density=True)
  plt.show()


#call function multiple times

sum_of_RVs(2000, 100000, "exponential")