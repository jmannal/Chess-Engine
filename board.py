from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King, Colour, Empty

class Board():
    def __init__(self, startFEN):
        self.extraInfo = startFEN.split('/')[-1]
        self.size = 8
        self.numberOfSquares = 64
        self.state = self.initialiseBoard(startFEN)

    def initialiseBoard(self, startFEN):

        extraInfo = startFEN.split('/')[-1]

        # Reverse the board rows so that position A1 is the first array element
        # and H8 is the last
        board = list(startFEN.split('/')[:self.size])
        board.reverse()
        board = list(''.join(board))

        for i in range(self.numberOfSquares):
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

    def print(self):
        rowDivider = " " + (" -------" * 8)
        lettersKey = "     A       B       C       D       E       F       G       H"

        print(lettersKey)
        print(rowDivider)

        # Current row being printed (values 1 <= x <= 8)
        currentRow = 8

        # Print row by row, each row contains 3 lines
        for i in range(self.size):
            line1 = " |"
            line2 = f"{currentRow}|"
            line3 = " |"
            
            # Print rows in reverse order so that white is on bottom
            for j in range(self.size):
                line1 = line1 + self.state[self.size * (self.size - i - 1) + j].Line1
                line2 = line2 + self.state[self.size * (self.size - i - 1) + j].Line2
                line3 = line3 + self.state[self.size * (self.size - i - 1) + j].Line3

            print(line1)
            print(line2 + f"{currentRow}")
            print(line3)
            print(rowDivider)
            currentRow -= 1

        print(lettersKey)