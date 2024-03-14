import numpy as np

trials = 100000
count = 0

for x in range(trials):
  
  die1 = np.random.randint(1, 6)
  die2 = np.random.randint(1, 6)
  
  sum = die1 + die2
  
  if sum > 7:
    count += 1

print(count/trials)