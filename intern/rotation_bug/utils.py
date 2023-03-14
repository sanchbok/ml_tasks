import cv2
import numpy as np
from skimage.transform import AffineTransform


def rotated_image(image: np.ndarray, angle: int = 45) -> np.ndarray:
    ''' Image rotation '''
    width, height, channels = image.shape
    transform = AffineTransform(rotation=np.deg2rad(angle))
    result = cv2.warpPerspective(image, transform.params, dsize=(height, width))
    return result
