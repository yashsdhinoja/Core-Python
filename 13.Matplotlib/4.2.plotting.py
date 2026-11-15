import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([23, 45, 33])
y_points = np.array([12, 34, 55])

plt.plot(x_points, y_points, 'o', color="red")
plt.show()