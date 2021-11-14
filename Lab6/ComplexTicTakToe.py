def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4])
    print('-+-+-+-')
    print(board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8])
    print('-+-+-+-')
    print(board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12])
    print('-+-+-+-')
    print(board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16])
    print("\n")


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if position in range(1,18):
        if spaceIsFree(position):
            board[position] = letter
            printBoard(board)
            if (checkDraw()):
                print("Draw!")
                exit()
            if checkForWin():
                if letter == 'X':
                    print("Bot wins!")
                    exit()
                else:
                    print("Player wins!")
                    exit()

            return


        else:
            print("Can't insert there!")
            position = int(input("Please enter new position:  "))
            insertLetter(letter, position)
            return
    else:
        print("Can't insert there Out Of Bounds!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return



def checkForWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] != ' ':
        return True
    elif (board[5] == board[6] and board[5] == board[7] and board[5] == board[8] and board[5] != ' '):
        return True
    elif (board[9] == board[10] and board[9] == board[11] and board[9] == board[12] and board[9] != ' '):
        return True
    elif (board[13] == board[14] and board[13] == board[15] and board[13] == board[16] and board[13] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == board[13] and board[1] != ' '):
        return True
    elif (board[2] == board[6] and board[2] == board[10] and board[2] == board[14] and board[2] != ' '):
        return True
    elif (board[3] == board[7] and board[3] == board[11] and board[3] == board[15] and board[3] != ' '):
        return True
    elif (board[4] == board[8] and board[4] == board[12] and board[4] == board[16] and board[4] != ' '):
        return True
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] != ' '):
        return True
    elif (board[13] == board[10] and board[13] == board[7] and board[13] == board[4] and board[13] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == mark:
        return True
    elif (board[5] == board[6] and board[5] == board[7] and board[5] == board[8] and board[5] == mark):
        return True
    elif (board[9] == board[10] and board[9] == board[11] and board[9] == board[12] and board[9] == mark):
        return True
    elif (board[13] == board[14] and board[13] == board[15] and board[13] == board[16] and board[13] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == board[13] and board[1] == mark):
        return True
    elif (board[2] == board[6] and board[2] == board[10] and board[2] == board[14] and board[2] == mark):
        return True
    elif (board[3] == board[7] and board[3] == board[11] and board[3] == board[15] and board[3] == mark):
        return True
    elif (board[4] == board[8] and board[4] == board[12] and board[4] == board[16] and board[4] == mark):
        return True
    elif (board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == mark):
        return True
    elif (board[13] == board[10] and board[13] == board[7] and board[13] == board[4] and board[13] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return


def playerOneMove():
    position = int(input("Enter the position for 'X':  "))
    insertLetter(bot, position)
    return


def compMove(difficulty):
    bestScore = -800
    bestMove = 0
    for key in board.keys():

        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False, difficulty)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing, difficulty):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' ' and depth != difficulty):
                board[key] = bot
                score = minimax(board, depth + 1, False, difficulty)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' ' and depth != difficulty):
                board[key] = player
                score = minimax(board, depth + 1, True, difficulty)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
         5: ' ', 6: ' ', 7: ' ', 8: ' ',
         9: ' ', 10: ' ', 11: ' ', 12: ' ',
         13: ' ', 14: ' ', 15: ' ', 16: ' '}
player = 'O'
bot = 'X'
whoPlays = input("Do you Want to Play Against AI or Friend : ")

while True:
    if whoPlays.lower() == "ai":
        whosFirst = input("Do You Want To Play first :")
        difficulty = input("What Level Of Difficulty Do You Want To Choose : Easy , Medium , Hard : ")
        dif = 0
        if difficulty.lower() == "easy":
            dif = 2
        elif difficulty.lower() == "medium":
            dif = 3
        else:
            dif = 4
        if whosFirst.lower() == "yes" or whosFirst == "y":
            printBoard(board)
            print("enter positions from 1 till 16 to put your mark on the board")
            while not checkForWin():
                playerMove()
                compMove(dif)
        else:
            while not checkForWin():
                compMove(dif)
                playerMove()
    elif whoPlays.lower() == "friend":
        while not checkForWin():
            playerOneMove()
            playerMove()

    else:
        whoPlays = input("invalid option please try again enter AI or Friend in any case : ")
