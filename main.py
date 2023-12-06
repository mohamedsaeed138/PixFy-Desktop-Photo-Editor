from Views.Intro_Screen.intro_screen import IntroScreen
from Views.Main_App.main_app import MainApp
from customtkinter import set_appearance_mode, set_default_color_theme


def main():
    set_appearance_mode("White")  # Modes: "System" (standard), "Dark", "Light"
    set_default_color_theme("./violet-theme.json")  # Th
    root = MainApp(
        title="PixFy Photo Editor",
        icon_path="./Assets/icon.ico",
        intro_image_path="./Assets/Intro Frame.png",
    )
    root.mainloop(intro_time=3000)


if __name__ == "__main__":
    main()
