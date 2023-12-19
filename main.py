from Views.Main_App.main_app import MainApp
from customtkinter import (
    set_appearance_mode,
    set_default_color_theme,
    get_appearance_mode,
)
from warnings import filterwarnings


# this app designed to work based on ratio =0.7037
def main() -> None:
    filterwarnings("ignore")
    set_appearance_mode(get_appearance_mode())
    set_default_color_theme("./violet-theme.json")  # Theme
    root = MainApp(
        title="PixFy Photo Editor",
        icon_path="./Assets/icon.ico",
        intro_image_path=f"./Assets/Intro Frame{' Dark'if get_appearance_mode()=='Dark' else ''}.png",
        initial_size_ratio=0.6,
    )

    root.mainloop(intro_time=4)


if __name__ == "__main__":
    main()
