import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

x = np.linspace(0, 2*np.pi)

plt.figure()
plt.plot(x, -np.cos(x) + 1, label="$\int{sin(x)}$", linestyle="--", linewidth=2)
plt.plot(x, cumulative_trapezoid(np.sin(x), x, initial=0), label="cumulative_trapezoidal")
plt.legend()
plt.show()