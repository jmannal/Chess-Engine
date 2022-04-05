from enum import Enum
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King, Colour, Empty

BOARD_SIZE = 8

startingFEN = "rnbqkbnr/pppppppp/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/PPPPPPPP/RNBQKBNR/ w KQkq - 0 1"

def main():
    board = convertFENtoBoard(startingFEN)
    printBoard(board)

# Converts the FEN String into the board
def convertFENtoBoard(FENstring):

    board = FENstring.split('/')

    # Convert FEN string into Pieces
    for i in range(BOARD_SIZE):
        board[i] = list(board[i])
        for j in range(BOARD_SIZE):
            if board[i][j] == 'p':
                board[i][j] = Pawn(Colour.BLACK)
                continue
            if board[i][j] == 'P':
                board[i][j] = Pawn(Colour.WHITE)
                continue
            if board[i][j] == 'r':
                board[i][j] = Rook(Colour.BLACK)
                continue
            if board[i][j] == 'R':
                board[i][j] = Rook(Colour.WHITE)
                continue
            if board[i][j] == 'b':
                board[i][j] = Bishop(Colour.BLACK)
                continue
            if board[i][j] == 'B':
                board[i][j] = Bishop(Colour.WHITE)
                continue
            if board[i][j] == 'n':
                board[i][j] = Knight(Colour.BLACK)
                continue
            if board[i][j] == 'N':
                board[i][j] = Knight(Colour.WHITE)
                continue
            if board[i][j] == 'q':
                board[i][j] = Queen(Colour.BLACK)
                continue
            if board[i][j] == 'Q':
                board[i][j] = Queen(Colour.WHITE)
                continue
            if board[i][j] == 'k':
                board[i][j] = King(Colour.BLACK)
                continue
            if board[i][j] == 'K':
                board[i][j] = King(Colour.WHITE)
                continue
            if board[i][j] == 'e':
                board[i][j] = Empty()
                continue

    return board

# Prints the board
def printBoard(board):

    rowDivider = "  ------- ------- ------- ------- ------- ------- ------- -------"
    header = "    A       B       C       D       E       F       G       H  "

    print(header)
    print(rowDivider)

    # Current row being printed (values 1 <= x <= 8)
    currentRow = 8

    # Print row by row, each row contains 3 lines
    for i in range(BOARD_SIZE):
        line1 = " |"
        line2 = f"{currentRow}|"
        line3 = " |"
        
        for j in range(BOARD_SIZE):
            line1 = line1 + board[i][j].Line1
            line2 = line2 + board[i][j].Line2
            line3 = line3 + board[i][j].Line3

        print(line1)
        print(line2 + f"{currentRow}")
        print(line3)
        print(rowDivider)
        currentRow -= 1

main()