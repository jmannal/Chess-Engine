from enum import Enum
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King, Colour, Empty
from board import Board

BOARD_SIZE = 8
NUMBER_OF_SQUARES = 64
startingFEN = "rnbqkbnr/pppppppp/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/PPPPPPPP/RNBQKBNR/ w KQkq - 0 1"

def main():
    #board = convertFENtoBoard(startingFEN)
    #printBoard(board)
    board = Board(startingFEN)
    board.print()

    # Game Loop
    while(True):
        newMove = input("Enter Move: ")
        validMove = False
        while True:
            validMove = board.checkValidMove(newMove)
            if validMove:
                break
            print("Invalid move")
            newMove = input("Enter Another Move: ")

        board.move(newMove)
        board.print()

def move(move, board):

    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    rowFrom = rows.index(move[0])
    columnFrom = int(move[1])
    rowTo = rows.index(move[2])
    columnTo = int(move[3])
 
    
    fromIndex = rowFrom + BOARD_SIZE * (columnFrom - 1)
    toIndex = rowTo + BOARD_SIZE * (columnTo - 1)

    valid = checkValidMove(rowFrom, rowTo, columnFrom, columnTo, board)


    board[toIndex] = board[fromIndex]
    board[fromIndex] = Empty()
    
    return board

def checkValidMove(rowFrom, rowTo, columnFrom, columnTo, board):
    # For a move to be valid:
    # Correct side must move
    # The piece must only move a distance and in a direction it is allowed to,
    # It must not move out of bounds, onto a piece that is of the same colour,
    # or past a piece in the way (except for knight)
    # And the king must not be in check after the move.

    """
     ------- ------- -------
    |       |       |       |
    |   7   |   8   |   9   |
     ------- ------- -------
    |       |       |       |
    |  -1   | PIECE |   1   |
     ------- ------- -------
    |       |       |       |
    |  -9   |  -8   |  -7   |
     ------- ------- -------
    """

    fromIndex = rowFrom + BOARD_SIZE * (columnFrom - 1)
    toIndex = rowTo + BOARD_SIZE * (columnTo - 1)

    if rowFrom == rowTo:
        moveDirection = 1
        moveDistance = columnTo - columnFrom
    elif columnFrom == columnTo:
        moveDirection = 8
        moveDistance = rowTo
    elif abs(rowFrom - rowTo) > 0 and abs(columnFrom - columnTo) > 0:
        moveDirection = 9
        moveDistance = (toIndex - fromIndex) / 9
    elif abs(rowFrom - rowTo) > 0 and abs(columnFrom - columnTo) < 0:
        moveDirection = 7
        moveDistance = (toIndex - fromIndex) / 7
    

    # if board[moveFrom].getClass() == 'Pawn':
    #     pass
    # elif board[moveFrom].getClass() == 'Rook':
    #     pass
    # elif board[moveFrom].getClass() == 'Bishop':
    #     pass
    # elif board[moveFrom].getClass() == 'Knight':
    #     pass
    # elif board[moveFrom].getClass() == 'Queen':
    #     pass
    # elif board[moveFrom].getClass() == 'King':
    #     pass
    # return 1


main()