import matplotlib.pyplot as plt
import numpy as np

x_pot = np.array([23,98,12,67,90])

plt.plot(x_pot, 'o-.', color="black", marker="H", ms=20, mec='r', mfc='r')

plt.show()