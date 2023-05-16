import chess
import chess.svg
import chess.pgn
from IPython.display import SVG, display

def print_board(board):
    print("  A B C D E F G H")
    print(" ┌─────────────────┐")
    for y in range(7, -1, -1):
        row = str(y + 1) + "|"
        for x in range(8):
            piece = board.piece_at(chess.square(x, y))
            if piece is None:
                row += " ·"
            elif piece.color == chess.WHITE:
                row += " " + piece.symbol().upper()
            else:
                row += " " + piece.symbol().lower()
        row += " |" + str(y + 1)
        print(row)
    print(" └─────────────────┘")
    print("  A B C D E F G H")

def get_possible_moves(board, square):
    piece = board.piece_at(square)
    moves = list(board.legal_moves)
    moves = [move for move in moves if move.from_square == square]
    if piece.piece_type == chess.PAWN:
        moves = [move for move in moves if move.to_square != square]
        if piece.color == chess.WHITE:
            if chess.square_rank(square) == 1:
                moves = [move for move in moves if move.to_square == square + 16 or move.to_square == square + 8]
            else:
                moves = [move for move in moves if move.to_square == square + 8]
            for move in moves:
                if board.piece_at(move.to_square) is not None:
                    moves.remove(move)
                    break
            for move in moves:
                if chess.square_rank(move.to_square) == 7:
                    promotion = input("Выберите фигуру для замены пешки: (q, r, b, n)")
                    if promotion == "q":
                        move.promotion = chess.QUEEN
                    elif promotion == "r":
                        move.promotion = chess.ROOK
                    elif promotion == "b":
                        move.promotion = chess.BISHOP
                    elif promotion == "n":
                        move.promotion = chess.KNIGHT
                    break
        else:
            if chess.square_rank(square) == 6:
                moves = [move for move in moves if move.to_square == square - 16 or move.to_square == square - 8]
            else:
                moves = [move for move in moves if move.to_square == square - 8]
            for move in moves:
                if board.piece_at(move.to_square) is not None:
                    moves.remove(move)
                    break
            for move in moves:
                if chess.square_rank(move.to_square) == 0:
                    promotion = input("Выберите фигуру для замены пешки: (q, r, b, n)")
                    if promotion == "q":
                        move.promotion = chess.QUEEN
                    elif promotion == "r":
                        move.promotion = chess.ROOK
                    elif promotion == "b":
                        move.promotion = chess.BISHOP
                    elif promotion == "n":
                        move.promotion = chess.KNIGHT
                    break
    elif piece.piece_type == chess.KING:
        moves = [move for move in moves if chess.square_distance(move.to_square, square) == 1 or chess.square_distance(move.to_square, square) == 2 and chess.square_file(move.to_square) == chess.square_file(square) and (move.to_square)]



def get_threatened_pieces(board, color):
    threatened_pieces = []
    for square in board.pieces(chess.PAWN, color):
        moves = get_possible_moves(board, square)
        for move in moves:
            if board.piece_at(move.to_square) is not None and board.piece_at(move.to_square).color != color:
                threatened_pieces.append(move.to_square)
    for square in board.pieces(chess.KNIGHT, color):
        moves = get_possible_moves(board, square)
        for move in moves:
            if board.piece_at(move.to_square) is not None and board.piece_at(
                    move.to_square).color != color and board.piece_at(move.to_square).piece_type != chess.KING:
                threatened_pieces.append(move.to_square)
    for square in board.pieces(chess.BISHOP, color):
        moves = get_possible_moves(board, square)
        for move in moves:
            if board.piece_at(move.to_square) is not None and board.piece_at(
                    move.to_square).color != color and board.piece_at(move.to_square).piece_type != chess.KING:
                threatened_pieces.append(move.to_square)
    for square in board.pieces(chess.ROOK, color):
        moves = get_possible_moves(board, square)
        for move in moves:
            if board.piece_at(move.to_square) is not None and board.piece_at(
                    move.to_square).color != color and board.piece_at(move.to_square).piece_type != chess.KING:
                threatened_pieces.append(move.to_square)
    for square in board.pieces(chess.QUEEN, color):
        moves = get_possible_moves(board, square)
        for move in moves:
            if board.piece_at(move.to_square) is not None and board.piece_at(
                    move.to_square).color != color and board.piece_at(move.to_square).piece_type != chess.KING:
                threatened_pieces.append(move.to_square)
    for square in board.pieces(chess.KING, color):
        moves = get_possible_moves(board, square)
        for move in moves:
            if board.piece_at(move.to_square) is not None and board.piece_at(
                    move.to_square).color != color and board.piece_at(move.to_square).piece_type != chess.KING:
                threatened_pieces.append(move.to_square)
    return threatened_pieces


