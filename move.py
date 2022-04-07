from enum import Enum

class Rank(Enum):
    RANK1 = 0
    RANK2 = 8
    RANK3 = 16
    RANK4 = 24
    RANK5 = 32
    RANK6 = 40
    RANK7 = 48
    RANK8 = 56

    def __int__(self):
        return self.value

class File(Enum):
    FILE1 = 0
    FILE2 = 1
    FILE3 = 2
    FILE4 = 3
    FILE5 = 4
    FILE6 = 5
    FILE7 = 6
    FILE8 = 7

    def __int__(self):
        return self.value

class Move():
    def __init__(self, move):

        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        ranks = [Rank.RANK1, Rank.RANK2, Rank.RANK3, Rank.RANK4, Rank.RANK5, Rank.RANK6, Rank.RANK7, Rank.RANK8]
        files = [File.FILE1, File.FILE2, File.FILE3, File.FILE4, File.FILE5, File.FILE6, File.FILE7, File.FILE8]
        rowFrom = move[0]
        columnFrom = int(move[1])
        rowTo = move[2]
        columnTo = int(move[3])

        self.fromFile = files[rows.index(rowFrom.lower())]
        self.fromRank = ranks[columnFrom - 1]

        self.toFile = files[rows.index(rowTo.lower())]
        self.toRank = ranks[columnTo - 1]

        rowTo = rows.index(move[2])
        columnTo = int(move[3])

        self.fromIndex = int(self.fromFile) + int(self.fromRank)
        self.toIndex = int(self.toFile) + int(self.toRank)

    def print():
        pass
