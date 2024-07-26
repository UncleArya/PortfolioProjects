import os

BOARD = {
    "A1": "   ",
    "A2": "   ",
    "A3": "   ",
    "B1": "   ",
    "B2": "   ",
    "B3": "   ",
    "C1": "   ",
    "C2": "   ",
    "C3": "   ",
}


class GameBoard:
    """Contains the logic required to draw and update the game board within the terminal."""

    def __init__(self):
        self.board = BOARD.copy()
        self.moves_made = 0

    def draw_board(self):
        """Draws the current board."""
        os.system("clear")
        print("Arya's Tic Tac Toe")
        print("    1   2   3")
        print("   --- --- ---")
        print(f"A |{self.board["A1"]}|{self.board["A2"]}|{self.board["A3"]}|")
        print("   ---+---+---")
        print(f"B |{self.board["B1"]}|{self.board["B2"]}|{self.board["B3"]}|")
        print("   ---+---+---")
        print(f"C |{self.board["C1"]}|{self.board["C2"]}|{self.board["C3"]}|")
        print("   --- --- ---")

    def clear_board(self):
        """Resets the board when a new game is started."""
        self.board = BOARD.copy()
        self.moves_made = 0

    def update_board(self, move, player):
        """Obtains the chosen move and updates the board.

        Parameters:

        move -> str
            selects the board position to update

        player -> str
            updates the board position with either a 'X' or an 'O'
        """
        self.board[move] = f" {player} "
        self.moves_made += 1
        return self.draw_board()

    def check_board_space(self, move):
        """Checks if the submitted move is open and available for a valid move.

        Parameters:

        move -> str
            refers to the board position to check
        """
        if self.board[move] == "   ":
            return True
        else:
            return False

    def check_rows_for_win(self, player):
        """Checks the submitted move for win conditions by row.

        Parameters

        player -> str
            refers to player 'X' or 'O'
        """
        for row in ["A", "B", "C"]:
            if self.board[f"{row}1"] == self.board[f"{row}2"] == self.board[f"{row}3"] == player:
                return True

    def check_columns_for_win(self, player):
        """Checks the submitted move for win conditions by column.

        Parameters

        player -> str
            refers to player 'X' or 'O'
        """
        for column in ["1", "2", "3"]:
            if self.board[f"A{column}"] == self.board[f"B{column}"] == self.board[f"C{column}"] == player:
                return True

    def check_diagonals_for_win(self, player):
        """Checks the submitted move for win conditions by diagonals.

        Parameters

        player -> str
            refers to player 'X' or 'O'
        """
        if self.board["A1"] == self.board["B2"] == self.board["C3"] == player:
            return True
        elif self.board["A3"] == self.board["B2"] == self.board["C1"] == player:
            return True

    def check_rows_move(self, player):
        """For the computer-player, checks all rows for a win condition. If no win condition exists, checks for a human-player imminent win condition that needs to be blocked.

        Parameters

        player -> str
            refers to player 'X' or 'O'
        """
        for row in ["A", "B", "C"]:
            if self.board[f"{row}2"] == self.board[f"{row}3"] == player and self.check_board_space(f"{row}1"):
                return f"{row}1"
            elif self.board[f"{row}1"] == self.board[f"{row}3"] == player and self.check_board_space(f"{row}2"):
                return f"{row}2"
            elif self.board[f"{row}1"] == self.board[f"{row}2"] == player and self.check_board_space(f"{row}3"):
                return f"{row}3"

    def check_columns_move(self, player):
        """For the computer-player, checks all columns for a win condition. If no win condition exists, checks for a human-player imminent win condition that needs to be blocked.

        Parameters

        player -> str
            refers to player 'X' or 'O'
        """
        for column in ["1", "2", "3"]:
            if self.board[f"B{column}"] == self.board[f"C{column}"] == player and self.check_board_space(f"A{column}"):
                return f"A{column}"
            elif self.board[f"A{column}"] == self.board[f"C{column}"] == player and self.check_board_space(
                f"B{column}"
            ):
                return f"B{column}"
            elif self.board[f"A{column}"] == self.board[f"B{column}"] == player and self.check_board_space(
                f"C{column}"
            ):
                return f"C{column}"

    def check_diagonals_move(self, player):
        """For the computer-player, checks all diagonals for a win condition. If no win condition exists, checks for a human-player imminent win condition that needs to be blocked.

        Parameters

        player -> str
            refers to player 'X' or 'O'
        """
        if self.board["B2"] == self.board["C3"] == player and self.check_board_space("A1"):
            return "A1"
        elif self.board["A1"] == self.board["C3"] == player and self.check_board_space("B2"):
            return "B2"
        elif self.board["A1"] == self.board["B2"] == player and self.check_board_space("C3"):
            return "C3"
        elif self.board["B2"] == self.board["C1"] == player and self.check_board_space("A3"):
            return "A3"
        elif self.board["A3"] == self.board["C1"] == player and self.check_board_space("B2"):
            return "B2"
        elif self.board["A3"] == self.board["B2"] == player and self.check_board_space("C1"):
            return "C1"
