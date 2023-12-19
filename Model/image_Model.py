from PIL.ImageFilter import MaxFilter, MinFilter
from PIL.Image import Image, open, LANCZOS, fromarray, BICUBIC, AFFINE
from PIL.ImageOps import contain
from skimage.util import random_noise
from cv2 import (
    Canny,
    Laplacian,
    Sobel,
    addWeighted,
    cvtColor,
    COLOR_RGB2RGBA,
    COLOR_RGBA2GRAY,
    THRESH_BINARY,
    equalizeHist,
    threshold,
    resize,
    CV_64F,
    filter2D,
    GaussianBlur,
    boxFilter,
    blur,
    medianBlur,
)

from matplotlib import pyplot as plt
from numpy import array, log, power, uint8, min, max

from Presenter.choice_enums import SharpeningChoice


class ImageModel:
    def __init__(self):
        self.image: Image = None
        self.edited_image: Image = None
        self.sharpening_filters = {
            SharpeningChoice.CompositeLaplacian1.value: array(
                [[1, 1, 1], [1, -7, 1], [1, 1, 1]]
            ),
            SharpeningChoice.CompositeLaplacian2.value: array(
                [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
            ),
        }

    def set_images(self, path: str):
        self.image = open(path)
        self.edited_image = self.image.copy()

    def get_scaled_images(self, size: tuple[int, int]) -> tuple[Image, Image]:
        return (
            contain(self.image, size, LANCZOS),
            contain(self.edited_image, size, LANCZOS),
        )

    def get_scaled_edited_image(self, size: tuple[int, int]) -> Image:
        return contain(self.edited_image, size)

    def gray_scale_filter(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        pillow_image = fromarray(cv2_image)
        self.edited_image = contain(pillow_image, self.edited_image.size, LANCZOS)

    def rotate(self, angle: int):
        # self.edited_image = self.edited_image.rotate(angle, BICUBIC, expand=True)
        self.edited_image = self.edited_image.convert("RGBA").rotate(
            angle, BICUBIC, expand=True, fillcolor=None
        )

    def resize(self, size):
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = resize(cv2_image, (size[0], size[1]))
        pillow_image = fromarray(cv2_image)
        self.edited_image = pillow_image

    def translate(self, displacement: tuple[int, int]):
        # old code
        # self.edited_image = self.edited_image.transform(
        #     self.edited_image.size,
        #     AFFINE,
        #     (1, 0, displacement[0], 0, 1, displacement[1]),
        #     resample=BICUBIC,
        # )
        translated_image = self.edited_image.transform(
            self.edited_image.size,
            AFFINE,
            (1, 0, displacement[0], 0, 1, displacement[1]),
            resample=BICUBIC,
        )
        bbox = translated_image.getbbox()

        self.edited_image = self.edited_image.crop(bbox)

    def histogram(self) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        gray = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        plt.hist(gray.ravel(), 256, [0, 255])
        plt.title("Histogram")
        plt.show()
        plt.close()

    def threshold(self, key: int) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        _, threshold_image = threshold(cv2_image, key, 255, THRESH_BINARY)
        self.edited_image = fromarray(threshold_image)

    def negative(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        negative_image = 255 - cv2_image
        self.edited_image = fromarray(negative_image)

    def contrast_stretching(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        min_in, max_in = min(cv2_image), max(cv2_image)
        min_out, max_out = 0, 255
        stretch_img = uint8(
            (cv2_image - min_in) * ((max_out - min_out) / (max_in - min_in)) + max_out
        )
        self.edited_image = fromarray(stretch_img)

    def equalization(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        equalized_image = equalizeHist(cv2_image)
        self.edited_image = fromarray(equalized_image)

    def log_transform(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        c = 255 / log(1 + max(cv2_image))
        log_image = uint8(c * log(1 + cv2_image))
        self.edited_image = fromarray(log_image)

    def power_law(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        normalized_image = cv2_image / 255.0
        gamma = 2.2
        power_image = uint8(power(normalized_image, gamma) * 255)
        self.edited_image = fromarray(power_image)

    def sharpening(self, choice: int) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        if choice != SharpeningChoice.Laplacian.value:
            sharpened_image = filter2D(cv2_image, -1, self.sharpening_filters[choice])
        else:
            laplacian_image = Laplacian(cv2_image, CV_64F)
            normalized_image = cv2_image + laplacian_image
            sharpened_image = normalized_image.clip(0, 255).astype(uint8)

        self.edited_image = fromarray(sharpened_image)

    def smooth_gaussian_filter(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        mask = (9, 9)
        gaussian_image = GaussianBlur(cv2_image, mask, 0)
        self.edited_image = fromarray(gaussian_image)

    def smooth_box_filter(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        mask = (9, 9)
        box_image = boxFilter(cv2_image, -1, mask)
        self.edited_image = fromarray(box_image)

    def smooth_mean_filter(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        mask = (9, 9)
        avg_image = blur(cv2_image, mask)
        self.edited_image = fromarray(avg_image)

    def smooth_median_filter(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        median_image = medianBlur(cv2_image, 3)
        self.edited_image = fromarray(median_image)

    def smooth_max_filter(self, param) -> None:
        self.edited_image = self.edited_image.filter(MaxFilter(3))

    def smooth_min_filter(self, param) -> None:
        self.edited_image = self.edited_image.filter(MinFilter(3))

    def canny_detection(self, param):
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        canny_image = Canny(cv2_image, 50, 200)
        self.edited_image = fromarray(canny_image)

    def sobelx_detection(self, param):
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        sobelx_image = Sobel(cv2_image, -1, 1, 0)
        self.edited_image = fromarray(sobelx_image)

    def sobely_detection(self, param):
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        sobely_image = Sobel(cv2_image, -1, 0, 1)
        self.edited_image = fromarray(sobely_image)

    def sobelxy_detection(self, param):
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        sobelx_image = Sobel(cv2_image, -1, 1, 0)
        sobely_image = Sobel(cv2_image, -1, 0, 1)
        sobelxy_image = addWeighted(sobelx_image, 1, sobely_image, 1, 0)
        self.edited_image = fromarray(sobelxy_image)

    def gaussian_noise(self, param) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        gaussian_noise_image = uint8(
            random_noise(cv2_image, mode="gaussian", mean=0, var=0.01) * 255
        )
        self.edited_image = fromarray(gaussian_noise_image)

    def sp_noise(self, amount: float) -> None:
        cv2_image = cvtColor(array(self.edited_image), COLOR_RGB2RGBA)
        cv2_image = cvtColor(cv2_image, COLOR_RGBA2GRAY)
        sp_noise_image = uint8(random_noise(cv2_image, mode="s&p", amount=amount) * 255)
        self.edited_image = fromarray(sp_noise_image)

    def apply_edits(self, events: list[tuple]):
        self.edited_image = self.image.copy()
        [event(param) for event, param in events]
