from ctypes import windll, byref, sizeof, c_int
from tkinter import PhotoImage
from customtkinter import (
    CTkFrame,
    CTkLabel,
    CTkImage,
    CTk,
    BOTH,
    AppearanceModeTracker,
    get_appearance_mode,
)
from Views.Main_Screen.main_screen import MainScreen
from Views.Intro_Screen.intro_screen import IntroScreen


class MainApp(CTk):
    def __init__(
        self,
        title: str,
        icon_path: str,
        intro_image_path: str,
        initial_size_ratio: float,
    ) -> None:
        super().__init__()

        self.set_window_properties(title, icon_path)
        self.set_window_geometry(initial_size_ratio)
        screen_width, screen_height = self.get_screen_dimensions()
        self.intro: IntroScreen = IntroScreen(
            self,
            intro_size=(
                int(screen_width * initial_size_ratio),
                int(screen_height * initial_size_ratio),
            ),
            image_path=intro_image_path,
        )
        self.main: MainScreen = MainScreen(self)

    def set_window_properties(self, title: str, icon_path: str) -> None:
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "Softawre Engineer.Mohamed Saeed.PixFy Desktop App.1.0"
        )
        self.title(title)
        self.iconbitmap(icon_path)
        # self.wm_iconbitmap(PhotoImage(icon_path))

    def set_window_geometry(self, initial_size_ratio: float) -> None:
        screen_width, screen_height = self.get_screen_dimensions()
        width, height = (
            int(screen_width * initial_size_ratio),
            int(screen_height * initial_size_ratio),
        )
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
        self.after(intro_time * 1000, self.start_intro)
        self.overrideredirect(1)
        super().mainloop(*args, **kwargs)

    def start_intro(self) -> None:
        self.intro.destroy()
        del self.intro
        self.intro = None
        self.overrideredirect(0)
        # region fix title color problem
        if get_appearance_mode() == "Dark":
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, 35, byref(c_int(0x000000)), sizeof(c_int)
            )
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, 36, byref(c_int(0x00FFFFFF)), sizeof(c_int)
            )
        # endregion
        self.main.pack(expand=True, fill=BOTH)
