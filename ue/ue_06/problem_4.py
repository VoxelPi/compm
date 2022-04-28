import matplotlib.pyplot as plt
import numpy as np

n = 11
x = np.triu(np.arange(1, n+1)*np.ones(n).reshape(n, 1)).flatten()
x = x[x != 0] - 1

plt.figure()
plt.hist(x, n, density=0.1)
plt.show()