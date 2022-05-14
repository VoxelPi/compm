import numpy as np
import matplotlib.pyplot as plt

a = -np.pi
b = np.pi
n = 201

x = np.linspace(a, b, n)
h = (b - a) / (n - 1) # Calculate h

fx = np.sin(x**2)
fx1 = fx[1::]

forward_diff = ((np.hstack([fx[1:], np.zeros(1)]) - fx) / h)[:-1]
backward_diff = ((fx - np.hstack([np.zeros(1), fx[:-1]])) / h)[1:]
central_diff = ((np.hstack([fx[1:], np.zeros(1)]) - np.hstack([np.zeros(1), fx[:-1]])) / (2*h))[1:-1]

plt.figure()
plt.plot(x, fx)
plt.plot(x[:-1], forward_diff)
plt.plot(x[1:], backward_diff)
plt.plot(x[1:-1], central_diff)
plt.show()