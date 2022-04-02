"""
Cell
Inherited from Frame
Each cell colored according to its status- live (poison or non poison) or dead (chosen or non chosen)
cell size decided according to rows and columns number.
"""
import tkinter as tk
from Classes.HumanPlayer import HumanPlayer
import static


class Cell(tk.Frame):
    def __init__(self, master, color=static.LIVE, cell_size=static.CELL_SIZE):
        self.master = master
        tk.Frame.__init__(self, master, bg=color, highlightbackground="black", highlightcolor="black",
                          highlightthickness=1, width=cell_size, height=cell_size, padx=3, pady=3)
        self.is_live = True

    def kill_cell(self, was_chosed=False):
        self.is_live = False
        self.configure(background=static.CHOSEN if was_chosed else static.DEAD)

    def is_poison(self):
        return self["background"] == static.POISON

    def bind_players_event(self, players_cycle_list):
        # players_cycle_list starts with the second_player
        second_player, first_player = next(players_cycle_list), next(players_cycle_list)
        self.bind(static.LEFT_MOUSE_BUTTON, first_player.choose_live_cell_from_board)
        if isinstance(second_player, HumanPlayer):
            button_event = static.LEFT_MOUSE_BUTTON
        else:
            button_event = static.LEFT_MOUSE_BUTTON_RELEASE
        self.bind(button_event, second_player.choose_live_cell_from_board)
