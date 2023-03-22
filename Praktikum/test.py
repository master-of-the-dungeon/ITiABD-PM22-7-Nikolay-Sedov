class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self, new_position):
        # Move the piece to a new position
        pass

    def __str__(self):
        return f"{self.color} piece at {self.position}"


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, new_position):
        # Move the pawn to a new position, following the rules of chess
        pass

    def __str__(self):
        return f"{self.color} pawn at {self.position}"


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, new_position):
        # Move the king to a new position, following the rules of chess
        pass

    def __str__(self):
        return f"{self.color} king at {self.position}"


class ChessBoard:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]

    def add_piece(self, piece, position):
        # Add a piece to the board
        pass

    def move_piece(self, piece, new_position):
        # Move a piece on the board to a new position
        pass

    def display(self):
        # Display the current state of the board
        pass


board = ChessBoard()
pawn = Pawn("White", (6, 0))
board.add_piece(pawn, (6, 0))
board.display()