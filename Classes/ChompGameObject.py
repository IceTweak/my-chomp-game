"""
Объект окна игры. Окно запускается при нажатии на кнопку в меню.
Отвечает за текущее игровое окно, которое было настроено с помощью меню.
"""

import tkinter as tk
import tkinter.messagebox as msgbox
from itertools import cycle

import static
from Classes.Cell import Cell
from Classes.ComputerPlayer import ComputerPlayer
from Classes.HumanPlayer import HumanPlayer


class GameObject(tk.Frame):

    def __init__(self, root, rows, columns, play_against):
        self.root = root
        root.iconbitmap("icons/chocolate_bar.ico")
        tk.Frame.__init__(self)
        self.rows = rows
        self.columns = columns
        self.play_against = play_against

        # Инициализация игроков - один человек, а другой определяется выбранным режимом.
        # Оба игрока содержатся в циклическом списке, где первый игрок всегда человек
        first_player = HumanPlayer(self)
        if self.play_against == static.PLAY_AGAINST_FRIEND:
            second_player = HumanPlayer(self, display_name=2)
        else:
            second_player = ComputerPlayer(self)
        self.players = cycle([first_player, second_player])
        self.current_player = next(self.players)

        # Конфигурация ячеек(плиток)
        self.cell_size = static.CELL_SIZE if max(self.rows, self.columns) < 10 else static.SMALL_CELL_SIZE
        self.board_frame = tk.Frame(self.root, bg='white', width=self.columns * self.cell_size,
                                    height=self.rows * self.cell_size, padx=3, pady=3)
        self.cells = [[Cell(master=self.board_frame) for _ in range(self.columns)] for _ in range(self.rows)]

        # Описание игры и очередность ходов
        self.instructions_title = tk.Label(self.root, text=static.INSTRUCTIONS_TITLE)
        self.instructions_label = tk.Label(self.root, text=static.INSTRUCTIONS)
        self.current_player_label = tk.Label(self.root, text=static.TURN_LABEL.format(self.current_player.display_name))

        self.set_new_game_window()
        self.set_new_game_board()

    def set_new_game_window(self):
        # Установка размеров окна
        self.root.title("{} - {}".format(static.GAME_TITLE, self.play_against))
        width = max(700, self.columns*self.cell_size) + 50
        height = 250 + self.rows * self.cell_size
        # Центрирование окна на экране
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width // 2) - (width // 2)
        y_position = (screen_height // 2) - (height // 2)
        self.root.geometry("{}x{}+{}+{}".format(str(width), str(height), str(x_position), str(y_position)))

        # Расположение всех основных блоков
        self.root.grid_rowconfigure(self.rows, weight=1)
        self.root.grid_columnconfigure(self.columns, weight=1)

        # Отображение описаний
        self.instructions_title.grid()
        self.instructions_title.config(font=("Courier", 20))
        self.instructions_label.grid()
        self.current_player_label.grid()
        self.current_player_label.config(font=("Courier", 40))

        # Создание сетки ячеек
        self.board_frame.grid()
        self.board_frame.grid_rowconfigure(1, weight=1)
        self.board_frame.grid_columnconfigure(1, weight=1)

    def set_new_game_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                color = static.POISON if (row == self.rows - 1 and column == 0) else static.LIVE
                cell = Cell(self.board_frame, color, cell_size=self.cell_size)
                cell.grid(row=row, column=column)
                self.cells[row][column] = cell

                # Привязка нажатий к игрокам
                # Если игра идет против компьютера, то выбор ячейки игроком, исполняет триггер для хода компьютера
                cell.bind_players_event(self.players)

    def remove_remainder_cells(self, chosen_cell):
        chosen_cell_info = chosen_cell.grid_info()
        chosen_cell_row, chosen_cell_column = chosen_cell_info["row"], chosen_cell_info["column"]

        # Удаление свех ячеек выше и правее той что выбрана игроком
        for row in range(chosen_cell_row + 1):
            for column in range(chosen_cell_column, self.columns):
                if self.cells[row][column].is_live:
                    self.cells[row][column].kill_cell()

    # Передача хода следующему игроку
    def finish_turn(self):
        if self.is_game_over():
            self.finish_game()
        else:
            self.current_player = next(self.players)
            self.current_player_label.configure(text=static.TURN_LABEL.format(self.current_player.display_name))

    def is_game_over(self):
        for row in self.cells:
            for cell in row:
                if cell.is_live:
                    return False
        return True

    # Сообщение о завершении игры с результатами
    def finish_game(self):
        respond = msgbox.showinfo(title=static.GAME_OVER_TITLE, message=static.GAME_OVER_MSG.format(
            next(self.players).display_name, self.current_player.display_name))
        if respond:
            self.after(1000, self.root.destroy)
