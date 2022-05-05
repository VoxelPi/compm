import numpy as np
from scipy.integrate import tplquad

def f(x, y, z):
    return 21 * (x + y + z)

x = np.linspace(-1, 1, 200)
print(f"tplquad: {tplquad(f, 0, 1, lambda x : x**2, lambda x : x, lambda x, y : x-y, lambda x, y : x+y)[0]}") # should be 5.