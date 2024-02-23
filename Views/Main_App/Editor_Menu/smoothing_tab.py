from customtkinter import CTkFont, CTkFrame, CTkLabel, IntVar, CTkRadioButton
from Presenter.presenter import Presenter
from Presenter.choice_enums import SmoothingChoice


class SmoothingTab(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "#212121"])
        self.presenter: Presenter = master.master.presenter

        self.create_children()
        self.place_children()

    def create_children(self):
        self.gaussian_label = CTkLabel(
            self, text="Gaussian Filter", font=CTkFont("Inter", 14), anchor="w"
        )
        self.box_label = CTkLabel(
            self,
            text="Box Filter",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.mean_label = CTkLabel(
            self,
            text="Mean Filter",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.median_label = CTkLabel(
            self,
            text="Median Filter",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.max_label = CTkLabel(
            self,
            text="Max Filter",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.min_label = CTkLabel(
            self,
            text="Min Filter",
            font=CTkFont("Inter", 14),
            anchor="w",
        )

        self.selected_var = IntVar(self, value=SmoothingChoice.Empty.value)
        self.was_selected = SmoothingChoice.Empty.value

        self.gaussian_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SmoothingChoice.Gaussian.value,
            text="",
            command=self.presenter.smoothing_handler,
        )
        self.box_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SmoothingChoice.Box.value,
            text="",
            command=self.presenter.smoothing_handler,
        )
        self.mean_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SmoothingChoice.Mean.value,
            text="",
            command=self.presenter.smoothing_handler,
        )
        self.median_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SmoothingChoice.Median.value,
            text="",
            command=self.presenter.smoothing_handler,
        )
        self.max_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SmoothingChoice.Max.value,
            text="",
            command=self.presenter.smoothing_handler,
        )
        self.min_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SmoothingChoice.Min.value,
            text="",
            command=self.presenter.smoothing_handler,
        )

    def place_children(self):
        self.gaussian_label.place(
            relwidth=0.229, relheight=0.138, relx=0.1197, rely=0.062
        )
        self.box_label.place(relwidth=0.229, relheight=0.138, relx=0.58, rely=0.062)
        self.mean_label.place(relwidth=0.229, relheight=0.138, relx=0.1197, rely=0.4275)
        self.median_label.place(relwidth=0.229, relheight=0.138, relx=0.58, rely=0.4275)
        self.max_label.place(relwidth=0.229, relheight=0.138, relx=0.1197, rely=0.8)
        self.min_label.place(relwidth=0.229, relheight=0.138, relx=0.58, rely=0.8)
        self.gaussian_radio_btn.place(relwidth=0.11, relx=0.3873, rely=0.069)
        self.box_radio_btn.place(relwidth=0.11, relx=0.8134, rely=0.062)
        self.mean_radio_btn.place(relwidth=0.11, relx=0.3873, rely=0.42)
        self.median_radio_btn.place(relwidth=0.11, relx=0.8134, rely=0.42)
        self.max_radio_btn.place(relwidth=0.11, relx=0.3873, rely=0.7655)
        self.min_radio_btn.place(relwidth=0.11, relx=0.8134, rely=0.7655)
