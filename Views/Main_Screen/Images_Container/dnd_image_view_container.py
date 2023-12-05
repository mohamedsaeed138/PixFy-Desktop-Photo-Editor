from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFont
from tkinterdnd2 import TkinterDnD, DND_ALL
from PIL.Image import open


class DNDImageViewContainer(CTkFrame, TkinterDnD.DnDWrapper):
    def __init__(self, master, title: str):
        super().__init__(
            master,
            fg_color=["white", "#D8D7DB"],
            corner_radius=5,
        )
        self.TkdndVersion = TkinterDnD._require(self)
        self.grid_rowconfigure(list(range(0, 20)), weight=1, uniform=1)
        self.grid_columnconfigure((0), weight=1, uniform=1)
        self.img_label = CTkLabel(
            master=self,
            text="",
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
        self.img_label.grid(row=0, column=0, rowspan=19, pady=2, sticky="nsew")
        self.title_label.grid(row=19, column=0, sticky="nsew")

        self.size = (100, 100)
