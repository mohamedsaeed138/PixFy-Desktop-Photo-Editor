from PIL.ImageTk import PhotoImage
from customtkinter import filedialog
from tkinter import Event, messagebox
from Model.image_Model import ImageModel

# from Views.Main_Screen.main_screen import MainScreen


class Presenter:
    def __init__(self, model: ImageModel, view):
        self.model = model
        self.view = view

    def drop_image(self, event: Event):
        path: str = event.data.strip(r"{}")
        try:
            # if path.split(".")[-1].lower() not in ["png", "jpg", "jpeg"]:
            #     messagebox.showerror("error", "This Format isn't valid !")
            #     return
            self.model.set_images(path)
            self.update_view_images(self.view.original_image_container.label_size())
            self.update_view_sizes()
        except:
            messagebox.showerror("error", "This Format isn't supported !")

    def upload_image(self):
        path = filedialog.askopenfilename(
            initialdir="D:/Images Tests",  # getcwd()
            title="Select Image",
            filetypes=(("Image files", "*.png;*.jpg;*.jpeg"),),
        )
        if path == "":
            return
        try:
            self.model.set_images(path)
            self.update_view_images(self.view.original_image_container.label_size())
            self.update_view_sizes()
        except:
            messagebox.showerror("error", "This Format isn't supported !")

    def rescale_images(self, event):
        if self.model.image is None:
            return
        self.update_view_images((event.width, event.height))

    def update_view_images(self, max_size: tuple[int, int]):
        original, edited = self.model.get_scaled_images(max_size)

        original_photo, edited_photo = PhotoImage(original), PhotoImage(edited)
        self.view.original_image_container.image_label.configure(image=original_photo)
        self.view.original_image_container.image_label._image = original_photo
        self.view.edited_image_container.image_label.configure(image=edited_photo)
        self.view.edited_image_container.image_label._image = edited_photo

    def update_view_sizes(self):
        original_size, edited_size = self.model.get_images_size()
        self.view.original_image_container.size_label().configure(
            text=f"{original_size[0]}x{original_size[1]}"
        )
        self.view.edited_image_container.size_label.configure(
            text=f"{edited_size[0]}x{edited_size[1]}"
        )
