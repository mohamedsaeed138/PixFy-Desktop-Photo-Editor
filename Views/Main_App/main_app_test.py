from ctypes import windll
from tkinter import PhotoImage
from customtkinter import CTkFrame, CTkLabel, CTkImage, CTk, BOTH
from Controller.upload_image import UploadImage
from Views.Main_Screen.Assistant_Menu.assistant_menu import AssistantMenu
from Views.Main_Screen.Editor_Menu.editor_menu import EditorMenu
from Views.Main_Screen.Images_Container.dnd_image_container import DNDImageContainer
from Views.Main_Screen.Images_Container.image_container import ImageContainer
from Views.Main_Screen.main_screen import MainScreen
from Views.Intro_Screen.intro_screen import IntroScreen
from tkinterdnd2 import DND_ALL


class MainApp(CTk):
    def __init__(self, title: str, icon_path: str, intro_image_path: str) -> None:
        super().__init__()

        self.set_window_properties(title, icon_path)
        self.set_window_geometry()

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
        self.intro: IntroScreen = IntroScreen(
            self, master_size=self.get_screen_dimensions(), image_path=intro_image_path
        )

    def set_window_properties(self, title: str, icon_path: str) -> None:
        self.title(title)
        self.wm_iconbitmap(PhotoImage(icon_path))

    def set_window_geometry(self) -> None:
        screen_width, screen_height = self.get_screen_dimensions()
        width, height = int(screen_width * 0.7037), int(screen_height * 0.7037)
        x_coordinate, y_coordinate = self.calculate_window_position(width, height)
        self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    def get_screen_dimensions(self) -> tuple[int, int]:
        user32 = windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    def calculate_window_position(self, width: int, height: int) -> tuple[int, int]:
        screen_width, screen_height = (
            self.winfo_screenwidth(),
            self.winfo_screenheight(),
        )
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)
        return int(x_coordinate), int(y_coordinate)

    def mainloop(self, intro_time: int = 0, *args, **kwargs) -> None:
        self.intro.pack(expand=True, fill=BOTH)
        self.after(intro_time, self.start_intro)
        self.overrideredirect(1)
        super().mainloop(*args, **kwargs)

    def start_intro(self) -> None:
        self.intro.destroy()
        self.overrideredirect(0)
