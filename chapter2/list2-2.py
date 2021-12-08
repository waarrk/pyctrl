import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()
plt.show()
