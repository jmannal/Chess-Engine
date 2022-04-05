from enum import Enum

class Colour(Enum):
    WHITE = 0
    BLACK = 1

class Piece:
    def __init__(self, colour):
        self.colour = colour

class Pawn(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == colour.WHITE:
            self.Line1 = "   _   |"
            self.Line2 = "  ( )  |"
            self.Line3 = "  /_\  |"

        elif self.colour == colour.BLACK:
            self.Line1 = "   _   |"
            self.Line2 = "  (@)  |"
            self.Line3 = "  /@\  |"

    # def getLine1(self):
    #     return self.Line1

    # def getLine2(self):
    #     return self.Line2

    # def getLine3(self):
    #     return self.Line3

class Rook(Piece):
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

class Bishop(Piece):
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

class Knight(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == colour.WHITE:
            self.Line1 = "  kkk  |"
            self.Line2 = "  kkk  |"
            self.Line3 = "  kkk  |"

        elif self.colour == colour.BLACK:
            self.Line1 = "  KKK  |"
            self.Line2 = "  KKK  |"
            self.Line3 = "  KKK  |"

class Queen(Piece):
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

class King(Piece):
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

class Empty():
    def __init__(self):
        self.Line1 = "       |"
        self.Line2 = "       |"
        self.Line3 = "       |"