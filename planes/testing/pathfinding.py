import numpy as np
import matplotlib.pyplot as plt
import plane
from clustering import find_fire_clusters

grid = np.load('planes/generation/grid.npy')

curr_grid = grid[30]
clustered_grid = curr_grid.copy()

clusters = find_fire_clusters(clustered_grid)

priority_queue = sorted(clusters, key= lambda x: clusters[x]['size'], reverse=True)

alpha_responder = plane.planes(100, 100)

loc = alpha_responder.get_min_distance_cell_from_cluster(clusters)


plt.imshow(clustered_grid)
plt.scatter(alpha_responder.y, alpha_responder.x, label='Plane', marker='s')
for i in range(len(loc)):
    plt.scatter(loc[i][1], loc[i][0], label=f'Cluster Priority {i+1}')
plt.legend()
plt.show()

print()