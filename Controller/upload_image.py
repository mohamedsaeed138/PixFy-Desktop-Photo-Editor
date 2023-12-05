from os import getcwd
from customtkinter import filedialog, CTkImage
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
        print((original_widget.winfo_width(), original_widget.winfo_height()))
        image.thumbnail((size[0], size[1] - 5))
        photo_image = CTkImage(image, image, image.size)
        original_widget.img_label.configure(image=photo_image)
        original_widget.img_label.image = photo_image  # type: ignore
        edited_widget.img_label.configure(image=photo_image)
        edited_widget.img_label.image = photo_image  # type: ignore
