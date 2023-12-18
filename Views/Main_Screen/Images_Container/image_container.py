from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFont
from PIL.Image import open


class ImageContainer(CTkFrame):
    def __init__(self, master, title: str):
        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0,
        )
        self.title = title
        self.create_children()
        self.place_children()

    def create_children(self):
        self.image_label = CTkLabel(
            master=self,
            text="",
            fg_color=["#e5e5e5", "#212121"],
            corner_radius=5,
        )
        self.size_label = CTkLabel(
            master=self,
            text="- x -    ratio= - : -",
            font=CTkFont("Inter", 14, weight="normal"),
        )
        self.title_label = CTkLabel(
            master=self,
            text=self.title,
            font=CTkFont("Inter", 24, weight="normal"),
            text_color=["black", "#DFDBDB"],
        )

    def place_children(self):
        self.image_label.place(relx=0, rely=0, relwidth=1, relheight=0.885)
        self.size_label.place(relx=0, rely=0.89, relwidth=1, relheight=0.04)
        self.title_label.place(relx=0, rely=0.9317, relwidth=1, relheight=0.0682)

    def label_size(self):
        return self.image_label.winfo_width(), self.image_label.winfo_height()
