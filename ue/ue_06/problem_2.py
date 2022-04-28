import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2)

plt.subplots(2, 2, sharex = True)

plt.subplot(2, 2, 1)
plt.ylabel("y")
plt.xlabel("x")
plt.yticks([1, 0, -1])
plt.plot(x, np.sin(4*x), color="red", label="sin(4x)")
plt.legend(loc = "center right")

plt.subplot(2, 2, 2)
plt.xlabel("x")
plt.yticks([0.5, 0, -0.5])
plt.plot(x, np.cos(x)*np.sin(x), color="green", label="cos(x)sin(x)")
plt.legend(loc = "center")

plt.subplot(2, 2, 3)
plt.ylabel("y")
plt.xlabel("x")
plt.xticks([-2, 0, 2])
plt.yticks([0, 10])
plt.plot(x, x**4, color="blue", label="x^4")
plt.legend(loc = "upper center")

plt.subplot(2, 2, 4)
plt.xlabel("x")
plt.yticks([1, 0, -1])
plt.plot(x, np.cos(x)+np.sin(x), color="black", label="cos(x)+sin(x)")
plt.legend(loc = "lower right")

plt.show()