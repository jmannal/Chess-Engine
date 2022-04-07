from enum import Enum

class Colour(Enum):
    WHITE = 0
    BLACK = 1
    EMPTY = 2

class Piece(Enum):
    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5
    EMPTY = 6

# Piece designs by "Alfe" https://stackoverflow.com/questions/19517374/
# pythonic-way-to-print-a-chess-board-in-console#comment28954981_19518200
class Pawn():
    def __init__(self, colour):
        self.colour = colour
        self.moved = False
        if self.colour == colour.WHITE:
            self.Line1 = "   _   |"
            self.Line2 = "  ( )  |"
            self.Line3 = "  /_\  |"
            self.moves = [8, 16, 7, 9]

        elif self.colour == colour.BLACK:
            self.Line1 = "   _   |"
            self.Line2 = "  (@)  |"
            self.Line3 = "  /@\  |"
            self.moves = [-8, -16, -7, -9]

    def getClass(self):
        return Piece.PAWN
        
class Rook():
    def __init__(self, colour):
        self.colour = colour
        if self.colour == colour.WHITE:
            self.Line1 = " [___] |"
            self.Line2 = "  [ ]  |"
            self.Line3 = " /___\ |"

        elif self.colour == colour.BLACK:
            self.Line1 = " @___@ |"
            self.Line2 = "  @@@  |"
            self.Line3 = " /@@@\ |"

        self.moves = [-1, 1, -8, 8]

    def getClass(self):
        return Piece.ROOK
class Bishop():
    def __init__(self, colour):
        self.colour = colour
        if self.colour == colour.WHITE:
            self.Line1 = "  .*.  |"
            self.Line2 = "  ( )  |"
            self.Line3 = " ./_\. |"

        elif self.colour == colour.BLACK:
            self.Line1 = "  .*.  |"
            self.Line2 = "  (@)  |"
            self.Line3 = " ./@\. |"
        
        self.moves = [7, 9, -7, -9]

    def getClass(self):
        return Piece.BISHOP

class Knight():
    def __init__(self, colour):
        self.colour = colour
        if self.colour == colour.WHITE:
            self.Line1 = "  KKK  |"
            self.Line2 = "  KKK  |"
            self.Line3 = "  KKK  |"

        elif self.colour == colour.BLACK:
            self.Line1 = "  kkk  |"
            self.Line2 = "  kkk  |"
            self.Line3 = "  kkk  |"

        self.moves = [17, 15, 6, 10, -6, -10, -15, -17]

    def getClass(self):
        return Piece.KNIGHT

class Queen():
    def __init__(self, colour):
        self.colour = colour
        if self.colour == colour.WHITE:
            self.Line1 = " \\v^v/ |"
            self.Line2 = "  [ ]  |"
            self.Line3 = " /___\ |"

        elif self.colour == colour.BLACK:
            self.Line1 = " \\v^v/ |"
            self.Line2 = "  [@]  |"
            self.Line3 = " /@@@\ |"

        self.moves = [1, 7, 8, 9, -1, -7, -8, -9]

    def getClass(self):
        return Piece.QUEEN

class King():
    def __init__(self, colour):
        self.colour = colour
        if self.colour == colour.WHITE:
            self.Line1 = " __+__ |"
            self.Line2 = " `. .' |"
            self.Line3 = " /___\ |"

        elif self.colour == colour.BLACK:
            self.Line1 = " __+__ |"
            self.Line2 = " `.@.' |"
            self.Line3 = " /@@@\ |"
        
        self.moves = [-1, 1, -7, 7, -8, 8, -9, 9]

    def getClass(self):
        return Piece.KING

class Empty():
    def __init__(self):
        self.colour = Colour.EMPTY
        self.Line1 = "       |"
        self.Line2 = "       |"
        self.Line3 = "       |"

    def getClass(self):
        return Piece.EMPTY
    