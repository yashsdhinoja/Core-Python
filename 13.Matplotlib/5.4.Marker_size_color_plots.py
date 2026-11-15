import matplotlib.pyplot as plt
import numpy as np

a_point = np.array([12,67,34,90,98])
b_point = np.array([4,23,56])
c_point = np.array([34,56,89])

# Use both the [ mec ] and [ mfc ] arguments to color the entire marker:
# You can use the keyword argument markerfacecolor or the shorter [ mfc ] to set the color inside the edge of the markers:
# You can use the keyword argument markeredgecolor or the shorter [ mec ] to set the color of the edge of the markers:
# You can use the keyword argument markersize or the shorter version, [ ms ] to set the size of the markers:
# This parameter is also called [ fmt ] , and is written with this syntax:
# marker|line|color
# You can use the keyword argument [ marker ] to emphasize each point with a specified marker:

plt.plot(a_point, linestyle='-.', color="orange",   marker="H", ms=20, mec='r', mfc='b')
plt.plot(b_point, linestyle='-.', color="black", marker="p", ms=20, mec='b', mfc='g')
plt.plot(c_point, linestyle='-.', color="red", marker="h", ms=20, mec='r', mfc='b')

# grid is in background line in graph
plt.grid(True)
plt.show()