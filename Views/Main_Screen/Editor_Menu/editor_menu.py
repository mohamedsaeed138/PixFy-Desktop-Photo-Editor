from typing import Callable, Optional, Tuple, Union
from customtkinter import CTkFont
import customtkinter as ctk


class EditorMenu(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(
            master,
        )
        self.add("Transform")
        self.add("Gray Filters")
        self.add("Smoothing")
        self.add("Sharpening")
        self.add("Noise")
        self.add("Edge Detection")
