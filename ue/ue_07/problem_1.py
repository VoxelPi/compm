import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(1, 2, 1)
plt.xlim((0, 1))
plt.ylim((0, 1))
plt.scatter([0.5, 0.499], [0.5, 0.499])

plt.subplot(1, 2, 2)
plt.xlim((0.45, 0.55))
plt.ylim((0.45, 0.55))
plt.scatter([0.5, 0.499], [0.5, 0.499])
plt.show()

x = np.linspace(0, 1)
y = x**2
coords = np.array((x, y)).T
plt.figure()
plt.plot(x, y)
plt.plot(plt.gca().transData.transform(coords)[:, 0], plt.gca().transData.transform(coords)[:, 1])
plt.show()