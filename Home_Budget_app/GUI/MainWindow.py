import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Home Budget App")
        self.geometry("1400x700")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self._current_frame = "Home"

        # Navigation frame
        self.nav_frame = ctk.CTkFrame(self, corner_radius=0)
        self.nav_frame.grid(row=0, column=0, sticky="nsew")
        self.nav_frame.grid_rowconfigure(4, weight=1)

        self.home_button = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                         fg_color=("gray75", "gray25"), text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"), anchor="w", font=ctk.CTkFont(size=15))
        self.home_button.grid(row=0, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.nav_frame, values=["System", "Light", "Dark"],
                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=5, column=0, padx=20, pady=20, sticky="s")

    def select_frame_by_name(self, name) -> None:
        match name:
            case "Home":
                pass
            case "Income/s":
                pass
            case "Add Expenses":
                pass
            case "History":
                pass
            case "Statistics":
                pass

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str) -> None:
        """
        Changes the appearance mode of the app, from the list of "light", "dark" and "system"

        :param new_appearance_mode: String with the name of new appearance mode
        :return: None
        """
        ctk.set_appearance_mode(new_appearance_mode)
