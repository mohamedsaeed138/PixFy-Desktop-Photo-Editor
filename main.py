from Views.Main_App.main_app import MainApp
from customtkinter import set_appearance_mode, set_default_color_theme


def main():
    set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    set_default_color_theme("./violet-theme.json")  # Th
    root = MainApp(title="PixFy Photo Editor")
    root.mainloop()


if __name__ == "__main__":
    main()
