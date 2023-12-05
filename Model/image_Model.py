from PIL.Image import Image, open


class ImageModel:
    def __init__(self):
        self.path: str
        self.image: Image
        self.size: tuple[int, int]

    def get_copy(self, max_size: tuple[int, int]) -> Image:
        new_image = self.image.copy()
        new_image.thumbnail(max_size)
        return new_image

    def set_img(self, path: str, max_size: tuple[int, int]) -> Image:
        self.path = path
        self.image = open(path)
        self.size = self.image.size
        return self.get_copy(max_size)
