from Views.intro import Intro
from customtkinter import (
    set_appearance_mode,
    set_default_color_theme,
    get_appearance_mode,
)
from resource_path import resource_path
from warnings import filterwarnings


# this main app designed to work based on ratio =0.7037
def main() -> None:
    filterwarnings("ignore")
    mode = get_appearance_mode()
    set_appearance_mode(mode)
    set_default_color_theme(resource_path(".\\Assets\\violet-theme.json"))
    if mode == "Dark":
        intro_image_path = resource_path(".\\Assets\\Intro Frame Dark.png")
    else:
        intro_image_path = resource_path(".\\Assets\\Intro Frame.png")
    intro = Intro(
        intro_image_path=intro_image_path,
        ratio=0.55,
        duration=4,
        color="black" if mode == "Dark" else "white",
    )
    intro.mainloop()


if __name__ == "__main__":
    main()
