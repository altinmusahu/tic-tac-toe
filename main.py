#Tic-tac-toe GAME!
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

win = 1
draw = -1
running = 0
stop = 1


game = running
mark = 'X'

def DrawBoard():
    print("%c  | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

def CheckPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False


def CheckWin():
    global game
    # Horizontal winning
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        game = win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        game = win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        game = win
    # Vertical Winning
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        game = win
    # Diagonal Winning
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        game = win
    # Match Tie or Draw
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        game = draw
    else:
        game = running


print("Welcome to tic-tac-toe game.")
while(game == running):
    DrawBoard()
    if(player % 2 != 0):
        print("Player 1's chance")
        mark = 'X'
    else:
        print("Player 2's chance")
        mark = 'O'
    choice = int(input("Choose a number between 1 to 9: "))
    if(CheckPosition(choice)):
        board[choice] = mark
        player += 1
        CheckWin()


DrawBoard()
if(game == draw):
    print("Game is draw")
elif(game == win):
    player -= 1
    if(player % 2 != 0):
        print("Player 1 won!")
        input("Would you like to play again?")
    else:
        print("Player 2 won!")
        input("Would you like to play again?")

    restart = input("yes")

    if restart == 'yes':
        DrawBoard()


