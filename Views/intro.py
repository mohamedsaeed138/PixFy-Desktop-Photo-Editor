from tkinter import Tk, BOTH, Label
from PIL.Image import open, LANCZOS
from PIL.ImageOps import contain
from PIL.ImageTk import PhotoImage
from Views.Main_App.main_app import MainApp
from resource_path import resource_path


class Intro(Tk):
    def __init__(
        self,
        intro_image_path: str,
        color: str,
        ratio: float | tuple[float, float] = 0.5,
        duration: float = 0,
    ):
        super().__init__()
        self.overrideredirect(1)
        self.image_path = intro_image_path
        self.color = color
        self.ratio = ratio
        self.duration = duration
        self.size = self.get_size()
        self.position = self.get_position()
        self.geometry(
            f"{self.size[0]}x{self.size[1]}+{self.position[0]}+{self.position[1]}"
        )
        self.setup_intro_label()

    def get_size(self) -> tuple[int, int]:
        if self.ratio is tuple[float, float]:
            width_ratio, height_ratio = self.ratio
        elif self.ratio is tuple and len(self.ratio) == 1:
            width_ratio = height_ratio = self.ratio[0]
        else:
            width_ratio = height_ratio = self.ratio
        return (
            int(self.winfo_screenwidth() * width_ratio * 1.25),
            int(self.winfo_screenheight() * height_ratio * 1.25),
        )

    def get_position(self) -> tuple[int, int]:
        x = (self.winfo_screenwidth() / 2) - (self.size[0] / 2)
        y = (self.winfo_screenheight() / 2) - (self.size[1] / 2)
        return int(x), int(y)

    def setup_intro_label(self) -> None:
        self.intro_image = PhotoImage(
            contain(open(self.image_path), self.size, LANCZOS)
        )
        self.image_label = Label(
            self,
            image=self.intro_image,
            bg=self.color,
        )
        self.image_label.pack(expand=True, fill=BOTH)

    def mainloop(self, n: int = 0) -> None:
        self.after(self.duration * 1000, self.start_app)
        return super().mainloop(n)

    def start_app(self):
        self.destroy()
        main_app = MainApp(
            "PixFy Photo Editor", resource_path(".\\Assets\\icon.ico"), 0.7037
        )
        main_app.mainloop()
