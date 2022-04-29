from mayavi import mlab
import numpy as np

a = 1
b = 2
c = 4

phi = np.linspace(0, 2*np.pi)
theta = np.linspace(0, np.pi)

Phi, Theta = np.meshgrid(phi, theta)
x = a * np.sin(Theta) * np.cos(Phi)
y = b * np.sin(Theta) * np.sin(Phi)
z = c * np.cos(Theta)

s = mlab.mesh(x, y, z)
mlab.show()


# C ----- D
# | \     |
# |   \   |
# |     \ |
# A ----- B
def addFace(indices, A, B, C, D):
    indices.append((A, B, C))
    indices.append((C, B, D))

#     3 ------- 7
#   / |       / |
# 2 ------- 6   |
# |   |     |   |
# |   1 ----|-- 5
# | /       | /
# 0 ------- 4
#
# Create vertices
vertices = np.array([
    [0.0, 0.0, 0.0], # back-bottom-left
    [0.0, 0.0, 1.0], # back-bottom-right
    [0.0, 1.0, 0.0], # back-top-left
    [0.0, 1.0, 1.0], # back-top-right
    [1.0, 0.0, 0.0], # front-bottom-left
    [1.0, 0.0, 1.0], # front-bottom-right
    [1.0, 1.0, 0.0], # front-top-left
    [1.0, 1.0, 1.0], # front-top-right
])

# Create indices
indices = []
addFace(indices, 0, 4, 2, 6) # Front
addFace(indices, 4, 5, 6, 7) # Right
addFace(indices, 5, 1, 7, 3) # Back
addFace(indices, 1, 0, 3, 2) # Left
addFace(indices, 2, 6, 3, 7) # Top
addFace(indices, 1, 5, 0, 4) # Bottom

# get x, y and z coordinate vectors of vertices.
x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

# Optional: print vertices and indices.
# print(f"x: {x}")
# print(f"y: {y}")
# print(f"z: {z}")
# print(f"indices: {indices}")

# Render cube.
mlab.triangular_mesh(x, y, z, indices)
mlab.show()