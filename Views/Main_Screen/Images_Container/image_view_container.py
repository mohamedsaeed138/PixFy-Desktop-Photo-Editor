from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFont
from PIL.Image import open


class ImageViewContainer(CTkFrame):
    def __init__(self, master, size: tuple[int, int], title: str):
        super().__init__(
            master,
            fg_color=["white", "#D8D7DB"],
            width=size[0],
            height=size[1],
            corner_radius=5,
        )
        # logic controller part
        self.path: str
        self.image = open(r"C:\Users\mohamed\Downloads\Vector.png")
        self.image.thumbnail((size[0], size[1] - 5))

        self.photo_image = CTkImage(self.image, self.image, size=self.image.size)
        self.img_label = CTkLabel(
            master=self,
            text="",
            width=size[0],
            height=size[1] - 5,
            fg_color=["#D8D7DB", "#D8D7DB"],
            corner_radius=5,
        )
        self.title_label = CTkLabel(
            master=self,
            text=title,
            text_color=["#000000", "white"],
            font=CTkFont("Arial", 20, weight="bold"),
        )
        self.title_label.grid(row=1, column=0)
        self.img_label.grid(row=0, column=0, pady=2)
        # logic controller part
        # self.img_label.configure(image=self.photo_image)
        # self.img_label.image = self.photo_image  # type: ignore
