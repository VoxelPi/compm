import numpy as np

def a(n):
    A = np.zeros((n - 2, n -2))
    A = np.vstack([np.ones(n - 2), A, np.ones(n - 2)])
    A = np.hstack([np.ones((n, 1)), A, np.ones((n, 1))])
    return A

print(a(5))

def b(n):
    B = np.arange(n**2).reshape((n, n))
    B = 1 - B % 2
    return B

print(b(5))

def c(n):
    C = np.arange(n).reshape((n, 1))
    C = 1 - C % 2
    C = C + np.zeros(n - 2)

    left = np.where((np.arange(n) - 1) % 4, 1, 0).reshape((n,1))
    right = np.where((np.arange(n) - 3) % 4, 1, 0).reshape((n,1))
    C = np.hstack([left, C, right])
    return C

print(c(5))