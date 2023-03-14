import utils
from skimage import data


def test_rotated_image():
    ''' Test image rotation '''
    image = data.astronaut()
    result = utils.rotated_image(image)
    assert image.shape == result.shape
