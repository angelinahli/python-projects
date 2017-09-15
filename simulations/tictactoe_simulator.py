"""
Tic Tac Toe Simulator

Given a set of either 2 or 3 non-strategic sequential players, this monte carlo
simulation will print the percentage of times a player wins the game, as well as
calculating ties.
==> Non strategic: Players choose a tile randomly from their available options.
==> X player always goes first, O player goes second, Z player goes last.

Date: 03/02/17
Written by: Angelina Li
"""

import random

def initializeBoard(n):

    grid = []
    for i in range(n):
        grid.append([])
        for j in range(n):
            grid[i].append('_')
    return grid

def genValidMoves(board):
    valid = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == '_':
                valid.append((row, col))
    return valid

def genRandomMove(board):
    validMoves = genValidMoves(board)
    rand = random.randint(0,len(validMoves)-1)
    return validMoves[rand]

def won(player, board):
    return (wonLRDiag(player, board) or wonRLDiag(player, board) or 
            wonRow(player, board) or wonColumn(player, board))

def wonLRDiag(player, board):
    playerSlots = 0
    for place in range(len(board)):
        if board[place][place] == player:
            playerSlots += 1
    if playerSlots == len(board):
        return True
    return False
    
def wonRLDiag(player, board):
    playerSlots = 0
    for place in range(len(board)):
        if board[place][len(board)-place-1] == player:
            playerSlots += 1
    if playerSlots == len(board):
        return True
    return

def wonRow(player, board):
    for row in board:
        playerSlots = 0
        for slot in row:
            if slot == player:
                playerSlots += 1
        if playerSlots == len(row):
            return True
    return False

def wonColumn(player, board):
    for col in range(len(board)):
        playerSlots = 0
        for row in range(len(board)):
            if board[row][col] == player:
                playerSlots += 1
        if playerSlots == len(board):
            return True
    return False

def playMove(coords, player, board):
    row, col = coords
    board[row][col] = player

def playRand(n, players):
    board = initializeBoard(n)
    for turn in range(n*n): 
        player = players[turn % len(players)] 
        playMove(genRandomMove(board), player, board)
        if won(player, board):
            return player  
    return 'tie'

def countRand(n, players):
    results = {}
    for i in range(10000):
        res = playRand(n, players)
        if res not in results:
            results[res] = 1
        else:
            results[res] += 1
    return {key: round((float(value)/10000)*100, 3) for 
            key, value in results.items()}

def genChart():
    for i in range(2,5):
        print str(i) + 'x' + str(i) + " | 2 player: "
        print countRand(i, ['X', 'O'])
        print str(i) + 'x' + str(i) + " | 3 player: "
        print countRand(i, ['X', 'O', 'Z'])
        print ""
        
genChart()