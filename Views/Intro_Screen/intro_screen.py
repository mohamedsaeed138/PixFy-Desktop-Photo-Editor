from customtkinter import CTkFrame, CTkLabel, CTkImage, CTk
from PIL.Image import open
from PIL.ImageTk import PhotoImage


class IntroScreen(CTkLabel):
    def __init__(
        self,
        master: CTk,
        master_size: tuple[int, int],
        image_path: str,
    ):
        super().__init__(master, text="")
        logo_image = open(image_path).copy()
        logo_image.thumbnail(master_size)
        photo_image = PhotoImage(logo_image)
        self.configure(image=photo_image)
        self._image = photo_image
