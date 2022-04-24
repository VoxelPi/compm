import numpy as np

def pseudo(A):
    # Check if matrix A is injective.
    if np.linalg.det(A.T @ A) < 1e-9:
        print("the given matrix is not injective.")
        return

    # Return pseudo-inverse (See lecture notes page 155)
    print("the given matrix is injective.")
    return np.linalg.inv(A.T @ A) @ A.T

# A = np.array([[1, 2, 0], [2, 4, 0], [1, 0, 3]]) # not injective
A = np.array([[1, 2, 0], [1, 4, 2], [1, 0, 3]]) # injective
print(pseudo(A))

A = np.array([[1, 0], [2, 1], [0, 2]])
b = np.array([1, 0, 1]).reshape((3, 1))
x = pseudo(A) @ b
print("\nOwn implementation:")
print(x)

print("\nNumpy implementation:")
print(np.linalg.lstsq(a = A, b = b, rcond=None)[0])