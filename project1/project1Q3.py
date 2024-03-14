import numpy as np

lowest = 1
highest = 0
trials = 100000
for x in range(10):
  coin_flips = np.random.randint(0, 2, trials)
  heads_count = np.sum(coin_flips == 1)
  prob = heads_count/trials
  if(prob < lowest):
    lowest = prob
  if(prob > highest):
    highest = prob

variation = highest - lowest
formatted_decimal = "{:.4f}".format(variation)  # 4 decimal places
print("Difference between highest and lowest found: ", formatted_decimal)
