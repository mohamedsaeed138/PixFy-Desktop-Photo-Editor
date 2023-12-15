from ctypes import windll
from tkinter import PhotoImage
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkImage,
    CTk,
    BOTH,
    AppearanceModeTracker,
)
from Views.Main_Screen.main_screen import MainScreen
from Views.Intro_Screen.intro_screen import IntroScreen


class MainApp(CTk):
    def __init__(self, title: str, icon_path: str, intro_image_path: str) -> None:
        super().__init__()
        self.set_window_properties(title, icon_path)
        self.set_window_geometry()
        self.intro: IntroScreen = IntroScreen(
            self,
            master_size=(
                int(self.get_screen_dimensions()[0] * 0.7037),
                int(self.get_screen_dimensions()[1] * 0.7037),
            ),
            image_path=intro_image_path,
        )
        print(
            int(self.get_screen_dimensions()[0] * 0.7037),
            int(self.get_screen_dimensions()[1] * 0.7037),
        )
        self.main: MainScreen = MainScreen(self)

    def set_window_properties(self, title: str, icon_path: str) -> None:
        self.title(title)
        self.wm_iconbitmap(PhotoImage(icon_path))

    def set_window_geometry(self) -> None:
        screen_width, screen_height = self.get_screen_dimensions()
        width, height = int(screen_width * 0.7037), int(screen_height * 0.7037)
        x_coordinate, y_coordinate = self.calculate_window_position(width, height)
        self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    def get_screen_dimensions(self) -> tuple[int, int]:
        user32 = windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    def calculate_window_position(self, width: int, height: int) -> tuple[int, int]:
        screen_width, screen_height = (
            self.winfo_screenwidth(),
            self.winfo_screenheight(),
        )
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)
        return int(x_coordinate), int(y_coordinate)

    def mainloop(self, intro_time: int = 0, *args, **kwargs) -> None:
        self.intro.pack(expand=True, fill=BOTH)
        self.after(intro_time, self.start_intro)
        self.overrideredirect(1)
        super().mainloop(*args, **kwargs)

    def start_intro(self) -> None:
        self.intro.destroy()
        del self.intro
        self.intro = None
        self.overrideredirect(0)
        self.main.pack(expand=True, fill=BOTH)
