import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,20)
y = np.linspace(-2, 1,30)
xx, yy = np.meshgrid(x, y)

def F(x, y):
    return np.where(x > 0, np.array([1 - y, 1 + x]), np.array([-1 + y, -1 - x]))

plt.figure()
plt.xlabel("x")
plt.ylabel("y")
plt.quiver(x, y, F(xx, yy)[0], F(xx, yy)[1], scale=80, label="F(x,y)")
plt.legend()
plt.show()