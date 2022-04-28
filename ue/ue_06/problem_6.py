from mayavi import mlab
import numpy as np

# WORK IN PROGRESS!!! NOT FINISHED YET!!!!!

# a = 1
# b = 4
# c = 1

# phi = np.linspace(0, 2*np.pi)
# theta = np.linspace(0, np.pi)

# Phi, Theta = np.meshgrid(phi, theta)
# x = a * np.sin(Theta) * np.cos(Phi)
# y = b * np.sin(Theta) * np.sin(Phi)
# z = c * np.cos(Theta)

# s = mlab.mesh(x, y, z)
# mlab.show()


# C ----- D
# | \     |
# |   \   |
# |     \ |
# A ----- B
def addFace(indices, A, B, C, D):
    indices.append((A, B, C))
    indices.append((C, B, D))

vertices = np.array([
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0],
    [1.0, 0.0, 0.0],
    [1.0, 0.0, 1.0],
    [1.0, 1.0, 0.0],
    [1.0, 1.0, 1.0],
])

indices = []
addFace(indices, 0, 4, 2, 6) # Front
addFace(indices, 4, 5, 6, 7) # Right
addFace(indices, 5, 1, 7, 3) # Back
addFace(indices, 1, 0, 3, 2) # Left
addFace(indices, 2, 6, 3, 7) # Top
addFace(indices, 1, 5, 0, 4) # Bottom
# indices = np.array(indices) # convert to numpy array

# get x, y, z indices vector.
x = vertices[:, 0]
y = vertices[:, 0]
z = vertices[:, 0]

print(indices)
# mlab.triangular_mesh(x, y, z, indices)
# mlab.show()

n = 8
t = np.linspace(-np.pi, np.pi, n)
z = np.exp(1j * t)
x = z.real.copy()
y = z.imag.copy()
z = np.zeros_like(x)

triangles = [(0, i, i + 1) for i in range(1, n)]
x = np.r_[0, x]
y = np.r_[0, y]
z = np.r_[1, z]
t = np.r_[0, t]

print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")
print(f"indices: {triangles}")
print(f"t: {t}")

mlab.triangular_mesh(x, y, z, triangles, scalars=t)
mlab.show()