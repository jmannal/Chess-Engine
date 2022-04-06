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
        board = move(newMove, board)
        printBoard(board)

# Converts the FEN String into the board
def convertFENtoBoard(FENstring):

    # Reverse the board rows so that position A1 is the first array element
    # and H8 is the last
    extraInfo = FENstring.split('/')[-1]
    board = list(FENstring.split('/')[:BOARD_SIZE])
    board.reverse()
    board = list(''.join(board))
    print(board)

    for i in range(NUMBER_OF_SQUARES):
        if board[i] == 'p':
            board[i] = Pawn(Colour.BLACK)
            continue
        if board[i] == 'P':
            board[i] = Pawn(Colour.WHITE)
            continue
        if board[i] == 'r':
            board[i] = Rook(Colour.BLACK)
            continue
        if board[i] == 'R':
            board[i] = Rook(Colour.WHITE)
            continue
        if board[i] == 'b':
            board[i] = Bishop(Colour.BLACK)
            continue
        if board[i] == 'B':
            board[i] = Bishop(Colour.WHITE)
            continue
        if board[i] == 'n':
            board[i] = Knight(Colour.BLACK)
            continue
        if board[i] == 'N':
            board[i] = Knight(Colour.WHITE)
            continue
        if board[i] == 'q':
            board[i] = Queen(Colour.BLACK)
            continue
        if board[i] == 'Q':
            board[i] = Queen(Colour.WHITE)
            continue
        if board[i] == 'k':
            board[i] = King(Colour.BLACK)
            continue
        if board[i] == 'K':
            board[i] = King(Colour.WHITE)
            continue
        if board[i] == 'e':
            board[i] = Empty()
            continue

    return board

# Prints the board
def printBoard(board):

    rowDivider = " " + (" -------" * 8)
    lettersKey = "     A       B       C       D       E       F       G       H"

    print(lettersKey)
    print(rowDivider)

    # Current row being printed (values 1 <= x <= 8)
    currentRow = 8

    # Print row by row, each row contains 3 lines
    for i in range(BOARD_SIZE):
        line1 = " |"
        line2 = f"{currentRow}|"
        line3 = " |"
        
        # Print rows in reverse order so that white is on bottom
        for j in range(BOARD_SIZE):
            line1 = line1 + board[BOARD_SIZE * (BOARD_SIZE - i - 1) + j].Line1
            line2 = line2 + board[BOARD_SIZE * (BOARD_SIZE - i - 1) + j].Line2
            line3 = line3 + board[BOARD_SIZE * (BOARD_SIZE - i - 1) + j].Line3

        print(line1)
        print(line2 + f"{currentRow}")
        print(line3)
        print(rowDivider)
        currentRow -= 1

    print(lettersKey)


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


def convertBoardtoFEN(board):
    pass

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