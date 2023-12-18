from datetime import time
import random
from customtkinter import CTkFrame, CTkLabel, CTkImage, CTk
from PIL.Image import open, LANCZOS
from PIL.ImageTk import PhotoImage
from PIL.ImageOps import contain


class IntroScreen(CTkLabel):
    def __init__(
        self,
        master: CTk,
        master_size: tuple[int, int],
        image_path: str,
    ):
        super().__init__(master, text="")
        self.intro = open(image_path)
        self.configure(
            image=PhotoImage(
                contain(
                    self.intro,
                    (int(master_size[0] * 1.24868), int(master_size[1] * 1.24868)),
                    LANCZOS,
                )
            )
        )

    #     self.bind("<Configure>", self.setup)

    # def setup(self, event):
    #     print((event.width, event.height))
    #     self.configure(
    #         image=PhotoImage(contain(self.intro, (event.width, event.height), LANCZOS))
    #     )
