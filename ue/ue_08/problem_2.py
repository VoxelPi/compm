import numpy as np
from scipy.integrate import fixed_quad

I_exact = np.log(3)
print(f"I_exact is {I_exact} (=ln(3))")

n = 1
while True:
    I_approx = fixed_quad(lambda x : 1/(1-x), -1/2, 1/2, n=n)[0]
    n += 1
    print(f"I_approx is {I_approx} with order of quadrature integration n={n}")
    if I_approx == I_exact:
        break