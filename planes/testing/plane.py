import numpy as np

class planes():

    def __init__(self, x: int, y: int, num_extinguish:int = 0):
        self.x = x
        self.y = y
        self.num_extinguish = num_extinguish

    def get_min_distance_cell_from_cluster(self, clusters: dict):
        priority_queue = sorted(clusters, key= lambda x: clusters[x]['size'], reverse=True)
        closest_cells = np.zeros(shape=(len(priority_queue), 2))

        for idx, x in enumerate(priority_queue):
            cells = np.array(clusters[x]['cells'])
            distances = ((self.x*np.ones(shape=cells.shape[0]) - cells[:, 0])**2 + (self.y*np.ones(shape=cells.shape[0]) - cells[:, 1])**2)**(1/2)
            closest_cells[idx] = cells[np.argmin(distances)]
        
        return closest_cells