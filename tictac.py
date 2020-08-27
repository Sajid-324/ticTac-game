import random

def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    while marker.upper() != 'X' and marker.upper() != 'O':
        marker = input('Player1, choose X or O :')
    
    player1 = marker.upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    #WIN TIC TAC TOE?
    return ((board[7]==board[8]==board[9]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[1]==board[2]==board[3]==mark) or    
    (board[3]==board[6]==board[9]==mark) or
    (board[2]==board[5]==board[8]==mark) or
    (board[1]==board[4]==board[7]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[3]==board[5]==board[7]==mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False        
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
            position = int(input(turn+' choose a position between 1-9 ==> '))
    return position 

def replay():
    
    choice = input("Play again? (y / n) : ")
    if choice == 'y' :
        game_on = True
    else:
        game_on = False

print('\nWelcome to TIC TAC TOE \n')

while True:
    
    the_board= [" "]*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? (y / n) : ')
    
    if play_game == 'y' :
        game_on = True
    else:
        game_on = False
     
    ##GAME PLAY
    
    while game_on:
        if turn == 'Player 1':
            
            #SHOW TTHE BOARD
            display_board(the_board)
 
            #CHOOSE A POSITION
            position = player_choice(the_board)
    
            #PLACE THE MARKER ON THE POSITION
            place_marker(the_board,player1_marker,position)
            
            #CHECK IF THEY WON
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            #SHOW TTHE BOARD
            display_board(the_board)
 
            #CHOOSE A POSITION
            position = player_choice(the_board)
    
            #PLACE THE MARKER ON THE POSITION
            place_marker(the_board,player2_marker,position)
            
            #CHECK IF THEY WON
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break