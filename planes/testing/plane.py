import numpy as np
from clustering import find_fire_clusters

import sys
sys.path.append('./planes/generation/')
from ForestFire import get_cell, set_cell

class planes():
    """
    Handles all behaviour and attributes of planes.
    
    All methods that will be used were built with this data handling in mind:
        - all a method requires must be a grid.
            - This ensures cleanliness of code.
            - Allows us to easily 'slot in' planes into existing fire model. 

    methods:
        get_loc                                 return location.
        extinguish                              extinguishing algorithm.
        get_min_distance_cell_from_cluster      target finding.
        norm_target_direction                   magnitude, direction, rotation finding.
        helper_move, move                       movement of plane.
    """
    def __init__(self, x: int, y: int, speed:float = 10.0):
        self.x = x
        self.y = y
        self.speed = speed
        self.num_extinguish = 0
        self.effective_radius = [
                                  (-2, -1), (-2, 0), (-2, 1),
                        (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
                        ( 0, -2), ( 0, -1), ( 0, 0), ( 0, 1), ( 0 , 2),
                        ( 1, -2), ( 1, -1), ( 1, 0), ( 1, 1), ( 1, 2),
                                (2, -1),  ( 2, 0), ( 2, 1)
                                 ]

    def get_loc(self):
        # Return the location of the plane as a numpy array.
        return np.array([self.x, self.y])

    def extinguish(self, grid):
        # Goes through cells in the plane's effective-radius and extinguishes them if they're burning.
        for loc in self.effective_radius:
            # get the locations of cell we're interested in.
            x_loc = self.x + loc[0]
            y_loc = self.y + loc[1]

            # if the cell is burning set it to extinguished '4' and increment the num_extinguish
            if get_cell(grid, x_loc, y_loc) == 3:
                set_cell(grid, x_loc, y_loc, 4)
                self.num_extinguish += 1

    def get_min_distance_cell_from_cluster(self, grid):
        """
        Clusters fires, finds closest cell in each fire.
        """
        # use depth-first-search to cluster fires and assign them values.
        clusters = find_fire_clusters(grid)

        # sort through the fires based on size and return a list from most severe to least severe.
        priority_queue = sorted(clusters, key= lambda x: clusters[x]['size'], reverse=True)
        closest_cells = np.zeros(shape=(len(priority_queue), 2))

        # loop through each fire cluster in the priority_queue
        for idx, x in enumerate(priority_queue):
            cells = np.array(clusters[x]['cells'])  # store all cells in the fire cluster as a numpy array.

            # find the euclidean distance between the plane and all cells in the cluster.
            distances = ((self.x*np.ones(shape=cells.shape[0]) - cells[:, 0])**2 \
                         + (self.y*np.ones(shape=cells.shape[0]) - cells[:, 1])**2) ** (1/2)
            
            # append the cell with the smallest distance into the closest_cells list.
            closest_cells[idx] = cells[np.argmin(distances)]
        
        return closest_cells
    
    def norm_target_direction(self, target:np.array):
        # Uses basic linear algebra to find the magnitude and direction of where the plane should go.
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

    def helper_move(self, target: np.array):
        # given a target, find the magnitude and direction
        _, dir = self.norm_target_direction(target)

        # find x, y distance update components based on speed.
        dx = dir[0] * self.speed
        dy = dir[1] * self.speed

        # force integer values since we're plotting on a grid.
        self.x = int(self.x + dx)
        self.y = int(self.y + dy)

    def move(self, grid):
        # Meant purely for cleanliness of code. I.e. take in a grid and run `helper_move()` with acceptable inputs.
        locs = self.get_min_distance_cell_from_cluster(grid)
        target = locs[0]
        self.helper_move(target)