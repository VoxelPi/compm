import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_axes([0.11, 0.11, 0.35, 0.8])
plt.xlabel("x")
plt.xticks([0, 1, 2])
plt.ylabel("y = x²")
plt.title("first plot")
ax2 = fig.add_axes([ 0.6, 0.11, 0.35, 0.8])
plt.xlabel("x")
plt.xticks([0, 1, 2])
plt.ylabel("y = x")
plt.title("second plot")

x = np.linspace(0, 2)
ax1.plot(x, x**2, color="r", label="x²")
ax1.legend()
ax2.plot(x, x, color="b", label="x")
ax2.legend()
plt.show()