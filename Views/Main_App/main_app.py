from tkinter import PhotoImage
from customtkinter import CTkFrame, CTkLabel, CTkImage, CTk, BOTH

import ctypes
from Views.Main_Screen.main_screen import MainScreen
from Views.Intro_Screen.intro_screen import IntroScreen


class MainApp(CTk):
    def __init__(self, title: str) -> None:
        CTk.__init__(self)
        self.wm_iconbitmap(PhotoImage("./Assets/icon.ico"))

        user32 = ctypes.windll.user32
        screen_width, screen_height = (
            user32.GetSystemMetrics(0),
            user32.GetSystemMetrics(1),
        )

        width, height = (int(screen_width * 0.7037), int(screen_height * 0.7037))
        print((width, height))
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)
        self.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
        self.title(title)
        self.intro: IntroScreen = IntroScreen(
            self, (width, height), 1, "./Assets/Intro Frame.png"
        )
        self.main: MainScreen = MainScreen(self, (width, height))

    def mainloop(self, *args, **kwargs) -> None:
        self.intro.pack(expand=True, fill=BOTH)
        self.after(self.intro.time, self.start_intro)
        self.overrideredirect(1)
        super().mainloop(*args, **kwargs)

    def start_intro(self) -> None:
        self.intro.destroy()
        self.overrideredirect(0)
        self.main.pack(expand=True, fill=BOTH)
