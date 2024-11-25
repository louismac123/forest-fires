import numpy as np
import matplotlib.pyplot as plt
import plane
from clustering import find_fire_clusters

# grid = np.load('planes/generation/grid.npy')
grid = np.load('planes/testing/M_tracked.npy')
alpha_responder = plane.planes(20, 20)
plane_loc = []
targets = []
grids = []

for i in range(10):
    curr_grid = grid[i]
    clustered_grid = curr_grid.copy()

    locs = alpha_responder.get_min_distance_cell_from_cluster(clustered_grid)
    grids.append(clustered_grid)

    target = locs[0]
    targets.append(target)

    alpha_responder.move(target)

    alpha_loc = alpha_responder.get_loc()
    plane_loc.append(alpha_loc)

for i in range(len(grids)):
    plt.imshow(grids[i], alpha = 0.1, label=f'grid {i}')

plt.scatter(20, 20, label='plane_init', marker=(3, 0))

for idx, location in enumerate(plane_loc):
    plt.scatter(location[1], location[0], label=f'plane_loc_{idx+1}', marker=(3, 0))

plt.legend()
plt.show()