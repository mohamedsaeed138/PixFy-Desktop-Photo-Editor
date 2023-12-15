from Views.Main_App.main_app import MainApp
from customtkinter import (
    get_appearance_mode,
    set_appearance_mode,
    set_default_color_theme,
)
from warnings import filterwarnings


def main() -> None:
    filterwarnings("ignore")  # Modes: "System" (standard), "Dark", "Light"
    set_appearance_mode("Light")
    set_default_color_theme("./violet-theme.json")  # Theme
    root = MainApp(
        title="PixFy Photo Editor",
        icon_path="./Assets/icon.ico",
        intro_image_path="./Assets/Intro Frame.png",
    )

    root.mainloop(10000)


if __name__ == "__main__":
    main()
