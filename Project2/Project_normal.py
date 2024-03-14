import numpy as np
import matplotlib.pyplot as plt

trials = 200
sigma = 0.1 
mu = 0

dist = np.random.normal(mu, sigma, trials)

# uncomment this for the shift
dist = dist * 3 + 4 
  

# Plot histogram with 30 bins
plt.hist(dist, bins=30,color = 'r', edgecolor='black', density=False)

# Plot the normal distribution curve
x = np.linspace(-0.5, 0.5, 1000)  # adjust the range as per your data
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Normal Distribution')
plt.grid(True)
plt.show()
