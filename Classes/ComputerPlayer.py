"""
Этот класс отвечает за поведение компьютерного игрока, логику выбора ячейки,
отображаемую метку текущего хода игрока и т.д.
"""
import random

from Classes.PlayerABC import PlayerABC
from random import choice
from Classes.AiSolver import wins


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
            live_cells_indices = frozenset([(x, y) for x in range(self.game_object.rows)
                                            for y in range(self.game_object.columns) if
                                            self.game_object.cells[x][y].is_live])

            # избранная клетка не будет отравленной, если есть какая-то другая живая ячейка.
            x, y = self.game_object.rows, 0
            if 10 > len(live_cells_indices) > 1:
                # если список возможный ходов не пуст
                try:
                    computer_move = wins(live_cells_indices)[0]
                    cells_to_kill = live_cells_indices - computer_move
                    x, y = max(cells_to_kill, key=lambda item: (item[0], -item[1]))
                except IndexError:
                    x, y = choice(list(live_cells_indices))

            # если доска большая то сначала выбираем случайно а потом по алгоритму
            elif len(live_cells_indices) > 10:
                x, y = choice(list(live_cells_indices))

            self.chosen_cell = self.game_object.cells[x][y]
            self.remove_block_from_board()
