"""
Computer Player
Inherited from PlayerABC
This class responsible for computer player behavior, cell-choosing logic, the current player turn label displayed etc'.
"""

from Classes.PlayerABC import PlayerABC
from random import choice


class ComputerPlayer(PlayerABC):
    def __init__(self, game_object, display_name=2):
        self.game_object = game_object
        self.display_name = display_name
        self.chosen_cell = None
        super().__init__(game_object, display_name)

    def choose_live_cell_from_board(self, event):
        """ Chooses a random live cell on the board. If possible, not the poison one.
            This function triggered by GameObject event - mouse release
        """
        if isinstance(self.game_object.current_player, ComputerPlayer):
            # get list of indices of the living cells
            live_cells_indices = [(x, y) for x in range(self.game_object.rows) for y in range(self.game_object.columns)
                                 if self.game_object.cells[x][y].is_live]
            x, y = choice(live_cells_indices)
            if len(live_cells_indices) > 1:
                while self.game_object.cells[x][y].is_poison():
                    x, y = choice(live_cells_indices)

            # the chosen one won't be the poison if there is any other living cell
            self.chosen_cell = self.game_object.cells[x][y]
            self.remove_block_from_board()
