import random
from IPython.display import clear_output

def game_list(board): #to dispaly the board in tic tac toe format
    clear_output()
    print ('  |  |')
    print (' '+board[7]+'| '+board[8]+'| '+board[9])
    print ('--------')
    print ('  |  |')
    print (' '+board[4]+'| '+board[5]+'| '+board[6])
    print ('--------')
    print ('  |  |')
    print (' '+board[1]+'| '+board[2]+'| '+board[3])

def player_input(): #to make user choose 'x' or 'o' as marker 
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input("player1 choose from X or O: ").lower()
        if marker != 'x' and marker != 'o':
            print("can only choose marker as X and O")
    if marker == 'x':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,postion): #place the marker on user defined postion
    board[postion]=marker

def win_check(board,marker): #possibility for winning the game
    #horizontal check
    return((board[7]==board[8]==board[9]==marker)or
    (board[4]==board[5]==board[6]==marker)or
    (board[1]==board[2]==board[3]==marker)or
    #vertical check
    (board[7]==board[4]==board[1]==marker)or
    (board[8]==board[5]==board[2]==marker)or
    (board[9]==board[6]==board[3]==marker)or
    #digonal check
    (board[9]==board[5]==board[1]==marker)or
    (board[7]==board[5]==board[3]==marker))

def choose_first():  #selecting randomly fron player1 or player 2
    flip = random.randint(0,1)
    if flip == 0:
        return ('player 1')
    else:
        return ('player 2')
    
def space_check(board,postion):  #to check whether space is empty
    return board[postion] == ' '

def full_board_check(board):  #to check if full board is full
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board): #to choose valid postion from user
    postion = 0 
    while postion not in (range(1,10)) or not space_check(board,postion):
        postion = int(input("choose a empty/postion from 1 to 9: "))
    return postion

def replay():  #loop to continue the game or not
    replay = 'wrong'
    while replay not in ['Y','N','y','n']:
        replay = input("keep playing (Y OR N): ").upper()
        if replay not in ['Y','N','y','n']:
            print ("wrong input select from (Y OR N)")
    if replay == 'Y':
        return True
    else:
        return False

#GAME LOGIC

print("WELCOME TO TIC TAC TOE")
while True:
    the_board = [' ']*10

    player1_marker , player2_marker = player_input()

    turn = choose_first()
    print (turn, "will play first")

    play_game = input('want to play game?? type y or n: ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on == True:
        if turn == 'player 1':
            game_list(the_board)

            postion = player_choice(the_board)

            place_marker(the_board,player1_marker,postion)

            if win_check(the_board,player1_marker):
                game_list(the_board)
                print("game win by player 1")
                game_on = False
            else:
                if full_board_check(the_board):
                    game_list(the_board)
                    print('game is tie')
                    game_on = False
                else:
                    print("player 2 turn")
                    turn = 'player 2'
        else:
            game_list(the_board)
            postion = player_choice(the_board)

            place_marker(the_board,player2_marker,postion)

            if win_check(the_board,player2_marker):
                game_list(the_board)
                print("game win by player 2")
                game_on = False
            else:
                if full_board_check(the_board):
                    game_list(the_board)
                    print('game is tie')
                    game_on = False
                else:
                    print("player 1 turn")
                    turn = 'player 1'
    if not replay():
        break
