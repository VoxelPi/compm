import numpy as np

def gendot(A, B):
    (n, m) = A.shape
    (p, q) = B.shape
    assert(n*m == p*q)

    return np.sum(np.reshape(A, (n*m, 1)) * np.reshape(B, (n*m, 1)))

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B = np.array([[1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0]])
print(gendot(A, B))

def genadd(A, B):
    (n, m) = A.shape
    (p, q) = B.shape
    assert(n*m == p*q)

    return np.sum(np.reshape(A, (n*m, 1)) + np.reshape(B, (n*m, 1)))

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B = np.array([[1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0]])
print(genadd(A, B))
