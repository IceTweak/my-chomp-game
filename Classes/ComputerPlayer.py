"""
Этот класс отвечает за поведение компьютерного игрока, логику выбора ячейки,
отображаемую метку текущего хода игрока и т.д.
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
        """
        Выбирает случайную живую клетку на доске. Если можно, не ядовитую.
        Эта функция активируется событием GameObject — отпусканием мыши.
        """
        if isinstance(self.game_object.current_player, ComputerPlayer):
            # получение списка "живых" ячеек
            live_cells_indices = [(x, y) for x in range(self.game_object.rows) for y in range(self.game_object.columns)
                                  if self.game_object.cells[x][y].is_live]
            x, y = choice(live_cells_indices)
            # избранная клетка не будет отравленной, если есть какая-то другая живая ячейка.
            if len(live_cells_indices) > 1:
                while self.game_object.cells[x][y].is_poison():
                    x, y = choice(live_cells_indices)
            self.chosen_cell = self.game_object.cells[x][y]
            self.remove_block_from_board()
