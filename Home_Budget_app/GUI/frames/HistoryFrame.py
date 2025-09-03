import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image


class HistoryFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.label = ctk.CTkLabel(self, text="History Frame", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, pady=20, padx=20)
