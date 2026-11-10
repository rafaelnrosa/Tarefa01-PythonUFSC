import unittest

from game import COLUMNS, ROWS, ConnectFourGame


class ConnectFourGameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ConnectFourGame()

    def test_pieces_fall_to_lowest_available_row_and_turns_alternate(self) -> None:
        self.assertTrue(self.game.drop_piece(3))
        self.assertTrue(self.game.drop_piece(3))
        self.assertEqual(self.game.board[ROWS - 1][3], 1)
        self.assertEqual(self.game.board[ROWS - 2][3], 2)
        self.assertEqual(self.game.current_player, 1)

    def test_rejects_invalid_and_full_columns(self) -> None:
        self.assertFalse(self.game.drop_piece(-1))
        self.assertFalse(self.game.drop_piece(COLUMNS))
        for _ in range(ROWS):
            self.assertTrue(self.game.drop_piece(0))
        self.assertFalse(self.game.drop_piece(0))

    def test_detects_horizontal_win(self) -> None:
        for column in (0, 0, 1, 1, 2, 2):
            self.game.drop_piece(column)
        self.assertTrue(self.game.drop_piece(3))
        self.assertEqual(self.game.winner, 1)
        self.assertFalse(self.game.drop_piece(4))

    def test_detects_vertical_win(self) -> None:
        for _ in range(3):
            self.game.drop_piece(0)
            self.game.drop_piece(1)
        self.assertTrue(self.game.drop_piece(0))
        self.assertEqual(self.game.winner, 1)

    def test_detects_diagonal_win(self) -> None:
        moves = (0, 1, 1, 2, 4, 2, 2, 3, 5, 3, 5, 3, 3)
        for column in moves:
            self.game.drop_piece(column)
        self.assertEqual(self.game.winner, 1)

    def test_detects_diagonal_win_in_other_direction(self) -> None:
        moves = (6, 5, 5, 4, 2, 4, 4, 3, 1, 3, 1, 3, 3)
        for column in moves:
            self.game.drop_piece(column)
        self.assertEqual(self.game.winner, 1)

    def test_detects_draw_when_board_is_full(self) -> None:
        moves = (
            3, 3, 0, 2, 5, 4, 5, 6, 4, 2, 2, 3, 3, 5, 5, 2, 2, 4, 3, 3, 1,
            1, 2, 1, 5, 5, 0, 4, 0, 4, 4, 6, 6, 6, 6, 0, 1, 0, 6, 0, 1, 1,
        )
        for column in moves:
            self.game.drop_piece(column)
        self.assertTrue(self.game.is_draw)
        self.assertTrue(self.game.is_over)
        self.assertIsNone(self.game.winner)

    def test_reset_starts_a_clean_game(self) -> None:
        self.game.drop_piece(4)
        self.game.reset()
        self.assertEqual(self.game.current_player, 1)
        self.assertIsNone(self.game.winner)
        self.assertFalse(self.game.is_draw)
        self.assertTrue(all(cell is None for row in self.game.board for cell in row))


if __name__ == "__main__":
    unittest.main()
