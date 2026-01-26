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

        # Window flags
        self.currently_editing_user_id = None

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
                if name == "" or income < 0:
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

    def load_users(self) -> None:
        # TODO: implement loading from DB
        if len(self.users) == 0:
            self.add_users_label.grid(row=6, column=0, columnspan=100, pady=20, padx=20)
        else:
            self.add_users_label.grid_forget()
            self.user_widgets = {}
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

                # Hidden buttons
                confirm_button = ctk.CTkButton(self.user_list_frame, text="Confirm", fg_color="green",
                                               hover_color="darkgreen", corner_radius=50, height=35, width=20,
                                               command=lambda uid=user_id: self.save_modified_user(uid))
                cancel_button = ctk.CTkButton(self.user_list_frame, text="Cancel", fg_color="red",
                                              hover_color="darkred", corner_radius=50, height=35, width=20,
                                              command=lambda uid=user_id: self.cancel_editing(uid))

                self.user_widgets[user_id] = {
                    "name": name_entry,
                    "income": income_entry,
                    "edit_button": edit_button,
                    "remove_button": remove_button,
                    "confirm_button": confirm_button,
                    "cancel_button": cancel_button,
                    "row": 1 + counter
                }

    def edit_user(self, user_id: int) -> None:
        if self.currently_editing_user_id:
            CTkMessagebox(title="Invalid action",
                          message="You can only edit one user at a time.",
                          icon="cancel")
            return

        self.currently_editing_user_id = user_id
        widgets = self.user_widgets[user_id]

        # Capture original values for restoring if no values has changed
        widgets["original_name"] = widgets["name"].get()
        widgets["original_income"] = widgets["income"].get()

        widgets["name"].configure(state="normal", border_color="Yellow")
        widgets["income"].configure(state="normal", border_color="Yellow")

        widgets["edit_button"].grid_forget()
        widgets["remove_button"].grid_forget()
        widgets["confirm_button"].grid(row=widgets["row"], column=6, padx=5, pady=10)
        widgets["cancel_button"].grid(row=widgets["row"], column=7, padx=5, pady=10)

    def save_modified_user(self, user_id: int) -> None:
        widgets = self.user_widgets[user_id]

        # Get window theme to ensure proper default border color
        theme = ctk.ThemeManager.theme["CTkEntry"]
        if widgets["name"]._get_appearance_mode() == "light":
            default = 0
        else:
            default = 1

        # Check if there are any changes and if so - validate them
        if widgets["name"].get() == widgets["original_name"] and widgets["income"].get() == widgets["original_income"]:
            pass
        else:
            try:
                if not widgets["name"].get():
                    raise ValueError("Invalid input")
                elif not widgets["income"].get():
                    widgets["income"].insert(0, float(0))
                elif float(widgets["income"].get()) < 0:
                    raise ValueError("Invalid input")
            except (ValueError, TypeError):
                CTkMessagebox(title="Invalid Input",
                              message="Please enter a valid name and a positive number for income.",
                              icon="cancel")
                return

        widgets["name"].configure(state="disabled", border_color=theme["border_color"][default])
        widgets["income"].configure(state="disabled", border_color=theme["border_color"][default])

        # Bring back original buttons
        widgets["confirm_button"].grid_forget()
        widgets["cancel_button"].grid_forget()
        widgets["edit_button"].grid(row=widgets["row"], column=6, padx=5, pady=10)
        widgets["remove_button"].grid(row=widgets["row"], column=7, padx=5, pady=10)

        self.currently_editing_user_id = None
        # TODO: DB editing

    def cancel_editing(self, user_id: int) -> None:
        widgets = self.user_widgets[user_id]

        # Get window theme to ensure proper default border color
        theme = ctk.ThemeManager.theme["CTkEntry"]
        if widgets["name"]._get_appearance_mode() == "light":
            default = 0
        else:
            default = 1

        # Restore entries to their original state
        widgets["name"].delete(0, "end")
        widgets["name"].insert(0, widgets["original_name"])
        widgets["name"].configure(state="disabled", border_color=theme["border_color"][default])
        widgets["income"].delete(0, "end")
        widgets["income"].insert(0, widgets["original_income"])
        widgets["income"].configure(state="disabled", border_color=theme["border_color"][default])

        # Bring back original buttons
        widgets["confirm_button"].grid_forget()
        widgets["cancel_button"].grid_forget()
        widgets["edit_button"].grid(row=widgets["row"], column=6, padx=5, pady=10)
        widgets["remove_button"].grid(row=widgets["row"], column=7, padx=5, pady=10)

        self.currently_editing_user_id = None

    def remove_user(self, user_id: int) -> None:
        del self.users[user_id]
        self.clear_user_list()
        self.load_users()

    def clear_user_list(self) -> None:
        for w in self.user_list_frame.winfo_children():
            w.destroy()
