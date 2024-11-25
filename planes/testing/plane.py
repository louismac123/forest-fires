import numpy as np
from clustering import find_fire_clusters, effective_radius

import sys
sys.path.append('./planes/generation/')
from ForestFire import get_cell, set_cell

class planes():
    def __init__(self, x: int, y: int, speed:float = 10.0):
        self.x = x
        self.y = y
        self.speed = speed

    def get_loc(self):
        return np.array([self.x, self.y])

    def extinguish(self, grid):

        effective_radius = [
                  (-2, -1), (-2, 0), (-2, 1),
        (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
        ( 0, -2), ( 0, -1), ( 0, 0), ( 0, 1), ( 0 , 2),
        ( 1, -2), ( 1, -1), ( 1, 0), ( 1, 1), ( 1, 2),
                  (2, -1),  ( 2, 0), ( 2, 1)
                  ]

        for loc in effective_radius:
            x_loc = self.x + loc[0]
            y_loc = self.y + loc[1]
            if get_cell(grid, x_loc, y_loc) == 3:
                set_cell(grid, x_loc, y_loc, 4)

    def get_min_distance_cell_from_cluster(self, grid):
        clusters = find_fire_clusters(grid)
        priority_queue = sorted(clusters, key= lambda x: clusters[x]['size'], reverse=True)
        closest_cells = np.zeros(shape=(len(priority_queue), 2))

        for idx, x in enumerate(priority_queue):
            cells = np.array(clusters[x]['cells'])
            distances = ((self.x*np.ones(shape=cells.shape[0]) - cells[:, 0])**2 + (self.y*np.ones(shape=cells.shape[0]) - cells[:, 1])**2)**(1/2)
            closest_cells[idx] = cells[np.argmin(distances)]
        
        return closest_cells
    
    def norm_target_direction(self, target:np.array):

        vec = np.array([target[0] - self.x,
                        target[1] - self.y])
        
        mag = ((target[0] - self.x)**2 + (target[1] - self.y)**2)**(1/2)
        dir = vec/mag

        loc = self.get_loc()
        ab = np.clip(np.dot(loc, target), -1.0, 1.0)
        mag_a = ((target[0])**(2) + (target[1])**(2))**(1/2)
        mag_b = ((loc[0])**(2) + (loc[1])**(2))**(1/2)
        rot = np.arccos((ab/(mag_a*mag_b)))

        return mag, dir

    def move(self, target: np.array):
        _, dir = self.norm_target_direction(target)
        dx = dir[0] * self.speed
        dy = dir[1] * self.speed

        self.x = int(self.x + dx)
        self.y = int(self.y + dy)