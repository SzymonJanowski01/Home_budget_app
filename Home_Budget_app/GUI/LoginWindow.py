import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image

from GUI.MainWindow import MainWindow

TESTING = True


class LoginWindow(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.login()

    def login(self):
        if TESTING:
            self.destroy()

            width, height = 1400, 700
            # noinspection PyUnresolvedReferences
            self.master.geometry(f"{width}x{height}")
            # noinspection PyUnresolvedReferences
            self.master.minsize(1200, 650)

            x = (self.master.winfo_screenwidth() // 2) - (width // 2)
            y = (self.master.winfo_screenheight() // 2) - (height // 2)
            # noinspection PyUnresolvedReferences
            self.master.geometry(f"{width}x{height}+{x}+{y}")

            MainWindow(self.master)
