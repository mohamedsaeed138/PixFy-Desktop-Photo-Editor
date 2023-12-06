from os import getcwd
from customtkinter import filedialog
from PIL.ImageTk import PhotoImage
from PIL.Image import open


class UploadImage:
    def upload_image(original_widget, edited_widget, size):
        image_path = filedialog.askopenfilename(
            initialdir=getcwd(),
            filetypes=(("JGP File", "*.jpg"), ("PNG File", "*.png")),
        )
        UploadImage.change_image(image_path, original_widget, edited_widget, size)

    def drop_image(event, original_widget, edited_widget, size):
        image_path: str = event.data
        image_path = image_path.strip(r"{}")
        UploadImage.change_image(image_path, original_widget, edited_widget, size)

    def change_image(image_path, original_widget, edited_widget, size):
        image = open(image_path)
        copy = image.copy()

        copy.thumbnail(size)

        photo_image = PhotoImage(copy)
        original_widget.image_label.configure(image=photo_image)
        original_widget.image_label.image = photo_image  # type: ignore
        edited_widget.image_label.configure(image=photo_image)
        edited_widget.image_label.image = photo_image  # type: ignore
