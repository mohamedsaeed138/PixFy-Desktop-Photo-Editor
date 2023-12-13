from os import getcwd
from customtkinter import filedialog, CTkLabel
from PIL.ImageTk import PhotoImage
from PIL.Image import open, Image, LANCZOS
from PIL.ImageOps import contain


class UploadImage:
    original_image: Image = None
    path: str = None

    def upload_image(original_label, edited_label, size):
        image_path = filedialog.askopenfilename(
            initialdir="D:/",  # getcwd()
            title="Select Image",
            filetypes=(("Image files", "*.png;*.jpg;*.jpeg"),),
        )
        UploadImage.change_image(image_path, original_label, edited_label, size)

    def drop_image(event, original_label, edited_label, size):
        image_path: str = event.data
        image_path = image_path.strip(r"{}")
        UploadImage.change_image(image_path, original_label, edited_label, size)

    def change_image(image_path, original_label, edited_label, size):
        UploadImage.original_image = open(image_path)
        UploadImage.path = image_path

        copy = contain(UploadImage.original_image, size, LANCZOS)

        photo_image = PhotoImage(copy)
        original_label.configure(image=photo_image)
        original_label._image = photo_image  # type: ignore
        edited_label.configure(image=photo_image)
        edited_label._image = photo_image  # type: ignore

    def rescale_image(event, original_label: CTkLabel, edited_label):
        if UploadImage.original_image == None:
            return
        print((event.width, event.height))

        copy = contain(UploadImage.original_image, (event.width, event.height), LANCZOS)

        photo_image = PhotoImage(copy)
        original_label.configure(image=photo_image)
        original_label._image = photo_image  # type: ignore
        edited_label.configure(image=photo_image)
        edited_label._image = photo_image  # type: ignore
