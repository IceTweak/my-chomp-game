"""
Human Player
Inherited from PlayerABC
This class responsible for the cell-choosing logic, the current player turn label displayed etc'.
"""

from Classes.PlayerABC import PlayerABC


class HumanPlayer(PlayerABC):
    def __init__(self, game_object, display_name=1):
        self.game_object = game_object
        self.display_name = display_name
        self.chosen_cell = None
        super().__init__(game_object, display_name)

    def choose_live_cell_from_board(self, event):
        """ Connect the click event to the Cell object.
        If cell is alive,  remove the chosen cell on the board.
        Else, do nothing.
        """
        player_selected_cell = self.game_object.root.winfo_containing(event.x_root, event.y_root)
        if player_selected_cell.is_live:
            self.chosen_cell = player_selected_cell
            self.remove_block_from_board()


