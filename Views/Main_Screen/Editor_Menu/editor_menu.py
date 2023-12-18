from customtkinter import CTkFont, CTkButton, CENTER, CTkFrame
import customtkinter as ctk
from Views.Main_Screen.Editor_Menu.edge_detection_tab import EdgeDetectionTab
from Views.Main_Screen.Editor_Menu.gray_filters_tab import GrayFiltersTab
from Views.Main_Screen.Editor_Menu.noise_tab import NoiseTab
from Views.Main_Screen.Editor_Menu.sharpening_tab import SharpeningTab
from Views.Main_Screen.Editor_Menu.smoothing_tab import SmoothingTab

from Views.Main_Screen.Editor_Menu.transform_tab import TransformTab


class EditorMenu(ctk.CTkTabview):
    def __init__(self, master, disabled: bool = True):
        super().__init__(master)
        self.presenter = master.presenter
        self.add("Transform")
        self.add("Gray Filters")
        self.add("Smoothing")
        self.add("Sharpening")
        self.add("Noise")
        self.add("Edge Detection")
        self.transform_tab = TransformTab(self.tab("Transform"))
        self.gray_filters_tab = GrayFiltersTab(self.tab("Gray Filters"))
        self.smoothing_tab = SmoothingTab(self.tab("Smoothing"))
        self.sharpening_tab = SharpeningTab(self.tab("Sharpening"))
        self.noise_tab = NoiseTab(self.tab("Noise"))
        self.edge_detection_tab = EdgeDetectionTab(self.tab("Edge Detection"))
        self.transform_tab.pack(expand=True, fill=ctk.BOTH)
        self.gray_filters_tab.pack(expand=True, fill=ctk.BOTH)
        self.smoothing_tab.pack(expand=True, fill=ctk.BOTH)
        self.sharpening_tab.pack(expand=True, fill=ctk.BOTH)
        self.edge_detection_tab.pack(expand=True, fill=ctk.BOTH)
        self.noise_tab.pack(expand=True, fill=ctk.BOTH)

        if disabled:
            self.disable()

    def disable(self):
        for i in self.transform_tab.winfo_children():
            wtype = i.winfo_class()
            if wtype != "CTkLabel":
                i.configure(state="disabled")
        self.configure(state="disabled")

    def enable(self):
        for i in self.transform_tab.winfo_children():
            wtype = i.winfo_class()
            if wtype != "CTkLabel":
                i.configure(state="normal")
        self.configure(state="normal")
