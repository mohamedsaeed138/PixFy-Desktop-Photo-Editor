from PIL.Image import Image, open, LANCZOS
from PIL.ImageOps import contain


class ImageModel:
    def __init__(self):
        self.image: Image = None
        self.edited_image: Image = None

    def set_images(self, path: str):
        self.image = open(path)
        self.edited_image = self.image.copy()

    def get_scaled_images(self, size: tuple[int, int]) -> tuple[Image, Image]:
        return (
            contain(self.image, size),
            contain(self.edited_image, size),
        )

    def get_images_size(self) -> tuple[Image, Image]:
        return self.image.size, self.edited_image.size
