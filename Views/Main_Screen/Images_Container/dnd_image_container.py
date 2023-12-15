from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFont, BOTH
from tkinterdnd2 import TkinterDnD, DND_ALL
from Presenter.presenter import Presenter

from Views.Main_Screen.Images_Container.image_container import ImageContainer


class DNDImageContainer(CTkFrame, TkinterDnD.DnDWrapper):
    def __init__(self, master, title: str):
        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0,
        )
        self.TkdndVersion = TkinterDnD._require(self)
        self.presenter: Presenter = master.presenter

        self.image_container = ImageContainer(self, title)
        self.image_container.pack(expand=True, fill=BOTH)
        self.add_events()

    def add_events(self):
        self.image_container.image_label.bind(
            "<Configure>", self.presenter.rescale_images
        )
        self.image_container.image_label.drop_target_register(DND_ALL)
        self.image_container.image_label.dnd_bind("<<Drop>>", self.presenter.drop_image)

    @property
    def image_label(self) -> CTkLabel:
        return self.image_container.image_label

    def size_label(self):
        return self.image_container.size_label

    def title_label(self):
        return self.image_container.title_label

    def label_size(self):
        return self.image_container.label_size()
