from gameboard import GameBoard
import random


class Game:
    """
    Contains the logic required to start and complete a game of Tic Tac Toe. The .start_game() function is all that needs to be called to run the game.
    """

    def __init__(self):
        """Constructs necessary game attributes."""
        self.gameboard = GameBoard()
        self.is_running = True
        self.game_over = False
        self.game_mode = 0
        self.valid_moves = list(self.gameboard.board.keys())
        self.moves_made = 0

    def obtain_game_mode(self):
        """Prompts the user to choose a single-player or multi-player game."""
        mode_select = input("Enter '1' for single-player or '2' for multi-player: ")
        if mode_select == "1":
            self.game_mode = 1
        elif mode_select == "2":
            self.game_mode = 2
        else:
            print("You must enter a '1 or a '2. Try again.")
            self.obtain_game_mode()

    def player_turn(self, player_name):
        """Begins the human-user turn by prompting for a move input, checking if that board space is playable, and
        checking for possible win conditions"""
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

    def obtain_player_move(self, player):
        """Prompts the player for their desired move."""
        player_move = input(f"Player {player} - Enter a row and column value (ex. 'A1'): ").upper()
        return f"{player_move[0]}{player_move[1]}"

    def computer_turn(self):
        """Begins the computer-player turn by checking for win or block conditions. If none exist then a random
        available space is selected."""
        if self.is_running:
            computer_move = self.get_computer_move()
            if self.gameboard.check_board_space(move=computer_move):
                self.gameboard.update_board(move=computer_move, player="O")
                self.check_win_conditions(active_player="O")
            else:
                self.computer_turn()

    def check_computer_move(self):
        """During the computer-player turn"""
        for player in [" O ", " X "]:
            if self.gameboard.check_rows_move(player):
                return self.gameboard.check_rows_move(player)
            elif self.gameboard.check_columns_move(player):
                return self.gameboard.check_columns_move(player)
            elif self.gameboard.check_diagonals_move(player):
                return self.gameboard.check_diagonals_move(player)

    def get_computer_move(self):
        if self.check_computer_move():
            return self.check_computer_move()
        else:
            row = random.choice(["A", "B", "C"])
            column = random.choice([1, 2, 3])
            return f"{row}{column}"

    def start_game(self):
        self.gameboard.draw_board()
        self.gameboard.clear_board()
        if self.game_mode == 0:
            self.obtain_game_mode()
        self.gameboard.draw_board()
        play_order = random.choice([1, 2])
        while self.is_running:
            if self.game_mode == 1:
                self.gameboard.draw_board()
                if play_order == 1:
                    self.player_turn("X")
                    self.computer_turn()
                else:
                    self.computer_turn()
                    self.player_turn("X")
            else:
                if play_order == 1:
                    self.player_turn("X")
                    self.player_turn("O")
                else:
                    self.player_turn("O")
                    self.player_turn("X")

    def check_win_conditions(self, active_player):
        player = f" {active_player} "
        if (
            self.gameboard.check_rows_for_win(player)
            or self.gameboard.check_columns_for_win(player)
            or self.gameboard.check_diagonals_for_win(player)
        ):
            print(f"Player {player} wins!")
            self.game_replay()
        elif self.gameboard.moves_made == 9:
            print("No Winner. Game over.")
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
