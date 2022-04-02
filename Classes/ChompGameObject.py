"""
GameObject
Inherited from Frame
Game Object for Chomp game is triggered by button pressing on GameMenu
Responsible for the current game window that being played, and configured bu player.
"""

import tkinter as tk
import tkinter.messagebox as msgbox
from random import choice
from itertools import cycle
from Classes.Cell import Cell
from Classes.HumanPlayer import HumanPlayer
from Classes.ComputerPlayer import ComputerPlayer
import static


class GameObject(tk.Frame):
    def __init__(self, root, rows, columns, board_mode, play_against):
        self.root = root
        root.iconbitmap("icons/chocolate_bar.ico")
        tk.Frame.__init__(self)
        self.rows = rows
        self.columns = columns
        self.board_mode = board_mode
        self.play_against = play_against

        # init players- one is human, the other one is defined by self.game_mode.
        # Keep both players in circular list where the first player is human
        first_player = HumanPlayer(self)
        if self.play_against == static.PLAY_AGAINST_FRIEND:
            second_player = HumanPlayer(self, display_name=2)
        else:
            second_player = ComputerPlayer(self)
        self.players = cycle([first_player, second_player])
        self.current_player = next(self.players)

        # board and cell config
        self.cell_size = static.CELL_SIZE if max(self.rows, self.columns) < 10 else static.SMALL_CELL_SIZE
        self.board_frame = tk.Frame(self.root, bg='white', width=self.columns * self.cell_size,
                                    height=self.rows * self.cell_size, padx=3, pady=3)
        self.cells = [[Cell(master=self.board_frame) for _ in range(self.columns)] for _ in range(self.rows)]

        self.instructions_title = tk.Label(self.root, text=static.INSTRUCTIONS_TITLE)
        self.instructions_label = tk.Label(self.root, text=static.INSTRUCTIONS)
        self.current_player_label = tk.Label(self.root, text=static.TURN_LABEL.format(self.current_player.display_name))

        self.set_new_game_window()
        self.set_new_game_board()

    def set_new_game_window(self):
        # window size and header
        self.root.title("{} - {} - {}".format(static.GAME_TITLE, self.play_against, self.board_mode))
        width = max(700, self.columns*self.cell_size) + 50
        height = 250 + self.rows * self.cell_size
        # centered game window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width // 2) - (width // 2)
        y_position = (screen_height // 2) - (height // 2)
        self.root.geometry("{}x{}+{}+{}".format(str(width), str(height), str(x_position), str(y_position)))

        # layout all of the main containers
        self.root.grid_rowconfigure(self.rows, weight=1)
        self.root.grid_columnconfigure(self.columns, weight=1)

        # display labels
        self.instructions_title.grid()
        self.instructions_title.config(font=("Courier", 20))
        self.instructions_label.grid()
        self.current_player_label.grid()
        self.current_player_label.config(font=("Courier", 40))

        # create the center widgets
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

                # binding for each player
                # if playing against computer, bind mouse click releasing to trigger computer turn
                cell.bind_players_event(self.players)
        if self.board_mode == static.BOARD_MODE_EATEN:
            self.eat_random_block_from_board()

    def eat_random_block_from_board(self):
        # get random index of cell out of list of indices of the living cells
        x, y = choice([(x, y) for x in range(self.rows-1) for y in range(1, self.columns) if self.cells[x][y].is_live])
        self.cells[x][y].kill_cell()
        self.remove_remainder_cells(self.cells[x][y])

    def remove_remainder_cells(self, chosen_cell):
        chosen_cell_info = chosen_cell.grid_info()
        chosen_cell_row, chosen_cell_column = chosen_cell_info["row"], chosen_cell_info["column"]

        # remove all the cells in the block above and right to the chosen cell
        for row in range(chosen_cell_row + 1):
            for column in range(chosen_cell_column, self.columns):
                if self.cells[row][column].is_live:
                    self.cells[row][column].kill_cell()

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

    def finish_game(self):
        respond = msgbox.showinfo(title=static.GAME_OVER_TITLE, message=static.GAME_OVER_MSG.format(
            next(self.players).display_name, self.current_player.display_name))
        if respond:
            self.after(1000, self.root.destroy)
