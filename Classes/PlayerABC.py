"""
PlayerABC
Inherited from ABC
Abstract class. using as a template for the players.
For new player logic, create inherited class and implement choose_live_cell_from_board.
"""

from abc import ABC, abstractmethod


class PlayerABC(ABC):
    def __init__(self, game_object, display_name):
        self.game_object = game_object
        self.display_name = display_name
        self.chosen_cell = None

    @abstractmethod
    def choose_live_cell_from_board(self, event):
        pass

    def remove_block_from_board(self):
        """After choosing valid cell, coloring it with "chosen" color and remove the rest of the block"""
        self.chosen_cell.kill_cell(was_chosed=True)
        self.game_object.remove_remainder_cells(self.chosen_cell)
        self.game_object.finish_turn()
