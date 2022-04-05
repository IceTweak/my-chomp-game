import tkinter as tk
from Classes.GameMenu import GameMenu


def main():
    root = tk.Tk()
    root.iconbitmap("icons/chocolate_bar.ico")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width // 2) - (400 // 2)
    y_position = (screen_height // 2) - (300 // 2)
    root.geometry(f'{400}x{300}+{x_position}+{y_position}')
    GameMenu(root)

    root.mainloop()


if __name__ == "__main__":
    main()
