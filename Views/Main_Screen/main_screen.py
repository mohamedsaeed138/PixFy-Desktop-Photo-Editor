from customtkinter import CTkFrame, CTkLabel, CTkImage
import customtkinter as ctk
from Views.Main_Screen.Assistant_Menu.assistant_menu import AssistantMenu
from Views.Main_Screen.Images_Container.images_container import ImagesContainer
from Views.Main_Screen.Editor_Menu.editor_menu import EditorMenu


class MainScreen(CTkFrame):
    def __init__(self, master, master_size: tuple[int, int]):
        super().__init__(master, fg_color=["#ffffff", "#ffffff"])
        self.grid_rowconfigure(list(range(0, 10)), pad=20)
        self.grid_columnconfigure(list(range(0, 10)), pad=20)

        self.images_container = ImagesContainer(
            self, size=(master_size[0] - 20, master_size[1] * 0.6 - 20)
        )
        self.images_container.grid(row=0, column=0, rowspan=6, columnspan=10, padx=6)

        self.assistant_menu = AssistantMenu(
            self, size=(master_size[0] * 0.4, master_size[1] * (3.55 / 45.5))
        )
        self.assistant_menu.grid(row=6, column=3, columnspan=4)

        self.editor_menu = EditorMenu(
            self, size=(master_size[0] * 0.6, master_size[1] * 0.281)
        )
        self.editor_menu.grid(row=7, column=2, rowspan=3, columnspan=6)
