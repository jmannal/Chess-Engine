from enum import Enum
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King, Colour, Empty

BOARD_SIZE = 8
NUMBER_OF_SQUARES = 64
startingFEN = "rnbqkbnr/pppppppp/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/PPPPPPPP/RNBQKBNR/ w KQkq - 0 1"

def main():
    board = convertFENtoBoard(startingFEN)
    printBoard(board)

    while(True):
        newMove = input("Enter Move: ")
        board = move(newMove, board)
        printBoard(board)

# Converts the FEN String into the board
def convertFENtoBoard(FENstring):

    # Reverse the board rows so that position A1 is the first array element
    # and H8 is the last
    board = list(FENstring.split('/')[0:BOARD_SIZE])
    board.reverse()
    board = list(''.join(board))
    print(board)
    #board = list(FENstring.replace('/', '')[0:NUMBER_OF_SQUARES])

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
    letters = "     A       B       C       D       E       F       G       H"

    print(letters)
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

    print(letters)


def move(move, board):
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    rowFrom = move[0]
    columnFrom = int(move[1])
    rowTo = move[2]
    columnTo = int(move[3])
    valid = checkValidMove(move)
    if not valid:
        return 'Invalid Move'
    


    board[rows.index(rowTo) + BOARD_SIZE * (columnTo - 1)] = board[rows.index(rowFrom) + BOARD_SIZE * (columnFrom - 1)]
    board[rows.index(rowFrom) + BOARD_SIZE * (columnFrom - 1)] = Empty()
    
    return board


def convertBoardtoFEN(board):
    pass

def checkValidMove(move):
    return 1


main()