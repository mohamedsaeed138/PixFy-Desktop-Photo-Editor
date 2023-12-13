from customtkinter import CTkFont, CTkButton, CENTER, CTkFrame
import customtkinter as ctk


class EditorMenu(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.add("Transform")
        self.add("Gray Filters")
        self.add("Smoothing")
        self.add("Sharpening")
        self.add("Noise")
        self.add("Edge Detection")
        frame = CTkFrame(self.tab("Transform"), fg_color=["#CFCFCF", "#292929"])
        frame.pack(expand=True, fill=ctk.BOTH)
        print(self._segmented_button._font)
        # for i in self.tab(self.get()).winfo_children():
        # wtype = i.winfo_class()
        # print(wtype)
        # if wtype != "CTkLabel":
        #   i.configure(state="disable")
