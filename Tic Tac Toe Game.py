# Importing the clear_output method:
from IPython.display import clear_output

# Printing the board function:
def print_board(board):
    clear_output()
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

# Rules:
def rules_tic_tac_toe():
    print('Welcome to a classic game of Tic Tac Toe.\nHere is the sample board. Input the number in which you would like to place your marker when prompted.')
    print_board(game_board)

# Player input function:
def player_choice():
    player1 = ''
    player2 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1, choose X or O: ')

    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'

    return player1,player2

# Player 1 Input
def player1_input():
    player1_choice = ''
    while player1_choice not in input_options:
        player1_choice = int(input('Player 1 please select a place in the board: '))
    return player1_choice

# Player 2 Input
def player2_input():
    player2_choice = ''
    while player2_choice not in input_options:
        player2_choice = int(input('Player 2 please select a place in the board: '))
    return player2_choice

# Choice of continuing game.
def play_again():
    play_choice = ''
    global game_board
    global round_counter
    global game_result
    global check_position
    global players_marker
    while play_choice != 'Y' and play_choice != 'N':
        play_choice = input('Do you want to play again, Y or N? ')
    if play_choice == 'Y':
        game_board = ['#','1','2','3','4','5','6','7','8','9']
        round_counter = 1
        game_result = False
        check_position = ''
        players_marker = player_choice()
        return True
    elif play_choice == 'N':
        return False

# Check whether anyone has won
def check_win():
    global check_position
    if game_board[1] == game_board[2] == game_board[3]:
        check_position = 1
        return True
    elif game_board[1] == game_board[4] == game_board[7]:
        check_position = 1
        return True
    elif game_board[1] == game_board[5] == game_board[9]:
        check_position = 1
        return True
    elif game_board[4] == game_board[5] == game_board[6]:
        check_position = 4
        return True
    elif game_board[7] == game_board[8] == game_board[9]:
        check_position = 7
        return True
    elif game_board[7] == game_board[5] == game_board[3]:
        check_position = 7
        return True
    elif game_board[8] == game_board[5] == game_board[2]:
        check_position = 8
        return True
    elif game_board[9] == game_board[6] == game_board[3]:
        check_position = 9
        return True
    else:
        return False

# Sample Board for the rules:
game_board = ['#','1','2','3','4','5','6','7','8','9']
input_options = [1,2,3,4,5,6,7,8,9]
continue_game = True
round_counter = 1
game_result = False
check_position = ''

# Start Game
rules_tic_tac_toe()
players_marker = player_choice()
while round_counter < 10 and continue_game is True:
    while game_result is False and round_counter <= 9:
        if round_counter%2 != 0:
            player1_marker = player1_input()
            if game_board[player1_marker] not in players_marker:
                game_board[player1_marker] = players_marker[0]
                round_counter += 1
                print_board(game_board)
                game_result = check_win()
                break
            else:
                print('Position is already filled!')
                break
        elif round_counter%2 == 0:
            player2_marker = player2_input()
            if game_board[player2_marker] not in players_marker:
                game_board[player2_marker] = players_marker[1]
                round_counter += 1
                print_board(game_board)
                game_result = check_win()
                break
            else:
                print('Position is already filled!')
                break

    if game_result is True and round_counter <= 9:
        if check_position == 1:
            if game_board[1] == players_marker[0]:
                print('Player 1 wins!')
                continue_game = play_again()
                continue
            elif game_board[1] == players_marker[1]:
                print('Player 2 wins!')
                continue_game = play_again()
                continue
        elif check_position == 4:
            if game_board[4] == players_marker[0]:
                print('Player 1 wins!')
                continue_game = play_again()
                continue
            elif game_board[4] == players_marker[1]:
                print('Player 2 wins!')
                continue_game = play_again()
                continue
        elif check_position == 7:
            if game_board[7] == players_marker[0]:
                print('Player 1 wins!')
                continue_game = play_again()
                continue
            elif game_board[7] == players_marker[1]:
                print('Player 2 wins!')
                continue_game = play_again()
                continue
        elif check_position == 8:
            if game_board[8] == players_marker[0]:
                print('Player 1 wins!')
                continue_game = play_again()
                continue
            elif game_board[8] == players_marker[1]:
                print('Player 2 wins!')
                continue_game = play_again()
                continue
        elif check_position == 9:
            if game_board[9] == players_marker[0]:
                print('Player 1 wins!')
                continue_game = play_again()
                continue
            elif game_board[9] == players_marker[1]:
                print('Player 2 wins!')
                continue_game = play_again()
                continue
    elif game_result is False and round_counter > 9:
        print('Game is a Tie')
        continue_game = play_again()
        continue