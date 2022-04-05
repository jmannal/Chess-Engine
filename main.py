from enum import Enum
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King, Colour, Empty

# class Piece(Enum):
#     W_PAWN = 'P'
#     B_PAWN = 'p'
#     W_ROOK = 'R'
#     B_ROOK = 'r'
#     W_BISHOP = 'B'
#     B_BISHOP = 'b'
#     W_KNIGHT = 'N'
#     B_KNIGHT = 'n'
#     W_QUEEN = 'Q'
#     B_QUEEN = 'q'
#     W_KING = 'K'
#     B_KING = 'k'

startingFEN = "rnbqkbnr/pppppppp/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/PPPPPPPP/RNBQKBNR"

def main():
    printBoard(startingFEN)

# Prints the board given by the FEN String
def printBoard(FENstring):

    horizontalPattern = "  ------- ------- ------- ------- ------- ------- ------- -------"
    print("    A       B       C       D       E       F       G       H  ")
    print(horizontalPattern)

    # Current row being printed (values 1 <= x <= 8)
    currentRow = 8
    
    # Each piece takes up three lines, this keeps track of 
    # which line must be printed (can take values 1, 2, 3)
    rows = FENstring.split('/')

    # Convert FEN string into Pieces
    for j in range(len(rows)):
        rows[j] = list(rows[j])
        for i in range(len(rows[j])):
            if rows[j][i] == 'p':
                rows[j][i] = Pawn(Colour.BLACK)
                continue
            if rows[j][i] == 'P':
                rows[j][i] = Pawn(Colour.WHITE)
                continue
            if rows[j][i] == 'r':
                rows[j][i] = Rook(Colour.BLACK)
                continue
            if rows[j][i] == 'R':
                rows[j][i] = Rook(Colour.WHITE)
                continue
            if rows[j][i] == 'b':
                rows[j][i] = Bishop(Colour.BLACK)
                continue
            if rows[j][i] == 'B':
                rows[j][i] = Bishop(Colour.WHITE)
                continue
            if rows[j][i] == 'n':
                rows[j][i] = Knight(Colour.BLACK)
                continue
            if rows[j][i] == 'N':
                rows[j][i] = Knight(Colour.WHITE)
                continue
            if rows[j][i] == 'q':
                rows[j][i] = Queen(Colour.BLACK)
                continue
            if rows[j][i] == 'Q':
                rows[j][i] = Queen(Colour.WHITE)
                continue
            if rows[j][i] == 'k':
                rows[j][i] = King(Colour.BLACK)
                continue
            if rows[j][i] == 'K':
                rows[j][i] = King(Colour.WHITE)
                continue
            if rows[j][i] == 'e':
                rows[j][i] = Empty()
                continue

    for i in range(len(rows)):
        currentLine = " |"
        for j in range(len(rows[i])):
            currentLine = ''.join([currentLine, rows[i][j].Line1])
        print(currentLine)

        currentLine = f"{currentRow}|"
        for j in range(len(rows[i])):
            currentLine = ''.join([currentLine, rows[i][j].Line2])
        print(currentLine + f'{currentRow}')

        currentLine = " |"
        for j in range(len(rows[i])):
            currentLine = ''.join([currentLine, rows[i][j].Line3])
        print(currentLine)
    
        print(horizontalPattern)
        currentRow -= 1

main()