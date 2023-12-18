from customtkinter import CTkFont, CTkFrame, CTkLabel, IntVar, CTkRadioButton, CTkEntry
from Presenter.presenter import Presenter
from Presenter.choice_enums import NoiseChoice


class NoiseTab(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "#212121"])
        self.presenter: Presenter = master.master.presenter

        self.create_children()
        self.place_children()
        self.add_events()

    def create_children(self):
        self.gaussian_label = CTkLabel(
            self, text="Gaussian Noise", font=CTkFont("Inter", 20), anchor="w"
        )
        self.sp_label = CTkLabel(
            self, text="S&P Noise", font=CTkFont("Inter", 20), anchor="w"
        )
        self.sp_amount_entry = CTkEntry(
            self,
            justify="center",
            border_color="black",
            placeholder_text="(0 - 1)",
            state="disabled",
        )
        self.selected_var = IntVar(self, value=NoiseChoice.Empty.value)
        self.was_selected = NoiseChoice.Empty.value

        self.gaussian_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=NoiseChoice.Gaussian.value,
            text="",
            command=self.presenter.noise_handler,
        )
        self.sp_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=NoiseChoice.SP.value,
            text="",
            command=self.presenter.noise_handler,
        )

    def place_children(self):
        self.gaussian_label.place(
            relwidth=0.3848, relheight=0.138, relx=0.166, rely=0.1724
        )
        self.sp_label.place(relwidth=0.21879, relheight=0.138, relx=0.166, rely=0.7)
        self.sp_amount_entry.place(
            relwidth=0.119, relheight=0.1655, relx=0.422, rely=0.71
        )
        self.gaussian_radio_btn.place(relwidth=0.3, relx=0.59, rely=0.158)
        self.sp_radio_btn.place(relwidth=0.3, relx=0.59, rely=0.7)

    def add_events(self):
        self.sp_amount_entry.bind("<FocusOut>", self.presenter.sp_handler)
        self.sp_amount_entry.bind("<Return>", self.presenter.sp_handler)
