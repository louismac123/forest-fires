import numpy as np
import matplotlib.pyplot as plt

grid = np.load('app/results/processed.npy')

print(grid.shape)

grid[grid > 0] = 1

plt.imshow(grid)
plt.show()
