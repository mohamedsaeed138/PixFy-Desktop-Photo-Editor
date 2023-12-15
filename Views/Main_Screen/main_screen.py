from customtkinter import CTkFrame, CTkLabel, CTkImage
import customtkinter as ctk
from Model.image_Model import ImageModel
from Presenter.presenter import Presenter
from Views.Main_Screen.Assistant_Menu.assistant_menu import AssistantMenu
from Views.Main_Screen.Images_Container.image_container import ImageContainer
from Views.Main_Screen.Images_Container.dnd_image_container import DNDImageContainer
from Views.Main_Screen.Editor_Menu.editor_menu import EditorMenu
from customtkinter import get_appearance_mode, set_appearance_mode


class MainScreen(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=["white", "black"])
        self.presenter = Presenter(model=ImageModel(), view=self)
        self.create_children()
        self.place_children()

    def create_children(self):
        self.original_image_container = DNDImageContainer(self, "Original")
        self.edited_image_container = ImageContainer(self, "After")
        self.assistant_menu = AssistantMenu(self)
        self.editor_menu = EditorMenu(self)

    def place_children(self):
        self.original_image_container.place(
            relx=0.02072, rely=0.03684, relwidth=0.4722, relheight=0.5592
        )
        self.edited_image_container.place(
            relx=0.507, rely=0.03684, relwidth=0.4722, relheight=0.5592
        )
        self.assistant_menu.place(
            relx=0.305, rely=0.615, relwidth=0.39, relheight=0.076
        )
        self.editor_menu.place(relx=0.2072, rely=0.7184, relwidth=0.585, relheight=0.26)
