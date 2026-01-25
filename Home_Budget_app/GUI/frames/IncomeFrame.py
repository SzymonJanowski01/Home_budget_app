import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image


class IncomeFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Master frame geometry
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Sub frames initialization
        self.user_management_frame = ctk.CTkFrame(self, corner_radius=20)
        self.user_management_frame.grid(row=0, column=0, sticky="nsew")
        self.user_list_frame = ctk.CTkFrame(self, corner_radius=20)
        self.user_list_frame.grid(row=1, column=0, sticky="nsew", pady=5)

        # Sub frames geometry
        self.user_management_frame.columnconfigure((1, 2, 3), weight=0)
        self.user_management_frame.columnconfigure((0, 4), weight=1)

        self.user_list_frame.columnconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=0)
        self.user_list_frame.columnconfigure((0, 9), weight=1)

        # User_management_frame widgets
        self.label = ctk.CTkLabel(self.user_management_frame, text="Chose income split:",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, columnspan=100, pady=20, padx=20)

        self.budget_split_button = ctk.CTkSegmentedButton(self.user_management_frame, corner_radius=50, height=35,
                                                          border_width=5, selected_color=("gray75", "gray25"),
                                                          selected_hover_color=("gray70", "gray30"),
                                                          values=["Equal", "Proportionate", "Custom"],
                                                          command=self.on_segmented_button_click)
        self.budget_split_button.grid(row=1, column=0, columnspan=100, pady=10, padx=10)
        self.budget_split_button.set("Equal")

        self.new_user_name_entry = ctk.CTkEntry(self.user_management_frame, placeholder_text="Enter user name",
                                                width=200, height=35, corner_radius=50)
        self.new_user_name_entry.grid(row=3, column=1, padx=5, pady=10)
        self.new_user_income_entry = ctk.CTkEntry(self.user_management_frame, placeholder_text="Enter user income",
                                                  width=200, height=35, corner_radius=50)
        self.new_user_income_entry.grid(row=3, column=2, padx=5, pady=10)
        self.confirm_user_button = ctk.CTkButton(self.user_management_frame, text="Confirm", fg_color="blue",
                                                 hover_color="darkblue", corner_radius=50, height=35, width=20,
                                                 command=self.confirm_user_button)
        self.confirm_user_button.grid(row=3, column=3, padx=5, pady=10)

        self.add_users_label = ctk.CTkLabel(self.user_management_frame, text="Let's add some users to get started!",
                                            font=ctk.CTkFont(size=16))

        # Load existing users from DB, otherwise create empty list
        # TODO: implement DB functionality to load users, for now just use test dict
        self.users = {}
        # 1: {"name": "Alice", "income": 5000}, 2: {"name": "Bob", "income": 3000}

        self.load_users()

    def on_segmented_button_click(self, value) -> None:
        if len(self.users) < 2:
            pass

    def confirm_user_button(self) -> None:
        if len(self.users) < 5:
            try:
                name = self.new_user_name_entry.get()
                income = float(self.new_user_income_entry.get())
                if name == "" or income <= 0:
                    raise ValueError("Invalid input")
                new_user_id = max(self.users.keys(), default=0) + 1
                self.users[new_user_id] = {"name": name, "income": income}
                self.load_users()
                self.new_user_name_entry.delete(0, "end")
                self.new_user_income_entry.delete(0, "end")
                self.focus_set()
            except ValueError:
                CTkMessagebox(title="Invalid Input",
                              message="Please enter a valid name and a positive number for income.",
                              icon="cancel")
        else:
            CTkMessagebox(title="User Limit Reached",
                          message="You have reached the maximum number of users (5)."
                                  " Please remove a user before adding another.",
                          icon="warning")
        # TODO: implement functionality to add user to DB

    def load_users(self):
        # TODO: implement loading from DB
        if len(self.users) == 0:
            self.add_users_label.grid(row=6, column=0, columnspan=100, pady=20, padx=20)
        else:
            self.add_users_label.grid_forget()
            name_label = ctk.CTkLabel(self.user_list_frame, text="Name:", font=ctk.CTkFont(size=20, weight="bold"))
            name_label.grid(row=0, column=1, padx=5, pady=10)
            earnings_label = ctk.CTkLabel(self.user_list_frame, text="Earnings:",
                                          font=ctk.CTkFont(size=20, weight="bold"))
            earnings_label.grid(row=0, column=2, padx=5, pady=10)
            contribution_label = ctk.CTkLabel(self.user_list_frame, text="Contribution:",
                                              font=ctk.CTkFont(size=20, weight="bold"))
            contribution_label.grid(row=0, column=4, padx=5, pady=10)
            for counter, (user_id, user_items) in enumerate(self.users.items()):
                name_entry = ctk.CTkEntry(self.user_list_frame, width=200, height=35, corner_radius=50)
                name_entry.insert(0, user_items["name"])
                name_entry.grid(row=1 + counter, column=1, padx=5, pady=10)
                name_entry.configure(state="disabled")
                income_entry = ctk.CTkEntry(self.user_list_frame, width=200, height=35, corner_radius=50)
                income_entry.insert(0, str(user_items["income"]))
                income_entry.grid(row=1 + counter, column=2, padx=5, pady=10)
                income_entry.configure(state="disabled")
                grid_splitter = ctk.CTkLabel(self.user_list_frame, text="|", font=ctk.CTkFont(size=20, weight="bold"))
                grid_splitter.grid(row=1 + counter, column=3, padx=5, pady=10)
                contribution = ctk.CTkEntry(self.user_list_frame, width=200, height=35, corner_radius=50)
                contribution.grid(row=1 + counter, column=4, padx=5, pady=10)
                grid_splitter_2 = ctk.CTkLabel(self.user_list_frame, text="|", font=ctk.CTkFont(size=20, weight="bold"))
                grid_splitter_2.grid(row=1 + counter, column=5, padx=5, pady=10)
                edit_button = ctk.CTkButton(self.user_list_frame, text="Edit", fg_color="blue", hover_color="darkblue",
                                            corner_radius=50, height=35, width=20,
                                            command=lambda uid=user_id: self.edit_user(uid))
                edit_button.grid(row=1 + counter, column=6, padx=5, pady=10)
                remove_button = ctk.CTkButton(self.user_list_frame, text="Remove", fg_color="red",
                                              hover_color="darkred", corner_radius=50, height=35, width=20,
                                              command=lambda uid=user_id: self.remove_user(uid))
                remove_button.grid(row=1 + counter, column=7, padx=5, pady=10)

