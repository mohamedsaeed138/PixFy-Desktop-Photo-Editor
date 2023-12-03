from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFont
from tkinterdnd2 import TkinterDnD, DND_ALL
from PIL.Image import open


class DNDImageViewContainer(CTkFrame, TkinterDnD.DnDWrapper):
    def __init__(self, master, size: tuple[int, int], title: str):
        super().__init__(
            master,
            fg_color=["white", "#D8D7DB"],
            width=size[0],
            height=size[1],
            corner_radius=5,
        )
        self.TkdndVersion = TkinterDnD._require(self)

        self.img_label = CTkLabel(
            master=self,
            text="",
            width=size[0],
            height=size[1] - 5,
            fg_color=["#D8D7DB", "#D8D7DB"],
            corner_radius=5,
        )

        self.img_label.grid_propagate(False)

        self.title_label = CTkLabel(
            master=self,
            text=title,
            text_color=["#000000", "white"],
            font=CTkFont("Arial", 20, weight="bold"),
        )
        self.title_label.grid(row=1, column=0)
        self.img_label.grid(row=0, column=0, pady=2)

        self.size = size
