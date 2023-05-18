import chess

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.move_count = 0

    def print_board(self):
        print(self.board.unicode(invert_color=False, borders=True))

    def move_piece(self, move):
        if chess.Move.from_uci(move) in self.board.legal_moves:
            self.board.push(chess.Move.from_uci(move))
            self.move_count += 1
        else:
            print("Эта фигура так не ходит")

def main():
    game = ChessGame()
    while not game.board.is_checkmate():
        game.print_board()
        move = input("Введите ваш ход: ")
        game.move_piece(move)

if __name__ == "__main__":
    main()
