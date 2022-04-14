"""
Этот класс отвечает за поведение игрока-челвека, логику выбора ячейки,
отображаемую метку текущего хода игрока и т.д.
Наследуется от PlayerABC
"""

from Classes.PlayerABC import PlayerABC


class HumanPlayer(PlayerABC):
    def __init__(self, game_object, display_name=1):
        self.game_object = game_object
        self.display_name = display_name
        self.chosen_cell = None
        super().__init__(game_object, display_name)

    def choose_live_cell_from_board(self, event):
        """
        Соединение события щелчка с объектом Cell.
        Если ячейка жива, удаляем выбранную ячейку с доски.
        В противном случае ничего не делаем.
        """
        player_selected_cell = self.game_object.root.winfo_containing(event.x_root, event.y_root)
        if player_selected_cell.is_live:
            self.chosen_cell = player_selected_cell
            self.remove_block_from_board()
