from customtkinter import CTkFrame, CTkLabel, CTkImage
from PIL.Image import open, Image


class IntroScreen(CTkFrame):
    def __init__(
        self, master, master_size: tuple[int, int], intro_time: int, image_path: str
    ):
        super().__init__(master, fg_color=("#ffffff", "#ffffff"))
        self.__time: int = intro_time
        logo_image: Image = open(image_path)
        logo_image.thumbnail(master_size)
        self.__image: CTkImage = CTkImage(logo_image, logo_image, size=logo_image.size)
        self.__image_label: CTkLabel = CTkLabel(self, text=str(), image=self.__image)
        self.__image_label.pack(expand=True)

    def get_time(self) -> int:
        return self.__time

    time = property(get_time)
