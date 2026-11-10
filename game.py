"""Regras do jogo Connect Four."""

from typing import List, Optional


ROWS = 6
COLUMNS = 7
CONNECT_LENGTH = 4


class ConnectFourGame:
    """Mantem o tabuleiro e aplica as regras do Connect Four."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        """Inicia uma nova partida."""
        self.board: List[List[Optional[int]]] = [
            [None for _ in range(COLUMNS)] for _ in range(ROWS)
        ]
        self.current_player = 1
        self.winner: Optional[int] = None
        self.is_draw = False

    @property
    def is_over(self) -> bool:
        return self.winner is not None or self.is_draw

    def drop_piece(self, column: int) -> bool:
        """Solta uma ficha na coluna indicada; retorna False se a jogada for invalida."""
        if self.is_over or not 0 <= column < COLUMNS:
            return False

        for row in range(ROWS - 1, -1, -1):
            if self.board[row][column] is None:
                self.board[row][column] = self.current_player
                if self._has_won(row, column):
                    self.winner = self.current_player
                elif all(cell is not None for line in self.board for cell in line):
                    self.is_draw = True
                else:
                    self.current_player = 2 if self.current_player == 1 else 1
                return True

        return False

    def _has_won(self, row: int, column: int) -> bool:
        player = self.board[row][column]
        if player is None:
            return False

        directions = ((0, 1), (1, 0), (1, 1), (1, -1))
        for row_step, column_step in directions:
            count = 1
            for step in (1, -1):
                next_row = row + row_step * step
                next_column = column + column_step * step
                while (
                    0 <= next_row < ROWS
                    and 0 <= next_column < COLUMNS
                    and self.board[next_row][next_column] == player
                ):
                    count += 1
                    next_row += row_step * step
                    next_column += column_step * step
            if count >= CONNECT_LENGTH:
                return True
        return False
