from customtkinter import CTkFrame
from Views.Main_Screen.Images_Container.image_view_container import ImageViewContainer
from Views.Main_Screen.Images_Container.dnd_image_view_container import (
    DNDImageViewContainer,
)


class ImagesContainer(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "white"])
        self.grid_columnconfigure(list(range(0, 20)), weight=1, uniform="a")
        self.grid_rowconfigure((0), weight=1, uniform="a")
        self.original_image_container = DNDImageViewContainer(self, title="Original")
        self.edited_image_container = ImageViewContainer(self, title="After Edit")
        self.original_image_container.grid(
            row=0, column=0, columnspan=10, padx=5, sticky="nsew"
        )
        self.edited_image_container.grid(
            row=0, column=10, columnspan=10, padx=5, sticky="nsew"
        )
