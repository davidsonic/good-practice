import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(1,1)
data = np.random.randint(0, 100, size=(10, 10))
ax1.imshow(data, cmap='jet', interpolation='nearest')
labels = ax1.get_xticklabels()
# ax1.set_xticklabels(['', 0,10,20,30,40])

plt.show()