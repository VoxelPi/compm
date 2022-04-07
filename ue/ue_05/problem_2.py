import numpy as np

def A(n):
    return np.arange(1, n+1) * np.arange(1, n+1).reshape(n,1)

print("\nA(5): ")
print(A(5))

def B(n):
    return np.arange(0, n+1) + np.arange(0, n+1).reshape(n+1,1)

print("\nB(5): ")
print(B(5))

def C(n):
    A = np.identity(n)*np.arange(1, n+1)
    B = np.vstack([np.hstack([np.zeros((n-1, 1)), np.diag(np.arange(1, n)*2)]), np.zeros((1, n))])
    C = np.vstack([np.zeros((1, n)), np.hstack([np.diag(np.arange(1, n)**2), np.zeros((n-1, 1))])])
    return A + B + C

print("\nC(5): ")
print(C(5))