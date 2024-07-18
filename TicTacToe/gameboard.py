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
    def __init__(self):
        self.board = BOARD

    def draw_board(self):
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

    def update_board(self, move, player):
        self.board[move] = f" {player} "
        return self.draw_board()

    def check_board_space(self, move):
        if self.board[move] == "   ":
            return True
        else:
            return False
