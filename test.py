from tkinter import Tk
from ctypes import windll

user32 = windll.user32
screen_width, screen_height = (
    user32.GetSystemMetrics(0),
    user32.GetSystemMetrics(1),
)

width, height = (int(screen_width * 0.7037), int(screen_height * 0.7037))
my_window = Tk()

screen_width = my_window.winfo_screenwidth()
screen_height = my_window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width / 2)
y_coordinate = (screen_height / 2) - (height / 2)
my_window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

my_window.mainloop()
print(my_window.winfo_geometry())
