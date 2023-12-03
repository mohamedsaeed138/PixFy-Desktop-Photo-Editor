from customtkinter import CTkSwitch, set_appearance_mode


class ThemeMode:
    def change_theme(widget):
        switch: CTkSwitch = widget
        if switch.get() == 1:
            set_appearance_mode("Dark")
            switch.configure(text="Light mode")

        else:
            set_appearance_mode("Light")
            switch.configure(text="Dark mode")
