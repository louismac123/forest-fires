import PIL.Image
import scipy as scipy
import numpy as np
import matplotlib.pyplot as plt

def _img_a_cast(img_a, dtype, true_color=False):
    """
    This function checks and corrects for any errors in our image format.
    """

    # Make sure the max and min are 255 and 0 for any given value.
    img_a = np.maximum(img_a, 0)                        
    img_a = np.minimum(img_a, 255)


    # round any floats to integers
    img_a = np.round(img_a, 0)
    img_a = np.array(img_a + 1.0e-6, dtype=dtype)

    # handles grayscale images
    if len(img_a.shape) == 2:
        if true_color:
            img_a_gs = np.zeros((img_a.shape[0], img_a.shape[1], 3),
                                dtype=dtype)
            for k in range(3):
                img_a_gs[:, :, k] = img_a
            return img_a_gs
        else:
            return img_a
        
    # tests for unexpected image types by seeing if there's more than RGB channels
    # or if the last shape has more than 3 channels.
    else:
        if len(img_a.shape) != 3 or img_a.shape[2] != 3:
            raise RuntimeError("Unexpected image type")
        return img_a

def linear_filter(img_a, W, **kwargs):
    """
    Applies a convolution with a kernel W to the supplied image
    """

    img_a = _img_a_cast(img_a, dtype=np.int64)
    W = np.fliplr(np.flipud(W))

    if len(img_a.shape) == 2:
        img_filtered_a = scipy.ndimage.convolve(img_a, W, **kwargs)
    else:
        if len(img_a.shape) != 3 or img_a.shape[2] != 3:
            raise RuntimeError("Unexpected image type")
        img_filtered_a = np.zeros_like(img_a)
        for k in range(3):
            img_filtered_a[:, :, k] = scipy.ndimage.convolve(
                img_a[:, :, k], W, **kwargs)

    return _img_a_cast(img_filtered_a, dtype=np.int64)

def imwrite(fp, img_a, **kwargs):
    img_a = _img_a_cast(img_a, dtype=np.uint8)
    img = PIL.Image.fromarray(img_a)
    img.save(fp, **kwargs)

with PIL.Image.open('image_processing/app/src/image.png', 'r') as h:
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

np.save('image_processing/app/results/processed.npy', img_linear)
imwrite('image_processing/app/results/processed.png', img_linear)