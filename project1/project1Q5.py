import numpy as np

biaspassed = 0
trials = 1000 # number of trials to be run

for i in range(trials):
  
  # run a trial for the biased coin
  coin1 = np.random.choice(2, 100,  p=[.55, .45])
  headsbiased = np.sum(coin1 == 1)
  probbiased = headsbiased/100
  
  coin2 = np.random.randint(0, 2, 100)
  headsfair = np.sum(coin2 == 1)
  
  probfair = headsfair/100
  if(probbiased >= probfair):
    biaspassed += 1


print(biaspassed/trials)