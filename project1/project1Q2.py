import numpy as np

lowest = 1 #the highest value found 
trials = 50 # number of trials per run
for x in range(10): # 10 runs
  coin_flips = np.random.randint(0, 2, trials) # create an array of trails amount of flips
  heads_count = np.sum(coin_flips == 1) # sum the heads
  prob = heads_count/trials
  if(prob < lowest): # update probability if highest is larger
    lowest = prob 
print(lowest)