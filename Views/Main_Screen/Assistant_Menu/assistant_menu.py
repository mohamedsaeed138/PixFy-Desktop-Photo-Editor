from customtkinter import CTkFrame, CTkButton, CTkSwitch, CTkFont
from Controller.theme_mode import ThemeMode
from Controller.upload_image import UploadImage


class AssistantMenu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)
        self.create_children()
        self.place_children()

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
            command=lambda: ThemeMode.change_theme(self.theme_switch),
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
