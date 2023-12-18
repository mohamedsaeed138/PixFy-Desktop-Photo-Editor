from customtkinter import (
    CTkFont,
    CTkFrame,
    CTkLabel,
    CTkEntry,
    IntVar,
    CTkRadioButton,
    CTkSwitch,
)

from Presenter.presenter import Presenter
from Presenter.choice_enums import GrayTabChoice


class GrayFiltersTab(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "#212121"])
        self.presenter: Presenter = master.master.presenter

        self.create_children()
        self.place_children()

    def create_children(self):
        self.gray_label = CTkLabel(
            self, text="Gray Scale", font=CTkFont("Inter", 14), anchor="w"
        )
        self.gray_switch = CTkSwitch(self, text="", command=self.presenter.gray_handler)
        self.threshold_label = CTkLabel(
            self,
            text="Threshold",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.negative_label = CTkLabel(
            self,
            text="Negative",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.stretching_label = CTkLabel(
            self,
            text="Contrast Stretching",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.equalize_label = CTkLabel(
            self,
            text="Histogram Equalization",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.log_label = CTkLabel(
            self,
            text="Log Transform",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.power_label = CTkLabel(
            self,
            text="Power Law",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.threshold_entry = CTkEntry(
            self,
            justify="center",
            border_color="black",
            placeholder_text="(0 - 255)",
            state="disabled",
        )
        self.selected_var = IntVar(self, value=GrayTabChoice.Empty.value)
        self.was_selected = GrayTabChoice.Empty.value

        self.threshold_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=GrayTabChoice.Threshold.value,
            text="",
            command=self.presenter.gray_radio_handler,
        )
        self.negative_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=GrayTabChoice.Negative.value,
            text="",
            command=self.presenter.gray_radio_handler,
        )
        self.stretching_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=GrayTabChoice.Stretching.value,
            text="",
            command=self.presenter.gray_radio_handler,
        )
        self.equalization_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=GrayTabChoice.Equalization.value,
            text="",
            command=self.presenter.gray_radio_handler,
        )
        self.log_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=GrayTabChoice.LogTransform.value,
            text="",
            command=self.presenter.gray_radio_handler,
        )
        self.power_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=GrayTabChoice.PowerLaw.value,
            text="",
            command=self.presenter.gray_radio_handler,
        )

    def place_children(self):
        self.gray_label.place(relwidth=0.229, relheight=0.138, relx=0.1197, rely=0.0896)
        self.gray_switch.place(relx=0.3873, rely=0.0758)
        self.threshold_label.place(
            relwidth=0.1003, relheight=0.138, relx=0.12, rely=0.317
        )
        self.threshold_entry.place(
            relwidth=0.109, relheight=0.131, relx=0.23, rely=0.324
        )

        self.negative_label.place(
            relwidth=0.229, relheight=0.138, relx=0.547, rely=0.324
        )

        self.stretching_label.place(
            relwidth=0.229, relheight=0.138, relx=0.1197, rely=0.5448
        )
        self.equalize_label.place(
            relwidth=0.229, relheight=0.138, relx=0.547, rely=0.5448
        )
        self.log_label.place(relwidth=0.229, relheight=0.138, relx=0.1197, rely=0.7724)
        self.power_label.place(relwidth=0.229, relheight=0.138, relx=0.547, rely=0.7724)
        self.threshold_radio_btn.place(relwidth=0.11, relx=0.387, rely=0.31)
        self.negative_radio_btn.place(relwidth=0.11, relx=0.7966, rely=0.31)
        self.stretching_radio_btn.place(relwidth=0.11, relx=0.387, rely=0.538)
        self.equalization_radio_btn.place(relwidth=0.11, relx=0.7966, rely=0.538)
        self.log_radio_btn.place(relwidth=0.11, relx=0.387, rely=0.751)
        self.power_radio_btn.place(relwidth=0.11, relx=0.7966, rely=0.751)
        self.threshold_entry.bind("<FocusOut>", self.presenter.threshold_handler)
        self.threshold_entry.bind("<Return>", self.presenter.threshold_handler)
