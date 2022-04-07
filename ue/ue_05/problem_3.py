import numpy as np

def properties(A):
    (n, m) = A.shape

    dimensins = A.ndim
    symmetric = n == m and np.all(A == A.T)
    skew_symmetric = n == m and np.all(A == -A.T)
    invertable = n == m and np.linalg.det(A) != 0
    orthogonal = np.allclose(A.dot(A.T), np.eye(np.min(A.shape)), atol=1e-6)
    return f"dimensions: {dimensins}\nsymmetry: {symmetric}\nskew symmetry: {skew_symmetric}\ninveratibility: {invertable}\northogonal: {orthogonal}"

# A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# A = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]]) # skew symmetric matrix
# A = np.array([[1, 2, 3], [2, 1, 0], [3, 0, 1]]) # symmetric matrix
A = np.array([[3, 4], [-4, 3]]) * 1/5 # orthogonal matrix
print(properties(A))