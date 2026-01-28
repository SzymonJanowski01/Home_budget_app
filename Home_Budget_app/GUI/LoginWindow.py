import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image

from GUI.MainWindow import MainWindow

TESTING = True


class LoginWindow(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Sub frames
        self.login_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.signup_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        # Sub frames geometry
        self.login_frame.columnconfigure((1, 2), weight=0)
        self.login_frame.columnconfigure((0, 3), weight=1)
        self.login_frame.rowconfigure((0, 2, 8), weight=1)

        self.signup_frame.columnconfigure((1, 2), weight=0)
        self.signup_frame.columnconfigure((0, 3), weight=1)
        self.signup_frame.rowconfigure((0, 2, 10), weight=1)

        # Login frame widgets
        self.welcome_label = ctk.CTkLabel(self.login_frame, text="Let's make your budget great again!",
                                          font=ctk.CTkFont(size=25, weight="bold"))
        self.welcome_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        self.login_label = ctk.CTkLabel(self.login_frame, text="Log-in!", font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        self.login_username_or_email_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Enter username or email!",
                                                          width=250, height=35, corner_radius=50)
        self.login_username_or_email_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        self.login_username_or_email_entry.bind("<Return>", lambda e: self.login())

        self.login_password = ctk.CTkEntry(self.login_frame, placeholder_text="Enter password!", width=250, height=35,
                                           corner_radius=50, show="*")
        self.login_password.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
        self.login_password.bind("<Return>", lambda e: self.login())
        self.login_button = ctk.CTkButton(self.login_frame, text="Confirm", fg_color="blue", hover_color="darkblue",
                                          corner_radius=50, height=35, width=150, command=self.login)
        self.login_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

        self.signup_option_frame = ctk.CTkFrame(self.login_frame, fg_color="transparent")
        self.signup_option_frame.grid(row=7, column=1, columnspan=2, padx=10, pady=10)
        self.signup_option_label = ctk.CTkLabel(self.signup_option_frame, text="No account? Sign up",
                                                font=ctk.CTkFont(size=15))
        self.signup_option_label.grid(row=0, column=0, pady=10)
        self.signup_option_button = ctk.CTkButton(self.signup_option_frame, text="Here!", fg_color="transparent",
                                                  hover_color="gray20", font=ctk.CTkFont(size=15, underline=True),
                                                  width=20, command=self.switch_to_signup)
        self.signup_option_button.grid(row=0, column=1, pady=10)

        # Signup frame widgets
        self.welcome_label = ctk.CTkLabel(self.signup_frame, text="Let's make your budget great again!",
                                          font=ctk.CTkFont(size=25, weight="bold"))
        self.welcome_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        self.signup_label = ctk.CTkLabel(self.signup_frame, text="Sign-in!", font=ctk.CTkFont(size=20, weight="bold"))
        self.signup_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        self.signup_username = ctk.CTkEntry(self.signup_frame, placeholder_text="Enter username", width=250, height=35,
                                            corner_radius=50)
        self.signup_username.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        self.signup_username.bind("<Return>", lambda e: self.signup())
        self.signup_email = ctk.CTkEntry(self.signup_frame, placeholder_text="Enter email", width=250, height=35,
                                         corner_radius=50)
        self.signup_email.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
        self.signup_email.bind("<Return>", lambda e: self.signup())
        self.signup_password = ctk.CTkEntry(self.signup_frame, placeholder_text="Enter password!", width=250, height=35,
                                            corner_radius=50, show="*")
        self.signup_password.grid(row=6, column=1, columnspan=2, padx=10, pady=10)
        self.signup_password.bind("<Return>", lambda e: self.login())
        self.signup_confirm_password = ctk.CTkEntry(self.signup_frame, placeholder_text="Confirm password!", width=250,
                                                    height=35, corner_radius=50, show="*")
        self.signup_confirm_password.grid(row=7, column=1, columnspan=2, padx=10, pady=10)
        self.signup_confirm_password.bind("<Return>", lambda e: self.login())
        self.signup_button = ctk.CTkButton(self.signup_frame, text="Confirm", fg_color="blue", hover_color="darkblue",
                                           corner_radius=50, height=35, width=150, command=self.signup)
        self.signup_button.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

        self.login_option_frame = ctk.CTkFrame(self.signup_frame, fg_color="transparent")
        self.login_option_frame.grid(row=9, column=1, columnspan=2, padx=10, pady=10)
        self.login_option_label = ctk.CTkLabel(self.login_option_frame, text="Already have an account? Log in",
                                               font=ctk.CTkFont(size=15))
        self.login_option_label.grid(row=0, column=0, pady=10)
        self.login_option_button = ctk.CTkButton(self.login_option_frame, text="Here!", fg_color="transparent",
                                                 hover_color="gray20", font=ctk.CTkFont(size=15, underline=True),
                                                 width=20, command=self.switch_to_login)
        self.login_option_button.grid(row=0, column=1, pady=10)

    # TODO: login and signup actual implementation
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

    def signup(self):
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

    def switch_to_signup(self):
        self.login_frame.grid_forget()
        self.signup_frame.grid(row=0, column=0, sticky="nsew")

    def switch_to_login(self):
        self.signup_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky="nsew")
