from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFont, BOTH
from tkinterdnd2 import TkinterDnD, DND_ALL
from PIL.Image import open

from Views.Main_Screen.Images_Container.image_container import ImageContainer


class DNDImageContainer(CTkFrame, TkinterDnD.DnDWrapper):
    def __init__(self, master, title: str):
        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0,
        )
        self.TkdndVersion = TkinterDnD._require(self)
        self.image_container = ImageContainer(self, title)
        self.image_container.pack(expand=True, fill=BOTH)

    @property
    def image_label(self) -> CTkLabel:
        return self.image_container.image_label

    def size_label(self):
        return self.image_container.size_label

    def title_label(self):
        return self.image_container.title_label

    def label_size(self):
        return self.image_container.label_size()
