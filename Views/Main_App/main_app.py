from platform import uname
from PIL.ImageTk import PhotoImage
from PIL.Image import open
from customtkinter import CTk
from Model.image_model import ImageModel
from Presenter.presenter import Presenter
from Views.Main_App.Assistant_Menu.assistant_menu import AssistantMenu
from Views.Main_App.Images_Container.image_container import ImageContainer
from Views.Main_App.Images_Container.dnd_image_container import DNDImageContainer
from Views.Main_App.Editor_Menu.editor_menu import EditorMenu


class MainApp(CTk):
    def __init__(
        self,
        title: str,
        icon_path: str,
        initial_size_ratio: float | tuple[float, float] = 0.7037,
    ):
        super().__init__()
        self.windows_title = title
        self.icon_path = icon_path
        self.ratio = initial_size_ratio
        self.size = self.get_size()
        self.position = self.get_position()
        self.geometry(
            f"{self.size[0]}x{self.size[1]}+{self.position[0]}+{self.position[1]}"
        )
        self.set_window_properties()
        self.presenter = Presenter(model=ImageModel(), view=self)
        self.create_children()
        self.place_children()

    def create_children(self):
        self.original_image_container = DNDImageContainer(self, "Original")
        self.edited_image_container = ImageContainer(self, "After")
        self.assistant_menu = AssistantMenu(self)
        self.editor_menu = EditorMenu(self, disabled=True)

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

    def rebuild_editor_menu(self):
        self.editor_menu.destroy()
        del self.editor_menu
        self.editor_menu = EditorMenu(self, disabled=False)
        self.editor_menu.place(relx=0.2072, rely=0.7184, relwidth=0.585, relheight=0.26)

    def set_window_properties(self) -> None:
        self.title(self.windows_title)
        if uname()[0] == "Windows":
            from ctypes import windll

            windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                "Softawre Engineer.Mohamed Saeed.PixFy Desktop App.1.0"
            )
            self.iconbitmap(self.icon_path)
        elif uname()[0] == "Linux":
            self.wm_iconphoto(False, PhotoImage(open(self.icon_path)))

    def get_size(self) -> tuple[int, int]:
        if self.ratio is tuple[float, float]:
            width_ratio, height_ratio = self.ratio
        elif self.ratio is tuple and len(self.ratio) == 1:
            width_ratio = height_ratio = self.ratio[0]
        else:
            width_ratio = height_ratio = self.ratio
        return (
            int(self.winfo_screenwidth() * width_ratio * 1.25),
            int(self.winfo_screenheight() * height_ratio * 1.25),
        )

    def get_position(self) -> tuple[int, int]:
        x = (self.winfo_screenwidth() / 2) - (self.size[0] / 2)
        y = (self.winfo_screenheight() / 2) - (self.size[1] / 2)
        return int(x), int(y) - 25
