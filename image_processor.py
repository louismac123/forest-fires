import PIL.Image
import numpy as np
from utils import imwrite, linear_filter


with PIL.Image.open('imaging/image.png', 'r') as h:
    img = np.array(h, dtype=np.int64)

img = img[:, :, :3]
img[:, :, 2] = 0
img[:, :, 1] = 0
img[img[:, :, 0] > 210] = 0

W_0 = np.array([[1,1,1],
                [1,1,1],
                [1,1,1]]
              ) * 10

img_linear = linear_filter(img, W_0, mode = "reflect")

# for i in range(1):
#     img_linear = linear_filter(img_linear, W_0, mode = "reflect")

img_linear = np.sum(img_linear, axis=2)

np.save('imaging/processed.npy', img_linear)
imwrite('imaging/processed.png', img_linear)