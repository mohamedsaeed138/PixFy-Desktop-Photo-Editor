from ctypes import byref, c_int, sizeof, windll
from customtkinter import (
    CTkFrame,
    CTkButton,
    CTkSwitch,
    CTkFont,
    set_appearance_mode,
    get_appearance_mode,
)


class AssistantMenu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)
        self.HWND = windll.user32.GetParent(self.master.master.winfo_id())
        self.presenter = master.presenter
        self.create_children()
        self.place_children()
        self.add_events()
        if get_appearance_mode() == "Dark":
            self.theme_switch.select()

    def create_children(self):
        self.upload_btn = CTkButton(
            self,
            text="Upload",
            corner_radius=10,
            font=CTkFont(family="Arial", size=15),
        )
        self.save_btn = CTkButton(
            self,
            text="Save",
            corner_radius=10,
            font=CTkFont(family="Arial", size=15),
        )

        self.theme_switch = CTkSwitch(
            master=self,
            text="Dark mode",
            command=self.handle_theme,
            font=CTkFont(family="Arial", size=15),
        )

    def place_children(self):
        self.upload_btn.place(
            relx=0.0246, rely=0.224, relwidth=0.3068, relheight=0.5517
        )
        self.save_btn.place(relx=0.346, rely=0.224, relwidth=0.3068, relheight=0.5517)
        self.theme_switch.place(
            relx=0.671, rely=0.224, relwidth=0.3068, relheight=0.5517
        )

    def add_events(self):
        self.upload_btn.configure(command=self.presenter.upload_image)
        self.save_btn.configure(command=self.presenter.save_image)

    def handle_theme(self):
        HWND = windll.user32.GetParent(self.master.master.winfo_id())
        text_color, bg_color = 0x000000, 0x00FFFFFF
        mode = "Light"
        if self.theme_switch.get() == 1:
            mode = "Dark"
            text_color, bg_color = bg_color, text_color
        windll.dwmapi.DwmSetWindowAttribute(
            HWND, 35, byref(c_int(bg_color)), sizeof(c_int)
        )
        windll.dwmapi.DwmSetWindowAttribute(
            HWND, 36, byref(c_int(text_color)), sizeof(c_int)
        )
        set_appearance_mode(mode)
