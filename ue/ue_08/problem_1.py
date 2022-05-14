import numpy as np
from numpy.polynomial.polynomial import Polynomial

def vandermond_integration(x, y, int_start, int_end):
    # Compute vector a
    vandermonde_inv = np.linalg.inv(np.vander(x, increasing=True))
    a_coeff = vandermonde_inv @ y

    # Generate the matrix that integrates polynomials.
    integral_matrix = np.vstack([np.zeros(x.size), np.diag(1 / np.arange(1, x.size+1))])

    # Integrate the polynomial a
    a_int_coeff = integral_matrix@a_coeff
    a_int = Polynomial(a_int_coeff)

    return a_int(int_end) - a_int(int_start)

# Define vector x
x1 = np.array([-1, -0.5, 0.5, 1])
x2 = np.array([-0.2, -0.1, 0.1, 0.2])
x3 = np.array([-np.sqrt(3/7 + 2/7 * np.sqrt(6/5)), -np.sqrt(3/7 - 2/7 * np.sqrt(6/5)), np.sqrt(3/7 - 2/7 * np.sqrt(6/5)), np.sqrt(3/7 + 2/7 * np.sqrt(6/5))])

print(f"Interpolated integral with x1 is: {vandermond_integration(x1, np.exp(x1), -1, 1)}")
print(f"Interpolated integral with x2 is: {vandermond_integration(x2, np.exp(x2), -1, 1)}")
print(f"Interpolated integral with x3 is: {vandermond_integration(x3, np.exp(x3), -1, 1)}")
print(f"integral should be {np.e - 1/np.e}")