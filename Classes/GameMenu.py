
import tkinter as tk
from Classes.ChompGameObject import GameObject
import tkinter.messagebox as msgbox
from re import match
import static


class GameMenu:
    def __init__(self, master):
        self.master = master
        self.master.title(static.MENU_TITLE)
        self.rows, self.columns = None, None
        self.inner_title = tk.Label(master, text=static.HEAD_TITLE)
        self.set_label_font(self.inner_title, 18)

        # Создание и позиционирование подменю установки размера поля для игры
        self.board_size_title = tk.Label(self.master, text=static.BOARD_SIZE_TITLE)
        self.board_size_title.grid(pady=10)
        self.set_label_font(self.board_size_title, 14)

        self.rows_text = tk.Label(self.master, text="Строки:").grid(row=2, column=0, padx=20)
        self.columns_text = tk.Label(self.master, text="Столбцы:").grid(row=3, column=0, padx=20)

        self.rows_entry = tk.Entry(self.master)
        self.columns_entry = tk.Entry(self.master)
        self.rows_entry.grid(row=2, column=1)
        self.columns_entry.grid(row=3, column=1)

        # Создание и позиционирование подменю выбора режима игры
        self.play_against_title = tk.Label(master, text=static.PLAY_AGAINST_TITLE)
        self.play_against_title.grid(pady=10)
        self.set_label_font(self.play_against_title, 14)
        self.play_against = tk.StringVar(master)

        self.play_against.set(static.PLAY_AGAINST_PC)  # по умолчанию выбран режим против компьютера
        play_against_options = [static.PLAY_AGAINST_FRIEND, static.PLAY_AGAINST_PC]
        self.game_mode_options_menu = tk.OptionMenu(master, self.play_against, *play_against_options).grid(columnspan=2)

        # Кнопка запуска игры
        self.start_button = tk.Button(master, text=static.START_BUTTON,
                                      command=lambda mainroot=master: self.start_game()).grid(columnspan=2, pady=20)

    # Создание объекта игрового поля или сообщение о неправильном вводе
    def start_game(self):
        if self.is_inputs_valid():
            root = tk.Toplevel(master=self.master)
            row_input = int(self.rows_entry.get())
            column_input = int(self.columns_entry.get())
            GameObject(root=root, rows=row_input, columns=column_input, play_against=self.play_against.get())
        else:
            msgbox.showinfo(title=static.INPUT_NOT_VALID_TITLE, message=static.INPUT_NOT_VALID_MSG.format(
                static.MIN_ROW_NUM, static.MAX_ROW_NUM, static.MIN_COL_NUM, static.MAX_COL_NUM))

    # Проверка ввода на корректность
    def is_inputs_valid(self):
        regex_pattern = "^[0-9]*$"
        row_input = self.rows_entry.get()
        column_input = self.columns_entry.get()
        if match(regex_pattern, row_input) and match(regex_pattern, column_input):
            is_row_valid = static.MIN_ROW_NUM <= int(row_input) <= static.MAX_ROW_NUM
            is_column_valid = static.MIN_COL_NUM <= int(column_input) <= static.MAX_COL_NUM
            return is_row_valid and is_column_valid

    # Установка стилей для заголовков
    def set_label_font(self, title, size):
        title.grid(columnspan=2)
        title.config(font=('Helvetica', size, 'bold'))
