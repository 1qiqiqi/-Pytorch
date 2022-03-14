import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1.0/(1+np.exp(-x))

x = np.arange(-10,10)

plt.plot(x,sigmoid(x))
plt.show()