from customtkinter import CTkFont, CTkFrame, CTkLabel, IntVar, CTkRadioButton
from Presenter.presenter import Presenter
from Presenter.choice_enums import SharpeningChoice


class SharpeningTab(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "#212121"])
        self.presenter: Presenter = master.master.presenter

        self.create_children()
        self.place_children()

    def create_children(self):
        self.laplacian_lapel = CTkLabel(
            self, text="Laplacian Filter", font=CTkFont("Inter", 20), anchor="w"
        )
        self.composite_laplacian1_lapel = CTkLabel(
            self,
            text="Composite Laplacian 1",
            font=CTkFont("Inter", 20),
            anchor="w",
        )
        self.composite_laplacian2_lapel = CTkLabel(
            self, text="Composite Laplacian 2", font=CTkFont("Inter", 20), anchor="w"
        )

        self.selected_var = IntVar(self, value=SharpeningChoice.Empty.value)
        self.was_selected = SharpeningChoice.Empty.value

        self.laplacian_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SharpeningChoice.Laplacian.value,
            text="",
            command=self.presenter.sharpening_handler,
        )
        self.composite_laplacian1_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SharpeningChoice.CompositeLaplacian1.value,
            text="",
            command=self.presenter.sharpening_handler,
        )
        self.composite_laplacian2_radio_btn = CTkRadioButton(
            self,
            variable=self.selected_var,
            value=SharpeningChoice.CompositeLaplacian2.value,
            text="",
            command=self.presenter.sharpening_handler,
        )

    def place_children(self):
        self.laplacian_lapel.place(
            relwidth=0.3848, relheight=0.138, relx=0.204, rely=0.09
        )
        self.composite_laplacian1_lapel.place(
            relwidth=0.3848, relheight=0.138, relx=0.204, rely=0.4
        )
        self.composite_laplacian2_lapel.place(
            relwidth=0.3848, relheight=0.138, relx=0.204, rely=0.717
        )
        self.laplacian_radio_btn.place(relwidth=0.302, relx=0.615, rely=0.0896)
        self.composite_laplacian1_radio_btn.place(relwidth=0.302, relx=0.615, rely=0.4)
        self.composite_laplacian2_radio_btn.place(
            relwidth=0.302, relx=0.615, rely=0.703
        )
