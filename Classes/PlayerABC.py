"""
abc — Abstract Base Classes, для создания и работы с абстрактынми классами
PlayerABC - абстрактный класс. Используется в качестве шаблона для игроков.
Для описания логики нового игрока необходимо создать новый унаследованный класс
и реализовать (Override) абстрактный метод choose_live_cell_from_board.
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
        # После выбора допустимой ячейки раскрасит ее «СHOSEN» цветом и удалит остальную часть блока.
        self.chosen_cell.kill_cell(was_chosed=True)
        self.game_object.remove_remainder_cells(self.chosen_cell)
        self.game_object.finish_turn()
