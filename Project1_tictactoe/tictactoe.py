#tic tac toe project
import random
import os

def showTheBoard(board):
    os.system('cls')
    print(board[7],board[8],board[9])
    print(board[4],board[5],board[6])
    print(board[1],board[2],board[3])

def getPlayerMove(board):
    choice = int(input("Which Tile?"))
    if board[choice] != "[]":
        print("this tile is occupied, choose another one")
        getPlayerMove(board)
    else:
        board[choice] = "X"
    return board

def checkForWin(board):
    if board[1] == board[2]==board[3] != "[]":
        return True
    elif board[4] == board[5]==board[6] != "[]":
        return True
    elif board[7] == board[8]==board[9] != "[]":
        return True
    elif board[1] == board[4]==board[7] != "[]":
        return True
    elif board[2] == board[5]==board[8] != "[]":
        return True
    elif board[3] == board[6]==board[9] != "[]":
        return True
    elif board[1] == board[5]==board[9] != "[]":
        return True
    elif board[3] == board[7]==board[9] != "[]":
        return True
    else:
        return False
    

def endGame(winner):
    if winner=="Tie":
        print("It's a Tie")
    else:
        print(winner,"won!")
    choice = input("Do you want to play again?(y/n)")
    if choice == "y":
        startGame()

def checkForTie(board):
    isTie = True
    n = 1
    while n<10:
        if board[n] == "[]":
            isTie = False
        n += 1 #n=n+1
    return isTie

def playHumanTurn(board):
    showTheBoard(board)
    board = getPlayerMove(board)
    if checkForWin(board):
        endGame("Human")
    else:
        if checkForTie(board):
            endGame("Tie")
        else:
            playAITurn(board)

def getAIMove(board):
    nextMoveChoices = []
    if board[1] == "[]" :
        if board[2] == board[3] == "X" or board[4] == board[7] == "X" or board[5] == board[9] == "X" :
            nextMoveChoices.append(1)
    if board[2] == "[]":
        if board[5] == board[8]== "X" or board[1] == board[3]== "X":
            nextMoveChoices.append(2)
    if board[3] == "[]":
        if board[1] == board[2]== "X" or board[5] == board[7]== "X" or board[6] == board[9]== "X":
            nextMoveChoices.append(3)
    if board[4] == "[]":
        if board[1] == board[7]== "X" or board[5] == board[6]== "X":
            nextMoveChoices.append(4)
    if board[5] == "[]":
        if board[2] == board[8]== "X" or board[3] == board[7]== "X" or board[1] == board[9]== "X" or board[4] == board[6]== "X":
            nextMoveChoices.append(5)
    if board[6] == "[]":
        if board[3] == board[9]== "X" or board[5] == board[4]== "X":
            nextMoveChoices.append(6)
    if board[7] == "[]":
        if board[8] == board[9]== "X" or board[4] == board[1]== "X" or board[5] == board[3]== "X":
            nextMoveChoices.append(7)
    if board[8] == "[]":
        if board[5] == board[2]== "X" or board[7] == board[9]== "X":
            nextMoveChoices.append(8)
    if board[9] == "[]":
        if board[5] == board[1]== "X" or board[6] == board[3]== "X" or board[8] == board[7]== "X":
            nextMoveChoices.append(9)                                                                
    if nextMoveChoices == []:
        choice = random.randrange(1, 9, 1)
        board[choice] = "O"
    else:
        choice = random.choice(nextMoveChoices)
        board[choice] = "O"
    return board              

def playAITurn(board):  
    board = getAIMove(board)
    if checkForWin(board):
        endGame("Computer")
    else:
        if checkForTie(board):
            endGame("Tie")
        else:
            playHumanTurn(board)

def startGame():
    board = {1:"[]", 2:"[]", 3:"[]", 4:"[]", 5:"[]", 6:"[]", 7:"[]", 8:"[]", 9:"[]"}
    isHumanTurn = random.choice([True, False])
    isHumanTurn = True
    if isHumanTurn:
        playHumanTurn(board)
    else:
        playAITurn(board)
    showTheBoard(board)

startGame()