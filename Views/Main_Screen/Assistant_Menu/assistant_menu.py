from customtkinter import CTkFrame, CTkButton, CTkSwitch, CTkFont, set_appearance_mode


class AssistantMenu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=10)
        self.presenter = master.presenter
        self.create_children()
        self.place_children()
        self.add_events()

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
            command=lambda: set_appearance_mode("Dark")
            if self.theme_switch.get() == 1
            else set_appearance_mode("Light"),
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
