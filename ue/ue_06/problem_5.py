import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

phi = np.linspace(0, 2*np.pi,20)
r = np.linspace(0, 1, 20)
rr, pp = np.meshgrid(r, phi)
colors = cm.rainbow(rr.flatten())


plt.figure()
plt.xlim((-1, 1))
plt.ylim((-1, 1))
plt.scatter(rr * np.cos(pp), rr * np.sin(pp), label="circles", color=colors)
plt.legend()
plt.show()

# ellipses
plt.figure()
plt.xlim((-1, 1))
plt.ylim((-1, 1))
plt.scatter(rr * np.cos(pp), rr * np.sin(pp) * 1/2, label="ellipses", color=colors)
plt.legend()
plt.show()