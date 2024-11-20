import sys
sys.path.append('./planes/generation')

import numpy as np
import matplotlib.pyplot as plt

import ForestFire as FF

from clustering import find_fire_clusters

grid = np.load('planes/generation/grid.npy')
clustered_grid = grid.copy()

clusters = find_fire_clusters(clustered_grid)

priority_queue = sorted(clusters, key= lambda x: clusters[x]['size'], reverse=True)

loc = np.zeros(shape=(len(priority_queue), 2))

for idx, x in enumerate(priority_queue):
    for cell in clusters[x]['cells']:
        if FF.get_cell(grid, cell[0], cell[1]) == 1:
            loc[idx] = cell
            break



print()