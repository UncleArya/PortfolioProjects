from gameboard import GameBoard
import random


class Game:
    def __init__(self):
        self.gameboard = GameBoard()
        self.is_running = True
        self.game_over = False
        self.game_mode = 0
        self.valid_moves = list(self.gameboard.board.keys())
        self.moves_made = 0

    def obtain_game_mode(self):
        mode_select = input("Enter '1' for single-player or '2' for multi-player: ")
        if mode_select == "1":
            self.game_mode = 1
        elif mode_select == "2":
            self.game_mode = 2
        else:
            print("You must enter a '1 or a '2. Try again.")
            self.obtain_game_mode()

    def obtain_player_move(self, player):
        player_move = input(f"Player {player} - Enter a row and column value (ex. 'A1'): ").upper()
        return f"{player_move[0]}{player_move[1]}"

    def player_turn(self, player_name):
        if self.is_running:
            player_move = self.obtain_player_move(player=player_name)
            if player_move in self.valid_moves:
                if self.gameboard.check_board_space(move=player_move):
                    self.gameboard.update_board(move=player_move, player=player_name)
                    self.check_win_conditions(active_player=player_name)
                else:
                    print("Space already taken. Play again.")
                    self.player_turn(player_name)
            else:
                print("Invalid move! Try again.")
                self.player_turn(player_name)

    def computer_turn(self):
        if self.is_running:
            row = random.choice(["A", "B", "C"])
            column = random.choice([1, 2, 3])
            computer_move = f"{row}{column}"
            print(computer_move)
            if self.gameboard.check_board_space(move=computer_move):
                self.gameboard.update_board(move=computer_move, player="O")
                self.check_win_conditions(active_player="O")
            else:
                self.computer_turn()

    def start_game(self):
        self.gameboard.draw_board()
        if self.game_mode == 0:
            self.obtain_game_mode()
        self.gameboard.draw_board()
        while self.is_running:
            if self.game_mode == 1:
                self.gameboard.draw_board()
                self.player_turn("X")
                self.computer_turn()
            else:
                self.player_turn("X")
                self.player_turn("O")

    def check_rows(self, player):
        if self.gameboard.board["A1"] == self.gameboard.board["A2"] == self.gameboard.board["A3"] == player:
            return True
        elif self.gameboard.board["B1"] == self.gameboard.board["B2"] == self.gameboard.board["B3"] == player:
            return True
        elif self.gameboard.board["C1"] == self.gameboard.board["C2"] == self.gameboard.board["C3"] == player:
            return True
        else:
            return False

    def check_columns(self, player):
        if self.gameboard.board["A1"] == self.gameboard.board["B1"] == self.gameboard.board["C1"] == player:
            return True
        elif self.gameboard.board["A2"] == self.gameboard.board["B2"] == self.gameboard.board["C2"] == player:
            return True
        elif self.gameboard.board["A3"] == self.gameboard.board["B3"] == self.gameboard.board["C3"] == player:
            return True
        else:
            return False

    def check_diagonals(self, player):
        if self.gameboard.board["A1"] == self.gameboard.board["B2"] == self.gameboard.board["C3"] == player:
            return True
        elif self.gameboard.board["A3"] == self.gameboard.board["B2"] == self.gameboard.board["C1"] == player:
            return True
        else:
            return False

    def check_win_conditions(self, active_player):
        player = f" {active_player} "
        if self.check_rows(player) or self.check_columns(player) or self.check_diagonals(player):
            print(f"Player {player} wins!")
            self.game_replay()

    def game_replay(self):
        replay = input("Would you like to play again? (Y/N) ").upper()
        if replay == "Y":
            self.start_game()
        elif replay == "N":
            self.is_running = False
        else:
            print("Enter 'Y' to play again or 'N' to quit.")
            self.game_replay()
