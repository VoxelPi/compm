import matplotlib.pyplot as plt
import numpy as np

n = 10
x = np.triu(np.arange(1, n+1)*np.ones(n).reshape(n, 1)).flatten()
x = x[x != 0] - 1

plt.figure()
plt.hist(x, np.arange(0, n+1), density=0.1)
plt.show()