def print_highlighted_board(board, threatened_pieces):
    print("  A B C D E F G H")
    print(" ┌─────────────────┐")
    for y in range(7, -1, -1):
        row = str(y + 1) + "|"
        for x in range(8):
            piece = board.piece_at(chess.square(x, y))
            if piece is None:
                if chess.square(x, y) in threatened_pieces:
                    row += " +"
                else:
                    row += " ·"
            elif piece.color == chess.WHITE:
                if chess.square(x, y) in threatened_pieces:
                    row += " +" + piece.symbol().upper()
                else:
                    row += " " + piece.symbol().upper()
            else:
                if chess.square(x, y) in threatened_pieces:
                    row += " +" + piece.symbol().lower()
                else:
                    row += " " + piece.symbol().lower()
        row += " |" + str(y + 1)
        print(row)
    print(" └─────────────────┘")
    print("  A B C D E F G H")


def main():
    board = chess.Board()
    print_highlighted_board(board, [])

    while not board.is_game_over():
        move = input("Введите ход: ")
        if move == "back":
            if board.move_stack:
                board.pop()
                print_highlighted_board(board, [])


while not board.is_game_over():
    move = input("Введите ход: ")
    if move == "back":
        if board.move_stack:
            board.pop()
            print_highlighted_board(board, [])

def play_game():
    board = chess.Board()
    move_history = []
    while not board.is_game_over():
        print_board(board)
        threatened_pieces = get_threatened_pieces(board, board.turn)
        if threatened_pieces:
            print("Фигуры под боем:", threatened_pieces)
        if board.is_check():
            print("Шах!")
        if board.turn == chess.WHITE:
            move = input("Ход белых: ")
        else:
            move = input("Ход черных: ")
        if move == "back":
            num_moves_to_undo = 1
            try:
                num_moves_to_undo = int(input("Введите количество ходов для отката (по умолчанию 1): "))
            except ValueError:
                pass
            for i in range(num_moves_to_undo):
                if move_history:
                    move = move_history.pop()
                    board.pop()
                    board.push_uci(move)
                else:
                    print("Невозможно вернуться назад")
                    break
        elif move == "view_mode":
            display(SVG(chess.svg.board(board=board)))
            continue
        elif move == "save":
            filename = input("Введите имя файла для сохранения: ")
            with open(filename, "w") as f:
                f.write(str(board))
            print("Доска сохранена в файл", filename)
            continue
        elif move.endswith("pgn"):
            try:
                with open(move, "r") as f:
                    game = chess.pgn.read_game(f)
                    board = game.board()
                    for move in game.mainline_moves():
                        move_history.append(move.uci())
                        board.push(move)
                    print("Игра из файла", move, "начата")
                    continue
            except FileNotFoundError:
                print("Файл не найден")
                continue
        else:
            try:
                move_uci = chess.Move.from_uci(move)
                if move_uci in board.legal_moves:
                    board.push(move_uci)
                    move_history.append(move_uci.uci())
                else:
                    print("Некорректный ход, попробуйте снова")
            except ValueError:
                print("Некорректный формат хода, попробуйте снова")
    print_board(board)
    print("Конец игры")

if __name__ == "__main__":
    play_game()