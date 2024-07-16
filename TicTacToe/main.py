import os

BOARD = [
    ["   ", "   ", "   "],
    ["   ", "   ", "   "],
    ["   ", "   ", "   "],
]

IS_RUNNING = True


def display_board():
    os.system('clear')
    print("Welcome to Arya's Tic Tac Toe")
    row_num = 1
    print("    A   B   C")
    print("   --- --- ---")
    for row in BOARD:
        print(f"{row_num} |{row[0]}|{row [1]}|{row[2]}|")
        print("   --- --- ---")
        row_num += 1


def obtain_player_move():
    player_move = input("Player 1 - Enter a column value then a row value (ex. 'A1'): ").upper()
    
    if player_move[0] == "A":
        player_column = 0
    elif player_move[0] == "B":
        player_column = 1
    else:
        player_column = 2

    player_row = int(player_move[1]) - 1
    
    return f"{player_column}{player_row}"


def player_1_turn():
    move = obtain_player_move()
    player_1_column = int(move[0])
    player_1_row = int(move[1])
    
    if check_board_space(player_1_column, player_1_row):
        BOARD[player_1_row][player_1_column] = " X "
    else:
        print("Space already taken. Play again.")
        player_1_turn()
    

def player_2_turn():
    player_2_move = input("Player 2 - Enter a column value then a row value (ex. 'A1'): ").upper()

    if player_2_move[0] == "A":
        player_2_column = 0
    elif player_2_move[0] == "B":
        player_2_column = 1
    else:
        player_2_column = 2
    
    player_2_row = int(player_2_move[1]) - 1
    
    if check_board_space(player_2_column, player_2_row):
        BOARD[player_2_row][player_2_column] = " O "
    else:
        print("Space already taken. Play again.")
        player_2_turn()
        

def game_loop():
    display_board()
    player_1_turn()
    display_board()
    player_2_turn()


def check_board_space(column, row):
    if BOARD[row][column] == "   ":
        return True
    else:
        return False


while IS_RUNNING:
    game_loop()