import numpy as np

m = 5
n = 4
p = 3

A = np.random.random((m, n))*1000
B = np.random.random((n, p))*1000
print(A)

def frobeniusnorm(A):
    return np.sqrt(np.sum(np.square(A)))

print(frobeniusnorm(A))
print(np.linalg.norm(A, ord="fro"))

print(f"{frobeniusnorm(A@B)} <= {frobeniusnorm(A) * frobeniusnorm(B)}")