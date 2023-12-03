from customtkinter import CTkFrame
from Views.Main_Screen.Images_Container.image_view_container import ImageViewContainer
from Views.Main_Screen.Images_Container.dnd_image_view_container import (
    DNDImageViewContainer,
)


class ImagesContainer(CTkFrame):
    def __init__(self, master, size: tuple[int, int]):
        super().__init__(
            master, fg_color=["white", "white"], width=size[0], height=size[1]
        )
        self.grid_columnconfigure(list(range(0, 20)), pad=0)
        self.original_image_container = DNDImageViewContainer(
            self, size=(int(size[0] * 0.5) - 5, size[1]), title="Original"
        )
        self.edited_image_container = ImageViewContainer(
            self, size=(int(size[0] * 0.5) - 5, size[1]), title="After Edit"
        )
        self.original_image_container.grid(row=0, column=0, columnspan=10, padx=5)
        self.edited_image_container.grid(row=0, column=10, columnspan=10, padx=5)
