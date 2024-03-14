import numpy as np

trials = 50 #50 trials
coin_flips = np.random.randint(0, 2, trials) #create an array of 50 flips
heads_count = np.sum(coin_flips == 1) #count the flips where the coin == 1
prob = heads_count/trials #find the relative frequency of heads
print(prob)