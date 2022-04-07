from enum import Enum
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King, Colour, Empty
from board import Board

BOARD_SIZE = 8
NUMBER_OF_SQUARES = 64
startingFEN = "rnbqkbnr/pppppppp/eeeeeeee/eeeeeeee/eeeeeeee/eeeeeeee/PPPPPPPP/RNBQKBNR/ w KQkq - 0"

def main():
    board = Board(startingFEN)
    board.print()

    # Game Loop
    while(True):
        # Check for valid move
        while(True):
            newMove = input("Enter Move: ")
            validMove = board.checkValidMove(newMove)
            if validMove:
                break
            print("Invalid move")

        board.move(newMove)
        board.print()
    
main()