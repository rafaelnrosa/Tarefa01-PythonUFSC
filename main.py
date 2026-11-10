"""Interface grafica do jogo Connect Four."""

import tkinter as tk

from game import COLUMNS, ROWS, ConnectFourGame


BACKGROUND = "#f3f5f9"
BOARD_COLOR = "#1746a2"
PLAYER_COLORS = {1: "#f04b45", 2: "#ffd43b"}
TEXT_COLOR = "#17233c"
MUTED_COLOR = "#65718a"


class ConnectFourApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.game = ConnectFourGame()
        self.column_buttons = []

        root.title("Connect Four")
        root.configure(bg=BACKGROUND)
        root.resizable(False, False)

        container = tk.Frame(root, bg=BACKGROUND, padx=24, pady=20)
        container.pack()

        tk.Label(
            container,
            text="CONNECT FOUR",
            font=("Segoe UI", 22, "bold"),
            fg=TEXT_COLOR,
            bg=BACKGROUND,
        ).pack()
        tk.Label(
            container,
            text="Conecte quatro fichas para vencer",
            font=("Segoe UI", 10),
            fg=MUTED_COLOR,
            bg=BACKGROUND,
        ).pack(pady=(2, 14))

        self.status = tk.Label(
            container,
            text="",
            font=("Segoe UI", 13, "bold"),
            fg=TEXT_COLOR,
            bg=BACKGROUND,
            height=2,
        )
        self.status.pack()

        controls = tk.Frame(container, bg=BACKGROUND)
        controls.pack(fill="x", pady=(8, 8))
        for column in range(COLUMNS):
            controls.grid_columnconfigure(column, weight=1, uniform="columns")
            button = tk.Button(
                controls,
                text=str(column + 1),
                command=lambda selected=column: self.play_column(selected),
                font=("Segoe UI", 11, "bold"),
                fg=TEXT_COLOR,
                bg="#e1e7f2",
                activebackground="#cbd6e8",
                relief="flat",
                cursor="hand2",
                padx=8,
                pady=7,
            )
            button.grid(row=0, column=column, padx=3, sticky="ew")
            self.column_buttons.append(button)

        self.canvas = tk.Canvas(
            container,
            width=560,
            height=480,
            bg=BOARD_COLOR,
            highlightthickness=0,
        )
        self.canvas.pack()

        tk.Button(
            container,
            text="Reiniciar Jogo",
            command=self.restart,
            font=("Segoe UI", 10, "bold"),
            fg="white",
            bg="#263b68",
            activebackground="#1c2d52",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=9,
        ).pack(pady=(14, 0))

        self.update_view()

    def play_column(self, column: int) -> None:
        if self.game.drop_piece(column):
            self.update_view()

    def restart(self) -> None:
        self.game.reset()
        self.update_view()

    def update_view(self) -> None:
        self.draw_board()
        if self.game.winner is not None:
            self.status.config(text=f"Jogador {self.game.winner} venceu!")
        elif self.game.is_draw:
            self.status.config(text="Empate! O tabuleiro está cheio.")
        else:
            self.status.config(text=f"Vez do Jogador {self.game.current_player}")

        for column, button in enumerate(self.column_buttons):
            is_full = self.game.board[0][column] is not None
            button.config(
                state="disabled" if self.game.is_over or is_full else "normal"
            )

    def draw_board(self) -> None:
        self.canvas.delete("all")
        width = max(self.canvas.winfo_width(), 560)
        height = max(self.canvas.winfo_height(), 480)
        cell_size = min(width / COLUMNS, height / ROWS)
        board_width = cell_size * COLUMNS
        board_height = cell_size * ROWS
        offset_x = (width - board_width) / 2
        offset_y = (height - board_height) / 2

        self.canvas.create_rectangle(
            offset_x,
            offset_y,
            offset_x + board_width,
            offset_y + board_height,
            fill=BOARD_COLOR,
            outline=BOARD_COLOR,
        )
        margin = cell_size * 0.1
        for row in range(ROWS):
            for column in range(COLUMNS):
                left = offset_x + column * cell_size + margin
                top = offset_y + row * cell_size + margin
                right = offset_x + (column + 1) * cell_size - margin
                bottom = offset_y + (row + 1) * cell_size - margin
                player = self.game.board[row][column]
                color = PLAYER_COLORS.get(player, BACKGROUND)
                self.canvas.create_oval(
                    left, top, right, bottom, fill=color, outline=color
                )


def main() -> None:
    root = tk.Tk()
    ConnectFourApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
