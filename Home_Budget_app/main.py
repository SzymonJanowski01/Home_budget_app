import customtkinter as ctk
from GUI.LoginWindow import LoginWindow

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Home Budget App")

    width, height = 400, 300
    root.geometry(f"{width}x{height}")
    root.update_idletasks()

    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    LoginWindow(root)
    root.mainloop()
