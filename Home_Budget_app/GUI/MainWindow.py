import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image

from GUI.frames.HomeFrame import HomeFrame
from GUI.frames.IncomeFrame import IncomeFrame
from GUI.frames.ExpensesFrame import ExpensesFrame
from GUI.frames.AnalyticsFrame import AnalyticsFrame
from GUI.frames.HistoryFrame import HistoryFrame


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Home Budget App")
        self.geometry("1400x700")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self._current_frame = "Home"

        # Navigation frame
        self.nav_frame = ctk.CTkFrame(self, corner_radius=0)
        self.nav_frame.grid(row=0, column=0, sticky="nsew")
        self.nav_frame.grid_rowconfigure(5, weight=1)

        # Other frames navigation buttons
        self.nav_buttons = {}
        self.nav_buttons["HomeFrame"] = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10,
                                                      text="Home",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"), anchor="w",
                                                      font=ctk.CTkFont(size=15),
                                                      command=lambda: self.show_frame("HomeFrame"))
        self.nav_buttons["HomeFrame"].grid(row=0, column=0, sticky="ew")

        self.nav_buttons["IncomeFrame"] = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10,
                                                        text="Income",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"), anchor="w",
                                                        font=ctk.CTkFont(size=15),
                                                        command=lambda: self.show_frame("IncomeFrame"))
        self.nav_buttons["IncomeFrame"].grid(row=1, column=0, sticky="ew")

        self.nav_buttons["ExpensesFrame"] = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10,
                                                          text="Expenses", fg_color="transparent",
                                                          text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w", font=ctk.CTkFont(size=15),
                                                          command=lambda: self.show_frame("ExpensesFrame"))
        self.nav_buttons["ExpensesFrame"].grid(row=2, column=0, sticky="ew")

        self.nav_buttons["AnalyticsFrame"] = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40,
                                                           border_spacing=10,
                                                           text="Analytics", fg_color="transparent",
                                                           text_color=("gray10", "gray90"),
                                                           hover_color=("gray70", "gray30"),
                                                           anchor="w", font=ctk.CTkFont(size=15),
                                                           command=lambda: self.show_frame("AnalyticsFrame"))
        self.nav_buttons["AnalyticsFrame"].grid(row=3, column=0, sticky="ew")
        self.nav_buttons["HistoryFrame"] = ctk.CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10,
                                                         text="History", fg_color="transparent",
                                                         text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         anchor="w", font=ctk.CTkFont(size=15),
                                                         command=lambda: self.show_frame("HistoryFrame"))
        self.nav_buttons["HistoryFrame"].grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.nav_frame, values=["System", "Light", "Dark"],
                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomeFrame, IncomeFrame, ExpensesFrame, AnalyticsFrame, HistoryFrame):
            frame = F(self.container, corner_radius=20)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomeFrame")

    def show_frame(self, frame_name) -> None:
        frame = self.frames[frame_name]
        frame.tkraise()

        for name, btn in self.nav_buttons.items():
            if name == frame_name:
                btn.configure(fg_color=("gray75", "gray25"))
            else:
                btn.configure(fg_color="transparent")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str) -> None:
        """
        Changes the appearance mode of the app, from the list of "light", "dark" and "system"

        :param new_appearance_mode: String with the name of new appearance mode
        :return: None
        """
        ctk.set_appearance_mode(new_appearance_mode)
