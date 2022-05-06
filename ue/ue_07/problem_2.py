import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange

# Interpolate basis vector e1.
plt.figure()
x = np.linspace(0, 1, 5)
e1 = np.array([1, 0, 0, 0, 0])
x_fine = np.linspace(0, 1)
print(f"x = {x}")

poly = lagrange(x, e1)
coef1 = poly.coef[::-1] # reverse order of coefficients

plt.scatter(x, e1, color="red", label="points and values")
plt.plot(x_fine, Polynomial(coef1)(x_fine), label="Lagrange polynomial")
plt.legend()
plt.show()

# Interpolate five basis vectors e1, e2, e3, e4, e5.
e2 = np.array([0, 1, 0, 0, 0])
e3 = np.array([0, 0, 1, 0, 0])
e4 = np.array([0, 0, 0, 1, 0])
e5 = np.array([0, 0, 0, 0, 1])

coef2 = lagrange(x, e2).coef[::-1] # reverse order of coefficients
coef3 = lagrange(x, e3).coef[::-1] # reverse order of coefficients
coef4 = lagrange(x, e4).coef[::-1] # reverse order of coefficients
coef5 = lagrange(x, e5).coef[::-1] # reverse order of coefficients

plt.figure()
plt.plot(x_fine, Polynomial(coef1)(x_fine), label="Lagrange polynomial of e1")
plt.plot(x_fine, Polynomial(coef2)(x_fine), label="Lagrange polynomial of e2")
plt.plot(x_fine, Polynomial(coef3)(x_fine), label="Lagrange polynomial of e3")
plt.plot(x_fine, Polynomial(coef4)(x_fine), label="Lagrange polynomial of e4")
plt.plot(x_fine, Polynomial(coef5)(x_fine), label="Lagrange polynomial of e5")
plt.legend()
plt.show()

# Interpolate arbitrary data vector y
y = np.random.sample(5)*10-5
coef = lagrange(x, y).coef[::-1] # reverse order of coefficients

plt.figure()
plt.scatter(x, y, color="red", label="points and values")
plt.plot(x_fine, Polynomial(coef1)(x_fine)*y[0] + Polynomial(coef2)(x_fine)*y[1] + Polynomial(coef3)(x_fine)*y[2] + Polynomial(coef4)(x_fine)*y[3] + Polynomial(coef5)(x_fine)*y[4], label="Sum")
plt.plot(x_fine, Polynomial(coef)(x_fine), label="Lagrange polynomial", linestyle="--")
plt.legend()
plt.show()