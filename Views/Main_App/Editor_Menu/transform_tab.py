from customtkinter import CTkFont, CTkButton, CTkFrame, CTkLabel, CTkEntry
from Presenter.presenter import Presenter


class TransformTab(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "#212121"])
        self.presenter: Presenter = master.master.presenter
        self.create_children()
        self.place_children()
        self.add_events()

    def create_children(self):
        self.rotate_label = CTkLabel(
            self, text="Rotate", font=CTkFont("Inter", 20), anchor="w"
        )
        self.resize_label = CTkLabel(
            self, text="Resize", font=CTkFont("Inter", 20), anchor="w"
        )
        self.translate_label = CTkLabel(
            self,
            text="Translate",
            font=CTkFont("Inter", 20),
            anchor="w",
        )

        self.rotate_angle_entry = CTkEntry(
            self,
            placeholder_text="degree",
            justify="center",
            border_color="black",
        )
        self.resize_width_entry = CTkEntry(
            self,
            placeholder_text="width",
            justify="center",
            border_color="black",
        )
        self.resize_height_entry = CTkEntry(
            self,
            placeholder_text="height",
            justify="center",
            border_color="black",
        )
        self.translate_x_entry = CTkEntry(
            self,
            placeholder_text="x",
            justify="center",
            border_color="black",
        )

        self.translate_y_entry = CTkEntry(
            self,
            placeholder_text="y",
            justify="center",
            border_color="black",
        )
        self.histogram_btn = CTkButton(
            self, text="Show Histogram", corner_radius=10, font=CTkFont("Inter", 15)
        )

    def place_children(self):
        self.rotate_label.place(
            relwidth=0.197, relheight=0.138, relx=0.1196, rely=0.089
        )
        self.resize_label.place(
            relwidth=0.197, relheight=0.138, relx=0.1196, rely=0.3172
        )
        self.translate_label.place(
            relwidth=0.197, relheight=0.138, relx=0.1196, rely=0.531
        )
        self.rotate_angle_entry.place(
            relwidth=0.1094, relheight=0.1655, relx=0.449, rely=0.0896
        )
        self.resize_width_entry.place(
            relwidth=0.1094, relheight=0.1655, relx=0.3861, rely=0.3034
        )
        self.resize_height_entry.place(
            relwidth=0.1094, relheight=0.1655, relx=0.503, rely=0.3034
        )
        self.translate_x_entry.place(
            relwidth=0.1094, relheight=0.1655, relx=0.3861, rely=0.531
        )
        self.translate_y_entry.place(
            relwidth=0.1094, relheight=0.1655, relx=0.503, rely=0.531
        )
        self.histogram_btn.place(
            relwidth=0.2265, relheight=0.22, relx=0.3861, rely=0.731
        )

    def add_events(self):
        self.histogram_btn.configure(command=self.presenter.histogram_handler)
        self.rotate_angle_entry.bind("<Return>", self.presenter.rotate_handler)
        self.rotate_angle_entry.bind("<FocusOut>", self.presenter.rotate_handler)
        self.resize_width_entry.bind(
            "<Return>", lambda _: self.presenter.resize_handler(True)
        )
        self.resize_width_entry.bind(
            "<FocusOut>", lambda _: self.presenter.resize_handler(True)
        )
        self.resize_height_entry.bind(
            "<Return>", lambda _: self.presenter.resize_handler(False)
        )
        self.resize_height_entry.bind(
            "<FocusOut>", lambda _: self.presenter.resize_handler(False)
        )

        self.translate_x_entry.bind(
            "<Return>", lambda _: self.presenter.translate_handler(True)
        )
        self.translate_x_entry.bind(
            "<FocusOut>", lambda _: self.presenter.translate_handler(True)
        )
        self.translate_y_entry.bind(
            "<Return>", lambda _: self.presenter.translate_handler(False)
        )
        self.translate_y_entry.bind(
            "<FocusOut>", lambda _: self.presenter.translate_handler(False)
        )
