import numpy as np
import matplotlib.pyplot as plt
import plane
from clustering import find_fire_clusters

grid = np.load('planes/testing/M_tracked.npy')

alpha_responder = plane.planes(40, 60)

curr_grid = grid[10].copy()
clustered_grid = curr_grid.copy()

locs = alpha_responder.get_min_distance_cell_from_cluster(clustered_grid)
target = locs[0]
alpha_responder.move(target)
alpha_responder.extinguish(curr_grid)

plt.imshow(grid[13])
plt.scatter(60, 40, label='plane_init')
plt.scatter(alpha_responder.y, alpha_responder.x, label='plane_next')
plt.legend()
plt.title('non_extinguished')
plt.show()

plt.imshow(curr_grid)
plt.scatter(60, 40, label='plane_init')
plt.scatter(alpha_responder.y, alpha_responder.x, label='plane_next')
plt.legend()
plt.title('extinguished')
plt.show()