from customtkinter import CTkFrame, CTkButton, CTkSwitch
from Controller.theme_mode import ThemeMode
from Controller.upload_image import UploadImage


class AssistantMenu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["#EAEAEA", "white"])
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.grid_rowconfigure((0), weight=1, uniform="a")
        self.grid_propagate(False)
        self.upload_btn = CTkButton(
            self,
            text="Upload Image",
            corner_radius=7,
        )
        self.upload_btn.grid(row=0, column=0, sticky="nsew", padx=(30, 20), pady=9)
        self.save_btn = CTkButton(
            self,
            text="Save",
            corner_radius=7,
        )
        self.save_btn.grid(row=0, column=1, sticky="nsew", padx=15, pady=9)
        self.theme_switch = CTkSwitch(
            master=self,
            text="Dark mode",
            command=lambda: ThemeMode.change_theme(self.theme_switch),
        )
        self.theme_switch.grid(row=0, column=2, sticky="nsew", padx=(15, 20))
