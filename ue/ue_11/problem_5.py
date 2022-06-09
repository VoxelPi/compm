import numpy as np

m = 5
n = 4
p = 3

# Erzeuge zwei zufaellige numpy arrays.
A = np.random.random((m, n))*1000
B = np.random.random((n, p))*1000
print(A)

# Definiere eigene Implementation
def frobeniusnorm(A):
    return np.sqrt(np.sum(np.square(A)))

# Vergleiche eigene Implementation mit
# numpy Implementation.
print(frobeniusnorm(A))
print(np.linalg.norm(A, ord="fro"))

