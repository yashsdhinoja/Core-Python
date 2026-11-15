import matplotlib.pyplot as plt
import numpy as np

x_pionts = np.array([5, 35, 51.3, 72.2, 90.5])
y_pionts = np.array([29, 59, 89, 19.9, 151.9])

plt.plot(x_pionts, y_pionts,  color="red")
plt.show()