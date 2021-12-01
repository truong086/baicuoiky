import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection='3d')
ax.plot3D(height,weight)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
plt.show()