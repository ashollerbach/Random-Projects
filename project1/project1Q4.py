import numpy as np

trials = 100000# number of trials to be run
fourinarow = 0
successes = 0
for i in range(trials):
  coin = np.random.randint(0, 2, 4) # stores the value of the flip (1 for heads, 0 for tails)
  heads = np.sum(coin == 1)
  if(heads == 4):
    successes += 1
prob = successes/trials # the probability is the number of successes divided by the number of trials
print(prob) 