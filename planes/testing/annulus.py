import matplotlib.pyplot as plt
import numpy as np

def create_annulus_array(size=120, inner_radius=20, outer_radius=40):
    # Create a grid of coordinates
    y, x = np.meshgrid(np.arange(size), np.arange(size))
    
    # Calculate the distance from the center
    center = size // 2
    distance_from_center = np.sqrt((x - center) ** 2 + (y - center) ** 2)
    
    # Create the annulus mask
    annulus_mask = (distance_from_center >= inner_radius) & (distance_from_center <= outer_radius)
    
    # Initialize the array and apply the mask
    array = np.zeros((size, size), dtype=int)
    array[annulus_mask] = 1
    
    return array