import numpy as np
from scipy.integrate import simpson, trapezoid

def f(x):
    return np.sqrt(1 - x**2)

x = np.linspace(-1, 1, 200)
trapezoid_pi = 2 * trapezoid(f(x), x)
print(f"trapezoid_pi: {trapezoid_pi}")
simpson_pi = 2 * simpson(f(x), x)
print(f"simpson_pi: {simpson_pi}")