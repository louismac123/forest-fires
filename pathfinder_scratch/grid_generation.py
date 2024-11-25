import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('./planes/testing/')
import plane as plane

board_size = 100

grid = np.zeros(shape=(board_size, board_size))

target = (50,22)

grid[target[0], target[1]] = 1

alpha_responder = plane.planes(x=10, y=6)
movement_speed = 1000

def norm_dir_vec(plane=alpha_responder, target=target):
    dir = np.array([target[0] - plane.x,
                    target[1] - plane.y])
    mag = (plane.x - target[0])**2 + (plane.y - target[1])
    dir = dir/mag
    return mag, dir

mag, dir = norm_dir_vec()

def move_plane(dir, speed, plane):
    dx = dir[0] * speed
    dy = dir[1] * speed

    plane.x = int(plane.x + dx)
    plane.y = int(plane.y + dy)

    return plane.x, plane.y

move_plane(dir=dir, speed=movement_speed, plane=alpha_responder)


plt.imshow(grid)
plt.scatter(6, 10, label='start_pos')
plt.scatter(alpha_responder.y, alpha_responder.x, label='new_pos')
plt.legend()
plt.show()