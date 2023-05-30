import chess
import chess.pgn

class ChessGame:
    def __init__(self, pgn_file=None):
        # Если указан файл PGN, загружаем игру из файла
        if pgn_file:
            self.game = chess.pgn.read_game(open(pgn_file))
            self.board = self.game.board()
            self.move_count = 0
            self.moves = list(self.game.mainline_moves())
            self.current_move = 0
            self.mode = "pgn"
        # Иначе начинаем новую игру
        else:
            self.board = chess.Board()
            self.move_count = 0
            self.mode = "game"

    # Выводим доску на экран
    def print_board(self):
        print(self.board.unicode(invert_color=False, borders=True))

    # Делаем ход
    def move_piece(self, move):
        # Проверяем, является ли ход допустимым
        if chess.Move.from_uci(move) in self.board.legal_moves:
            self.board.push(chess.Move.from_uci(move))
            self.move_count += 1
        else:
            print("Эта фигура так не ходит")

    # Переходим к следующему ходу в записи партии
    def next_move(self):
        if self.current_move < len(self.moves):
            self.board.push(self.moves[self.current_move])
            self.current_move += 1
            self.move_count += 1

    # Возвращаемся к предыдущему ходу в записи партии
    def previous_move(self):
        if self.current_move > 0:
            self.board.pop()
            self.current_move -= 1
            self.move_count -= 1

    # Откатываем ходы в обычной игре
    def undo_move(self, count=1):
        for _ in range(count):
            if self.move_count > 0:
                self.board.pop()
                self.move_count -= 1

    # Выводим список фигур, которые находятся под угрозой
    def threatened_pieces(self):
        threatened = []
        for square in chess.SQUARES:
            if self.board.piece_at(square) and self.board.piece_at(square).color == self.board.turn:
                if self.board.is_attacked_by(not self.board.turn, square):
                    threatened.append(chess.square_name(square))
        if self.board.is_check():
            print("Шах королю!")
        return threatened

def main():
    pgn_file = input("Введите имя файла PGN или нажмите Enter для новой игры: ")
    game = ChessGame(pgn_file) if pgn_file else ChessGame()
    while not game.board.is_checkmate():
        game.print_board()
        print("Угрожаемые фигуры: ", game.threatened_pieces())
        if game.mode == "pgn":
            command = input("Введите команду (n (следующий ход), p (предыдущий)): ")
            if command == "n":
                game.next_move()
            elif command == "p":
                game.previous_move()
        else:
            command = input("Введите ваш ход или команду (u (откат хода) , u N (откат на  несколько шагов, где N - кол-во шагов) ): ")
            if command.startswith("u"):
                _, _, count= command.partition(' ')
                game.undo_move(int(count) if count else 1)
            else:
                game.move_piece(command)

if __name__ == "__main__":
    main()
