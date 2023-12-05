from customtkinter import CTkFrame, CTkLabel, CTkImage
import customtkinter as ctk
from Views.Main_Screen.Assistant_Menu.assistant_menu import AssistantMenu
from Views.Main_Screen.Images_Container.images_container import ImagesContainer
from Views.Main_Screen.Editor_Menu.editor_menu import EditorMenu
from Controller.upload_image import UploadImage
from tkinterdnd2 import TkinterDnD, DND_ALL


class MainScreen(CTkFrame):
    def __init__(self, master, master_size: tuple[int, int]):
        super().__init__(master, fg_color=["white", "#ffffff"])
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform="a")
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform="a")

        self.images_container = ImagesContainer(self)
        self.images_container.grid(
            row=0, column=0, rowspan=6, columnspan=10, padx=6, pady=6, sticky="nsew"
        )

        self.assistant_menu = AssistantMenu(self)
        self.assistant_menu.grid(row=6, column=3, columnspan=4, sticky="nsew", pady=14)

        self.editor_menu = EditorMenu(self)
        self.editor_menu.grid(row=7, column=2, rowspan=3, columnspan=6, sticky="nsew")

        self.assistant_menu.upload_btn.configure(
            command=lambda: UploadImage.upload_image(
                self.images_container.original_image_container,
                self.images_container.edited_image_container,
                (self.images_container.edited_image_container.size),
            )
        )
        self.images_container.original_image_container.img_label.drop_target_register(
            DND_ALL
        )
        self.images_container.original_image_container.img_label.dnd_bind(
            "<<Drop>>",
            lambda event: UploadImage.drop_image(
                event,
                self.images_container.original_image_container,
                self.images_container.edited_image_container,
                (self.images_container.edited_image_container.size),
            ),
        )
