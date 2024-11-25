import numpy as np
from clustering import find_fire_clusters

class planes():

    def __init__(self, x: int, y: int, num_extinguish:int = 0, speed:float = 10.0):
        self.x = x
        self.y = y
        self.speed = speed
        self.num_extinguish = num_extinguish

    def get_loc(self):
        return np.array([self.x, self.y])

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

        return mag, dir

    def move(self, target: np.array):
        _, dir = self.norm_target_direction(target)
        dx = dir[0] * self.speed
        dy = dir[1] * self.speed

        self.x = int(self.x + dx)
        self.y = int(self.y + dy)