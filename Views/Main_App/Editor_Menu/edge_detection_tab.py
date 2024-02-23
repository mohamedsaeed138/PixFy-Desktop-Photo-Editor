from customtkinter import CTkFont, CTkFrame, CTkLabel, IntVar, CTkRadioButton
from Presenter.presenter import Presenter
from Presenter.choice_enums import EdgeDetectionChoice


class EdgeDetectionTab(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "#212121"])
        self.presenter: Presenter = master.master.presenter

        self.create_children()
        self.place_children()

    def create_children(self):
        self.canny_label = CTkLabel(
            self, text="Canny", font=CTkFont("Inter", 14), anchor="w"
        )
        self.sobelxy_label = CTkLabel(
            self,
            text="Sobel XY",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.sobelx_label = CTkLabel(
            self,
            text="Sobel X",
            font=CTkFont("Inter", 14),
            anchor="w",
        )
        self.sobely_label = CTkLabel(
            self,
            text="Sobel Y",
            font=CTkFont("Inter", 14),
            anchor="w",
        )

        self.selected_var = IntVar(self, value=EdgeDetectionChoice.Empty.value)
        self.was_selected = EdgeDetectionChoice.Empty.value

        self.canny_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=EdgeDetectionChoice.Canny.value,
            text="",
            command=self.presenter.edge_handler,
        )
        self.sobelxy_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=EdgeDetectionChoice.SobelXY.value,
            text="",
            command=self.presenter.edge_handler,
        )
        self.sobelx_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=EdgeDetectionChoice.SobelX.value,
            text="",
            command=self.presenter.edge_handler,
        )
        self.sobely_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=EdgeDetectionChoice.SobelY.value,
            text="",
            command=self.presenter.edge_handler,
        )

    def place_children(self):
        self.canny_label.place(relwidth=0.229, relheight=0.138, relx=0.1184, rely=0.22)
        self.sobelxy_label.place(relwidth=0.229, relheight=0.138, relx=0.58, rely=0.22)
        self.sobelx_label.place(
            relwidth=0.229, relheight=0.138, relx=0.1184, rely=0.634
        )
        self.sobely_label.place(relwidth=0.229, relheight=0.138, relx=0.58, rely=0.634)

        self.canny_radio_btn.place(relwidth=0.11, relx=0.3873, rely=0.234)
        self.sobelxy_radio_btn.place(relwidth=0.11, relx=0.8134, rely=0.234)
        self.sobelx_radio_btn.place(relwidth=0.11, relx=0.3873, rely=0.618)
        self.sobely_radio_btn.place(relwidth=0.11, relx=0.8134, rely=0.618)
