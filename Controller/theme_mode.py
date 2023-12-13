from customtkinter import CTkSwitch, set_appearance_mode


class ThemeMode:
    def change_theme(widget):
        switch: CTkSwitch = widget
        if switch.get() == 1:
            set_appearance_mode("Dark")
        else:
            set_appearance_mode("Light")
