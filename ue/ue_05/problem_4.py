import numpy as np
import scipy.linalg as spla

def poweriteration(A, t, x_0):
    # Check if matrix is symmetric square matrix.
    (n, m) = A.shape
    assert(n == m)
    assert(np.all(A == A.T))

    x_k = x_0
    Ax_k = A@x_k # cache matrix vector product.
    lambda_k_1 = -1
    lambda_k = np.sum(x_k * Ax_k)
    
    while True:
        lambda_k_1 = lambda_k

        x_k = Ax_k / np.linalg.norm(Ax_k, 2)
        Ax_k = A@x_k
        lambda_k = np.sum(x_k * Ax_k)

        if np.linalg.norm(Ax_k - lambda_k*x_k, 2) <= t and np.abs(lambda_k_1 - lambda_k) <= (t if np.abs(lambda_k) <= t else t * np.abs(lambda_k)):
            break

    return (lambda_k, x_k)

# Test
n = 5
A = np.random.sample((n, n)) * 100
A = A + A.T
x = np.random.sample((n, 1)) * 100

print("\npoweriteration:")
print(poweriteration(A, 1e-6, x)[0])
print(poweriteration(A, 1e-6, x)[1])

print("scipy.linag.eig:")
print(spla.eig(A)[0])
print(spla.eig(A)[1])