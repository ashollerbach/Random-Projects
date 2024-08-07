import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dataset = pd.read_csv('Project_5_data.csv')
# initialize input and output
X = dataset['X data'].values
Y = dataset['Y data'].values

x_mean = np.mean(X)
y_mean = np.mean(Y)
n = len(X)


Sxy = 0
Sxx = 0
for i in range(n):
  Sxy += (X[i] - x_mean) * (Y[i] - y_mean)
  Sxx += (X[i] - x_mean) ** 2

b1 = Sxy / Sxx
b0 = y_mean - b1 * x_mean
b0 = round(b0, 2)
b1 = round(b1, 2)
print("b0: ", b0)
print("b1: ", b1)


A = np.linspace(min(X), max(X), 100)

B = b0 + b1 * A

plt.figure(figsize=(12, 6))
plt.scatter(X, Y)
plt.plot(A, B, color='red')
plt.title("Slope " + str(b1) + " Intercept " + str(b0))
plt.show()

slope, intercept, r, p, std_err = stats.linregress(X, Y)
slope = round(slope, 2)
intercept = round(intercept, 2)

A = np.linspace(min(X), max(X), 100)
B = slope * A + intercept

print("Intercept: ", intercept)
print("Slope: ", slope)

plt.figure(figsize=(12, 6))
plt.scatter(X, Y, color='green')
plt.plot(A, B, color='orange')
plt.title("Slope " + str(slope) + " Intercept " + str(intercept))
plt.show()

