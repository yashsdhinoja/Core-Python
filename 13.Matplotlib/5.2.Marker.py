import matplotlib.pyplot as plt
import numpy as np

x_pot = np.array([23,98,12,67,90])
y_pot = np.array([12,78,45,55,23])

plt.plot(x_pot,y_pot, 'o-.', color="black", marker="H")
plt.show()

# Line Reference

# Line Syntax	Description
#    '-'	        Solid line	
#    ':'	        Dotted line	
#    '--'	        Dashed line	
#    '-.'	        Dashed/dotted line