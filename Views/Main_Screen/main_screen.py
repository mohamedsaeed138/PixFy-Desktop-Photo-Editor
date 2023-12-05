from customtkinter import CTkFrame, CTkLabel, CTkImage
import customtkinter as ctk
from Views.Main_Screen.Assistant_Menu.assistant_menu import AssistantMenu
from Views.Main_Screen.Images_Container.image_container import ImageContainer
from Views.Main_Screen.Images_Container.dnd_image_container import DNDImageContainer
from Views.Main_Screen.Editor_Menu.editor_menu import EditorMenu
from Controller.upload_image import UploadImage
from tkinterdnd2 import TkinterDnD, DND_ALL


class MainScreen(CTkFrame):
    def __init__(self, master, master_size: tuple[int, int]):
        super().__init__(master, fg_color=["white", "black"])
        self.original_image_container = ImageContainer(self, "Original")
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
        self.editor_menu.place(relx=0.207, rely=0.718, relwidth=0.585, relheight=0.26)

        # self.assistant_menu.upload_btn.configure(
        #     command=lambda: UploadImage.upload_image(
        #         self.images_container.original_image_container,
        #         self.images_container.edited_image_container,
        #         (self.images_container.edited_image_container.label_size()),
        #     )
        # )
        # self.images_container.original_image_container.img_label.drop_target_register(
        #     DND_ALL
        # )
        # self.images_container.original_image_container.img_label.dnd_bind(
        #     "<<Drop>>",
        #     lambda event: UploadImage.drop_image(
        #         event,
        #         self.images_container.original_image_container,
        #         self.images_container.edited_image_container,
        #         (self.images_container.edited_image_container.label_size()),
        #     ),
        # )
