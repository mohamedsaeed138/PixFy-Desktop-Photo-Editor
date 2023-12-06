from customtkinter import CTkFrame, CTkLabel, CTkImage
import customtkinter as ctk
from Views.Main_Screen.Assistant_Menu.assistant_menu import AssistantMenu
from Views.Main_Screen.Images_Container.image_container import ImageContainer
from Views.Main_Screen.Images_Container.dnd_image_container import DNDImageContainer
from Views.Main_Screen.Editor_Menu.editor_menu import EditorMenu
from Controller.upload_image import UploadImage
from tkinterdnd2 import TkinterDnD, DND_ALL


class MainScreen(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "black"])
        self.original_image_container = DNDImageContainer(self, "Original")
        self.edited_image_container = ImageContainer(self, "After")
        self.original_image_container.place(
            relx=0.02072, rely=0.03684, relwidth=0.4722, relheight=0.5592
        )
        self.edited_image_container.place(
            relx=0.507, rely=0.03684, relwidth=0.4722, relheight=0.5592
        )

        self.assistant_menu = AssistantMenu(self)
        self.assistant_menu.place(
            relx=0.305, rely=0.615, relwidth=0.39, relheight=0.076
        )

        self.editor_menu = EditorMenu(self)
        self.editor_menu.place(relx=0.2072, rely=0.7184, relwidth=0.585, relheight=0.26)

        self.assistant_menu.upload_btn.configure(
            command=lambda: UploadImage.upload_image(
                self.original_image_container,
                self.edited_image_container,
                self.original_image_container.label_size(),
            )
        )
        self.original_image_container.image_label.drop_target_register(DND_ALL)
        self.original_image_container.image_label.dnd_bind(
            "<<Drop>>",
            lambda event: UploadImage.drop_image(
                event,
                self.original_image_container.image_label,
                self.edited_image_container.image_label,
                self.original_image_container.label_size(),
            ),
        )
