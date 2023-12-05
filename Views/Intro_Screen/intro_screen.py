from customtkinter import CTkFrame, CTkLabel, CTkImage, BOTH
from PIL.Image import open, Image


class IntroScreen(CTkFrame):
    def __init__(
        self, master, master_size: tuple[int, int], intro_time: int, image_path: str
    ):
        super().__init__(master, fg_color=("#ffffff", "#ffffff"))
        self.__time: int = intro_time
        self.original_image = open(image_path)
        self.logo_image: Image = self.original_image.copy()
        self.logo_image.thumbnail(master_size)
        self.__image: CTkImage = CTkImage(
            self.logo_image, self.logo_image, size=self.logo_image.size
        )
        self.__image_label: CTkLabel = CTkLabel(
            self, text=str(), image=self.__image, fg_color=("#eeeeee", "#ffffff")
        )
        self.__image_label.pack(expand=True, fill=BOTH)

    def get_time(self) -> int:
        return self.__time

    time = property(get_time)
